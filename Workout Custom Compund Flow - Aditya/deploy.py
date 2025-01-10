from mira_sdk import MiraClient, CompoundFlow
from mira_sdk.exceptions import FlowError
from dotenv import load_dotenv
import os

# Load environment variables from .env file
load_dotenv()

api_key = os.getenv("API_KEY")

client = MiraClient(config={"API_KEY": api_key})
flow = CompoundFlow(source="flow.yaml")

try:
    client.flow.deploy(flow)
    print("Compound flow deployed successfully!")
except FlowError as e:
    print(f"Deployment error: {str(e)}")
