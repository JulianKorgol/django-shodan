import pytest
from ShodanAPP.models import Configuration
from django.urls import reverse
from ShodanAPP.views import index


@pytest.mark.django_db #give test access to database
def test_database():
    # Create dummy data
    shodan = Configuration.objects.create(ShodanAPIName="ShodanAPIKey", ShodanAPIKey="54390683498isdfyuwu2ir8y289g2ufi2",)
    # Assert the dummy data saved as expected
    assert shodan.ShodanAPIName=="ShodanAPIKey"
    assert shodan.ShodanAPIKey=="54390683498isdfyuwu2ir8y289g2ufi2"

@pytest.mark.django_db
# Test the index view
def test_index_view(client):
    # Create dummy data
    shodan = Configuration.objects.create(ShodanAPIName="ShodanAPIKey", ShodanAPIKey="54390683498isdfyuwu2ir8y289g2ufi2",)
    # Get the response from the index view
    response = client.get(reverse('index'))
    # Assert the response is 200 OK
    assert response.status_code == 200
    # Assert the response contains the dummy data
    assert b"ShodanAPIKey" in response.content