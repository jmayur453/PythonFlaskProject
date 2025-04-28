import ipinfo

def test_ipinfo():
    access_token = 'e9349ffdb5b878'  # Use your actual token
    handler = ipinfo.getHandler(access_token)
    details = handler.getDetails()
    print(details)

test_ipinfo()
