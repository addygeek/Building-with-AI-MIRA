from mira_sdk import MiraClient, Flow
from dotenv import load_dotenv
import os

# Load environment variables from .env file
load_dotenv()

api_key = os.getenv("API_KEY")

# Initialize the client
client = MiraClient(config={"API_KEY": api_key})

version = "0.0.2"
input_data = {"topic": "Hard Life", "style": "Lil Wayne"}

# If no version is provided it'll use latest version by default
if version:
	flow_name = f"addy/raps-song-generator/{version}"
else:
	flow_name = "addy/raps-song-generator"

result = client.flow.execute(flow_name, input_data)
print(result)