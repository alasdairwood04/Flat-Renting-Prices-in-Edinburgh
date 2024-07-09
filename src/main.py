
from scraper import Scraper
from create_excel import ExcelWriter
from clean_data import Cleaner

def main():
    url = "https://www.citylets.co.uk/flats-rent-edinburgh/"
    scraper = Scraper(url)
    


    html = scraper.fetch_data(url)  # Fetch raw HTML data
    
    flats = scraper.parse_data(html)  # Parse the raw HTML into BeautifulSoup object
    
    cleaner = Cleaner()
    cleaned_flats_data = cleaner.clean_data(flats)


    for flat in cleaned_flats_data:
        print(flat)


    writer = ExcelWriter()
    writer.write_to_excel(cleaned_flats_data)



if __name__ == "__main__":
    main()
