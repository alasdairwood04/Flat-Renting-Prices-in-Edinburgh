# Flat Renting Prices in Edinburgh
 A program to help students find flats in edinburgh

## Description
This project scrapes rental prices from a property website in Edinburgh to help students find accomodation

## Project Structure
- `data/`: Directory for storing scraped data.
- `src/`: Directory containing the source code.
- `tests/`: Directory for unit tests.
- `requirements.txt`: List of dependencies.
- `README.md`: Project documentation.

### Current State
- Scrapes all the pages of the website and puts all the flats for rent in an excel file. Aiming to improve the functinality to allow the user to input certain criteria e.g. number of rooms, HMO etc. 
- Just incorporated the use of Pandas to clean the data before going into the excel file
- Added different graphs that people may want to view while searching for flats in Edinburgh - e.g. rent per room/area of Edinburgh
- Added a rent predictor using a ML model to predict the total rent based on number of rooms and post code