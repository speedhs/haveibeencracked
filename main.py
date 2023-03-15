from flask import Flask, render_template, request, url_for

app = Flask(__name__)


@app.route('/', methods =["GET", "POST"])

def App():
    if request.method == "POST":
        password = request.form.get("password")
        print(password)
    return render_template('App.html')

@app.route('/About')

def About():

    return render_template('About.html')

@app.route('/Team')

def Team():

    return render_template('Team.html')


if __name__ == '__main__':
    app.run(debug = True)