from flask import Flask, render_template, request

app = Flask(__name__)


@app.route('/', methods =["GET", "POST"])

def App():
    if request.method == "POST":
        user_password = request.form.get("password")
        data = user_password
        return render_template('app.html', result = user_password)

    return render_template('app.html')

@app.route('/about', methods =["GET", "POST"])

def About():

    return render_template('about.html')

@app.route('/team', methods =["GET", "POST"])

def Team():

    return render_template('team.html')


if __name__ == '__main__':
    app.run(debug = True)