import requests

url = "http://mgk-tm.minsk.edu.by/ru/main.aspx?guid=23201"

if __name__ == '__main__':
	response = requests.get(url=url)

	print(response.status_code)
