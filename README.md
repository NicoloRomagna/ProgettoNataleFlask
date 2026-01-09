# ProgettoNataleFlask
## BoardBuddy
BoardBuddy è una web app realizzata con Flask.
Gli utenti possono registrarsi e organizzare serate di gioco da tavolo.

### Funzionalità
- Registrazione e login utenti
- Creazione di serate con titolo, data, luogo e note
- Lista di tutte le serate create
- Dashboard con il totale delle serate create dall’utente

### Struttura del progetto
ProgettoNataleFlask
│
├── run.py
├── boardbuddy
│────── __init__.py
│────── config.py
│────── models.py
│   
│── auth
│────── __init__.py
│────── routes.py
│  
│── main
│────── __init__.py
│──────routes.py
│   
│── dashboard
│────── __init__.py
│────── routes.py
│
└── templates
│────── base.html
│ 
├── auth
│────── login.html
│────── register.html
│ 
│── main
│──────index.html
│──────create_night.html
│ 
│── dashboard
│────── stats.html


