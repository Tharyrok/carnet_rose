from django.shortcuts import render

from .forms import CSVUploaderForm


def upload_record_bank_csv(request):
    return render(request, "accounts/upload_record_bank_csv.haml", {
        "form": CSVUploaderForm(),
    })
