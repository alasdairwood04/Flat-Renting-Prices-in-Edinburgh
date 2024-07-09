from bs4 import BeautifulSoup
import requests

class Scraper:
    def __init__(self, base_url):
        self.base_url = base_url

    def fetch_data(self, url):
        headers = {
            "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/58.0.3029.110 Safari/537.3"
        }
        response = requests.get(url, headers=headers)
        response.raise_for_status()
        
        return response.text  # Return the raw HTML text

    def parse_data(self, html):
        all_flats = []
        page_number = 1

        while True:
            if page_number == 1:
                url = self.base_url
            else:
                url = f"{self.base_url}{page_number}/"
            
            html = self.fetch_data(url)
            soup = BeautifulSoup(html, "html.parser")
            list_of_flats = soup.find("ul", class_="search-results")

            if not list_of_flats:
                break

            flats = list_of_flats.find_all("li")
            count = len(all_flats)

            for flat in flats:
                listing_details = flat.find("h2", class_="listing-title")
                if listing_details is not None:
                    count += 1
                    rent_per_month = listing_details.find('span', {'class': 'rent', 'itemscope': True, 'itemtype': 'http://schema.org/SellAction'}).get_text(strip=True)
                    no_of_bedrooms = listing_details.find("div", itemprop="name").get_text(strip=True)
                    address = flat.find("span", itemprop="streetAddress").get_text(strip=True)
                    postcode = flat.find("span", itemprop="postalCode").get_text(strip=True)
                    estate_agent = flat.find("a", class_="listing-contact-agent").get_text(strip=True)
                    
                    comma_index = address.find(',')
                    if comma_index != -1:
                        area = address[comma_index + 1:].strip()
                    else:
                        area = ""

                    each_flat = {
                        "number": count,
                        "area": area,
                        "address": address,
                        "postcode": postcode,
                        "rent": rent_per_month,
                        "no_of_rooms": no_of_bedrooms,
                        "estate_agent": estate_agent
                    }
                    all_flats.append(each_flat)

            page_number += 1

        return all_flats