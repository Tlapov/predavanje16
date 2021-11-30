
from flask import Flask, render_template, request, make_response
import datetime


app = Flask(__name__)

@app.route("/")
def index():

    year = datetime.datetime.now().year
    poruka= "Ovo je poruka iz main.py! Hellou"

    gradovi = {"Zagreb", "Split", "Rijeka"}

    user = "Ivo Ivić"

    return render_template("index.html", year=year, poruka=poruka, gradovi=gradovi, user=user)

@app.route("/about", methods=["GET", "POST"])
def about():
    if request.method == "GET":
        user_name = request.cookies.get("user_name")
        return render_template("about.html", name=user_name)
    elif request.method =="POST":
        name = request.form.get("contact-name")
        email = request.form.get("contact-email")
        massage = request.form.get("contact-message")

        print(name)
        print(email)
        print(massage)

        response = make_response(render_template("success.html"))
        response.set_cookie("user_name", name)

        return response
if __name__ == "__main__":
    app.run(use_reloader=True)
