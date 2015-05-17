import json
from django.http import HttpResponse

from .models import Member


def ffdn_api(request):
    response = {
        "name": "Neutrinet",
        "email": "contact@neutrinet.be",
        "description": "Neutrinet is a project to setup an associative ISP in Belgium, focusing so far on the area of Brussels (open to other cities)",
        "website": "http://neutrinet.be",
        "mainMailingList": "neutrinet@lists.entransition.be",
        "progressStatus": 7,
        "memberCount": Member.objects.filter(member_end__isnull=True).count(),
        "subscriberCount": 0,
        "chatrooms": ["irc://irc.freenode.net#neutrinet"],
        "coveredAreas": [
            {
                "name": "Brussels",
                "technologies": ["vpn", "brique"],
            }
        ],
        "coordinates": {
            "latitude": 50.84,
            "longitude": 4.35,
        },
        "version": 0.1
    }

    return HttpResponse(json.dumps(response, indent=4))
