import os
from flask import Flask

def create_app():
    # 1. Creiamo l'istanza di Flask
    # instance_relative_config=True dice a Flask: 
    # "Cerca la cartella 'instance' fuori da 'app', non dentro."
    app = Flask(__name__, instance_relative_config=True)

    # 2. Configurazione di base
    # Qui impostiamo le variabili fondamentali.
    app.config.from_mapping(
        # SECRET_KEY serve a Flask per firmare i dati sicuri (es. sessioni).
        # 'dev' va bene per sviluppare, ma in produzione andrà cambiata.
        SECRET_KEY='nicolò',
        # Diciamo a Flask dove salvare il file del database SQLite che contiene i film
        DATABASE=os.path.join(app.instance_path, 'film.sqlite'),
    )

    # --- REGISTRAZIONE BLUEPRINT MAIN ---
    from . import main
    app.register_blueprint(main.bp)
    # --------------------------------

    # --- CONNESSIONE AL DATABASE ---
    from . import db
    db.init_app(app)
    # -----------------------

    # --- REGISTRAZIONE BLUEPRINT AUTH ---
    from . import auth
    app.register_blueprint(auth.bp)
    # --------------------------------

    return app