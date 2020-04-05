# AWS API GATEWAY SETTINGS
URL = 'AWS-API-GATEWAY-URL-FROM-CDK-STACK'
API_KEY = 'AWS-API-GATEWAY-KEY-FROM-CDK-STACK'
CUSTOMER_NAME = "YOUR-NAME"
HEADERS = {'x-api-key': API_KEY}
# forces the selection of a single speed test server
SERVERS = [
    {
        'url': 'http://speedtest.rd.om.cox.net:8080/speedtest/upload.php',
        'lat': '41.2500',
        'lon': '-96.0000',
        'name': 'Omaha, NE',
        'country': 'United States',
        'cc': 'US',
        'sponsor': 'Cox - Omaha',
        'id': '16621',
        'host': 'speedtest.rd.om.cox.net:8080',
        'd': 13.092320718374381
    }
]
