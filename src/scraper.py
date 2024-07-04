from bs4 import BeautifulSoup
import requests

class Scraper:
    def __init__(self, url):
        self.url = url

    def fetch_data(self):
        headers = {
            "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/58.0.3029.110 Safari/537.3"
        }
        response = requests.get(self.url, headers=headers)
        response.raise_for_status()
        return response.text  # Return the raw HTML text

    def parse_data(self, html):
        count = 0
        soup = BeautifulSoup(html, "html.parser")
        flats_list = []

        list_of_flats = soup.find("ul", class_="search-results")

        flats = list_of_flats.find_all("li")

        for flat in flats:
            listing_details = flat.find("h2", class_="listing-title")
            if listing_details is not None:
                count += 1
                rent_per_month = listing_details.find('span', {'class': 'rent', 'itemscope': True, 'itemtype': 'http://schema.org/SellAction'}).get_text(strip=True)[:4]
                no_of_bedrooms = listing_details.find("div", itemprop="name").get_text(strip=True)[:1]
                address = flat.find("span", itemprop="streetAddress").get_text(strip=True)
                postcode = flat.find("span", itemprop="postalCode").get_text(strip=True)
                estate_agent = flat.find("a", class_="listing-contact-agent").get_text(strip=True)[7:]
                
                each_flat = {
                            "number": count,
                            "address": address,
                            "postcode": postcode,
                            "rent": rent_per_month,
                            "no_of_rooms": no_of_bedrooms,
                            "estate_agent": estate_agent
                        }
                flats_list.append(each_flat)
        return flats_list


