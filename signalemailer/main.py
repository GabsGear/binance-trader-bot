import ccxt
import time
import smtplib
from pyti import stochrsi as RSI
from pyti import bollinger_bands as BB
from pyti import volume_oscillator as VO
import pandas as pd
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from ta import *
import MySQLdb as mysql


_BINANCE = ccxt.binance()
_BITTREX = ccxt.bittrex()


def main():
    LIST = 'alechaito@gmail.com'
    SUBJECT = 'Protraderbot - Sinal'
    PAIRS = ['XLM/BTC']

    for pair in PAIRS:
        signal = vortex(pair)
        #if(signal == True):
        html = construct_signal(pair)
        send_to_list(html)

def sendemail(to, subject, html):
    msg = MIMEMultipart('alternative')
    msg['Subject'] = subject
    msg['From'] = 'signal@protraderbot.com'
    msg['To'] = to

    part = MIMEText(html, 'html')
    msg.attach(part)
    
    server = smtplib.SMTP('mail.protraderbot.com:587')
    server.starttls()
    server.login('signal@protraderbot.com', '252528')
    problems = server.sendmail('signal@protraderbot.com', to, msg.as_string())
    server.quit()
    print("enviei")
    print(problems)

def get_candles(pair=None, timeframe=None):
    delay = int(_BINANCE.rateLimit / 1000)
    time.sleep(delay)
    return _BINANCE.fetch_ohlcv(pair, timeframe)

def get_list(pair, timeframe, col, last=False):
    matrix = get_candles(pair, timeframe)
    data = pd.DataFrame(matrix)
    aux = []
    for index, row in data.iterrows():
        aux.append(row[col])
    if(last == False):
        aux.remove(aux[-1])
    return aux

def send_to_list(html):
    EMAILS = ['alechaito@gmail.com']
    for email in EMAILS:
        sendemail(to=email, subject='Signal', html=html)

def construct_signal(pair):
    PRICE = _BINANCE.fetchTicker(pair)['bid']
    txt1 = "<b>Entrada:</b> %.8f~%.8f \n"% (PRICE*0.995, PRICE)
    txt2 = "<b>Alvo 1:</b> %.8f \n" % (PRICE*1.005)
    txt3 = "<b>Alvo 2:</b> %.8f \n" % (PRICE*1.01)
    txt4 = "<b>Alvo 3:</b> %.8f \n" % (PRICE*1.015)
    txt5 = "<b>Stop:</b> %.8f \n" % (PRICE*0.98)
    txt6 = "<b>Risco:</b> %s \n" % check_btc()
    
    html = """\
        <html>
        <head></head>
        <body>
            <h4>Sinal: """+str(pair)+"""</h4>
            <table>
                <tr>
                    <td>"""+str(txt1)+"""</td>
                </tr>
                <tr>
                    <td>"""+str(txt2)+"""</td>
                </tr>
                <tr>
                    <td>"""+str(txt3)+"""</td>
                <tr>
                    <td>"""+str(txt4)+"""</td>
                </tr>
                <tr>
                    <td>"""+str(txt5)+"""</td>
                </tr>
                <tr>
                    <td>"""+str(txt6)+"""</td>
                </tr>
            </table>
            <p>Oferecimento: Protraderbot.com</p>
        </body>
        </html>
    """
    return html
    #sendemail(to='alechaito@gmail.com', subject='test', html=html)


def check_btc():
    CLOSE = get_list('BTC/USDT', '1d', col=4, last=True)
    perc = get_change(CLOSE[-1], CLOSE[-2])
    if(perc > 0.5):
        return "baixo"
    elif(perc < 0):
        return "alto"
    else:
        return "medio"


def get_change(current, previous):
    if current == previous:
        return 100.0
    try:
        return (abs(current - previous) / previous) * 100.0
    except ZeroDivisionError:
        return 0

def get_mail_list():
    db = mysql.connect(host="142.44.243.98", user="root", passwd="J8k5yZDV7z3X", db="protrader")
    cursor = db.cursor()
    query = ("SELECT * FROM email_signals")
    cursor.execute(query,)
    emails = []
    for trans in cursor:
        emails.append(str(trans[1]))
    print(emails)
    cursor.close()

def vortex(pair):
    #Create pandas dataframe
    matrix = get_candles(pair, '1h')
    df = pd.DataFrame(matrix)
    #Calculando vortex com TA: Tecnical Analysis Lib
    df[6] = vortex_indicator_pos(df[2], df[3], df[4], n=14, fillna=False)
    df[7] = vortex_indicator_neg(df[2], df[3], df[4], n=14, fillna=False)
    # Penultimo vortex idx
    last_pos = df[6][df.index[-3]]
    last_neg = df[7][df.index[-3]]
    # Ultimo vortex idx
    pos = df[6][df.index[-2]]
    neg = df[7][df.index[-2]]

    '''print("------------------- \n")
    print(pair)
    print("LP:%.2f" % last_pos)
    print("LN:%.2f"% last_neg)
    print("P:%.2f"% pos)
    print("N:%.2f"% neg)'''
    return pos > neg and last_pos < last_neg

main()

