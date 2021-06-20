from flask_app import app
from flask import render_template, redirect, request, session, flash
from flask_app.models.ninja import Ninja
from flask_app.models.dojo import Dojo

@app.route("/ninjas")
def create_ninja_page():
    dojos = Dojo.get_all()
    return render_template("ninjas.html", all_dojos = dojos)


# @app.route('/create_ninja', methods=["POST"])
# def create_ninja():
#     data = {
#         "id": int(request.form["dojos_id"]),
#         "first_name": request.form["first_name"],
#         "last_name" : request.form["last_name"],
#         "age" : int(request.form["age"])
#     }

@app.route('/create_ninja', methods=["POST"])
def create_ninja():
    data = {
        "id": request.form["dojos_id"],
        "first_name": request.form["first_name"],
        "last_name" : request.form["last_name"],
        "age" : request.form["age"]
    }

    Ninja.saveNinja(data)
    return redirect('/dojos')

# @app.route("/create_user")
# def createpage():
#     return render_template("create_user.html")

# @app.route("/edituser/<int:id>")
# def updaterender(id):
#     data = {
#         "id" : id
#     }
#     users = User.get_one(data)
#     return render_template("update.html", user = users)

# @app.route("/read")
# def readpage():
#     users = User.get_all()
#     print(users)
#     return render_template("read.html", all_users = users)

# @app.route("/read_one/<int:id>")
# def readOnePage(id):
#     data = {
#         "id" : id
#     }
#     users = User.get_one(data)
#     print(users)
#     return render_template("read_one.html", user = users)



# @app.route('/create_user', methods=["POST"])
# def create_user():
#     data = {
#         "fname": request.form["fname"],
#         "lname" : request.form["lname"],
#         "email" : request.form["email"]
#     }

#     User.save(data)
#     return redirect('/read')

