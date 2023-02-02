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
        "users_id": session["user_id"]
    }
    player.Player.save(data)
    return redirect('/dashboard')

@app.route("/edit/<int:id>")
def edit(id):
    if 'user_id' not in session:
        return redirect('/')
    data = {
        "id": id
    }
    print("hi", data)
    onePlayer = player.Player.get_one_player(data)
    print("testinggg",onePlayer.name)
    return render_template("edit.html", onePlayer=onePlayer)

@app.route('/edit_player', methods=['POST'])
def update():
    if 'user_id' not in session:
        return redirect('/')
    id = request.form['id']
    if not player.Player.validate_player(request.form):
        return redirect(f'/edit/{id}')
    player.Player.update(request.form)
    return redirect('/dashboard')

@app.route('/destroy/<int:id>')
def destroy(id):
    if 'user_id' not in session:
        return redirect('/')
    data = {
        "id":id
    }
    player.Player.destroy(data)
    return redirect('/dashboard')

@app.route('/green')
def run():
    if 'user_id' not in session:
        return redirect('/')
    data = {
        "id": 2
    }
    print("hi", data)
    onePlayer = player.Player.get_one_player(data)
    print("testinggg",onePlayer.name)
    return render_template('greenLight.html', onePlayer=onePlayer )

@app.route('/red')
def eliminated():
    if 'user_id' not in session:
        return redirect('/')
    data = {
        "id": 3
    }
    print("hi", data)
    onePlayer = player.Player.get_one_player(data)
    print("testinggg",onePlayer.name)
    return render_template('redLight.html', onePlayer=onePlayer )

@app.route('/fallen')
def fallenStatus():
    if 'user_id' not in session:
        return redirect('/')
    data = {
        "id": 3
    }
    print("hi", data)
    onePlayer = player.Player.get_one_player(data)
    print("testinggg",onePlayer.name)
    return render_template('fallen.html', onePlayer=onePlayer )

@app.route('/winner')
def displayWinner():
    if 'user_id' not in session:
        return redirect('/')
    data = {
        "id": 4
    }
    print("hi", data)
    onePlayer = player.Player.get_one_player(data)
    print("testinggg",onePlayer.name)
    return render_template('win.html', onePlayer=onePlayer )