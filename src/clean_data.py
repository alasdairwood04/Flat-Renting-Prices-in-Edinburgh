import pandas as pd

class Cleaner:
    def clean_data(self, flats):
        # Convert list of dictionaries to a Pandas DataFrame
        df = pd.DataFrame(flats)
        
        # Clean Address column (remove commas)
        df['address'] = df['address'].str.split(',').str[0]
        
        # Clean Rent column (extract numeric part)
        df['rent'] = df['rent'].str.extract(r'(\d+)').astype(int)
        
        # Clean No of Bedrooms column (extract numeric part)
        df['no_of_rooms'] = df['no_of_rooms'].str.extract(r'(\d+)').astype(int)
        
        
        # Extract last word from Address and create Area column
        df['Area'] = df['address'].str.split().str[-1]

        # Clean the estage agent part
        df['estate_agent'] = df['estate_agent'].str.replace('Contact', '').str.strip()

        # Convert DataFrame back to list of dictionaries
        cleaned_flats = df.to_dict(orient='records')
        
        return cleaned_flats
