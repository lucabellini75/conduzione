'''
Created on 11/nov/2013

@author: bellini
'''

class scriviScript(object):
   

        def scriviScriptInv(self,script,inc):
            out_file = open("InvalidazioneDomanda_"+inc+".sql","a")
            out_file.write(script)
            out_file.close()
            
        def scriviScriptDatNot(self,script,inc):
            out_file = open("AggiornaDataNotifica_"+inc+".sql","a")
            out_file.write(script)
            out_file.close()
            
        def scriviScriptArchDoc(self,script,inc):
            out_file = open("ArchiviaDocUscita"+inc+".sql","a")
            out_file.write(script)
            out_file.close()
            
        def scriviScriptXMLINS(self,script,inc):
            out_file = open("ins_scref"+inc+".sql","a")
            out_file.write(script)
            out_file.close()
            
        def scriviScriptXMLSEL(self,script,inc):
            out_file = open("sel_scref"+inc+".sql","a")
            out_file.write(script)
            out_file.close()
            
        def scriviScriptXMLUPD(self,script,inc):
            out_file = open("upd_scref"+inc+".sql","a")
            out_file.write(script)
            out_file.close()
            
        def scriviScriptPraFas(self,script,inc):
            out_file = open("ModificaStatoPratica_"+inc+".sql","a")
            out_file.write(script)
            out_file.close()
            
        def scriviDataPres(self,script,inc):
            out_file = open("UpdateDataPresentazione_"+inc+".sql","a")
            out_file.write(script)
            out_file.close()
            
        def scriviInputB5Li(self,script,now):
            out_file = open("LOTTIINVIATI"+now.strftime("%d%m%Y")+".OK","a")
            out_file.write(script)
            out_file.close()
            
        def scriviInputB5Do(self,script,now):
            out_file = open("RICEVUTE."+now.strftime("%d%m%Y"),"a")
            out_file.write(script)
            out_file.close()
            
        def scriviInputB5Rf(self,pdz):
            out_file = open("RF170003E99-"+str(pdz)+".S00","a")
#            out_file.write(script)
            out_file.close()
            
        def scriviInputB7(self,script,now):
            out_file = open("OK"+now.strftime("%d%m%Y")+".TXT","a")
            out_file.write(script)
            out_file.close()