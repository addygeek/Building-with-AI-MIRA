from mira_sdk import MiraClient, Flow
from mira_sdk.exceptions import FlowError
import os
from dotenv import load_dotenv
load_dotenv()
# Initialize the client

client = MiraClient(config={"API_KEY": os.getenv("MIRA_API_KEY")})

# Load the flow configuration
flow = Flow(source="flow.yaml")

# Deploy the flow
try:
    client.flow.deploy(flow)
    print("Flow deployed successfully.")
except FlowError as e:
    print(f"Deployment error: {str(e)}")
