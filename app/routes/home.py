from flask import Blueprint, render_template, session, redirect, url_for

home_bp = Blueprint('home', __name__)

@home_bp.route('/dashboard')
def dashboard():
    if 'usuario_id' not in session:
        return redirect(url_for('auth.login_form'))
    return render_template('index.html')
