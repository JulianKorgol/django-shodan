from .models import Configuration

def ShodanApiKey(name):
    ApiKey = Configuration.objects.get(ShodanAPIName=name)
    return ApiKey.ShodanAPIKey

def ShodanApiNames():
    answer = Configuration.objects.values_list('ShodanAPIName', flat=True)
    return answer