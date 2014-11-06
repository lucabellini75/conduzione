'''
Created on 25/ott/2013

@author: bellini
'''

class scriptQuery(object):
    
    def annullaQS(self,numPratica): 
        queryAnnullamentoStatic = """
    select distinct(a.pcpr_numprati_vb) as "NUMERO PRATICA",
       a.pcpr_id_va as "ID PRATICA",
       b.pcid_id_va as "PCID", 
       b.pcid_pcde_com_vr as "PCDE",
       c.PCDE_FLAGACQFUSIS_VB as "FLAG ACQUISIZIONE VB",
       b.pcid_FLAGVALI_VB as "FLAG VALIDITA",
       c.pcde_azmps_sit1_vr as "SIT1",
       f.aztst_descr_tipostato_doc as "DESCRIZIONE SIT1",
       c.pcde_azmps_sit2_vr as "SIT2",
       m.AZMPR_DESCR_MODPRE as "DESCRIZIONE SIT2",
       d.AZALL_PCDE_ID_VA_PK as "(PCDE)ALLEGATO",
       c.PCDE_PCDU_ERI_VR as "DOC.USCITA",
       e.AUDOC_PCCU_ID_VA_PK AS "PCCU",
       e.AUDOC_PCDU_ID_VA_PK AS "PCDU",
       g.PCTD_DESCRIZI_VB as "DESCRIZIONE TIPO DOCUMENTO",
       g.PCTD_FLAGANN_VB as "ANNULLAMENTO DATI SPECIFICI",
       h.PCCT_DES_VB as "CATEGORIA",
       a.PCPR_FLAGPAT_VB as "PATROCINATA"
  from pcpr_pratica_cl a, 
       pcid_infodoce_cl b, 
       pcde_docentra_cl c,
       awdba.tb_azall_allegato_cl d,
       AWDBA.TB_AUDOC_DOCCOMUNIC_CL e,
       AWDBA.TB_AZTST_TIPOSTATO_CT f,
       PCTD_TIDOCUEN_CT g,
       PCCT_CATDOC_CT h,
       AWDBA.TB_AZSDO_SOGGDOC_CL i,
       AWDBA.TB_AZSOG_SOGGETTO_CL l,
       AWDBA.TB_AZMPR_MODPRE_CT m,
       pcsp_tipstpra_ct o,
       AWDBA.TB_AZITD_ITERDOC_CL n
"""

        queryAnnullamentoDynamic = """ 
    where a.pcpr_numprati_vb = '"""+str(numPratica)+"""' 
          and ((a.pcpr_id_va = b.pcid_pcpr_eri_vr)or(a.pcpr_id_va = b.pcid_pcpr_pge_vr))
          and (c.pcde_id_va = b.pcid_pcde_com_vr)
          and d.AZALL_AZDPR_ID_VA (+)= b.pcid_pcde_com_vr
          and e.AUDOC_PCDU_ID_VA_PK (+)=  c.PCDE_PCDU_ERI_VR
          and f.aztst_cod_tipostato_pk = c.pcde_azmps_sit1_vr
          and m.AZMPR_COD_MODPRE_PK = c.pcde_azmps_sit2_vr
          and b.PCID_PCTD_EUN_VR = pctd_id_va
          and h.pcct_id_va = g.PCTD_PCCT_EUN_VR 
          and b.pcid_id_va = l.AZSOG_PCID_ID_VA_PK
          and i.AZSDO_AZSOG_ID_VA_PK = l.AZSOG_PCID_ID_VA_PK
          and a.PCPR_PCSP_HAU_VR = o.PCSP_ID_VA
          and c.pcde_id_va = n.AZITD_PCDE_ID_VA_PK
    order by b.pcid_pcde_com_vr asc

"""

        return queryAnnullamentoStatic+queryAnnullamentoDynamic


    def annullaQSNSI(self,numPratica):
        queryAnnullamentoStaticNSI = """
select distinct(a.pcpr_numprati_vb) as "NUMERO PRATICA",
       a.pcpr_id_va as "ID PRATICA",
       b.pcid_id_va as "PCID", 
       b.pcid_pcde_com_vr as "PCDE",
       b.pcid_FLAGVALI_VB as "FLAG VALIDITA",
       c.pcde_azmps_sit1_vr as "SIT1",
       c.pcde_azmps_sit2_vr as "SIT2",
       c.PCDE_PCDU_ERI_VR as "DOC.USCITA",
       b.PCID_PCTD_EUN_VR as "TIPO DOCUMENTO",
       g.PCTD_DESCRIZI_VB as "DESCRIZIONE TIPO DOCUMENTO",
       g.PCTD_FLAGANN_VB as "ANNULLAMENTO DATI SPECIFICI",
       h.PCCT_DES_VB as "CATEGORIA"
  from pcpr_pratica_cl a, 
       pcid_infodoce_cl b, 
       pcde_docentra_cl c, 
       PCTD_TIDOCUEN_CT g,
       PCCT_CATDOC_CT h 
"""
        queryAnnullamentoDynamicNSI = """ 
  where a.pcpr_numprati_vb = """+str(numPratica)+""" 
      and ((a.pcpr_id_va = b.pcid_pcpr_eri_vr)or(a.pcpr_id_va = b.pcid_pcpr_pge_vr))
      and (c.pcde_id_va = b.pcid_pcde_com_vr)
      and b.PCID_PCTD_EUN_VR = pctd_id_va
      and h.pcct_id_va = g.PCTD_PCCT_EUN_VR 
    order by b.pcid_pcde_com_vr asc

"""
        return queryAnnullamentoStaticNSI+queryAnnullamentoDynamicNSI
    
    
    def processiScrivVirt(self,numPratica,pcde,pcpr):
        processi = """   
SELECT WFISP_ID_ISTANZA_PK
  FROM SPDBA.TB_WFISP_ISTPROCESSO_CL
WHERE
   (WFISP_PCPR_ID_VA = '"""+str(pcpr)+"""' OR
   WFISP_ID_CHIAVE_APPL = 'PCDE_ID_VA_"""+str(pcde)+"""' OR
   WFISP_ID_CHIAVE_APPL = '"""+str(numPratica)+"""'
)and
   WFISP_DATA_FINELAV is null
"""
        return processi
    
    
    def dataNotPCID(self,PCID): 
        queryDataNotPCID = """
    SELECT
    A.AUDOC_PCDU_ID_VA_PK as "PCDU",
    A.AUDOC_PCCU_ID_VA_PK as "PCCU",
    B.PCCU_CODRACCOM_VB as "CODICE RACCOMANDATA",
    B.PCCU_NOTE_VB as "NOTIFICA", 
    C.AZCRR_PCID_ID_VA_PK as "PCID"
    
FROM
    AWDBA.TB_AUDOC_DOCCOMUNIC_CL A,
    CREATOR.PCCU_COMUNIC_CL B,
    AWDBA.TB_AZCRR_CARTOLRIT_CL C

where C.AZCRR_PCID_ID_VA_PK = """+str(PCID)+""" and
      A.AUDOC_PCCU_ID_VA_PK = B.PCCU_ID_VA and
      C.AZCRR_COD_RACCOM = B.PCCU_CODRACCOM_VB
"""
        return queryDataNotPCID 
    
    def dataNotPCDU(self,PCDU): 
        queryDataNotPCDU = """
    SELECT
    A.AUDOC_PCDU_ID_VA_PK as "PCDU",
    A.AUDOC_PCCU_ID_VA_PK as "PCCU",
    B.PCCU_CODRACCOM_VB as "CODICE RACCOMANDATA",
    B.PCCU_NOTE_VB as "NOTIFICA", 
    C.AZCRR_PCID_ID_VA_PK as "PCID"
    
FROM
    AWDBA.TB_AUDOC_DOCCOMUNIC_CL A,
    CREATOR.PCCU_COMUNIC_CL B,
    AWDBA.TB_AZCRR_CARTOLRIT_CL C

where A.AUDOC_PCDU_ID_VA_PK = """+str(PCDU)+""" and
      A.AUDOC_PCCU_ID_VA_PK = B.PCCU_ID_VA and
      C.AZCRR_COD_RACCOM = B.PCCU_CODRACCOM_VB
"""
        return queryDataNotPCDU
    

    def archiviaDocUsc(self,pcdu): 
        queryArchDocUsc = """
SELECT
    A.AUDOC_PCDU_ID_VA_PK as "PCDU",
    A.AUDOC_PCCU_ID_VA_PK as "PCCU",
    B.PCSU_ID_VA as "PCSU",
    B.PCSU_PCTS_EDI_VR as "STATO",
    C.PCTS_DESC_VB 

FROM
    AWDBA.TB_AUDOC_DOCCOMUNIC_CL A, 
    CREATOR.PCSU_STDOCUSC_CL B,
    CREATOR.PCTS_TPSTDUSC_CT C
    
WHERE A.AUDOC_PCDU_ID_VA_PK in("""+str(pcdu)+""") and
      B.PCSU_PCDU_EIN_VR = A.AUDOC_PCDU_ID_VA_PK AND
      B.PCSU_PCTS_EDI_VR = C.PCTS_ID_VA
"""
        return queryArchDocUsc 
    
    def accoglienzaXml(self,idacc): 
        queryAccXml = """
SELECT a.SCREP_SEQ_FILE_PK, a.SCREP_SCFOR_COD_FORMFILE, a.SCREP_SCREP_SEQ_FILE, b.SCFOR_DESCR_FORMFILE 
FROM "SPDBA"."TB_SCREP_REPOSITORY_CL" a,
      "SPDBA"."TB_SCFOR_FORMFILE_CT" b
WHERE (a.SCREP_SEQ_FILE_PK = """+str(idacc)+""" 
   OR a.SCREP_SCREP_SEQ_FILE = """+str(idacc)+"""
  AND (a.SCREP_SCFOR_COD_FORMFILE = b.SCFOR_COD_FORMFILE_PK)
"""
        return queryAccXml 
    
    def pratiche(self,numPratica):
        queryStatoPratica = """ 
 SELECT PCST_PCSP_ERI_VR,b.pcpr_id_va
   FROM PCST_STATPRAT_CL a,
        PCPR_PRATICA_CL b 
  WHERE b.pcpr_numprati_vb = '"""+str(numPratica)+"""'
  AND b.pcpr_id_va = a.PCST_PCPR_ERE_VR
  AND a.PCST_DAORCHST_VB IS NULL"""
  
        return queryStatoPratica
    
    
 #   def dataPresIter(self,PCDE): 
 #       queryPresIter = """
