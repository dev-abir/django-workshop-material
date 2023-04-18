from flask import Flask, request, make_response, render_template

app = Flask(__name__)


@app.route("/", methods=["GET", "POST"])
def index():
    if request.method == "GET":
        return render_template("index.html")

    if request.method == "POST":
        name = request.form.get("name")
        print("server got name =", name)

        response = make_response(render_template("index.html", name=name))
        response.set_cookie("token", "23")

        return response
