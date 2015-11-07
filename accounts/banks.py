import csv
from datetime import datetime
from StringIO import StringIO

from .models import Movement

def handle_recordbank_csv(csv_file):
    for entry in csv.DictReader(StringIO("\r\n".join(csv_file.read().split("\n")[1:]) + "\r\n"), delimiter=";"):
        # I've already imported this movement, don't do anything
        if Movement.objects.filter(bank_id=entry["Ref. v/d verrichting"]).exists():
            continue

        movement = Movement()
        movement.bank_id = entry["Ref. v/d verrichting"]
        movement.date = datetime.strptime(entry["Datum v. verrichting"], "%d-%m-%Y").date()
        movement.amount = float(entry["Bedrag v/d verrichting"].replace(".", "").replace(",", "."))

        if movement.amount < 0:
            movement.kind = "debit"

            # XXX could we have float errors here?
            # I might want to do string parsing to remove the "-"
            # but that sucks
            movement.amount = -1 * movement.amount
        else:
            movement.kind = "credit"

        movement.comment = "From: %s\nCommunition: '%s'" % (entry["Naam v/d tegenpartij :"], entry["Mededeling 1 :"])

        movement.title = "FIXME"

        print movement
