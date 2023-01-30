from flask_app.config.mysqlconnection import connectToMySQL
from flask import flash
import re
# from flask_bcrypt import Bcrypt


# bcrypt = Bcrypt(app)
EMAIL_REGEX = re.compile(r'^[a-zA-Z0-9.+_-]+@[a-zA-Z0-9._-]+\.[a-zA-Z]+$')
NAME_REGEX = re.compile(r'^[a-zA-Z -]+$')

mydb = 'SquidGames'

class User:
    def __init__(self, data):
        self.id = data['id']
        self.first_name = data['first_name']
        self.last_name = data['last_name']
        self.email = data['email']
        self.password = data['password']
        self.created_at = data['created_at']
        self.updated_at = data['updated_at']
        self.players = []


    @classmethod
    def save(cls, data):
        query = '''INSERT INTO users 
        ( first_name,  last_name, email, 
        password, created_at, updated_at ) 
        VALUES ( %(first_name)s , %(last_name)s, 
        %(email)s, %(password)s, NOW() , NOW() );'''
        # data is a dictionary that will be passed into the save method from server.py
        return connectToMySQL(mydb).query_db( query, data )

    @classmethod
    def getById(cls, data):
        query = ''' SELECT *
        FROM users WHERE id = %(id)s;'''
        results = connectToMySQL(mydb).query_db( query, data )
        print(results)
        return cls(results[0])

    @classmethod
    def get_by_email(cls,data):
        query = '''SELECT * FROM users 
        WHERE email = %(email)s;'''
        result = connectToMySQL(mydb).query_db(query,data)
        # Didn't find a matching user
        if len(result) < 1:
            return False
        return cls(result[0])

    @staticmethod
    def validate_registration(user):
        is_valid = True # we assume this is true

        # First Name Validations
        if len(user['first_name']) < 1:
            flash("Please Enter First Name.", 'regError')
            is_valid = False
        elif len(user['first_name']) < 2:
            flash("First Name must be at least 2 characters.", 'regError')
            is_valid = False
        elif not NAME_REGEX.match(user['first_name']):
            flash("First name requires letters only", 'regError')
            is_valid = False

        # Last Name Validations
        if len(user['last_name']) < 1:
            flash("Please Enter Last Name.", 'regError')
            is_valid = False    
        elif len(user['last_name']) < 2:
            flash("Last Name must be at least 2 characters.", 'regError')
            is_valid = False
        elif not NAME_REGEX.match(user['last_name']):
            flash("Last name requires letters only", 'regError')
            is_valid = False

        # Email Validations
        if len(user['email']) < 1:
            flash("Please Enter An Email Address", 'regError')
            is_valid = False
        elif not EMAIL_REGEX.match(user['email']): 
            flash("Invalid email address!", 'regError')
            is_valid = False

        # Password Validation
        if len (user['password']) < 8:
            flash("Password must be at least 8 characters.", 'regError')
            is_valid = False
        if len (user['confirm_password']) < 1:
            flash("Please Confirm Your Password.", 'regError')
            is_valid = False
        elif (user['password'])!= (user['confirm_password']):
            flash("Passwords Do Not Match.", 'regError')
            is_valid = False
        return is_valid