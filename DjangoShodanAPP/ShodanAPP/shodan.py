from .shodanAPIKey import ShodanApiKey
import shodan


def ShodanSearch(name, query, type):
    apiKey = ShodanApiKey(name)
    api = shodan.Shodan(apiKey)

    if type == 'ip':
        results = api.host(query)
    return results
