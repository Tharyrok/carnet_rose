import csv
from StringIO import StringIO

def handle_recordbank_csv(csv_file):
    for entry in csv.DictReader(StringIO("\r\n".join(csv_file.read().split("\n")[1:]) + "\r\n"), delimiter=";"):
        break
