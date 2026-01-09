# app/main.py
#from flask import Blueprint, render_template
from flask import (
    Blueprint, flash, g, redirect, render_template, request, session, url_for
)
from werkzeug.security import check_password_hash, generate_password_hash
from app.repositories import film_repository

bp = Blueprint('main', __name__)

@bp.route('/')
def index():
    # Chiamiamo il Repository
    success = film_repository.get_film_visti()
    film_visti = []
    for film in success:
        film_visti.append(film['title'] + " - " + film['regista'])

    film_da_vedere = []
    success = film_repository.get_film_da_vedere()
    for film in success:
        film_da_vedere.append(film['title'] + " - " + film['regista'])

    # Passiamo la variabile 'film_visti' al template
    return render_template('index.html', filmv=film_visti, filmdavedere=film_da_vedere)

@bp.route('/creafilm', methods=('GET', 'POST'))
def creafilm():
    # CASO 2: POST (L'utente ha inviato i dati)
    if request.method == 'POST':
        titolo = request.form['titolo']
        regista = request.form['regista']
        visto = request.form.get('visto') == 'on'  
        error = None

        if not titolo:
            error = 'titolo obbligatorio.'
        elif not regista:
            error = 'regista obbligatorio.'
        elif visto not in [True, False]:
            error = 'stato di visione obbligatorio.'
        
        if error is None:
            
            # Chiamiamo il Repository
            success = film_repository.create_film(titolo, regista, visto)
            
            if success:
                return redirect(url_for('main.index'))
            else:
                error = f"Errrore nella creazione del film."

        flash(error)

    # CASO 1: GET (Mostriamo il form)
    return render_template('creafilm.html')

@bp.route('/about')
def about():
    return render_template('about.html')
