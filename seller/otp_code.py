def sendSMS(contactno,message):
    import requests
    url = "https://www.fast2sms.com/dev/bulk"
    payload = "sender_id=FSTSMS&message="+message+"&language=english&route=p&numbers="+contactno
    headers = {
        'authorization': "ImVTdwKfpz83bMx6ejFDcHqOk74JutYW0ghUnPA9BLEiry5GCoaHA1qnbLMR4uFKp0Yjfhz3QirS5y6I",
        'Content-Type': "application/x-www-form-urlencoded",
        'Cache-Control': "no-cache",}
    response = requests.request("POST", url, data=payload, headers=headers)
    return response.text