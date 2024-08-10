import matplotlib.pyplot as plt
import numpy as np

class DataAnalyzer:
    def draw_distribution(self, data): # histogram graph
        rents = [flat['rent'] for flat in data]

        plt.figure(figsize=(10, 5))  # Create a new figure with a specified size
        plt.hist(rents, bins=10, color='g', edgecolor='black')  # Creating a histogram with specified bins, color, and edge color
        plt.title('Distribution of Rent Prices')  # Adding a title to the plot
        plt.xlabel('Rent (£)')  # Labeling the X-axis
        plt.ylabel('Frequency')  # Labeling the Y-axis
        plt.grid(axis='y')  # Adding grid lines to the Y-axis
        plt.show()  # Display the plot

    def plot_rooms_vs_rent(self, data):
        # Extract data for the plot
        areas = list(set([flat['area'] for flat in data]))
        rents_by_area = {area: [flat['rent'] for flat in data if flat['area'] == area] for area in areas}

        plt.figure(figsize=(10, 5))  # Create a new figure with a specified size
        plt.boxplot(rents_by_area.values(), patch_artist=True, labels=rents_by_area.keys())  # Creating a box plot
        plt.title('Rent Prices by Area')  # Adding a title to the plot
        plt.xlabel('Area')  # Labeling the X-axis
        plt.ylabel('Rent (£)')  # Labeling the Y-axis
        plt.xticks(rotation=90)  # Rotating x-axis labels for better readability
        plt.grid(axis='y')  # Adding grid lines to the Y-axis
        plt.show()  # Display the plot

    def plot_rent_per_room_vs_area(self, data):
        # Extract data for the plot
        areas = list(set([flat['area'] for flat in data]))
        rent_per_room_by_area = {area: [flat['rent'] / flat['no_of_rooms'] for flat in data if flat['area'] == area] for area in areas}

        plt.figure(figsize=(10, 5))  # Create a new figure with a specified size
        plt.boxplot(rent_per_room_by_area.values(), patch_artist=True, labels=rent_per_room_by_area.keys())  # Creating a box plot
        plt.title('Rent per Room by Area')  # Adding a title to the plot
        plt.xlabel('Area')  # Labeling the X-axis
        plt.ylabel('Rent per Room (£)')  # Labeling the Y-axis
        plt.xticks(rotation=90)  # Rotating x-axis labels for better readability
        plt.grid(axis='both')  # Adding grid lines to the Y-axis
        plt.show()  # Display the plot

    def plot_rent_per_room_vs_postcode(self, data):
        # Extract data for the plot
        postcodes = list(set([flat['postcode'] for flat in data]))
        rent_per_room_by_postcode = {postcode: [flat['rent'] / flat['no_of_rooms'] for flat in data if flat['postcode'] == postcode] for postcode in postcodes}

        plt.figure(figsize=(10, 5))  # Create a new figure with a specified size
        plt.boxplot(rent_per_room_by_postcode.values(), patch_artist=True, labels=rent_per_room_by_postcode.keys())  # Creating a box plot
        plt.title('Rent per Room by Postcode')  # Adding a title to the plot
        plt.xlabel('Postcode')  # Labeling the X-axis
        plt.ylabel('Rent per Room (£)')  # Labeling the Y-axis
        plt.xticks(rotation=90)  # Rotating x-axis labels for better readability
        plt.grid(axis='y')  # Adding grid lines to the Y-axis
        plt.show()  # Display the plot

    def plot_rent_per_room_for_4_bedrooms_vs_area(self, data):
        # Filter data for flats with 4 bedrooms and specific areas
        specific_areas = ['Marchmont', 'Newington', 'Tollcross', 'Old Town']
        flats_with_4_bedrooms = [flat for flat in data if flat['no_of_rooms'] == 4 and flat['area'] in specific_areas]

        # Extract data for the plot
        areas = list(set([flat['area'] for flat in flats_with_4_bedrooms]))
        rent_per_room_by_area = {area: [flat['rent'] / flat['no_of_rooms'] for flat in flats_with_4_bedrooms if flat['area'] == area] for area in areas}

        plt.figure(figsize=(10, 5))  # Create a new figure with a specified size
        plt.boxplot(rent_per_room_by_area.values(), patch_artist=True, labels=rent_per_room_by_area.keys())  # Creating a box plot
        plt.title('Rent per Room for 4-Bedroom Flats in Specific Areas')  # Adding a title to the plot
        plt.xlabel('Area')  # Labeling the X-axis
        plt.ylabel('Rent per Room (£)')  # Labeling the Y-axis
        plt.xticks(rotation=90)  # Rotating x-axis labels for better readability
        plt.grid(axis='y')  # Adding grid lines to the Y-axis
        plt.show()  # Display the plot

    def plot_rent_per_room_for_3_bedrooms_vs_area(self, data):
        # Filter data for flats with 4 bedrooms and specific areas
        specific_areas = ['Marchmont', 'Newington', 'Tollcross', 'Old Town']
        flats_with_3_bedrooms = [flat for flat in data if flat['no_of_rooms'] == 3 and flat['area'] in specific_areas]

        # Extract data for the plot
        areas = list(set([flat['area'] for flat in flats_with_3_bedrooms]))
        rent_per_room_by_area = {area: [flat['rent'] / flat['no_of_rooms'] for flat in flats_with_3_bedrooms if flat['area'] == area] for area in areas}

        plt.figure(figsize=(10, 5))  # Create a new figure with a specified size
        plt.boxplot(rent_per_room_by_area.values(), patch_artist=True, labels=rent_per_room_by_area.keys())  # Creating a box plot
        plt.title('Rent per Room for 3-Bedroom Flats in Specific Areas')  # Adding a title to the plot
        plt.xlabel('Area')  # Labeling the X-axis
        plt.ylabel('Rent per Room (£)')  # Labeling the Y-axis
        plt.xticks(rotation=90)  # Rotating x-axis labels for better readability
        plt.grid(axis='y')  # Adding grid lines to the Y-axis
        plt.show()  # Display the plot


    def draw_graphs(self, data):
        self.draw_distribution(data)  
        self.plot_rooms_vs_rent(data)  
        self.plot_rent_per_room_vs_area(data)
        self.plot_rent_per_room_for_4_bedrooms_vs_area(data)
        self.plot_rent_per_room_for_3_bedrooms_vs_area(data)
