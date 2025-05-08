import pandas as pd
from sqlalchemy import create_engine

#Load and clean data
df = pd.read_excel('E:\HDD Docs\Career Stuff\Deloitte\DEM_Challenge_Section1_DATASET.xlsx')

#Standardize column names
df.columns = df.columns.str.strip().str.lower().str.replace(" ", "_")

#Simplify gender categories
def simplify_gender(g):
    if g.lower() in ['male', 'female']:
        return 'Binary'
    elif 'non' in g.lower() or 'gender' in g.lower():
        return 'Nonbinary'
    else:
        return 'Other'

df['gender_group'] = df['gender'].apply(simplify_gender)

#Extract email domain and type
df['email_domain'] = df['email'].str.split('@').str[-1]

def categorize_domain(domain):
    if domain.endswith('.edu'):
        return 'Academic'
    elif domain in ['gmail.com', 'yahoo.com', 'outlook.com']:
        return 'Personal'
    else:
        return 'Corporate'

df['email_type'] = df['email_domain'].apply(categorize_domain)

#Optional enrichment
df['name_length'] = df['first_name'].str.len() + df['last_name'].str.len()

#Database connection
username = 'nina'
password = 'password123'
host = 'localhost'
port = '5432'
database = 'challenge_db'
table_name = 'chemberta_dataset'

connection_string = f'postgresql://{username}:{password}@{host}:{port}/{database}'
engine = create_engine(connection_string)

#Load to PostgreSQL
df.to_sql(table_name, engine, if_exists='replace', index=False)