import requests


url = "http://182.254.213.162:9980/getOtherParams"

payload = {
    "xg":"0404283100018ac245e2912775e8a1467f6ffb9f827298a9361f",
    "xk":"1612880684"
}

response = requests.post(url, data=payload, verify=False)
print(response.text)