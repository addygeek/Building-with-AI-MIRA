from mira_sdk import MiraClient, CompoundFlow
from mira_sdk.exceptions import FlowError
from dotenv import load_dotenv
import os

# Load environment variables from .env file
load_dotenv()

api_key = os.getenv("MIRA_API_KEY")

# Initialize Mira Client with your API key
client = MiraClient(config={"API_KEY": api_key})

# Load your compound flow configuration
flow = CompoundFlow(source="flow.yaml")

# Prepare test input data
test_input = {
    "prime_input_1": "test data",
    "prime_input_2": "test parameters"
}

try:
    # Test the entire pipeline
    response = client.flow.test(flow, test_input)
    print("Test response:", response)
except FlowError as e:
    print("Test failed:", str(e))
