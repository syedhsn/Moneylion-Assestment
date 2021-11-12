import requests
import getMethod
from urllib.parse import urlparse, parse_qs\

email = input("Enter your email: ")
feature = input("Enter your feature: ")

param = {"email": email, "featureName": feature}
url = requests.get("https://httpbin.org/get", params=param)

parsed_url = urlparse(url.url)
value = parse_qs(parsed_url.query)
data = {k:v[0] for k,v in value.items()}

email_val = str(data.get("email"))
feature_val = str(data.get("featureName"))

getMethod.getMethod(email_val, feature_val)