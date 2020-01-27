import requests
import re
import json
import argparse

parser = argparse.ArgumentParser()
parser.add_argument('-t', "--target", type=str, help="your target website e.g. https://blog.mann-ivanov-ferber.ru/ ")
args = parser.parse_args()

url = re.sub(r'(.*://)?([^/?]+).*', '\g<1>\g<2>'+"/wp-json/wp/v2/users", args.target)

req = requests.get(url)
if req.status_code == 200:
	try:
		response = req.json()
		print("UserLogin UserName:")
		for value in response:
			user_login=value['slug']
			user_name=value['name']
			print(user_login + " " + user_name)
	except Exception as err:
		print('Can\'t get users')
elif req.status_code == 401:
	print('Can\'t get users')
else:
	print('Can\'t get users')
exit()
