from flask import Flask, render_template

app = Flask(__name__)
""" 
@app.route("/<here>/")
def homepage(test):
    test = test.upper()
    return render_template("index.html", my_var = test)
 """


@app.route("/")
def homepage():
    f = open("goods.txt", "r", encoding = "utf-8")
    txt = f.readlines()
    return render_template("index.html", goods = txt)


if __name__ == "__main__":
    app.run()
