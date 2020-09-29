from flask import Flask, render_template, request
import pymysql

app = Flask(__name__)


@app.route("/")
def index():
    return render_template("index.html")


@app.route("/register", methods=['POST', 'GET'])
def register():
    if request.method == 'POST':
        username = request.form['username']
        email = request.form['email']
        phone = request.form['phone']
        id_no = request.form['id_no']
        password = request.form['password']
        gender = request.form['gender']
        country = request.form['country']

        conn = pymysql.connect("localhost", "root", "", "users")
        cursor = conn.cursor()
        sql = "INSERT INTO user (username, email, phone, id_no, password, gender, country) VALUES(%s, %s, %s, %s, %s, " \
              "%s, %s) "
        result = cursor.execute(sql, (username, email, phone, id_no, password, gender, country))
        conn.commit()
        if result:
            return render_template("view.html")
        else:
            return render_template("register.html")
    else:
        return render_template("register.html")


@app.route("/view")
def view():
    conn = pymysql.connect("localhost", "root", "", "users")
    cursor = conn.cursor()
    query = "SELECT * FROM user"
    cursor.execute(query)
    if cursor.rowcount < 1:
        return render_template("view.html", msg="No information found")
    else:
        rows = cursor.fetchall()
        return render_template("view.html", rows=rows)


if __name__ == "__main__":
    app.debug = True
    app.run()