# Importiamo la nostra funzione per prendere la connessione
from app.db import get_db

# Crea un film nel database, prendento titolo, regista e stato di visione
def create_film(titolo, regista, visto):
    """Inserisce un nuovo film."""
    db = get_db()
    try:
        db.execute(
            "INSERT INTO film (title, regista, visto) VALUES (?, ?, ?)",
            (titolo, regista, visto),
        )
        db.commit() # Salviamo le modifiche
        return True
    except db.IntegrityError:
        # Errore: lo username esiste già
        return False

def get_film_visti():
    """Cerca i film visti."""
    db = get_db()
    films = db.execute(
        "SELECT * FROM film WHERE visto = ?", (True,)
    ).fetchall()
    return films

def get_film_da_vedere():
    """Cerca i film da vedere."""
    db = get_db()
    films = db.execute(
        "SELECT * FROM film WHERE visto = ?", (False,)
    ).fetchall()
    return films
