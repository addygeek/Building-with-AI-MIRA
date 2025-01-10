from mira_sdk import Flow, MiraClient
from mira_sdk.exceptions import FlowError
import os
from dotenv import load_dotenv
# Load environment variables from .env file
load_dotenv()

api_key = os.getenv("MIRA_API_KEY")

client = MiraClient(config={"API_KEY": api_key})     # Initialize client

# Load existing flow
# flow = client.flow.get("author/flow_name")                  # Get current version
# flow.save("flow.yaml")                            # Save for editing

flow  = Flow(source='flow.yaml')
# Deploy updated flow
try:
    client.flow.deploy(flow)                                # Deploy new version
except FlowError as e:
    print(f"Error occurred: {str(e)}")                      # Handle update error

# In case you forget to bump the flow version, it will get bumped by default every time you deploy the same flow.