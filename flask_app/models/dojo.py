# from flask.templating import render_template
# from mysqlconnection import connectToMySQL
from flask_app.config.mysqlconnection import connectToMySQL
from flask_app.models import ninja

class Dojo:
    def __init__(self, data):
        self.id = data['id']
        self.name= data['name']
        self.created_at = data['created_at']
        self.updated_at = data['updated_at']
        self.ninjas = []

    @classmethod
    def get_all(cls):
        query = "SELECT * FROM dojos;"
        results = connectToMySQL('dojos_and_ninjas').query_db(query)
        dojos = []

        for dojo in results:
            # user_data = {
            #     "id" : user["user.id"],
            #     "first_name" : user["user.first_name"],
            #     "last_name" : user["user.last_name"],
            #     "email" : user["user.email"],
            #     "created_at" : user ["user.created_at"],
            #     "updated_at" : user["user.updated_at"]
            # }
            # users.append(user.User(user_data))
            dojos.append(cls(dojo))
        return dojos


    @classmethod
    def get_dojos_with_ninjas(cls, id):
        query = f"SELECT * FROM ninjas JOIN dojos on ninjas.dojos_id = dojos.id WHERE ninjas.dojos_id = {id};"
        # query = "SELECT * FROM ninjas JOIN dojos on ninjas.dojos_id = dojos.id WHERE ninjas.dojos_id = %(id)s;"
        results = connectToMySQL('dojos_and_ninjas').query_db(query)
        return results
        # dojo  = results[0]
        # for ninja in results:
        #     ninja_data = {
        #         "id" : ninja["id"],
        #         "first name" : ninja["ninjas.first_name"],
        #         "last name" : ninja["ninjas.last_name"],
        #         "age" : ninja["ninjas.age"],
        #         "created_at" : ninja["ninja.created_at"],
        #         "updated_at" : ninja["ninja.updated_at"]
        #     }
        #     dojo.ninjas.append( ninja.Ninja(ninja_data))
        # return dojo




    @classmethod
    def get_one(cls, data):
        query = "SELECT * FROM users WHERE dojos.id = %(id)s"
        results = connectToMySQL('dojos_and_ninjas').query_db(query, data)
        return cls (results[0])

        # for user in results:
        #     user_data = {
        #         "id" : user["user.id"],
        #         "first_name" : user["user.first_name"],
        #         "last_name" : user["user.last_name"],
        #         "email" : user["user.email"],
        #         "created_at" : user ["user.created_at"],
        #         "updated_at" : user["user.updated_at"]
        #     }
        # return user_data.id
        print(results)



    @classmethod
    def save(cls, data):
        query = "INSERT INTO dojos (name , created_at, updated_at ) VALUES ( %(name)s, NOW() , NOW() );"
        return connectToMySQL('dojos_and_ninjas').query_db(query, data)



