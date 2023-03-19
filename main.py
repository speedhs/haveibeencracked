from flask import Flask, render_template, request

app = Flask(__name__)


@app.route('/', methods =["GET", "POST"])


def App():
    if request.method == "POST":
        user_password = request.form.get("password")
        data = transform(user_password)
        return render_template('app.html', result = data)

    return render_template('app.html')

@app.route('/about', methods =["GET", "POST"])

def About():

    return render_template('about.html')

@app.route('/team', methods =["GET", "POST"])

def Team():

    return render_template('team.html')

def transform(p):
    return p+"pad"
if __name__ == '__main__':
    app.run(debug = True)