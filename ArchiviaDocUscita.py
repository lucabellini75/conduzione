from scriviScript import scriviScript
import ConnOra
import etichette
import queryOracle
import tuttiScript
import decimal

cursDB = ConnOra.connDataBase()
dbBDU = cursDB.connBdupro()
cursBdu = dbBDU.cursor()
scriviOUT = scriviScript() 

queryCercaDocArch = queryOracle.scriptQuery()
etichetta = etichette.Mail()
esecuzioneScript = tuttiScript.tuttiScript() 

def lanciaQueryDocArch(query):
    resultCursB = cursBdu.execute(query)            
    return resultCursB
    
    
def elaboraArchiviaDocUscita(numbsPCDU,inc):  
            
        contRigheDatNot = 0;
        
        query = queryCercaDocArch.archiviaDocUsc(numbsPCDU)  
            
        cursore = lanciaQueryDocArch(query)     

        for rows in cursore:
            if rows[4] == "Annullato":
                contRigheDatNot +=1                
                scriptArchDoc = esecuzioneScript.scriptArchiviaDocUscita(rows[2], rows[1], numbsPCDU)
                scriviOUT.scriviScriptArchDoc(scriptArchDoc,inc)                         
            
        if contRigheDatNot > 0:
            print etichetta.etichettaBancaDatiArchDocUsc(inc)
        else:
            print "NESSUNA OCCORRENZA TROVATA!!!!"
            
                
        dbBDU.close()


if __name__ == '__main__':
    class mainexecution:
        numbsPCDU=raw_input("inserire il PCDU: ")
        inc = raw_input("Inserire numero INC: ")
        elaboraArchiviaDocUscita(numbsPCDU,inc)