from flask import Flask, render_template, request, redirect, url_for, session, flash, jsonify
from werkzeug.security import generate_password_hash, check_password_hash
from flask_session import Session
from app.web.__user_config import Config


class NovaViewFlask:
    def __init__(self):
        self.app = Flask(__name__)

        self.conf = Config

        self._configure_session()
        self._configure_routes()

    def _configure_session(self):
        self.app.config['SECRET_KEY'] = self.conf.SECRET_KEY
        self.app.config['SESSION_TYPE'] = self.conf.SESSION_TYPE
        Session(self.app)

        print(f"secret key: {self.app.config['SECRET_KEY']}, session type: {self.app.config['SESSION_TYPE']}")

    def _configure_routes(self):
        @self.app.route('/')
        def index():
            if 'username' in session:
                theme = session.get('theme', 'light')  # Par défaut, c'est le light mode
                background = session.get('custom_background', None)
                nav = session.get('custom_nav', None)
                text = session.get('custom_text', None)
                return render_template("index.html", title="Home", theme=theme, custom_color=[background, nav, text])
            return redirect(url_for('login'))

        # Page de connexion
        @self.app.route('/login', methods=['GET', 'POST'])
        def login():
            if request.method == 'POST':
                users_db = self.conf.USERS
                username = request.form['username']
                password = request.form['password']

                # Vérifier si l'utilisateur existe dans la "base de données"
                if username in users_db and check_password_hash(users_db[username], password):
                    session['username'] = username  # Enregistrer l'utilisateur dans la session
                    return redirect(url_for('index'))  # Rediriger vers la page d'accueil
                else:
                    flash('Nom d\'utilisateur ou mot de passe incorrect!', 'danger')

            theme = session.get('theme', 'light')  # Par défaut, c'est le light mode
            background = session.get('custom_background', None)
            nav = session.get('custom_nav', None)
            text = session.get('custom_text', None)
            return render_template('login.html', title="Log In", theme=theme, custom_color=[background, nav, text])

        # Page de déconnexion
        @self.app.route('/logout')
        def logout():
            session.pop('username', None)  # Supprimer l'utilisateur de la session
            return redirect(url_for('login'))

        @self.app.route('/network')
        def network():
            if 'username' in session:
                theme = session.get('theme', 'light')  # Par défaut, c'est le light mode
                background = session.get('custom_background', None)
                nav = session.get('custom_nav', None)
                text = session.get('custom_text', None)
                return render_template("network.html", title="Network", theme=theme, custom_color=[background, nav, text])
            return redirect(url_for('login'))

        @self.app.route('/processus')
        def processus():
            if 'username' in session:
                theme = session.get('theme', 'light')  # Par défaut, c'est le light mode
                background = session.get('custom_background', None)
                nav = session.get('custom_nav', None)
                text = session.get('custom_text', None)
                return render_template("processus.html", title="Process", theme=theme, custom_color=[background, nav, text])
            return redirect(url_for('login'))

        @self.app.route('/system')
        def system():
            if 'username' in session:
                theme = session.get('theme', 'light')  # Par défaut, c'est le light mode
                background = session.get('custom_background', None)
                nav = session.get('custom_nav', None)
                text = session.get('custom_text', None)
                return render_template("system.html", title="System", theme=theme, custom_color=[background, nav, text])
            return redirect(url_for('login'))

        @self.app.route('/setting', methods=['GET', 'POST'])
        def setting():
            if 'username' in session:
                if request.method == 'GET':
                    theme = session.get('theme', 'light')  # Par défaut, c'est le light mode
                    background = session.get('custom_background', None)
                    nav = session.get('custom_nav', None)
                    text = session.get('custom_text', None)
                    return render_template('setting.html', title="Setting", theme=theme, custom_color=[background, nav, text])
                elif request.method == 'POST':
                    session['theme'] = request.form.get('theme')
                    session['custom_background'] = request.form.get('custom_background')
                    session['custom_nav'] = request.form.get('custom_nav')
                    session['custom_text'] = request.form.get('custom_text')
                    return redirect(url_for('setting'))
            return redirect(url_for('login'))

        @self.app.route('/api/status', methods=['GET'])
        def status():
            # Exemples de données fictives pour test
            return jsonify({
                "cpu": "15%",
                "ram": "45%",
                "gpu": "10%",
                "disks": [{"name": "C:", "usage": "60%"}],
            })

    def run(self, host="127.0.0.1", port=5000, debug=False):
        self.app.run(host=host, port=port, debug=debug)


# Lancement si exécuté seul
if __name__ == "__main__":
    app_instance = NovaViewFlask()
    app_instance.run(port=5000)
