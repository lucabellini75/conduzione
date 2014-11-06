'''
Created on 04/nov/2014

@author: ura
'''
from scriviScript import scriviScript
import ConnOra
import etichette
import queryOracle
import tuttiScript
import decimal

cursDB = ConnOra.connDataBase()
dbBDU = cursDB.connBdupro()
dbIST = cursDB.connIstpro()
cursBdu = dbBDU.cursor()
cursIst = dbIST.cursor()

contPra      = 0;
 
queryCercaPratica = queryOracle.scriptQuery()
esecuzioneScript = tuttiScript.tuttiScript()
scriviOUT = scriviScript() 
etichetta = etichette.Mail()

def lanciaQuery(query):
    cursB = cursBdu.execute(query)            
    return cursB

def elaboraDatiPratFasc(sold,idprat,snew, inc):
    prat = esecuzioneScript.scriptCambioStatoPrat(idprat, sold, snew)
    scriviOUT.scriviScriptPraFas(prat, inc)
    
    
    
def elaboraPratiche(pratiche,stato,inc):  
    
    for pratica in pratiche:
        
        queryPraFas = queryCercaPratica.pratiche(pratica)
        cursorePratiche = lanciaQuery(queryPraFas)
                            
        for rowPr in cursorePratiche:
            elaboraDatiPratFasc(rowPr[0], rowPr[1], stato, inc)
            contPra += 1
        
        
if __name__ == '__main__':
    class mainexecution:
        x = 0
        pratiche=[]
        numbs=raw_input("inserire il numero pratica separato da una virgola: ").split(",")
        pratiche.append(numbs)
        inc = raw_input("Inserire numero INC: ")
        stato = raw_input ("Stato della pratica: ")
        elaboraPratiche(pratiche,stato,inc)
       
    