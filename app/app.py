from flask import Flask, render_template, request, redirect
from models import init_db, TestCase, db

app = Flask(__name__)
app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:///testcases.db"
app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False
db.init_app(app)
init_db(app)

@app.route("/")
def index():
    tests = TestCase.query.all()
    return render_template("index.html", tests=tests)

@app.route("/add", methods=["POST"])
def add_test():
    title = request.form["title"]
    new_test = TestCase(title=title)
    db.session.add(new_test)
    db.session.commit()
    return redirect("/")

@app.route("/update/<int:test_id>/<status>")
def update_status(test_id, status):
    test = TestCase.query.get(test_id)
    test.status = status
    db.session.commit()
    return redirect("/")

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
