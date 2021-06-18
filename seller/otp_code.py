def sendSMS(contactno,message):
    import requests
    url = "https://www.fast2sms.com/dev/bulk"
    payload = "sender_id=FSTSMS&message="+message+"&language=english&route=p&numbers="+contactno
    headers = {
        'authorization': "Place your sms API authention",
        'Content-Type': "application/x-www-form-urlencoded",
        'Cache-Control': "no-cache",}
    response = requests.request("POST", url, data=payload, headers=headers)
    return response.text
