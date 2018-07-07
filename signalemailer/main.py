import ccxt
import time
import smtplib
from pyti import stochrsi as RSI
from pyti import bollinger_bands as BB
import pandas as pd
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
import MySQLdb as mysql


_BINANCE = ccxt.binance()
_BITTREX = ccxt.bittrex()


def main():
    LIST = 'alechaito@gmail.com'
    SUBJECT = 'Protraderbot - Sinal'
    MSG = 'test'
    PAIRS = ['USDT/BTC', 'BNB/BTC']
    #sendemail(to=LIST, subject=SUBJECT, message=MSG)
    band('BTC/USDT', '1h')

def sendemail(to, subject, html):
    msg = MIMEMultipart('alternative')
    msg['Subject'] = subject
    msg['From'] = 'noreply@protraderbot.com'
    msg['To'] = to

    part = MIMEText(html, 'html')
    msg.attach(part)
    
    server = smtplib.SMTP('mail.protraderbot.com:587')
    server.starttls()
    server.login('noreply@protraderbot.com', '252528')
    problems = server.sendmail('noreply@protraderbot.com', to, msg.as_string())
    server.quit()
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
    
def band(pair, timeframe):
    LOW = get_list(pair, timeframe, col=3, last=False)
    CLOSE = get_list(pair, timeframe, col=4, last=False)
    OPEN = get_list(pair, timeframe, col=1, last=True)
    BAND = BB.lower_bollinger_band(CLOSE, 20)
    print("BB:%.3f/LOW:%.3f \n"% (BAND[-1], LOW[-1]))
    if(BAND[-1] >= LOW[-1]):
        print("Enviei...")
        txt1 = "<b>Entrada:</b> %.3f~%.3f \n"% (OPEN[-1]*0.995, OPEN[-1])
        txt2 = "<b>Alvo 1:</b> %.3f \n" % (OPEN[-1]*1.005)
        txt3 = "<b>Alvo 2:</b> %.3f \n" % (OPEN[-1]*1.01)
        txt4 = "<b>Alvo 3:</b> %.3f \n" % (OPEN[-1]*1.015)
        txt5 = "<b>Stop:</b> %.3f \n" % (OPEN[-1]*0.98)
        txt6 = "<b>Risco:</b> %s \n" % check_btc()
    
        html = """\
            <html>
            <head></head>
            <body>
                <h4>Sinal: USDT-BTC</h4>
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
        sendemail(to='alechaito@gmail.com', subject='test', html=html)


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



main()

