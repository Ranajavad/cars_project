import pandas as pd
from sqlalchemy import create_engine
df=pd.read_csv('vehicle_data.csv') 
engine = create_engine('postgresql://postgres:1905@localhost:5432/cars_analysis')
df.to_sql('vehicles', engine, index=False, if_exists='replace')
print("Success! Data is now in PostgreSQL.")
