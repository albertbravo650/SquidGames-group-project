from flask_app.config.mysqlconnection import connectToMySQL
from flask import flash

db = "squidgames"

class Player:
    def __init__(self , db_data ):
        self.id = db_data['id']
        self.name = db_data['name']
        self.age = db_data['age']
        self.image = db_data['image']
        self.gender = db_data['gender']
        self.created_at = db_data['created_at']
        self.updated_at = db_data['updated_at']
        self.players = []

    @classmethod
    def save( cls , data ):
        query = "INSERT INTO players (name, age, image, gender, created_at, updated_at, users_id) VALUES (%(name)s, %(age)s, %(image)s, %(gender)s, NOW(), NOW(), %(users_id)s);"
        return connectToMySQL(db).query_db( query, data)

    @classmethod
    def get_all(cls):
        query = "SELECT * FROM players;"
        results = connectToMySQL(db).query_db(query)
        players = []
        for player in results:
            players.append(cls(player))
        return players

    @classmethod
    def get_one_player(cls, data):
        query = "SELECT * FROM players WHERE id = %(id)s;"
        # print(data)
        result = connectToMySQL(db).query_db(query, data)
        # print(result)
        return cls(result[0])

    @staticmethod
    def validate_player(player):
        is_valid = True # we assume this is true
        if len(player['name']) < 1:
            flash("Name cannot be blank", "add_player")
            is_valid = False
        if (int(player['age'])) <= 0:
            flash("Enter age", "add_player")
            is_valid = False
        if len(player['image']) < 1:
            flash("Image URL cannot be blank", "add_player")
            is_valid = False
        return is_valid

    @classmethod
    def destroy(cls, data):
        query = "DELETE FROM players WHERE id = %(id)s;"
        return connectToMySQL(db).query_db(query, data)

    @classmethod
    def update(cls, data):
        query = "UPDATE players SET name=%(name)s, age=%(age)s, image=%(image)s, gender=%(gender)s, updated_at=NOW() WHERE id = %(id)s;"
        # data is a dictionary that will be passed into the save method from server.py
        return connectToMySQL(db).query_db(query, data)