from mira_sdk import MiraClient

import os
from dotenv import load_dotenv
load_dotenv()
# Initialize the client
client = MiraClient(config={"API_KEY": os.getenv("MIRA_API_KEY")})

# Fetch and save the current flow version
flow = client.flow.get("addy/workout-planner")
flow.save("flow.yaml")

# Make updates to the flow in the YAML file, then redeploy
client.flow.deploy(flow)
