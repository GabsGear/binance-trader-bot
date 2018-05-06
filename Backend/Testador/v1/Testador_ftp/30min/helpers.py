import datetime as datetime
import numpy as np
import pytz
import sys
import binance_

class Helpers:
    #Time on my timezone  
    def time_now(self):
        brasil = pytz.timezone('America/Sao_Paulo')
        ct = datetime.datetime.now(tz=brasil)
        return ct.strftime("%d/%m/%y-%X")
    
    #convert timestamp to date
    def tstampToData(self, timestamp):
        return(
            datetime.datetime.fromtimestamp(
                int(timestamp)/1000.0
            ).strftime('%Y-%m-%d %H:%M:%S')
        )

    #write log for plot
    def writeOutput(self, bot_id, data):
	    file = open('/home/backtest/30min/DataPlot/'+str(bot_id)+'-output.txt', 'a+')
	    file.write('['+str(self.time_now())+'] '+data+"\n")

    #write simple log
    def writeOutputTest(self, strategie,coin , time, buyValue, sellValue):
        file = open('/home/backtest/30min/Rank/'+str(strategie)+'-'+ str(coin)+'-Test-output.txt', 'a+')
        file.write('['+ str(time) +']' + ',' + str(buyValue) + ',' + str(sellValue)+"\n")
        #file.close()

    def insertRank(self, strategy, coin, profit,acerto):
        file = open('/home/backtest/30min/Rank/StrategyRankProfit.txt', 'a+')
        file.write('Best for ' + str(coin) + ' is ' + str(strategy)+ ' Profit = ' + str(profit) + '             || Chance = ' + str(acerto) + "\n")
    
    #progress bar
    def progress(self, count, total, status=''):
        bar_len = 60
        filled_len = int(round(bar_len * count / float(total)))

        percents = round(100.0 * count / float(total), 1)
        bar = '=' * filled_len + '-' * (bar_len - filled_len)

        sys.stdout.write('[%s] %s%s ...%s\r' % (bar, percents, '%', status))
        sys.stdout.flush()  

    #return number of operations
    def operationCOunter(self, log):
        return (log[0] + log[2] + log[5]) 


    def GainPercent(self, log):
        #log: [chanceb, valorb, chances, valors, fator de lucro, nstoploss]
        try:
            return log[2] / log[0] 
        except:
            return 0

    #eval profit 
    def getProfitFactor(self, profit, loss):
        try:
            return profit / loss 
        except:
            return 0

    #calc Stop Loss
    def stopLoss(self, value, percent):
        return value - (value * percent)/100
    
    #Verivy Stop Loss
    def isStopLoss(self, lastOperation, minn, futureLow):
        if lastOperation[1] == 0 and minn <= float(self.stopLoss(futureLow, 10)):
            return True
        else:
            return False


    def returnHashtag(self):
        return  ("####################################################################################\n")

    def generateFinalLog(self, strategy, log, coin, begin, end, ncandles):
        profit_factor = self.getProfitFactor(log[3], log[1])
        file = open('/home/backtest/30min/FinalLog/'+str(strategy)+'-'+ str(coin)+'-Final-output.txt', 'a+')
        file.write(self.returnHashtag()) 
        file.write('                    Relatorio de Analise de estrategia\n\n\n')
        file.write('Nome da estrategia : ' + str(strategy)+ '\n')
        file.write('Moeda Analisada: ' + str(coin) + '\n\n') 
        file.write('Data da analise: ' + str(self.time_now())+'\n')           
        file.write('Inicio da analise: ' + str(begin)+ '\n')
        file.write('Final da analise: ' + str(end)+ '\n') 
        file.write(self.returnHashtag())  
        file.write('Total de candles analisados: ' + str(ncandles) + '\n\n')  
        #[chanceb, valorb, chances, valors, fator de lucro]
        file.write('Numero de indicadores de compra: ' + str(log[0]) + '\n')  
        file.write('Montante total da compra considerando uma coin por buy : ' + str(log[1]) + '\n\n')  
        file.write('Numero de indicadores de venda sem stopLoss: ' + str(log[2]) + '\n')  
        file.write('Montante total da venda considerando uma coin por buy : ' + str(log[3]) + '\n\n')  
        file.write('Fator de lucro = ' + str(profit_factor) + '\n\n')
        file.write('Porcentagem de Acertos = ' +str(self.GainPercent(log) * 100) + '%' + '\n\n')
        file.write('Numero de StopLoss = ' + str(log[5]) + '\n\n')
        file.write('Final da analise\n')                    
        file.write(self.returnHashtag()) 


    def createDict(self,strategy, log, coin):

        log = {
            strategy: [
                    {   
                        "coin": coin,
                        "buyChance": log[0],
                        "sellChance": log[2],
                        "profitFactor": self.getProfitFactor(log[3], log[1])
                    }
            ]
        }
        return log