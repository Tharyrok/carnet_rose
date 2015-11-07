import csv
from StringIO import StringIO

from .models import Movement

def handle_recordbank_csv(csv_file):
    for entry in csv.DictReader(StringIO("\r\n".join(csv_file.read().split("\n")[1:]) + "\r\n"), delimiter=";"):
        # I've already imported this movement, don't do anything
        if Movement.objects.filter(bank_id=entry["Ref. v/d verrichting"]):
            continue
