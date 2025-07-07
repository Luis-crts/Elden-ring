from flask import Blueprint, request, redirect, render_template, session, url_for, flash
from app.models import get_connection
from werkzeug.security import generate_password_hash, check_password_hash

auth_bp = Blueprint('auth', __name__)

@auth_bp.route('/')
def login_form():
    return render_template('login.html')

@auth_bp.route('/login', methods=['POST'])
def login():
    correo = request.form['correo']
    contraseña = request.form['contraseña']

    conn = get_connection()
    cursor = conn.cursor(dictionary=True)
    cursor.execute("SELECT * FROM usuarios WHERE correo = %s", (correo,))
    user = cursor.fetchone()
    cursor.close()
    conn.close()

    if user and check_password_hash(user['contraseña'], contraseña):
        session['usuario_id'] = user['id']
        return redirect(url_for('home.dashboard'))
    else:
        flash("Correo o contraseña incorrectos", "error") 
        return redirect(url_for('auth.login_form'))

@auth_bp.route('/registro', methods=['GET', 'POST'])
def registro():
    if request.method == 'POST':
        correo = request.form['correo']
        contraseña = request.form['contraseña']
        repetir = request.form['repetir']

        if contraseña != repetir:
            flash("Las contraseñas no coinciden", "error")  
            return redirect(url_for('auth.registro'))

        hash_pass = generate_password_hash(contraseña)

        conn = get_connection()
        cursor = conn.cursor()
        try:
            cursor.execute("INSERT INTO usuarios (correo, contraseña) VALUES (%s, %s)", (correo, hash_pass))
            conn.commit()
        except:
            flash("El correo ya está registrado", "error")  
            return redirect(url_for('auth.registro'))
        finally:
            cursor.close()
            conn.close()

        flash("Registrado correctamente, ahora puedes iniciar sesión", "exito")  
        return redirect(url_for('auth.login_form'))

    return render_template('registro.html')
