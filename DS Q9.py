import pandas as pd
data = {
    'property_id': [1, 2, 3, 4, 5],
    'location': ['City A', 'City B', 'City A', 'City C', 'City B'],
    'number_of_bedrooms': [3, 4, 5, 2, 6],
    'area_sqft': [1500, 1800, 2200, 1200, 2500],
    'listing_price': [250000, 300000, 350000, 200000, 400000]
}
df = pd.DataFrame(data)
avg = df.groupby('location')['listing_price'].mean()
bedrooms = df[df['number_of_bedrooms'] > 4]
nbedrooms = len(bedrooms)
area = df[df['area_sqft'] == df['area_sqft'].max()]
print("1. Average listing price of properties in each location:")
print(avg)

print("\n2. Number of properties with more than four bedrooms:")
print(nbedrooms)

print("\n3. Property with the largest area:")
print(area)