'''
Created on 25/ott/2013

@author: bellini
'''

class tuttiScript(object):
            
        def scriptannullamento(self,pcid,pcde):
            scriptAnnullamento = """
update AWDBA.TB_AZITD_ITERDOC_CL set AZITD_DATA_FINE = sysdate, AZITD_COD_APPL = 'XX' , AZITD_DATA_AGGIORN = SYSDATE
 where AZITD_PCDE_ID_VA_PK = """+str(pcde)+ """ AND AZITD_DATA_FINE = to_date('31/12/9999','dd/mm/yyyy');

insert into AWDBA.TB_AZITD_ITERDOC_CL(AZITD_PCDE_ID_VA_PK, AZITD_AZTST_COD_TIPOSTATO_PK, AZITD_DATA_INIZ_PK, AZITD_COD_UTENTE, AZITD_DATA_AGGIORN, AZITD_COD_APPL, AZITD_FLAG_STATO)
values("""+str(pcde)+""", 11, sysdate, 'AWAZAPPL', sysdate, 'XX', 'A');

update CREATOR.PCDE_DOCENTRA_CL set PCDE_AZMPS_SIT1_VR = 11,PCDE_NOTE_VB = 'Richiesto intervento manuale di invalidazione su SIN', PCDE_BDST_ERI_VR = 1, PCDE_DTVAR_VB = sysdate 
where PCDE_ID_VA = """+str(pcde)+""";

update CREATOR.PCID_INFODOCE_CL set PCID_FLAGVALI_VB  = 'N',
       PCID_DTVAR_VB = SYSDATE,
       PCID_BDST_ERI_VR = 1 
 where PCID_ID_VA = """+str(pcid)+""";
"""
            return scriptAnnullamento

        def scriptannullamentoPCID(self,pcid):
            scriptAnnullamentoPCID = """
update CREATOR.PCID_INFODOCE_CL set PCID_FLAGVALI_VB  = 'N',
       PCID_DTVAR_VB = SYSDATE,
       PCID_BDST_ERI_VR = 1 
 where PCID_ID_VA = """+str(pcid)+""";
 """
            return scriptAnnullamentoPCID
        
       
            
        def scriptannullamentoDocUscita(self,pcdu,pccu):
            scriptAnnullamentoDocUsc = """
INSERT INTO creator.pcsu_stdocusc_cl
           (pcsu_id_va, pcsu_dtora_vb,
            pcsu_note_vb, pcsu_pcdu_ein_vr, pcsu_pcts_edi_vr,
            pcsu_modrec_vb, pcsu_utente_vb, pcsu_dtvar_vb, pcsu_bdst_eri_vr)
VALUES (pcsu_seq.NEXTVAL, SYSDATE,'annullato a mano perche generato per errore',
        """+str(pcdu)+""" , 5, SYSDATE, 'AWAUAPPL', SYSDATE, 1);

UPDATE creator.pccu_comunic_cl
   SET pccu_pcts_hau_vr = 5,
       pccu_bdst_eri_vr = 1,
       pccu_dtvar_vb = SYSDATE,
       pccu_modrec_vb = SYSDATE
WHERE pccu_id_va = """+str(pccu)+""";
            """
            return scriptAnnullamentoDocUsc
        
        def scriptModificaDataNotifica(self,data,pccu,pcdi):
            scriptModificaDataNotifica="""
UPDATE creator.pccu_comunic_cl
   SET PCCU_DATACONS_VB = to_date('"""+str(data)+"""','dd/mm/yyyy'),
       pccu_utente_vb = 'AWAUAPPL',
       pccu_bdst_eri_vr = 1,
       pccu_dtvar_vb = SYSDATE,
       pccu_modrec_vb = SYSDATE,
       pccu_note_vb = null
 WHERE pccu_id_va = """+str(pccu)+"""  

UPDATE AWDBA.TB_AZCRR_CARTOLRIT_CL
   SET AZCRR_DATA_NOTIFICA = to_date('"""+str(data)+"""','dd/mm/yyyy'),
       AZCRR_DATA_AGGIORN = SYSDATE,
       AZCRR_COD_APPL = 'XX'
 WHERE AZCRR_PCID_ID_VA_PK = """+str(pcdi)+""";  """
            return scriptModificaDataNotifica
        
        def scriptArchiviaDocUscita(self,pcsu,pccu,pcdu):
            scriptArchiviaDocUscita="""
INSERT INTO CREATOR.PCSU_STDOCUSC_CL
            (pcsu_id_va, pcsu_dtora_vb,
             pcsu_note_vb, pcsu_pcdu_ein_vr, pcsu_pcts_edi_vr,
             pcsu_modrec_vb, pcsu_utente_vb, pcsu_dtvar_vb, pcsu_bdst_eri_vr
            )
     VALUES (pcsu_seq.NEXTVAL, SYSDATE,
             'archiviato a mano', """+str(pcdu)+""", 10,
             SYSDATE, 'AWAUAPPL', SYSDATE, 1
            );
            
UPDATE CREATOR.PCSU_STDOCUSC_CL 
   SET PCSU_NOTE_VB = 'chiuso manualmente',
       PCSU_BDST_ERI_VR = 1,
       PCSU_DTVAR_VB    = sysdate,
       PCSU_DATAFIN_VB = sysdate
 WHERE PCSU_ID_VA     = """+str(pcsu)+""";

UPDATE CREATOR.PCCU_COMUNIC_CL
   SET pccu_pcts_hau_vr = 10,
       pccu_utente_vb = 'AWAUAPPL',
       pccu_bdst_eri_vr = 1,
       pccu_dtvar_vb = SYSDATE,
       pccu_modrec_vb = SYSDATE
 WHERE pccu_id_va = """+str(pccu)+""";  """
            return scriptArchiviaDocUscita
        
        def scriptAccXmlINS(self,idacc,idacco):
            scriptINSacc="""
INSERT INTO SPDBA.TB_SCREF_REFREPOS_CL (SCREF_SCREP_SEQ_FILE_PK,SCREF_BLOB_FILE,SCREF_COD_UTENTE,SCREF_DATA_AGGIORN,SCREF_COD_APPL)
VALUES("""+str(idacco)+"""),EMPTY_BLOB(),'SPDBA',SYSDATE,'75');

INSERT INTO SPDBA.TB_SCREF_REFREPOS_CL (SCREF_SCREP_SEQ_FILE_PK,SCREF_BLOB_FILE,SCREF_COD_UTENTE,SCREF_DATA_AGGIORN,SCREF_COD_APPL)
VALUES("""+str(idacc)+""",EMPTY_BLOB(),'SPDBA',SYSDATE,'75'); """
            return scriptINSacc
        
        def scriptAccXmlSEL(self,idacc,idacco):
            scriptSELacc="""
SELECT SCREF_BLOB_FILE
FROM SPDBA.TB_SCREF_REFREPOS_CL
WHERE SCREF_SCREP_SEQ_FILE_PK = """+str(idacco)+""";

SELECT SCREF_BLOB_FILE
FROM SPDBA.TB_SCREF_REFREPOS_CL
WHERE SCREF_SCREP_SEQ_FILE_PK = """+str(idacc)+"""; """
            return scriptSELacc

        def scriptAccXmlUPD(self,idacc):
            scriptUPDacc="""
UPDATE SPDBA.TB_SCREP_REPOSITORY_CL
SET SCREP_STAT_ARCHIVIO = 'DB',
SCREP_STAT_ACQUISIZIONE = 'DT',
SCREP_DATA_AGGIORN = SYSDATE,
SCREP_TMST_ACQUISIBILE = '',
SCREP_TMST_ACQUISITO = ''
WHERE SCREP_SEQ_FILE_PK = """+str(idacc)+""";
 """
            return scriptUPDacc
        
        def scriptCambioStatoPrat(self,idprat,sold,snew):
            scriptUPStato ="""
update CREATOR.PCST_STATPRAT_CL set PCST_DAORCHST_VB = SYSDATE, PCST_BDST_ERI_VR = 1, PCST_DTVAR_VB = SYSDATE 
where PCST_PCPR_ERE_VR = """+str(idprat)+""" and PCST_DAORCHST_VB is null and PCST_PCSP_ERI_VR =""" +str(sold)+""";
insert into CREATOR.PCST_STATPRAT_CL (PCST_ID_VA, PCST_BDPS_EVA_VR, PCST_DAORCHST_VB, PCST_DAORVARI_VB, PCST_NOTESTAT_VB, PCST_PCPR_ERE_VR, PCST_PCSP_ERI_VR, PCST_UTENTE_VB, PCST_BDST_ERI_VR, PCST_DTVAR_VB) 
values (PCST_SEQ.NEXTVAL, NULL, NULL, SYSDATE, NULL, """+str(idprat)+""", """+str(snew)+""", 'FAFSAPPL', 1, SYSDATE);
update CREATOR.PCPR_PRATICA_CL set PCPR_PCSP_HAU_VR = """+str(snew)+""", PCPR_BDST_ERI_VR = 1, PCPR_DTVAR_VB = SYSDATE where PCPR_ID_VA = """+str(idprat)+""";
"""
            return scriptUPStato
        

        def scriptCambioDataPres(self,data,pcde,stato,idpratica):
            scriptDataPres ="""
            
UPDATE CREATOR.PCPR_PRATICA_CL set PCPR_DATAVVIO_VB=TO_DATE('"""+str(data)+"""','DD/MM/YYYY'), 
      PCPR_DTVAR_VB = SYSDATE, 
      PCPR_BDST_ERI_VR = 1  
where PCPR_ID_VA = """+str(idpratica)+""";
            
UPDATE AWDBA.TB_AZITD_ITERDOC_CL 
set AZITD_DATA_INIZ_PK = to_date('"""+str(data)+"""','dd/mm/yyyy') ,
    AZITD_COD_APPL = 'XX' , 
    AZITD_DATA_AGGIORN = SYSDATE
where AZITD_PCDE_ID_VA_PK = """+str(pcde)+""" 
  and AZITD_AZTST_COD_TIPOSTATO_PK = """+str(stato)+""";

update CREATOR.PCDE_DOCENTRA_CL 
set PCDE_DATAPRES_VB = to_date('"""+str(data)+"""','dd/mm/yyyy'),
PCDE_NOTE_VB = 'Richiesto intervento manuale data presentazione su SIN', 
PCDE_BDST_ERI_VR = 1, 
PCDE_DTVAR_VB = sysdate 
where PCDE_ID_VA = """+str(pcde)+""";
"""
            return scriptDataPres
        
        def scriptCambioDataPres2(self,data,pcde,stato):
            scriptDataPres2 ="""
            
UPDATE AWDBA.TB_AZITD_ITERDOC_CL 
set AZITD_DATA_INIZ_PK = to_date('"""+str(data)+"""','dd/mm/yyyy') ,
    AZITD_COD_APPL = 'XX' , 
    AZITD_DATA_AGGIORN = SYSDATE
where AZITD_PCDE_ID_VA_PK = """+str(pcde)+""" 
  and AZITD_AZTST_COD_TIPOSTATO_PK = """+str(stato)+""";

update CREATOR.PCDE_DOCENTRA_CL 
set PCDE_DATAPRES_VB = to_date('"""+str(data)+"""','dd/mm/yyyy'),
PCDE_NOTE_VB = 'Richiesto intervento manuale data presentazione su SIN', 
PCDE_BDST_ERI_VR = 1, 
PCDE_DTVAR_VB = sysdate 
where PCDE_ID_VA = """+str(pcde)+""";
"""
            return scriptDataPres2
        
        
        def scriptCambioDataPres3(self,data,pcde):
            scriptDataPres3 ="""
            
update CREATOR.PCDE_DOCENTRA_CL 
set PCDE_DATAPRES_VB = to_date('"""+str(data)+"""','dd/mm/yyyy'),
PCDE_NOTE_VB = 'Richiesto intervento manuale data presentazione su SIN', 
PCDE_BDST_ERI_VR = 1, 
PCDE_DTVAR_VB = sysdate 
where PCDE_ID_VA = """+str(pcde)+""";
"""
            return scriptDataPres3
        
        
        def scriptCambioDataPres4(self,data,pcde,idpratica):
            scriptDataPres4 ="""
            
UPDATE CREATOR.PCPR_PRATICA_CL set PCPR_DATAVVIO_VB=TO_DATE('"""+str(data)+"""','DD/MM/YYYY'), 
      PCPR_DTVAR_VB = SYSDATE, 
      PCPR_BDST_ERI_VR = 1  
where PCPR_ID_VA = """+str(idpratica)+""";
            

update CREATOR.PCDE_DOCENTRA_CL 
set PCDE_DATAPRES_VB = to_date('"""+str(data)+"""','dd/mm/yyyy'),
PCDE_NOTE_VB = 'Richiesto intervento manuale data presentazione su SIN', 
PCDE_BDST_ERI_VR = 1, 
PCDE_DTVAR_VB = sysdate 
where PCDE_ID_VA = """+str(pcde)+""";
"""
            return scriptDataPres4
        
        