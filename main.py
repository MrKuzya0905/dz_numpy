import pandas as pd
import dask.dataframe as dd
import numpy as np
import random
import faker
from sqlalchemy import create_engine


fake = faker.Faker()
engine = create_engine("sqlite:///big_data.db", echo=True)
URI = "sqlite:///big_data.db"


# data = {
#     'Category': [random.choice(['A', 'B', 'C', 'D']) for _ in range(100000)],
#     'Value1': [random.randint(1, 100) for _ in range(100000)],
#     'Value2': [random.uniform(10.0, 50.0) for _ in range(100000)]
# }
# df = pd.DataFrame(data)
# df.to_csv("big_data.csv", index=False)

# data = {
#     'Class': [random.choice(['1-А', '3-Б', '10-А', '8-В']) for _ in range(100000)],
#     'Numbers': [random.randint(1, 100) for _ in range(100000)],
#     'Grades': [random.uniform(60.0, 100.0) for _ in range(100000)]
# }
# df = pd.DataFrame(data)
# df.to_csv("school_data.csv", index=False)

# df = pd.read_csv("big_data.csv")
# print(df.head())

# type_dict = {
#     "Category": "category",
#     "Value1": int,
#     "Value2": float
# }

# ddf = dd.read_csv("big_data.csv", dtype=type_dict)

# print(ddf.head())
# ddf.info()
# print(ddf.describe())
# grouped_int = ddf.groupby("Category").mean()
# print(grouped_int.compute())

# pdf = pd.DataFrame({
#     'A': range(1000),
#     'B': ['Category1'] * 500 + ['Category2'] * 500
# })
# ddf = dd.from_pandas(pdf, npartitions=10)
# print(ddf.tail(20))

# dd.to_sql(ddf, "name_table", engine)

# ddf = dd.read_csv("big_data.csv")
# grouped = ddf.groupby("Category").agg(Count=("Category", "count")).reset_index()
# print(grouped.compute())

# if __name__ == "__main__":
#     from dask.distributed import Client
#     client = Client(n_workers=4, threads_per_worker=1, memory_limit='1GB')

#     dtype_dict = {
#         'survived': 'int64', 'pclass': 'int64', 'sex': 'object', 'age': 'float64',
#         'sibsp': 'int64', 'parch': 'int64', 'fare': 'float64', 'embarked': 'object',
#         'class': 'object', 'who': 'object', 'adult_male': 'bool', 'deck': 'object',
#         'embark_town': 'object', 'alive': 'object', 'alone': 'bool'
#     }

#     ddf = dd.read_csv('large_titanic.csv', dtype=dtype_dict)
#     feature_cols = ['survived', 'pclass', 'sex', 'age', 'sibsp', 'parch', 'fare', 'embarked', 'adult_male', 'alone']
#     ddf = ddf[feature_cols]
#     ddf['age'] = ddf['age'].fillna(ddf['age'].mean())
#     ddf['pclass'] = ddf['pclass'].astype(str)
#     categorical_cols = ['sex', 'embarked', 'pclass', 'adult_male', 'alone']
#     ddf = ddf.categorize(columns=categorical_cols)
#     ddf = dd.get_dummies(ddf, columns=categorical_cols)
#     X = ddf.drop(['survived'], axis=1)
#     X = X.astype(float)
#     y = ddf['survived']
#     X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, shuffle=True)
#     X_train_array = X_train.to_dask_array(lengths=True)
#     X_test_array = X_test.to_dask_array(lengths=True)
#     y_train_array = y_train.to_dask_array(lengths=True)
#     y_test_array = y_test.to_dask_array(lengths=True)
#     model = LogisticRegression()
#     model.fit(X_train_array, y_train_array)
#     score = model.score(X_test_array, y_test_array)
#     print(f"Model Accuracy: {score.compute()}")


