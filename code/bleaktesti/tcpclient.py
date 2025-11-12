import requests
import asyncio
import pandas as pd
from io import StringIO

def fetch_data(url):
    try:
        response = requests.get(url)
        response.raise_for_status()  # Raise an error for bad responses
        return response.text
    except requests.exceptions.RequestException as e:
        print(f"An error occurred: {e}")
        return None
    
def main():
    url = "http://172.20.241.9/luedataa_kannasta_groupid_csv.php?groupid=25"
    data = fetch_data(url)
    if data:
        print("Data fetched successfully:")
        print(data)
    else:
        print("No data received.")
        return
    
    df = pd.read_csv(StringIO(data))
    df.to_csv("mittaustiedot.csv", index=False)
    
    

    

if __name__ == "__main__":
    main()
