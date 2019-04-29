from flask import Flask, render_template, request

import pymysql.cursors



# do hard refresh on web page if something not loading
app = Flask(__name__)



@app.route("/")
def home():
    return render_template('index.html', styles = 'album.css', bodyclass = 'bg-light')

@app.route("/signup.html", methods = ['GET', 'POST'])
def signup():
    if request.method == 'POST':
        idn = 0
        # Connect to the database
        client = pymysql.connect("localhost", "public", "password123", "eCommerce")
        name = request.form['firstName']
        email = request.form['email']
        password = request.form['password']
        phone = request.form['phone']
        print(name, email, password, phone)
        try:
            idn += 1
            cursor = client.cursor()
            query = "INSERT INTO Person(ID, Email, Named, DateOfBirth, Phone, Address, DateJoined, IsEmployee)\
                values(%s, %s, %s, %s, %s, %s, %s, %s)"
            cursor.execute(query, (idn, email, name, '1998-11-25', phone, 'Ithaca', '1998-11-25', 'N'))
            client.commit()
        except Exception:
            print('h')
            client.rollback()
        finally:
            client.close()
    else:
        print("error")
    return render_template('signup.html', styles= 'signin.css', bodyclass= 'text-center')

@app.route("/signin.html")
def login():
    return render_template('signin.html', styles= 'signin.css', bodyclass= 'text-center')

@app.route("/checkout.html")
def checkout():
    return render_template('checkout.html', styles= 'form-validation.css', bodyclass= 'bg-light')

@app.route("/shop.html")
def shop():
    return render_template('shop.html', styles= '', bodyclass= 'bg-light')

@app.route("/item.html")
def item():
    return render_template('item.html', styles= '', bodyclass= 'bg-light')

# to run in python
if __name__ == '__main__':
    app.run(debug = True)