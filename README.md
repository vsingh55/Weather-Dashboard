# Weather Data Collection and Storage
<details>
<summary>📑 Quick Navigation</summary>

- [Weather Data Collection and Storage](#weather-data-collection-and-storage)
  - [Project Overview](#project-overview)
    - [Objective](#objective)
    - [Features](#features)
  - [Architecture](#architecture)
    - [System Design](#system-design)
    - [Workflow](#workflow)
  - [Technologies Used](#technologies-used)
  - [Project Structure](#project-structure)
  - [Prerequisites](#prerequisites)
    - [System Requirements](#system-requirements)
    - [Required Credentials](#required-credentials)
  - [How to Setup](#how-to-setup)
    - [Step 1: Clone the Repository](#step-1-clone-the-repository)
    - [Step 2: Install Dependencies](#step-2-install-dependencies)
    - [Step 3: Set Up Environment Variables](#step-3-set-up-environment-variables)
  - [Configuration](#configuration)
  - [Execution](#execution)
    - [Expected Output](#expected-output)
    - [Screenshots](#screenshots)
  - [Future Development](#future-development)
  - [Blog🔗](#blog)
  - [Contributing](#contributing)
  - [License](#license)

</details>

## Project Overview
![](/Assests/thumbnail.png)

### Objective
The purpose of this project is to fetch weather data for selected cities using the OpenWeather API and store the data in an AWS S3 bucket for further analysis or integration with downstream systems.

### Features
- Fetch real-time weather data for multiple cities.
- Extract relevant data fields such as city name, temperature, and humidity.
- Save the weather data locally in JSON format.
- Upload the saved data to an AWS S3 bucket.

## Architecture
![architechturedia](/Assests/architechture.png)

### System Design

1. **Data Source**: OpenWeather API for weather information.
2. **Processing Script**: Python script for data fetching, processing, and uploading.
3. **Storage**: AWS S3 bucket for centralized data storage.

### Workflow

1. The Python script fetches data from OpenWeather API.
2. Relevant data fields are extracted and saved locally as JSON files.
3. The JSON files are uploaded to an AWS S3 bucket.

## Technologies Used
| Category        | Technologies              |
|-----------------|---------------------------|
| Programming     | Python                    |
| Cloud Storage   | AWS S3                    |
| Environment Mgmt| Python dotenv             |
| API Integration | OpenWeather API           |

## Project Structure

```
Weather Dashboard/
├── Assests/         # Directory for imgages
├──src
   └── weather_dashboard.py     # Main script to fetch, process and save data
├── weather_data/         # Directory for locally saved weather data
├── requirements.txt      # Python dependencies
└──README.md             # Project documentation
```

## Prerequisites

### System Requirements
- Python 3.8 or above
- AWS account with appropriate permissions for S3 operations

### Required Credentials
- [OpenWeather API Key](https://openweathermap.org/api)
- AWS Access Key ID and Secret Access Key

## How to Setup

### Step 1: Clone the Repository
```bash
git clone https://github.com/vsingh55/AWS-NBA-DevOpsAllStars-Challenge-2025.git
cd AWS-NBA-DevOpsAllStars-Challenge-2025/D1-Weather-Dashboard
```

### Step 2: Install Dependencies
```bash
pip install -r requirements.txt
```

### Step 3: Set Up Environment Variables
Create a `.env` file in the root directory with the following content:
```env
S3_BUCKET_NAME=your-s3-bucket-name
API_KEY=your-openweather-api-key
```

## Configuration
- Replace `your-s3-bucket-name` with the name of the S3 bucket.
- Add your OpenWeather API Key to `API_KEY`.
- Configure AWS credentials using the AWS CLI:
  ``` aws configure ```

## Execution
Run the main script to fetch and upload data:
```bash
python weather_dashboard.py
```

### Expected Output
1. Local JSON files saved in the `weather_data/` directory.
2. Weather data uploaded to the S3 bucket under the `weather_data/` folder.

### Screenshots
![alt text](/Assests/uploadedDataS3.png)

## Future Development
1. Build a dashboard using AWS QuickSight or Grafana for data visualization.
2. Automate the script execution with a scheduler such as AWS Lambda or cron jobs.
3. Add additional error handling and logging mechanisms.
4. Implement CI/CD pipelines for streamlined deployment and testing.

## Blog🔗
[To visit blog click here](https://blogs.vijaysingh.cloud/weather-dashboard)


## Contributing
- Contributions are welcome. Please open an issue or submit a pull request for suggestions or improvements.

## License
This project is licensed under the MIT License. See the LICENSE file for details.

