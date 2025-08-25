# Beep Talkie 📡

**Beep Talkie** est une application web minimaliste et ludique permettant d'envoyer et de recevoir des signaux sonores ("beeps") en temps réel entre deux utilisateurs. Inspiré des talkies-walkies ou du code Morse, ce projet utilise les WebSockets pour une communication instantanée. Chaque utilisateur dispose d'un identifiant unique, et peut envoyer des "beeps" en appuyant sur un bouton poussoir. La durée de l'appui est fidèlement retransmise, permettant une communication basique mais expressive.

---

## 🎯 Fonctionnalités

✅ **Identifiants uniques** : Chaque utilisateur reçoit un ID aléatoire (4 lettres + 4 chiffres) stocké dans un cookie.
✅ **Communication en temps réel** : Transmission instantanée des "beeps" via WebSocket.
✅ **Gestion des appuis** : La durée des appuis (courts ou longs) est mesurée et retransmise.
✅ **Rafraîchissement de l'ID** : Possibilité de régénérer un nouvel ID aléatoire à tout moment.
✅ **Design moderne et responsive** : Interface intuitive adaptée aux mobiles, tablettes et ordinateurs.
✅ **Hébergement local** : Conçu pour être hébergé sur un PC avec tunneling (ngrok, Cloudflare Tunnel).

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

## 🚀 Installation

### 1. Cloner le dépôt

```bash
git clone https://github.com/votre-utilisateur/beep-talkie.git
cd beep-talkie
