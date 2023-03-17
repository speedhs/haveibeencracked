from flask import Flask, render_template, request

app = Flask(__name__)


@app.route('/', methods =["GET", "POST"])

def App():
    if request.method == "POST":
        password = request.form.get("password")
        print(password)
    return render_template('app.html')





if __name__ == '__main__':
    app.run(debug = True)