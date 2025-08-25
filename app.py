from flask import Flask, render_template, request, make_response
from flask_socketio import SocketIO, emit
import random
import string
from datetime import datetime

app = Flask(__name__)
app.config['SECRET_KEY'] = 'votre_cle_secrete'
socketio = SocketIO(app, cors_allowed_origins="*")

# Dictionnaire pour stocker les connexions actives
active_connections = {}

def generate_unique_id():
    # Génère un ID aléatoire de 8 caractères (4 lettres et 4 chiffres)
    chars = string.ascii_uppercase + string.digits
    return ''.join(random.choice(chars) for _ in range(8))

@app.route('/')
def index():
    # Vérifie si l'utilisateur a déjà un ID dans les cookies
    user_id = request.cookies.get('user_id')
    if not user_id:
        user_id = generate_unique_id()
    resp = make_response(render_template('index.html', user_id=user_id))
    resp.set_cookie('user_id', user_id, max_age=365*24*60*60)  # 1 an
    return resp

@socketio.on('connect')
def handle_connect():
    user_id = request.cookies.get('user_id')
    if user_id:
        active_connections[user_id] = request.sid
        print(f"Utilisateur connecté : {user_id}")

@socketio.on('disconnect')
def handle_disconnect():
    user_id = request.cookies.get('user_id')
    if user_id and user_id in active_connections:
        del active_connections[user_id]
        print(f"Utilisateur déconnecté : {user_id}")

@socketio.on('send_beep')
def handle_send_beep(data):
    sender_id = request.cookies.get('user_id')
    recipient_id = data.get('recipient_id')
    duration = data.get('duration', 0.1)  # Durée en secondes

    if recipient_id in active_connections:
        emit('receive_beep', {'duration': duration}, room=active_connections[recipient_id])
        print(f"Beep envoyé de {sender_id} à {recipient_id} (durée: {duration}s)")

if __name__ == '__main__':
    socketio.run(app, debug=True, host='0.0.0.0', port=5000)
