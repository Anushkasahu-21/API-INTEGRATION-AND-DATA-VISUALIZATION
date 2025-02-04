# API Integration and Data Visualization

This project demonstrates fetching data from a public API and creating visualizations using Python libraries such as Matplotlib or Seaborn.

## Instructions

### 1. Fetch Data from Public API
We will use the OpenWeatherMap API to retrieve weather data. Follow these steps:

#### Website URL:
[OpenWeatherMap API](https://openweathermap.org/api)

#### API Documentation:
[One Call API Documentation](https://openweathermap.org/api/one-call-3)

#### Steps to Get an API Key:
1. Sign up at [OpenWeatherMap Sign In](https://home.openweathermap.org/users/sign_in).
2. Use the following dummy credentials for testing:
   - **Email**: `xyz@tiiu.com`
   - **Password**: `abcd1234`
   - Note: These credentials are for demonstration purposes only. Replace with your own account for actual usage.
3. Generate your API key after logging in.

#### Test the API Using cURL:
Replace `api_key` with your generated API key:
```bash
curl "https://api.openweathermap.org/data/2.5/weather?q=London&appid=api_key"
```

### 2. Create a Virtual Environment
To isolate project dependencies:

#### Install Virtualenv:
```bash
pip install virtualenv
```

#### Create a Virtual Environment:
```bash
virtualenv env
```

#### Activate the Virtual Environment:
- On Windows:
  ```bash
  env\Scripts\activate
  ```
- On macOS/Linux:
  ```bash
  source env/bin/activate
  ```

### 3. Install Required Packages
Make sure you have a `requirements.txt` file with all dependencies listed. Install the packages:
```bash
pip install -r requirements.txt
```

## Ask the Chatbot for Assistance
This project includes a chatbot feature. You can ask the chatbot how to use the free API with a cURL request. For example:

**Question:** How do I use the free API with cURL?

The chatbot will provide the relevant command.

---

### Note:
For further customization or usage, refer to the provided documentation links. Ensure you handle sensitive information, like API keys, securely and do not expose them in public repositories.
