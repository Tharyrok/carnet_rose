# encoding: utf-8

import csv
from datetime import datetime
from StringIO import StringIO

from django.db import transaction

from .models import Movement

lang_bank = dict()
lang_bank['fr'] = dict()
lang_bank['nl'] = dict()

lang_bank['fr']['bank_id'] = "R\xe9f\xe9rence de l'op\xe9ration"
lang_bank['fr']['date'] = 'Date d\'op\xe9ration'
lang_bank['fr']['amount'] = 'Montant de l\'op\xe9ration'
lang_bank['fr']['num_acount'] = 'Nom de la contrepartie :'
lang_bank['fr']['name'] = 'Communication 1 :'
lang_bank['fr']['name_cont'] = 'Nom de la contrepartie :'
lang_bank['fr']['compte_cont'] = 'Compte de contrepartie'
lang_bank['fr']['comment'] = 'Communication 1 :'

lang_bank['nl']['bank_id'] = 'Valutadatum'
lang_bank['nl']['date'] = 'Datum v. verrichting'
lang_bank['nl']['amount'] = 'Bedrag v/d verrichting'
lang_bank['nl']['num_acount'] = 'Naam v/d tegenpartij :'
lang_bank['nl']['name'] = 'Mededeling 1 :'
lang_bank['nl']['name_cont'] = 'Naam v/d tegenpartij :'
lang_bank['nl']['compte_cont'] = 'Rekening tegenpartij'
lang_bank['nl']['comment'] = 'Mededeling 1 :'


def handle_recordbank_csv(csv_file):
    for_report = {
        "movement_that_might_be_the_same": [],
        "need_title": [],
        "guessed_title": [],
        "skip_because_already_imported": [],
    }

    with transaction.atomic():
        for entry in csv.DictReader(StringIO("\r\n".join(csv_file.read().split("\n")[1:]) + "\r\n"), delimiter=";"):
            if 'Valutadatum' in entry:
                bank_lib = lang_bank['nl']
                
            elif "Num\xe9ro d'op\xe9ration" in entry:
                bank_lib = lang_bank['fr']
                
            else:
                raise Exception("Can't detect language")

            movement = Movement()
            movement.bank_id = entry[bank_lib["bank_id"]]
            movement.date = datetime.strptime(entry[bank_lib['date']], "%d-%m-%Y").date()
            movement.amount = float(entry[bank_lib['amount']].replace(".", "").replace(",", "."))

            if movement.amount < 0:
                movement.kind = "debit"

                # XXX could we have float errors here?
                # I might want to do string parsing to remove the "-"
                # but that sucks
                movement.amount = -1 * movement.amount
            else:
                movement.kind = "credit"

            movement.comment = "From: %s\nCommunication: '%s'" % (entry[bank_lib['num_acount']], entry[bank_lib['name']])

            movement.title = "FIXME"

            # I've already imported this movement, don't do anything
            if Movement.objects.filter(bank_id=entry[bank_lib['bank_id']]).exists():
                for_report["skip_because_already_imported"].append(Movement.objects.get(bank_id=entry[bank_lib['bank_id']]))
                continue

            movement_that_might_be_the_same = Movement.objects.filter(date=movement.date, amount=movement.amount, kind=movement.kind, bank_id__isnull=True)

            if movement_that_might_be_the_same.exists():
                for_report["movement_that_might_be_the_same"].append((movement, movement_that_might_be_the_same[0]))
                continue

            title = guess_title(movement, entry)

            if title is None:
                for_report["need_title"].append(movement)
            else:
                movement.title = title
                for_report["guessed_title"].append((movement, entry[bank_lib['name']], entry[bank_lib['num_acount']]))

            movement.save()

    return for_report


def guess_title(movement, entry):
    
    if 'Valutadatum' in entry:
        bank_lib = lang_bank['nl']

    elif "Num\xe9ro d'op\xe9ration" in entry:
        bank_lib = lang_bank['fr']

    else:
        raise Exception("Can't detect languag")
                
    if movement.kind == "debit" and entry[bank_lib['name_cont']] == "BE52 6528 3497 8409":
        return "Frais Bancaires"

    if movement.kind == "debit" and entry[bank_lib['compte_cont']] == "GB24 MIDL 4005 1570 5243 70":
        return "Commande Olimex UK"

    if movement.kind == "debit" and entry[bank_lib['compte_cont']] == "NL51 INGB 0004 4900 08":
        return "Housting i3d"

    if movement.kind == "debit":
        return None

    # everything is a credit starting from here

    title = entry[bank_lib['comment']]

    if movement.amount in (6, 8, 10):
        return "Redevance VPN"

    if "cotisation" in title.lower() and movement.amount < 70:
        return "Cotisation"

    if "cube order" in title.lower() or "order" in title.lower() or "brique" in title.lower():
        return "Commande de Brique Internet"

    if 60 <= movement.amount <= 80:
        return "Commande de Brique Internet"

    return None
