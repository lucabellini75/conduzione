import ConnOra
import etichette
import queryOracle
import tuttiScript
import decimal
from scriviScript import scriviScript

cursDB = ConnOra.connDataBase()
dbIST = cursDB.connIstman()
cursBdu = dbIST.cursor()

queryCercaDocArch = queryOracle.scriptQuery()
etichetta = etichette.Mail()
scriviOUT = scriviScript() 
esecuzioneScript = tuttiScript.tuttiScript()

def lanciaQueryDocArch(query):
    resultCursB = cursBdu.execute(query)            
    return resultCursB
    
    
def elaboraArchiviaDocUscita(idacc,inc):  
            
        contRigheDatNot = 0;
        
        query = queryCercaDocArch.accoglienzaXml(idacc)  
            
        cursore = lanciaQueryDocArch(query)     

        for rows in cursore:
            contRigheDatNot +=1                
            scriptAccXml = esecuzioneScript.scriptAccXmlINS(rows[0], rows[2])
            scriptAccXml = esecuzioneScript.scriptAccXmlSEL(rows[0], rows[2])
            scriptAccXml = esecuzioneScript.scriptAccXmlUPD(rows[0])
            scriviOUT.scriviScriptXMLINS(scriptAccXml, inc)
            scriviOUT.scriviScriptXMLSEL(scriptAccXml, inc)   
            scriviOUT.scriviScriptXMLUPD(scriptAccXml, inc)                      
            
        if contRigheDatNot > 0:
            print etichetta.etichettaBancaDatiXML(inc)
        else:
            print "NESSUNA OCCORRENZA TROVATA!!!!"
            
                
        dbIST.close()


if __name__ == '__main__':
    class mainexecution:
        idacc=raw_input("inserire l'ID: ")
        inc = raw_input("Inserire numero INC: ")
        elaboraArchiviaDocUscita(idacc,inc)