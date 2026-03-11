import requests
import pandas as pd

def extract_data():
    url = "https://jsonplaceholder.typicode.com/posts"
    response = requests.get(url)
    data = response.json()
    df = pd.DataFrame(data)
    return df
