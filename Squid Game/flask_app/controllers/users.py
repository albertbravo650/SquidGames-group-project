from flask_app.models.user import User
from flask_app.models import player
from flask_app import app
from flask import render_template,redirect,request,session,flash

@app.route('/dashboard')
def dashboard():
    if 'user_id' not in session:
        return redirect('/')
    data = {
        'id': session['user_id']
    }
    users_players = User.get_user_with_players(data)
    return render_template('dashboard.html', user=User.getById(data), users_players=users_players)

@app.route('/add')
def new_player():
    if 'user_id' not in session:
        return redirect('/')
    data = {
        'id': session['user_id']
    }
    return render_template('add.html',  user = User.getById(data))

@app.route('/add_player', methods=["POST"])
def add_player():
    if 'user_id' not in session:
        return redirect('/')
    if not player.Player.validate_player(request.form):
        return redirect('/add')
    data = {
        "name" : request.form["name"],
        "age" : request.form["age"],
        "image" : request.form["image"],
        "gender" : request.form["gender"],
        "user_id": session["user_id"]
    }
    player.Player.save(data)
    return redirect('/dashboard')