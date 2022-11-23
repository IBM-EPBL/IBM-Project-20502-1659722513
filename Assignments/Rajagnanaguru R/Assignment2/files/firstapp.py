from flask import Flask, render_template, request
import ibm_db
import re

## Connection
app = Flask(__name__, template_folder="template")
dsn_hostname = "815fa4db-dc03-4c70-869a-a9cc13f33084.bs2io90l08kqb1od8lcg.databases.appdomain.cloud"
dsn_uid = "*****"
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
    
## Creating db connection
try:
    conn = ibm_db.connect(dsn, "", "")
    print ("Connected to database: ", dsn_database, "as user: ", dsn_uid, "on host: ", dsn_hostname)
except:
    print ("Unable to connect: ", ibm_db.conn_errormsg())


@app.route("/")
def homepage():
    return render_template("registerPage.html")

@app.route("/registration")
def register():
    if request.method == 'GET':
        email1 = request.args.get('iemail')
        user1 = request.args.get('iusern')
        rollno1 = request.args.get('irollno')
        pass1 = request.args.get('ipasswd')

        iquery = ("INSERT INTO STUDENT VALUES(" "'{0}'," "'{1}'," "'{2}'," "'{3}')").format(email1, user1, rollno1, pass1)
        insert_ack = ibm_db.exec_immediate(conn, iquery)

        return "Inserted"+str(insert_ack)
    return request.method

@app.route('/loginpage')
def loginpage():
    return render_template("loginPage.html")

@app.route("/login")
def login():
    if request.method == 'GET':
        email2 = request.args.get('iemail')
        pass2 = request.args.get('ipasswd')

        squery = ("SELECT * FROM STUDENT WHERE(emailid =" "'{0}' AND passwd=" "'{1}')").format(email2, pass2)
        resdata = ibm_db.exec_immediate(conn, squery)

        if ibm_db.fetch_row(resdata) != False:
            return render_template("dashboard.html")
        else:
            return "Incorrect credentials!"
    return "No appropriate method"

if __name__=="__main__":
    app.run()

#python -m flask --app firstapp.py run
