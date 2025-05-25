from flask import Flask, render_template

app = Flask(__name__)

@app.route("/")
def home():
    return '''
    <h1>Welcome to Lab 1</h1>
    <ul>
        <li><a href="/Exercise1">Exercise 1 - Linear Equation</a></li>
        <li><a href="/Exercise2">Exercise 2 - Student Info</a></li>
        <li><a href="/Exercise3">Exercise 3 - Form</a></li>
    </ul>
    '''

@app.route("/Exercise1")
def Exercise1():
    x = -2
    y = 5 * x + 7
    return render_template("Exercise1.html", x=x, y=y)

@app.route("/Exercise2")
def Excercise2():
    student = {
        "name": "Ho Phu Loc",
        "student_id": "2374802010288",
        "year": "2023–2027",
        "major": "Information Technology",
        "hobbies": ["Coding", "Play video game", "Play football"]
    }
    return render_template("Exercise2.html", student=student)

@app.route("/Exercise3")
def Exercise3():
    return render_template("Exercise3.html")

if __name__ == "__main__":
    app.run(debug=True)