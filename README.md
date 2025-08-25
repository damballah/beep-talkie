# Beep Talkie 📡

**Beep Talkie** est une application web minimaliste et ludique permettant d'envoyer et de recevoir des signaux sonores ("beeps") en temps réel entre deux utilisateurs. Inspiré des talkies-walkies ou du code Morse, ce projet utilise les WebSockets pour une communication instantanée. Chaque utilisateur dispose d'un identifiant unique, et peut envoyer des "beeps" en appuyant sur un bouton poussoir. La durée de l'appui est fidèlement retransmise, permettant une communication basique mais expressive.

---

## 🎯 Fonctionnalités

✅ **Identifiants uniques** : Chaque utilisateur reçoit un ID aléatoire (4 lettres + 4 chiffres) stocké dans un cookie. <br>
✅ **Communication en temps réel** : Transmission instantanée des "beeps" via WebSocket. <br>
✅ **Gestion des appuis** : La durée des appuis (courts ou longs) est mesurée et retransmise. <br>
✅ **Rafraîchissement de l'ID** : Possibilité de régénérer un nouvel ID aléatoire à tout moment. <br>
✅ **Design moderne et responsive** : Interface intuitive adaptée aux mobiles, tablettes et ordinateurs. <br>
✅ **Hébergement local** : Conçu pour être hébergé sur un PC avec tunneling (ngrok, Cloudflare Tunnel). <br>

---

## 🛠 Technologies

| Technologie          | Usage                          |
|----------------------|--------------------------------|
| **Flask**            | Backend en Python              |
| **Flask-SocketIO**   | Communication temps réel       |
| **HTML/CSS/JS**      | Frontend et design             |
| **Web Audio API**    | Génération des sons            |
| **Font Awesome**     | Icônes                         |

---

## 📦 Prérequis

- Python 3.11+
- Un navigateur moderne (Chrome, Firefox, Edge, Safari)
- Modules Python : `flask`, `flask-socketio`, `eventlet`

---

## 🚀 Installation et lancement

### 1. Cloner le dépôt

```bash
git clone https://github.com/votre-utilisateur/beep-talkie.git
cd beep-talkie
```

## 2. Installer des dépendences
```bash
pip install flask flask-socketio eventlet
```

## 3. Démarrer le serveur
```bash
python app.py
```
## 4. Accéder à l'application
Ouvrir http://localhost:5000 dans votre navigateur

## 🌐 Utilisation
1. Votre identifiant unique s'affiche automatiquement à l'écran
2. Partagez cet identifiant avec votre correspondant
3. Entrez l'identifiant de votre correspondant dans le champ prévu
4. Appuyez sur le bouton "Beep!" pour envoyer un signal sonore

## 📁 Structure du Projet
beep-talkie/ <br>
├── app.py              # Code serveur Flask <br>
├── templates/ <br>
│   └── index.html      # Interface utilisateur <br>
├── static/ <br>
│   └── styles.css      # Feuille de style <br>
└── README.md           # Documentation <br>

## ⚠️ Limitations Connues
Certains navigateurs bloquent les sons automatiques <br>
→ Solution : Interagir avec la page avant d'envoyer un beep et vérifier que les WebSockets ne sont pas bloqués par un pare-feu <br>

## 📄 Licence
Ce projet est sous licence MIT.


