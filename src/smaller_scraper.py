from bs4 import BeautifulSoup
import requests, openpyxl
from clean_data import Cleaner


filename='flats_to_rent_edinburgh.xlsx'
excel = openpyxl.Workbook()
sheet = excel.active
sheet.title = "Flats to rent in Edinburgh"
sheet.append(["Number", "Address", "Postcode", "Rent", "No of Bedrooms", "Estage Agent"])



try:
    headers = {
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/58.0.3029.110 Safari/537.3"
    }
    source = requests.get("https://www.citylets.co.uk/flats-rent-edinburgh/", headers=headers)
    source.raise_for_status()

    count = 0
    soup = BeautifulSoup(source.text, "html.parser")

    flats_list = []

    list_of_flats = soup.find("ul", class_="search-results")

    flats = list_of_flats.find_all("li")

    for flat in flats:
        listing_details = flat.find("h2", class_="listing-title")
        if listing_details is not None:
            count += 1
            rent_per_month = listing_details.find('span', {'class': 'rent', 'itemscope': True, 'itemtype': 'http://schema.org/SellAction'}).get_text(strip=True)
            no_of_bedrooms = listing_details.find("div", itemprop="name").get_text(strip=True)
            address = flat.find("span", itemprop="streetAddress").get_text(strip=True)
            postcode = flat.find("span", itemprop="postalCode").get_text(strip=True)
            estate_agent = flat.find("a", class_="listing-contact-agent").get_text(strip=True)
            
            each_flat = {
                        "number": count,
                        "address": address,
                        "postcode": postcode,
                        "rent": rent_per_month,
                        "no_of_rooms": no_of_bedrooms,
                        "estate_agent": estate_agent
                    }
            flats_list.append(each_flat)
    
except Exception as e:
    print(e)


cleaner = Cleaner()
cleaned_flats_data = cleaner.clean_data(flats_list)

    
for flat in cleaned_flats_data:
    print(flat)

for flat in cleaned_flats_data:
    sheet.append([
        flat["number"],
        flat["address"],
        flat["postcode"],
        flat["rent"],
        flat["no_of_rooms"],
        flat["estate_agent"]
    ])


excel.save(filename)
