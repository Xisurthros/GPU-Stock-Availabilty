import requests, time
from bs4 import BeautifulSoup

cards = [{'name': 'NVIDIA GeForce RTX 3090 24GB', 'url': 'https://www.bestbuy.com/site/nvidia-geforce-rtx-3090-24gb-gddr6x-pci-express-4-0-graphics-card-titanium-and-black/6429434.p?skuId=6429434'},
		{'name': 'NVIDIA GeForce RTX 3080 Ti 12GB', 'url': 'https://www.bestbuy.com/site/nvidia-geforce-rtx-3080-ti-12gb-gddr6x-pci-express-4-0-graphics-card-titanium-and-black/6462956.p?skuId=6462956'},
		{'name': 'NVIDIA GeForce RTX 3080 10GB', 'url': 'https://www.bestbuy.com/site/nvidia-geforce-rtx-3080-10gb-gddr6x-pci-express-4-0-graphics-card-titanium-and-black/6429440.p?skuId=6429440'}]

headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/56.0.2924.76 Safari/537.36', "Upgrade-Insecure-Requests": "1","DNT": "1","Accept": "text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8","Accept-Language": "en-US,en;q=0.5","Accept-Encoding": "gzip, deflate"}

def main():
	while True:
		for card in cards:
			r = requests.get(card["url"], headers=headers)
			soup = BeautifulSoup(r.text, 'html.parser')
			html = soup.find("div", class_="fulfillment-fulfillment-summary")
			if 'Sold Out' in html.text:
				print(f'{card["name"]}: Sold out')
			else:
				print(f'{card["name"]}: In Stock!!!')
		time.sleep(30)


if __name__ == '__main__':
	main()
