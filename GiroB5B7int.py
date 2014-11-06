from scriviScript import scriviScript
import ConnOra
import etichette
import queryOracle
import tuttiScript
import datetime

amb ="";

cursDB = ConnOra.connDataBase()

def dbistcol():
    dbBDUSVIL = cursDB.connBdusvil()
    dbISTSVIL = cursDB.connIstsvil()
    
    return [dbBDUSVIL,dbISTSVIL]

def ambiente(amb,dbBDUSVIL,dbISTSVIL):
   
#        dbBDUSVIL = cursDB.connBdusvil()
#        dbISTSVIL = cursDB.connIstsvil()
        cursBdu = dbBDUSVIL.cursor()
        cursIst = dbISTSVIL.cursor()
        
        return [cursBdu,cursIst]

queryCercaPccu = queryOracle.scriptQuery()
etichetta = etichette.Mail()
esecuzioneScript = tuttiScript.tuttiScript() 
scriviOUT = scriviScript() 
#isEmpty = True

    
def lanciaQueryDataNot(query,cursori):
    if not cursori[0]:
        resultCurs = cursori[1].execute(query)
        cursori.pop(1)
    else: 
        resultCurs = cursori[0].execute(query) 
        cursori.pop(0)
                               
    return resultCurs

    
    
def elaboraDataNotifica(numbsPCDU,numbsDATA,amb):  
            
        contRigheDatNot = 0
        
        dbambiente = dbistcol()
        cursori = ambiente(amb,dbambiente[0],dbambiente[1])
        
        query = queryCercaPccu.cercaPCCU(numbsPCDU)   
        cursore = lanciaQueryDataNot(query,cursori)     
#        isEmpty = controlloCursore(cursore)
            
#        if not isEmpty:
        for rows in cursore:
            contRigheDatNot +=1
            query =  queryCercaPccu.cercaPOCOM(rows[1])  
            cursorePocom =  lanciaQueryDataNot(query,cursori)   
            for rows in cursorePocom:  
                now = datetime.datetime.now()
                scriviOUT.scriviInputB5Li(etichetta.lottiInviati(now, rows[26]),now)
                scriviOUT.scriviInputB5Do(etichetta.ricevute(now, rows[26]),now)
                scriviOUT.scriviInputB5Rf(rows[26])
                scriviOUT.scriviInputB7(etichetta.inputOK(numbsDATA, rows[0]),now)        
                       
       
            dbambiente[0].close()
            dbambiente[1].close()
             

            
        return "Elaborazione eseguita, controllare la correttezza dei file di OUTPUT!"   


if __name__ == '__main__':
    class mainexecution:
        x = 0
        pratiche=[]
        #ambiente=raw_input("inserire l'ambiente BDUCOL o BDUSVIL")
        numbsPCDU=raw_input("inserire il PCDU: ")
        numbsDATA=raw_input("inserire la DATA GGMMAAAA: ")
        elaboraDataNotifica(numbsPCDU,numbsDATA,ambiente)