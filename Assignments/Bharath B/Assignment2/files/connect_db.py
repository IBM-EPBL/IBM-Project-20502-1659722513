# from flask import Flask, render_template, request, redirect, url_for, session
# import re

import ibm_db

dsn_hostname = "815fa4db-dc03-4c70-869a-a9cc13f33084.bs2io90l08kqb1od8lcg.databases.appdomain.cloud"
dsn_uid = "*******"
dsn_pwd = "xw314ojpKtHYpJYh"

dsn_driver = "{IBM DB2 ODBC DRIVER}"
dsn_database = "BLUDB"         
dsn_port = "30367"     
dsn_protocol = "TCPIP"    
dsn_security = "SSL"

#Create the dsn connection string
dsn = (
    "DRIVER={0};"
    "DATABASE={1};"
    "HOSTNAME={2};"
    "PORT={3};"
    "PROTOCOL={4};"
    "UID={5};"
    "PWD={6};"
    "SECURITY={7};").format(dsn_driver, dsn_database, dsn_hostname, dsn_port, dsn_protocol, dsn_uid, dsn_pwd,dsn_security)

print(dsn)

## Creating db connection
try:
    conn = ibm_db.connect(dsn, "", "")
    print ("Connected to database: ", dsn_database, "as user: ", dsn_uid, "on host: ", dsn_hostname)

except:
    print ("Unable to connect: ", ibm_db.conn_errormsg())
    
# app = Flask(__name__)
# app.secret_key = 'a'
# conn = ibm_db.connect("DATABASE=bludb;HOSTNAME=815fa4db-dc03-4c70-869a-a9cc13f33084.bs2io90l08kqb1od8lcg.databases.appdomain.cloud;PORT=30367;SECURITY=SSL;SSLServerCertificate=DigiCertGlobalRootCA.crt;UID=rxz06099;PWD=xw314ojpKtHYpJYh",'','')
# stmt = ibm_db.prepare(conn,sql)
# ibm_db.execute(stmt)
# acc = ibm_db.fetch_assoc(stmt)
# print(acc)

# if __name__ =='__main__':
#     app.run()
