'''
Created on 05/nov/2013

@author: bellini
'''
import cx_Oracle


#import jaydebeapi
class connDataBase(object):

    def connBdupro(self):
       
        #ip = '10.192.197.11'
        #port = 1521
        #SID = 'BDUPRO'
    
        ip = '10.192.192.112'
        port = 1521
        SID = 'BDUSVIL'
        
        dsn_tns = cx_Oracle.makedsn(ip, port, SID)
        #db = cx_Oracle.connect('UE_LBELLINI', 'revelation', dsn_tns)
        db = cx_Oracle.connect('BDUREAD', 'BDUREAD', dsn_tns)
    
#        curs1 = db.cursor()
        
        return db
        
    def connIstpro(self):
       
        #ip = '10.192.197.1'
        #port = 1536
        #SID = 'ISTPRO1'
        
        ip = '10.192.192.1'
        port = 1523
        SID = 'ISTSVIL'
    
        dsn_tns = cx_Oracle.makedsn(ip, port, SID)
        #db = cx_Oracle.connect('UE_LBELLINI', 'revelation', dsn_tns)
        db = cx_Oracle.connect('BDNREAD', 'BDNREAD', dsn_tns)  
#        curs1 = db.cursor()
        
        return db
    
    def connIstsvil(self):
       
        #ip = '10.192.197.1'
        #port = 1536
        #SID = 'ISTPRO1'
        
        ip = '10.192.192.1'
        port = 1523
        SID = 'ISTSVIL'
    
        dsn_tns = cx_Oracle.makedsn(ip, port, SID)
        #db = cx_Oracle.connect('UE_LBELLINI', 'revelation', dsn_tns)
        db = cx_Oracle.connect('BDNREAD', 'BDNREAD', dsn_tns)  
#        curs1 = db.cursor()
        
        return db
    
    def connBdusvil(self):
       
        #ip = '10.192.197.11'
        #port = 1521
        #SID = 'BDUPRO'
    
        ip = '10.192.192.112'
        port = 1521
        SID = 'BDUSVIL'
        
        dsn_tns = cx_Oracle.makedsn(ip, port, SID)
        #db = cx_Oracle.connect('UE_LBELLINI', 'revelation', dsn_tns)
        db = cx_Oracle.connect('BDUREAD', 'BDUREAD', dsn_tns)
    
#        curs1 = db.cursor()
        
        return db
    
    def connBducol(self):
       
        #ip = '10.192.197.11'
        #port = 1521
        #SID = 'BDUPRO'
    
        ip = '10.192.193.1'
        port = 1521
        SID = 'BDUCOL'
        
        dsn_tns = cx_Oracle.makedsn(ip, port, SID)
        #db = cx_Oracle.connect('UE_LBELLINI', 'revelation', dsn_tns)
        db = cx_Oracle.connect('BDUREAD', 'BDUREAD', dsn_tns)
    
#        curs1 = db.cursor()
        
        return db
    
    def connIstcol(self):
       
        #ip = '10.192.197.1'
        #port = 1536
        #SID = 'ISTPRO1'
        
        ip = '10.192.193.1'
        port = 1523
        SID = 'ISTCOL'
    
        dsn_tns = cx_Oracle.makedsn(ip, port, SID)
        #db = cx_Oracle.connect('UE_LBELLINI', 'revelation', dsn_tns)
        db = cx_Oracle.connect('BDNREAD', 'BDNREAD', dsn_tns)  
#        curs1 = db.cursor()
        
        return db
    
    
    def connIstman(self):
       
        ip = '10.192.192.9'
        port = 1536
        SID = 'ISTMAN'


        dsn_tns = cx_Oracle.makedsn(ip, port, SID)
        db = cx_Oracle.connect('bdnread', 'bdnread', dsn_tns)
    
#        curs1 = db.cursor()
        
        return db