# num_records = 1000000 
# data = {
#     'TransactionId': range(1, num_records + 1),
#     'CustomerId': [fake.uuid4() for _ in range(num_records)],
#     'ProductId': [f"P{random.randint(1000, 9999)}" for _ in range(num_records)],
#     'Quantity': [random.randint(1, 10) for _ in range(num_records)],
#     'Price': [round(random.uniform(5.0, 500.0), 2) for _ in range(num_records)],
#     'Date': [fake.date_between(start_date='-2y', end_date='today') for _ in range(num_records)],
#     'Country': [fake.country() for _ in range(num_records)]
# }
# df_sales = pd.DataFrame(data)
# df_sales.to_csv('large_sales_data.csv', index=False)

# Встановити типи даних за допомогою словника, зазначивши, що колонка CustomerId має тип category, а Price — float32.
# Додайте один рядок коду для встановлення 'ProductId' як індекс перед групуванням

# type_dict = {
#     "TransactionId": int,
#     "CustomerId": "category",
#     "ProductId": "category",
#     "Quantity": int,
#     "Price": "float32",
#     "Date": "object",
#     "Country": str
# }
# # pd.to_datetime
# ddf = dd.read_csv("large_sales_data.csv", dtype=type_dict)
# # ddf = ddf.set_index("ProductId")
# ddf["Date"] = dd.to_datetime(ddf["Date"], errors="coerce")
# # 


# ddf["Total"] = ddf["Quantity"] * ddf["Price"]
# grouped = ddf.groupby(ddf["ProductId"])["Total"].sum().reset_index()

# # dd.to_sql(ddf, "Data", URI, if_exists="replace", index=False, engine_kwargs=dict(echo=True))
# dd.to_sql(grouped, "Total", URI, if_exists="replace", index=False, engine_kwargs=dict(echo=True))
# print(grouped.compute())

# ddf = dd.read_sql("")


import folium


location = [46.4629926, 30.7336229]
m = folium.Map(location=location, zoom_start=20)

# folium.Marker(
#     location=[50.4501, 30.5234],
#     popup='Центр Києва',
#     icon=folium.Icon(icon='info-sign')
# ).add_to(m)

# polygon = [
#     [50.4547, 30.5238],
#     [50.4547, 30.5338],
#     [50.4447, 30.5338],
#     [50.4447, 30.5238],
#     [50.4547, 30.5238]
# ]
# folium.Polygon(
#     locations=polygon,
#     color='blue',
#     fill=True,
#     fill_color='cyan'
# ).add_to(m)

m.save('map.html')

# from geopy.geocoders import Nominatim

# geolocator = Nominatim(user_agent="my_geocoder")
# location = geolocator.geocode("вулиця Водопровідна 10, Одеса, Україна")
# print((location.latitude, location.longitude))

# from geopy.distance import geodesic
# point1 = (37.7749, -122.4194)  # Сан-Франциско
# point2 = (34.0522, -118.2437)  # Лос-Анджелес
# distance = geodesic(point1, point2).miles
# print(f"Відстань: {distance:.2f} миль")
# distance = geodesic(point1, point2).km
# print(f"Відстань: {distance:.2f} км")


# from geopy.geocoders import Nominatim


# geolocator = Nominatim(user_agent="geo_app")

# addresses = [
#     "1600 Amphitheatre Parkway, Mountain View, CA",
#     "1 Infinite Loop, Cupertino, CA",
#     "350 Fifth Avenue, New York, NY"
# ]
# locations = []
# for address in addresses:
#     location = geolocator.geocode(address)
#     if location:
#         locations.append((location.latitude, location.longitude))
#     else:
#         print(f"Не вдалося геокодувати адресу: {address}")
# print(locations)

import requests
import json


def load_and_validate_api_data(url, required_fields, output_file="api_data.json"):
    try:
        response = requests.get(url)
        response.raise_for_status()

        data = response.json()

        with open(output_file, "w", encoding="utf-8") as f:
            json.dump(data, f, ensure_ascii=False, indent=4)

        if isinstance(data, dict):
            data = [data]

        valid_data = []

        for record in data:
            if all(field in record for field in required_fields):
                valid_data.append(record)
            else:
                print(f"Пропущено запис: відсутні поля {required_fields}")

        print(f"Валідних записів: {len(valid_data)}")

        return valid_data

    except requests.exceptions.RequestException as e:
        print(f"Помилка API: {e}")
        return []