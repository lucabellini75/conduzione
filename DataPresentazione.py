from scriviScript import scriviScript
import ConnOra
import etichette
import queryOracle
import tuttiScript
from datetime import *
import decimal

cursDB = ConnOra.connDataBase()
dbBDU = cursDB.connBdupro()
cursBdu = dbBDU.cursor()

queryCercaDataPres = queryOracle.scriptQuery()
etichetta = etichette.Mail()
esecuzioneScript = tuttiScript.tuttiScript() 
scriviOUT = scriviScript() 
#isEmpty = True

isDataAvvio = False;
isDataPres = False;
    
def lanciaQueryData(query):
    print query
    resultCursB = cursBdu.execute(query)            
    return resultCursB
    
#def controlloCursore(cursBdu):
#    data=cursBdu.fetchall()
#    if data <> [(None,)]:
#        isEmpty = False
#    return isEmpty
    
    
def elaboraDataPresentazione(numbsPCDE,numbsDATA,inc,):  
            
        contRigheDatPres = 0;
        query = queryCercaDataPres.dataAvvio(numbsPCDE)
        cursore = lanciaQueryData(query)
        
        for rows in cursore:
        
            data_avvio = datetime.strptime(rows[4], "%d/%m/%y")     
            
            if (data_avvio == numbsDATA):
                isDataAvvio = True
             
         
        query = queryCercaDataPres.dataPresIter(numbsPCDE)
        cursore = lanciaQueryData(query)
        
        for rows in cursore:
            
            data_pres = datetime.strptime(rows[0], "%d/%m/%y")
            
            if (data_pres == numbsDATA):
                isDataPres = True
            
                
               
        if isDataAvvio and isDataPres:
            scriptDataPres = esecuzioneScript.scriptCambioDataPres(numbsDATA,numbsPCDE,rows[0],rows[4])
        elif isDataAvvio and not isDataPres:
            scriptDataPres = esecuzioneScript.scriptCambioDataPres4(numbsDATA,numbsPCDE,rows[0],rows[4])
        elif not isDataAvvio and not isDataPres:
            scriptDataPres = esecuzioneScript.scriptCambioDataPres3(numbsDATA,numbsPCDE,rows[0],rows[4])
        elif not isDataAvvio and isDataPres:      
            scriptDataPres = esecuzioneScript.scriptCambioDataPres2(numbsDATA,numbsPCDE,rows[1])
                
                
        scriviOUT.scriviDataPres(scriptDataPres,inc)                         
            
        if contRigheDatPres > 0:
            print etichetta.etichettaDataPresentazione(inc)
        else:
            print "NESSUNA OCCORRENZA TROVATA!!!!"
            
                
        dbBDU.close()




if __name__ == '__main__':
    class mainexecution:
        x = 0
        pratiche=[]
        numbsPCDE=raw_input("inserire il PCDE: ")
        numbsDATA=raw_input("inserire la DATA: ")
        inc = raw_input("Inserire numero INC: ")
        elaboraDataPresentazione(numbsPCDE, numbsDATA, inc)