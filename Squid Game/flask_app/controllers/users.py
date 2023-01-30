from flask_app.models.user import User
from flask_app import app
from flask import render_template,redirect,request,session,flash

@app.route('/dashboard')
def dashboard():
    if 'user_id' in session:

        return render_template('dashboard.html', 
            user = User.getById({'id': session['user_id']}))
    return redirect('/')