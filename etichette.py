'''
Created on 28/ott/2013

@author: bellini
'''

class Mail(object):
    
        def etichettaPraticaIntesta(self):
            etichetta_FasPraIntesta = ''' 
Per poter risolvere le segnalazioni  in oggetto si richiede di inviarci gli script di annullamento delle seguenti pratiche:'''
        
            return etichetta_FasPraIntesta
    
        #def etichettaPratica(self,pratica,id,stato):
        #    etichetta_FasPra = ''' 
 
        #   NUMERO PRATICA : '''+str(pratica)+'''
        #   ID PRATICA: '''+str(id)+'''
        #   STATO ANNULLAMENTO: '''+str(stato)

            '''
            '''
        #   return etichetta_FasPra
        
        
        def etichettaBancaDatiDU(self,inc,row):
            etichetta_Gid = ''' 
            Buongiorno,
            per risolvere la segnalazione in oggetto, si richiede di eseguire gli script allegati in ambiente BDUPRO.

            Lo script Invalidazionedomanda_AnnullaDocUscita_'''+inc+'''.sql esegue le seguenti operazioni:

            aggiorna  '''+str(row)+''' record nella tabella AWDBA.TB_AZITD_ITERDOC_CL
            inserisce '''+str(row)+''' record nella tabella  AWDBA.TB_AZITD_ITERDOC_CL
            aggiorna  '''+str(row)+''' record nella tabella CREATOR.PCDE_DOCENTRA_CL
            aggiorna  '''+str(row)+''' record nella tabella CREATOR.PCID_INFODOCE_CL
            aggiorna  '''+str(row)+''' record nella tabella  creator.pcsu_stdocusc_cl
            aggiorna  '''+str(row)+''' record nella tabella  creator.pccu_comunic_cl
            Grazie
            Saluti

            '''
            return etichetta_Gid
        
        def etichettaBancaDati(self,inc,row):
            etichetta_Gid = ''' 
            
            Lo script Invalidazionedomanda_'''+inc+'''.sql esegue le seguenti operazioni:

            aggiorna  '''+str(row)+''' record nella tabella AWDBA.TB_AZITD_ITERDOC_CL
            inserisce '''+str(row)+''' record nella tabella AWDBA.TB_AZITD_ITERDOC_CL
            aggiorna  '''+str(row)+''' record nella tabella CREATOR.PCDE_DOCENTRA_CL
            aggiorna  '''+str(row)+''' record nella tabella CREATOR.PCID_INFODOCE_CL
            
            Grazie
            Saluti

            '''
            return etichetta_Gid
        
        def etichettaBancaDatiPCID(self,inc,row):
            etichetta_Gid = ''' 
            Buongiorno,
            per risolvere la segnalazione in oggetto, si richiede di eseguire gli script allegati in ambiente BDUPRO.

            Lo script Invalidazionedomanda_'''+inc+'''.sql esegue le seguenti operazioni:

            aggiorna  '''+str(row)+''' record nella tabella CREATOR.PCID_INFODOCE_CL
            
            Grazie
            Saluti

            '''
            return etichetta_Gid
        
        def etichettaBancaDatiDataNotifica(self,inc):
            etichetta_Gid = """
            Buongiorno,
            per risolvere la segnalazione in oggetto, si richiede di eseguire gli script allegati in ambiente BDUPRO.

            Lo script aggiornaDataNotifica_"""+inc+""".sql esegue le seguenti operazioni:

            aggiorna  1 record nella tabella AWDBA.TB_AZCRR_CARTOLRIT_CL 
            aggiorna  1 record nella tabella CREATOR.PCCU_COMUNIC_CL 
            
            Saluti."""
            return etichetta_Gid
        
        def etichettaBancaDatiArchDocUsc(self,inc):
            etichetta_Gid = """
            Buongiorno,
            per risolvere la segnalazione in oggetto, si richiede di eseguire gli script allegati in ambiente BDUPRO.

            Lo script archiviaDocUscita_"""+inc+""".sql esegue le seguenti operazioni:

            inserisce 1 record nella tabella CREATOR.PCSU_STDOCUSC_CL
            aggiorna  1 record nella tabella CREATOR.PCSU_STDOCUSC_CL
            aggiorna  1 record nella tabella CREATOR.PCCU_COMUNIC_CL 
            
            Saluti."""
            return etichetta_Gid
        
        def etichettaBancaDatiXML(self,inc):
            etichetta_Gid = """
            Buongiorno,
 
            si richiede con urgenza sul database di manutenzione (ISTMAN) di eseguire gli script in allegato.
 
            Lo script ins_scref_"""+str(inc)+""".sql effettua due inserimenti nel campo blob della tabella SPDBA.TB_SCREF_REFREPOS_CL.
            Lo script sel_scref_"""+str(inc)+""".sql contiene due script per la selezione delle due occorrenze in cui inserire il file xml 2086870.xml (allegato).  
            Lo script upd_screp_"""+str(inc)+""".sql effettua l'aggiornamento di una occorrenza nella tabella SPDBA.TB_SCREP_REPOSITORY_CL.
 
            Tale richiesta serve a correggere in manutenzione una anomalia segnalata.
 
            Si ringrazia per la collaborazione.
 
            Saluti."""
            return etichetta_Gid
        
        def etichettaBancaDatiPraFas(self,inc,row):
            etichetta_Gid = ''' 
            Buongiorno,
            per risolvere la segnalazione in oggetto, si richiede di eseguire gli script allegati in ambiente BDUPRO.

            Lo script ModificaSataoPratica_'''+inc+'''.sql esegue le seguenti operazioni:

            aggiorna  '''+str(row)+''' record nella tabella CREATOR.PCST_STATPRAT_CL
            inserisce '''+str(row)+''' record nella tabella CREATOR.PCST_STATPRAT_CL
            aggiorna  '''+str(row)+''' record nella tabella CREATOR.PCST_STATPRAT_CL
            
            '''
            return etichetta_Gid
        
        def etichettaDataPresentazione(self,inc):
            etichetta_Gid = """
            Buongiorno,
            per risolvere la segnalazione in oggetto, si richiede di eseguire gli script allegati in ambiente BDUPRO.

            Lo script aggiornaDataNotifica_"""+inc+""".sql esegue le seguenti operazioni:

            aggiorna  1 record nella tabella UPDATE AWDBA.TB_AZITD_ITERDOC_CL  
            aggiorna  1 record nella tabella UPDATE CREATOR.PCDE_DOCENTRA_CL 
            
            Saluti."""
            return etichetta_Gid
        
        def lottiInviati(self,now,pdz):
            input_B5lotti = """"""+now.strftime("%d/%m/%Y")+""" """+str(pdz)+""".pdz
            """
            return input_B5lotti
        
        def ricevute(self,now,pdz):
            input_B5ricevute = """"""+now.strftime("%d/%m/%Y")+""" RF170003E99-"""+str(pdz)+""".S00
            """
            return input_B5ricevute
        
        def inputOK(self,data,seq):
            
            lunghezza = len(str(seq))
            
            if (lunghezza == 5):
                lunghezza = str(seq)+" "
            else:
                lunghezza = str(seq)
                
                
            input_B7 = """000000000000 """+lunghezza+"""               LEBANI EVARISTO                                                                          00010  P.ZA C.SFORZA 2 I                            MORICONE RM                                  """+str(data)+""" 0"""
            
            return input_B7