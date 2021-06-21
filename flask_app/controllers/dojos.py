from flask_app import app
from flask import render_template, redirect, request, session, flash
from flask_app.models.dojo import Dojo


@app.route("/dojos")
def ShowDojos():
    dojos = Dojo.get_all()
    print(dojos)
    return render_template("dojos.html", all_dojos = dojos)


@app.route('/create_dojo', methods=["POST"])
def create_dojo():
    data = {
        "name": request.form["name"]
    }

    Dojo.save(data)
    return redirect('/dojos')


@app.route("/dojos/<int:id>")
def dojosandninjas(id):
    data = {
        "id": id
    }
    dojos = Dojo.get_dojos_with_ninjas(data)
    print(dojos)
    return render_template("show.html", dojo = dojos)