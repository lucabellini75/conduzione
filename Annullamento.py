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

contDocUsc   = 0;
contDoc      = 0;
contSoloPcid = 0;
dataCP=[]; 

 
queryCercaPratica = queryOracle.scriptQuery()
esecuzioneScript = tuttiScript.tuttiScript()
scriviOUT = scriviScript() 
etichetta = etichette.Mail()

def lanciaQueryprocessi(queryPro):
    cursI = cursIst.execute(queryPro)            
    return cursI
    
def lanciaQueryAnnulla(query):
    cursB = cursBdu.execute(query)            
    return cursB

def elaboraDatiQueryPcid(curs0,stato,inc,rows):
    pcid = esecuzioneScript.scriptannullamentoPCID(rows[2])
    scriviOUT.scriviScriptInv(pcid, inc)
   
def elaboraDatiQueryDoc(curs0,stato,inc,rows):
    pcidpcde = esecuzioneScript.scriptannullamento(rows[2], rows[3])           
    scriviOUT.scriviScriptInv(pcidpcde, inc)

def elaboraDatiQueryDocUsc(curs0,stato,inc,rows):
    pcidpcde = esecuzioneScript.scriptannullamento(rows[2], rows[3])
    pcdupccu = esecuzioneScript.scriptannullamentoDocUscita(rows[12], rows[13])              
    scriviOUT.scriviScriptInv(pcidpcde+pcdupccu, inc)
    
def controlloCursore(curs0):
    isEmpty = False
    data=curs0.fetchall()
    if data == [(None,)]:
        isEmpty = True
    return isEmpty
    
def elaboraPratiche(pratiche,stato,inc,contDocUsc,contDoc,contSoloPcid):  
    
    print etichetta.etichettaPraticaIntesta()
    
    for pratica in pratiche:
    
        for i in pratica:
            
            query = queryCercaPratica.annullaQS(i)
            cursore = lanciaQueryAnnulla(query)
            
            isEmpty = controlloCursore(cursore)
            
            if not isEmpty:
                cursore = lanciaQueryAnnulla(query)
                for rows in cursore:    
                    if str(rows[8]) == "6" or str(rows[8]) == "4" or str(rows[8]) == "3" or str(rows[8]) == "2":
                        if str(rows[8]) == "2" or str(rows[8]) == "4":             
                            elaboraDatiQueryPcid(cursore,stato,inc,rows)
                            contSoloPcid +=1
                        elif str(rows[8]) == "11":
                            print ('PRATICA GIA'' ANNULLATA!!!! IN STATO '+str(rows[8]))    
                            break                        
                        else:
                            print etichetta.etichettaPratica(rows[0], rows[1], stato)
                            print "SOLO PRATICA!"                     
                            break                        
                    elif rows[11] == None:             
                        elaboraDatiQueryDoc(cursore,stato,inc,rows)  
                        contDoc += 1 
                                   
                    else:                          
                        elaboraDatiQueryDocUsc(cursore,stato,inc,rows)
                        contDocUsc += 1
                            
                print etichetta.etichettaPratica(rows[0], rows[1], stato)
                
            else:
                
                print etichetta.etichettaPratica(rows[0], rows[1], stato)
                print "PRATICA NSI!" 
                
                query = queryCercaPratica.annullaQSNSI(i)
                cursore = lanciaQueryAnnulla(query)
                  
                                    
            queryPro = queryCercaPratica.processiScrivVirt(i,rows[1],rows[3])
            cursoreProcessi = lanciaQueryprocessi(queryPro)
                
            for row in cursoreProcessi:
                dataCP.append([str(row[0])])
            
            
    if contSoloPcid > 0:
        print etichetta.etichettaBancaDatiPCID(inc, contSoloPcid)
    elif contDocUsc > 0:
        print etichetta.etichettaBancaDatiDU(inc, contDocUsc)
    elif contDoc > 0:
        print etichetta.etichettaBancaDati(inc, contDoc)
    

    for item in dataCP:
        print str(item)
            
    dbBDU.close()
    dbIST.close()
    
    
if __name__ == '__main__':
    class mainexecution:
        x = 0
        pratiche=[]
        numbs=raw_input("inserire il numero pratica separato da una virgola: ").split(",")
        pratiche.append(numbs)
        inc = raw_input("Inserire numero INC: ")
        stato = raw_input ("Stato della pratica: ")
        elaboraPratiche(pratiche,stato,inc,contDocUsc,contDoc,contSoloPcid)
       
       
        