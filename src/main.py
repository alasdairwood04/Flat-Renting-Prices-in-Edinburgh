from scraper import Scraper
from create_excel import ExcelWriter

def main():
    url = "https://www.citylets.co.uk/flats-rent-edinburgh/"
    scraper = Scraper(url)
    


    html = scraper.fetch_data(url)  # Fetch raw HTML data
    
    flats = scraper.parse_data(html)  # Parse the raw HTML into BeautifulSoup object
    

    for flat in flats:
        print(flat)


    writer = ExcelWriter()
    writer.write_to_excel(flats)



if __name__ == "__main__":
    main()
