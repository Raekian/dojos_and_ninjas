# from flask.templating import render_template
# from mysqlconnection import connectToMySQL
from flask_app.config.mysqlconnection import connectToMySQL

class Ninja:
    def __init__(self, data):
        self.id = data['id']
        self.first_name = data['first_name']
        self.last_name = data['last_name']
        self.age = data['age']
        self.created_at = data['created_at']
        self.updated_at = data['updated_at']

    @classmethod
    def get_all(cls):
        query = "SELECT * FROM ninjas;"
        results = connectToMySQL('dojos_and_ninjas').query_db(query)
        ninjas = []

        for ninja in results:
            # user_data = {
            #     "id" : user["user.id"],
            #     "first_name" : user["user.first_name"],
            #     "last_name" : user["user.last_name"],
            #     "email" : user["user.email"],
            #     "created_at" : user ["user.created_at"],
            #     "updated_at" : user["user.updated_at"]
            # }
            # users.append(user.User(user_data))
            ninjas.append(cls(ninja))
        return ninjas


    @classmethod
    def get_one(cls, data):
        query = "SELECT * FROM ninjas WHERE ninjas.id = %(id)s"
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
    def saveNinja(cls, data):
        query = "INSERT INTO ninjas (dojos_id, first_name , last_name , age , created_at, updated_at ) VALUES ( %(id)s, %(first_name)s , %(last_name)s , %(age)s , NOW() , NOW() );"
        # query = f"INSERT INTO ninjas (dojos_id, first_name , last_name , age , created_at, updated_at ) VALUES ( {data['id']}, '{data['first_name']}' , '{data['last_name']}' , {data['age']} , NOW() , NOW() );"
        return connectToMySQL('dojos_and_ninjas').query_db(query, data)
