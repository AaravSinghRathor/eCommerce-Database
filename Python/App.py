from flask import Flask, render_template

app = Flask(__name__)

@app.route("/")
def home():
    return render_template('index.html', styles = 'album.css', bodyclass = 'bg-light')

@app.route("/signup.html")
def signup():
    return render_template('signup.html', styles= 'signin.css', bodyclass= 'text-center')

@app.route("/signin.html")
def login():
    return render_template('signin.html', styles= 'signin.css', bodyclass= 'text-center')

@app.route("/checkout.html")
def checkout():
    return render_template('checkout.html', styles= 'form-validation.css', bodyclass= 'bg-light')

# to run in python
if __name__ == '__main__':
    app.run(debug = True)