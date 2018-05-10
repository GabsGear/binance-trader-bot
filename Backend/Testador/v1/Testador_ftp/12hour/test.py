import strategies
import binance_
import helpers
import time 
import logging
import os

class Testador():

    #data process buy, sell and none
    def dataProcess(self,result , strategy, logList, coin, data, futureLow, futureHigh, lastOperation):
        if (result == 0): #if buy
            lastbuy = futureLow
            logList[0] += 1
            logList[1] += futureLow
            return [lastbuy, 0]

        if (result == 1): #if sell
            lasSell = futureHigh
            logList[2] += 1
            logList[3] += futureHigh
            return [0, lasSell]


        if (result == 3): #if sell
            lasSell = futureHigh
            logList[5] += 1
            logList[3] += futureHigh
            return [0, lasSell]

        if (result == 2): #if none
            return lastOperation


    def test(self,coin ,inicial):

        data = binance_.Binance_opr()
        convert = helpers.Helpers()
        obj = helpers.Helpers()
        lopen, lhigh, llow, lclose, lvol, closetime = data.getStoricalCandles(coin, inicial)

        turtleLog = [0, 0.0, 0, 0.0, 0.0, 0.0] #[chanceb, valorb, chances, valors, fator de lucro, stoploss]
        insideLog = [0, 0.0, 0, 0.0, 0.0, 0.0]
        doubleUpLog = [0, 0.0, 0, 0.0, 0.0, 0.0]
        pivotUpLog = [0, 0.0, 0, 0.0, 0.0, 0.0]
        lastOperationTurtle = [0.0, 0.0] #last buy, last sell
        lastOperationInside = [0.0, 0.0] #last buy, last sell
        lastOperationDoubleUp = [0.0, 0.0] #last buy, last sell
        lastOperationPivot = [0.0, 0.0]   
 
        begin = convert.tstampToData(closetime[0])
        end = convert.tstampToData(closetime[len(closetime) -1])
        ncandles = len(lclose)
        
        for x in range(0, len(lopen)-40):

            turtle = strategies.ContraTurtle(lopen[x:x + 20], lhigh[x:x + 20], llow[x:x + 20], lclose[x:x + 20], lvol[x:x + 20])
            inside = strategies.insideBar(lopen[x:x + 20], lhigh[x:x + 20], llow[x:x + 20], lclose[x:x + 20], lvol[x:x + 20], closetime[x:x + 20])
            doubleUp = strategies.double_up(lopen[x:x + 20], lhigh[x:x + 20], llow[x:x + 20], lclose[x:x + 20], lvol[x:x + 20], closetime[x:x + 20])
            pivotUp = strategies.pivotUp(lopen[x:x + 20], lhigh[x:x + 20], llow[x:x + 20], lclose[x:x + 20], lvol[x:x + 20])

            if x < len(lopen) - 21:
                futureHigh = lhigh[x + 21]
                futureLow = llow[x + 21]
                time = closetime[x + 21]            
                time = convert.tstampToData(time)

            x = turtle.startTurtle(coin, futureLow, futureHigh, lastOperationTurtle)
            y = inside.startInside(coin, futureLow, futureHigh, 1.10, lastOperationInside)            
            z = doubleUp.startDOubleUp(coin, futureLow, futureHigh, 1.10, lastOperationDoubleUp)
            w = pivotUp.startPivot(coin, futureLow, futureHigh, lastOperationPivot)

            try: 
                lastOperationTurtle = self.dataProcess(x , "ContraTurtle", turtleLog, coin, time, futureLow, futureHigh, lastOperationTurtle)
                lastOperationInside = self.dataProcess(y , "InsideBar", insideLog, coin, time, futureLow, futureHigh, lastOperationInside)
                lastOperationDoubleUp = self.dataProcess(z , "DoubleUp", doubleUpLog, coin, time, futureLow, futureHigh, lastOperationDoubleUp)
                lastOperationPivot = self.dataProcess(w , "PivotUp", pivotUpLog, coin, time, futureLow, futureHigh, lastOperationPivot)
            except:
                print("Erro a executar uma extrategia")
                
         
        obj.generateFinalLog('Contra-Turtle', turtleLog, coin, begin, end, ncandles)
        obj.generateFinalLog('Inside-Bar', insideLog, coin, begin, end, ncandles)
        obj.generateFinalLog('Double-up', doubleUpLog, coin, begin, end, ncandles)
        obj.generateFinalLog('PivotUp', pivotUpLog, coin, begin, end, ncandles)
        #[chanceb, valorb, chances, valors, fator de lucro]

        profifTurtle = obj.getProfitFactor(turtleLog[3], turtleLog[1])
        profitInside = obj.getProfitFactor(insideLog[3], insideLog[1])
        profitDoubleUp = obj.getProfitFactor(doubleUpLog[3], doubleUpLog[1])
        profitPivotUp = obj.getProfitFactor(pivotUpLog[3], pivotUpLog[1])


        # RANK
        acerto = obj.GainPercent(turtleLog)
        if profifTurtle <= profitInside and profifTurtle <= profitDoubleUp <= profitPivotUp and acerto >= 0.5:
            obj.insertRank('ContraTurtle', coin, profifTurtle, acerto)

        acerto = obj.GainPercent(insideLog)
        if profitInside < profifTurtle and profitInside < profitDoubleUp <= profitPivotUp and acerto >= 0.5:
            obj.insertRank('InsideBar', coin, profitInside, acerto)
        
        acerto = obj.GainPercent(doubleUpLog)
        if profitDoubleUp < profifTurtle and profitDoubleUp < profitInside <= profitPivotUp and acerto >= 0.5:
            obj.insertRank('DoubleUp', coin, profitDoubleUp, acerto)
        
        acerto = obj.GainPercent(pivotUpLog)
        if profitPivotUp < profitDoubleUp < profifTurtle and profitDoubleUp < profitInside and acerto >= 0.5:
            obj.insertRank('PivotUp', coin, profitPivotUp, acerto)
        





    