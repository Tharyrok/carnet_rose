Carnet Rose
===========

Gestion de la liste de cotisation des membres avec versionning. Ultra simple pour l'instant.

Installation
============

Attention: besoin de postgresql.


    virtualenv ve
    source ve/bin/activate
    
    pip install -r requirements.txt
    
    createdb carnet_rose
    python manage.py syncdb
