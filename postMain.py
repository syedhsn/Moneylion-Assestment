import requests
import postMethod

email = input("Enter your email: ")
feature = input("Enter your feature: ")
enable = bool(1)

url = requests.post('https://httpbin.org/post', json={'email': email, 'featureName': feature, 'enable': enable})

response_Json = url.json()['data']
postMethod.postMethod(response_Json)

