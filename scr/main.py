from flask import Flask

app = Flask(__name__)


@app.route("/")
def hello_main_page():
    return '<a href="/cats/">Коты и кошечки</a>'

@app.route("/cats/")
def hello_cats():
    return "catsdshjjefjol"



if __name__ == "__main__":
    app.run(debug=True, port=15000)