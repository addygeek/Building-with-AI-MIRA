from mira_sdk import MiraClient, CompoundFlow
from mira_sdk.exceptions import FlowError
from dotenv import load_dotenv
import os

# Load environment variables from .env file
load_dotenv()

api_key = os.getenv("API_KEY")

client = MiraClient(config={"API_KEY":api_key })
flow = CompoundFlow(source="flow.yaml")

test_input = {
    "fitness_goal": "strength",
    "available_equipment": "dumbbells, yoga mat",
    "time_available": 30
}

try:
    response = client.flow.test(flow, test_input)
    print("Test response:", response)
except FlowError as e:
    print("Test failed:", str(e))
