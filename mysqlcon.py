from flask import Flask ,render_template
from flask_mysqldb import MySQL 


app = Flask(__name__, template_folder='template')
app.config['MYSQL_HOST'] = 'us-cdbr-east-06.cleardb.net' #localhost
app.config['MYSQL_USER']='b1a5a43416daaa'
app.config['MYSQL_PASSWORD']='c00249cd07ca62d'
app.config['MYSQL_DB']='heroku_5e3abbc608c2126'

mysql = MySQL(app)



@app.route('/')
def Home():
    cur = mysql.connection.cursor()
    cur.execute("SELECT * FROM elec_usage ORDER BY account_no DESC LIMIT 1")
    fetchdata = cur.fetchall()
    cur.close()
    return render_template('index.html', data=fetchdata)


if __name__ == "__main__":
    app.run(debug=True)

