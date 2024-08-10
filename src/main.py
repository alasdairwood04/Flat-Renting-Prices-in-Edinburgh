from scraper import Scraper
from create_excel import ExcelWriter
from clean_data import Cleaner
from data_analysis import DataAnalyzer
from ml_on_data import RentPredictor
import pandas as pd

def main():
    url = "https://www.citylets.co.uk/flats-rent-edinburgh/"
    scraper = Scraper(url)
    
    html = scraper.fetch_data(url)  # Fetch raw HTML data
    
    flats = scraper.parse_data(html)  # Parse the raw HTML into BeautifulSoup object
    
    cleaner = Cleaner()
    cleaned_flats_data = cleaner.clean_data(flats)

    cleaned_flats_data_df = pd.DataFrame(cleaned_flats_data)

    for flat in cleaned_flats_data:
        print(flat)


    writer = ExcelWriter()
    writer.write_to_excel(cleaned_flats_data)

    '''
    predictor = RentPredictor()

    X_train, X_test, y_train, y_test = predictor.prepare_data(cleaned_flats_data_df)

    model = predictor.train_model(X_train, y_train)
    predictor.evaluate_model(model, X_test, y_test)

    new_data = pd.DataFrame([[16, 3]], columns=["postcode", "no_of_rooms"])  # Example new data with postcode and number of rooms
    predicted_rent = predictor.predict_rent(model, new_data)
    print("Predicted rent:", predicted_rent)

    '''
    create_charts = DataAnalyzer()
    create_charts.draw_graphs(cleaned_flats_data)

    print("Hello world")
if __name__ == "__main__":
    main()

