"""
Author: Vijay Kumar Singh
Date: 9 Jan 2025
Description: Fetching data from OpenWeather and saving it to AWS-S3 bucket.
Version: 1.0.1
"""
import os
import boto3
from dotenv import load_dotenv
import requests
import json

# Load environment variables from .env file
print("Loading environment variables from .env file...")
load_dotenv()

def bucket_exists(client, bucket_name):
    """Check if S3 bucket exists"""
    print(f"Checking if bucket {bucket_name} exists...")
    try:
        client.head_bucket(Bucket=bucket_name)
        print(f"Bucket {bucket_name} exists.")
        return True
    except client.exceptions.NoSuchBucket:
        print(f"Bucket {bucket_name} does not exist.")
        return False
    except client.exceptions.ClientError as e:
        print(f"Error checking bucket: {e}")
        return False

def create_bucket(client, bucket_name):
    """Create S3 bucket"""
    try:
        print(f"Creating bucket {bucket_name}...")
        response = client.create_bucket(
            Bucket=bucket_name,
            CreateBucketConfiguration={
                'LocationConstraint': boto3.Session().region_name
            }
        )
        print(f"Bucket {bucket_name} created successfully.")
        return response
    except Exception as e:
        print(f"Error creating bucket: {e}")

def save_to_local(data, city):
    """Save weather data to a local directory"""
    directory = "weather_data"
    os.makedirs(directory, exist_ok=True)
    file_path = os.path.join(directory, f"{city}_weather.json")
    with open(file_path, "w") as file:
        json.dump(data, file, indent=4)
    print(f"Weather data for {city} saved locally at {file_path}.")
    return file_path

def upload_to_s3(client, bucket_name, file_path, s3_key):
    """Upload a local file to an S3 bucket"""
    try:
        print(f"Uploading {file_path} to S3 bucket {bucket_name} as {s3_key}...")
        client.upload_file(file_path, bucket_name, s3_key)
        print(f"Successfully uploaded {file_path} to S3 as {s3_key}.")
    except Exception as e:
        print(f"Error uploading file to S3: {e}")

def fetch_weather_data(api_key, city):
    """Fetch weather data from OpenWeather API"""
    base_url = "https://api.openweathermap.org/data/2.5/weather"
    params = {
        "q": city,
        "appid": api_key
    }
    try:
        response = requests.get(base_url, params=params)
        response.raise_for_status()
        print(f"Weather data for {city} fetched successfully.")
        return response.json()
    except requests.exceptions.RequestException as e:
        print(f"Error fetching weather data for {city}: {e}")
        return None

def extract_relevant_data(data):
    """Extract relevant data from API response"""
    return {
        "name": data.get("name"),
        "description": data["weather"][0]["description"] if "weather" in data else None,
        "temp": data["main"]["temp"] if "main" in data else None,
        "feels_like": data["main"]["feels_like"] if "main" in data else None,
        "humidity": data["main"]["humidity"] if "main" in data else None,
    }

def main():
    print("Starting the script...")
    
    # Step 1: Create S3 client
    client = boto3.client('s3')
    bucket_name = os.getenv("S3_BUCKET_NAME")
    api_key = os.getenv("API_KEY")

    if not bucket_name or not api_key:
        print("Missing S3_BUCKET_NAME or API_KEY in environment variables.")
        return

    # Step 2: Check and create bucket
    if not bucket_exists(client, bucket_name):
        create_bucket(client, bucket_name)

    # Step 3: Fetch, process and save weather data
    cities = ["London", "New York", "Amsterdam", "Delhi", "Oslo"]
    for city in cities:
        print(f"\nProcessing weather data for {city}...")
        data = fetch_weather_data(api_key, city)
        if data:
            relevant_data = extract_relevant_data(data)
            print(f"Extracted data for {city}: {relevant_data}")
            
            # Step 4: Save locally
            local_file_path = save_to_local(relevant_data, city)
            
            # Step 5: Upload to S3
            s3_key = f"weather-data/{city}_weather.json"
            upload_to_s3(client, bucket_name, local_file_path, s3_key)
    
    print("Hurrey you have successfully uploaded the data to S3 bucket.")

if __name__ == "__main__":
    main()
