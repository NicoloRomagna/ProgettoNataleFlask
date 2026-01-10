# ProgettoNataleFlask
## CineList
CineList è una web app realizzata con Flask.
Gli utenti possono registrarsi e visualizzare i film visti o meno dalla coomunity.

### Funzionalità
- Registrazione e login utenti
- Creazione di film
- Lista di film visti e no
- Dashboard con i film visti e non visti

### Struttura del progetto
ProgettoNataleFlask
| CineList
├── run.py
|── setup_db.py
|── app
│────── repositories
│──────────── film_repository.py
│──────────── user_repository.py
│────── templates
│──────────── auth
│────────────────── login.html
│────────────────── register.html
│──────────── about.html
│──────────── base.html
│──────────── creafilm.html
│──────────── index.html
│────── __init__.py
│────── auth.py
│────── db.py
│────── main.py
│────── schema.sql
|── instance
│────── film.sqlite

-  link per aprire il Browser --> http://127.0.0.1:5000/
