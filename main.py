from flask import Flask, render_template, request, Response

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

@app.route('/f.js' , methods = ["GET"])
def f():
    js_code = '''
        function addDiv() {
            const div = document.createElement("div");
            const text = " hi there";
            const divContent = document.createTextNode(text);
            div.appendChild(divContent)

            div.style.color = "red";
            div.style.border = "1px solid green";
            div.style.padding = "4px";
            appDiv = document.querySelector(".App");
            appDiv.appendChild(div);
            }
        
        function add(a, b) {
            return a + b;
        }
        // Export the functions
        window.f = {
            greet: greet,
            add: add,
            addDiv: addDiv
        };
    '''
    return Response(js_code, mimetype='text/javascript')

if __name__ == '__main__':
    app.run(debug = True)