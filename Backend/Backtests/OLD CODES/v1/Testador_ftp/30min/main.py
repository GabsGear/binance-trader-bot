import test
import binance_
import helpers
import botconfig 

def main():
    symbols = binance_.Binance_opr()
    obj = helpers.Helpers()
    teste = test.Testador()

    symbol = symbols.getSymbolList()
    size = len(symbol) - 1
    nErr = 0
    for x in range(0, size):
        obj.progress(x, size-1, status=' Analisando estrategias || ' + str(symbol[x]) + ' passo ' + str(x) + ' de ' + str(size))

        try:
            teste.test(symbol[x], 1)
        except:
             x += 1
             nErr +=1
    print('\n'+ str(nErr) + ' Erros foram encontrados no processo')
    
main()
