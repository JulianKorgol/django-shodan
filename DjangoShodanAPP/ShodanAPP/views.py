from django.shortcuts import render
from django.http import HttpResponse
from .shodanAPIKey import ShodanApiNames
from .shodan import ShodanSearch

def index(request):
    if request.method == 'GET':
        shodanApiKeysNames = ShodanApiNames()
        return render(request, 'shodanapp/index.html', {'shodanApiKeysNames': shodanApiKeysNames})
    elif request.method == 'POST':
        shodanApiKeyName = request.POST.get('APIKey')
        shodanQuery = request.POST.get('IP_input')

        # Checking Shodan API Key Name is in the database
        shodanApiKeysNames = ShodanApiNames()
        if shodanApiKeyName not in shodanApiKeysNames:
            return HttpResponse('API Key not found')

        # Run Shodan Search
        shodanAnswer = ShodanSearch(shodanApiKeyName, shodanQuery, 'ip')

        # Operate on data - TODO
        def FormatData(host):
            answer = [
                'IP: {}'.format(host['ip_str']),
                'Organization: {}'.format(host.get('org', 'n/a')),
                'Operating System: {}'.format(host.get('os', 'n/a'))
            ]

            return answer

        FinalAnswer = FormatData(shodanAnswer)

        return render(request, 'shodanapp/results.html', {'FinalAnswer': FinalAnswer})