#SELECT AZITD_AZTST_COD_TIPOSTATO_PK
#  FROM AWDBA.TB_AZITD_ITERDOC_CL
#WHERE AZITD_PCDE_ID_VA_PK = """+str(PCDE)+"""
#AND AZITD_DATA_FINE = to_date('31/12/9999','dd/mm/yyyy')"""
      
#        return queryPresIter
    
    def dataPresIter(self,PCDE): 
        queryPresIter = """
SELECT DISTINCT (c.AZITD_DATA_INIZ_PK) as "DPRES",
                 c.AZITD_AZTST_COD_TIPOSTATO_PK as "STATO",
                 a.PCID_PCDE_COM_VR as "PCDE",
                 b.PCPR_ID_VA as "IDPRATICA", 
                 b.PCPR_DATAVVIO_VB as "DAVVIO"

FROM pcid_infodoce_cl a, pcpr_pratica_cl b,AWDBA.TB_AZITD_ITERDOC_CL c

WHERE 
      a.PCID_PCDE_COM_VR in("""+str(PCDE)+""" and((
      a.PCID_PCPR_ERI_VR = b.PCPR_ID_VA) or ( 
      a.PCID_PCPR_PGE_VR = b.PCPR_ID_VA)) and
      c.AZITD_PCDE_ID_VA_PK = a.PCID_PCDE_COM_VR 
      ORDER BY c.AZITD_AZTST_COD_TIPOSTATO_PK
     """
     
        return queryPresIter
     
    def dataAvvio(self,PCDE): 
        queryAvvio = """
       select to_char(b.PCPR_DATAVVIO_VB, 'DD/MM/YYYY')

from pcid_infodoce_cl a, pcpr_pratica_cl b


where a.PCID_PCDE_COM_VR in("""+str(PCDE)+""") and((
      a.PCID_PCPR_ERI_VR = b.PCPR_ID_VA) or ( 
      a.PCID_PCPR_PGE_VR = b.PCPR_ID_VA))
     
     """
      
        return queryAvvio
    
    def cercaPCCU(self,PCDU): 
        queryPCCU = """
SELECT
    A.AUDOC_PCDU_ID_VA_PK as "PCDU",
    A.AUDOC_PCCU_ID_VA_PK as "PCCU"
    
FROM
    AWDBA.TB_AUDOC_DOCCOMUNIC_CL A,
    CREATOR.PCCU_COMUNIC_CL B
 

where A.AUDOC_PCDU_ID_VA_PK = """+str(PCDU)+""" and
      A.AUDOC_PCCU_ID_VA_PK = B.PCCU_ID_VA
"""
        return queryPCCU
    
    def cercaPOCOM(self,PCCU): 
        queryPOCOM = """
SELECT *
      FROM SPDBA.TB_POCOM_COMUNIC_CL
WHERE POCOM_PCCU_ID_VA = """+str(PCCU)+"""
"""
        return queryPOCOM
    
    def cercaPG(self,pgiuridica): 
        queryPG = """
SELECT *
      FROM AWDBA.TB_AZSOG_SOGGETTO_CL
WHERE AZSOG_BDSO_ID_VA = """+str(pgiuridica)+"""
"""
        return queryPG
    
    def cercaPF(self,pfisica): 
        queryPF = """
SELECT *
      FROM AWDBA.TB_AZSOG_SOGGETTO_CL
WHERE AZSOG_BDPS_ID_VA = """+str(pfisica)+"""
"""
        return queryPF
    
    def cercaCF(self,identificaCF): 
        queryCF = """
SELECT *
      FROM AWDBA.TB_AZSOG_SOGGETTO_CL
WHERE AZSOG_COD_FSC_SOGG = """+str(identificaCF)+"""
"""
        return queryCF
    