from scriviScript import scriviScript
import ConnOra
import etichette
import queryOracle
import tuttiScript
import decimal

cursDB = ConnOra.connDataBase()
dbBDU = cursDB.connBdupro()
cursBdu = dbBDU.cursor()

queryCercaDataNot = queryOracle.scriptQuery()
etichetta = etichette.Mail()
esecuzioneScript = tuttiScript.tuttiScript() 
scriviOUT = scriviScript() 
#isEmpty = True

    
def lanciaQueryDataNot(query):
    resultCursB = cursBdu.execute(query)            
    return resultCursB
    
#def controlloCursore(cursBdu):
#    data=cursBdu.fetchall()
#    if data <> [(None,)]:
#        isEmpty = False
#    return isEmpty
    
def controlloPcidPcdu(numbsPCID,numbsPCDU):
    if numbsPCID == "":
        return numbsPCDU
    else:
        return numbsPCID
    
def elaboraDataNotifica(numbsPCID,numbsPCDU,numbsDATA,inc,):  
            
        contRigheDatNot = 0;
        
        iddu = controlloPcidPcdu(numbsPCID,numbsPCDU)
        
        if numbsPCDU == "":
            query = queryCercaDataNot.dataNotPCID(iddu)
        else:
            query = queryCercaDataNot.dataNotPCDU(iddu)
            
        cursore = lanciaQueryDataNot(query)     
#        isEmpty = controlloCursore(cursore)
            
#        if not isEmpty:
        for rows in cursore:
            contRigheDatNot +=1                
            scriptDataNot = esecuzioneScript.scriptModificaDataNotifica(numbsDATA,rows[1],rows[4])
            scriviOUT.scriviScriptDatNot(scriptDataNot,inc)                         
            
        if contRigheDatNot > 0:
            print etichetta.etichettaBancaDatiDataNotifica(inc)
        else:
            print "NESSUNA OCCORRENZA TROVATA!!!!"
            
                
        dbBDU.close()




if __name__ == '__main__':
    class mainexecution:
        x = 0
        pratiche=[]
        numbsPCID=raw_input("inserire il PCID: ")
        numbsPCDU=raw_input("inserire il PCDU: ")
        numbsDATA=raw_input("inserire la DATA: ")
        inc = raw_input("Inserire numero INC: ")
        elaboraDataNotifica(numbsPCID,numbsPCDU,numbsDATA,inc,)