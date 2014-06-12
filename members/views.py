import json
from django.http import HttpResponse

from .models import Member


def ffdn_api(request):
    response = {
        "name": "Neutrinet",
        "email": "contact@neutrinet.be",
        "website": "http://neutrinet.be",
        "mainMailingList": "neutrinet@lists.entransition.be",
        "progressStatus": 5,
        "memberCount": Member.objects.filter(member_end__isnull=True).count(),
        "subscriberCount": 0,
        "chatrooms": ["irc://irc.freenode.net#neutrinet"],
        "coveredAreas": [
            {
                "name": "Brussels",
                "technologies": ["wifi"],
            }
        ],
        "coordinates": {
            "latitude": 50.84,
            "longitude": 4.35,
        },
        "version": 0.1
    }

    return HttpResponse(json.dumps(response, indent=4))
