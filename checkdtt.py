#!/usr/bin/python3
from sqlalchemy import create_engine, inspect
from sqlalchemy.orm import sessionmaker, scoped_session

engine = create_engine("mysql+mysqldb://hbnb_dev:hbnb_dev_pwd@localhost/hbnb_dev_db",
                       pool_pre_ping=True)
inspector = inspect(engine)

# Get table metadata
# places_columns = inspector.get_columns("places")
cities_columns = inspector.get_columns("cities")

# Check for data type mismatch in 'id' and 'city_id'
id_type = None
city_id_type = None

# for column in places_columns:
#     if column["name"] == "city_id":
#         city_id_type = column["type"]

for column in cities_columns:
    if column["name"] == "id":
        id_type = column["type"]

# Print data types for comparison
print("Data Type of 'id' in 'cities':", id_type)
# print("Data Type of 'city_id' in 'places':", city_id_type)

# Check for mismatch
if id_type != city_id_type:
    print("**ERROR: Data type mismatch between 'id' and 'city_id'.")
else:
    print("Data types seem compatible.")

# Optionally, print all columns and their data types for further inspection
# for table, columns in inspector.get_table_details().items():
#     print(f"Table: {table}")
#     for column in columns.values():
#         print(f"  - Column: {column['name']}, Type: {column['type']}")
