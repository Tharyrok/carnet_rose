from django.shortcuts import render
from django.views.generic import View

from .forms import CSVUploaderForm


class UploadRecordBankCsv(View):
    def get(self, request):
        return render(request, "accounts/upload_record_bank_csv.haml", {
            "form": CSVUploaderForm(),
        })
