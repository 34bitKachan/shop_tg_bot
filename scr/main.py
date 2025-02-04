from flask import Flask, request

app = Flask(__name__)


@app.route("/")
def hello_main_page():
    return '<a href="/cats/">Коты и кошечки</a>'

@app.route("/cats/")
def hello_cats():
    return "catsdshjjefjol"

@app.route("/registry")
def registration():
    return """Регистрация:<br>
    <form>
    <input type='text' name='name'>
    <input type='text' name='answer'>
    <input type='submit' value = 'тык'>
    </form>
    """ + request.args.get("name", 'noname') + request.args.get("answer", '')

if __name__ == "__main__":
    app.run(debug=True, port=15000)