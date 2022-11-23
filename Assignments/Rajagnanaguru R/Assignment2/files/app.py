from flask import Flask, render_template, request, redirect, url_for, session
import ibm_db
import re

dsn_hostname = "815fa4db-dc03-4c70-869a-a9cc13f33084.bs2io90l08kqb1od8lcg.databases.appdomain.cloud"
dsn_uid = "rxz06099"
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


from flask import Flask, render_template, request, redirect, session, url_for
import ibm_db


code for connect:
app.secret_key = 'a'
print("Trying to connect...")
conn = ibm_db.connect("DATABASE=bludb;HOSTNAME=;PORT=30119;SECURITY=SSL;SSLServerCertificate=DigiCertGlobalRootCA.crt;UID=qvk70423;PWD=;", '', '')
print("connected..")


selecting details from db2 table:
    sql = "select * from table_name"
    data = []
    stmt = ibm_db.prepare(conn, sql)
    ibm_db.execute(stmt)
    dictionary = ibm_db.fetch_assoc(stmt)
    while dictionary != False:
        data.append(dictionary)
        dictionary = ibm_db.fetch_assoc(stmt)


sending data to another html file:
return render_template('index.html', data=data)


accessing data in html file using jinja2:
{{ data['key_name'] }}