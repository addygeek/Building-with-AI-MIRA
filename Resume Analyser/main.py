from mira_sdk import MiraClient, Flow
import os
from dotenv import load_dotenv
load_dotenv()

# Initialize the client
client = MiraClient(config={"API_KEY": os.getenv("MIRA_API_KEY")})

version = "1.0.0"
input_data = {
    "resume_query": "What did john do at meta?"
}

# If no version is provided, latest version is used by default
if version:
    flow_name = f"@cosmic-labs/resume-analyser/{version}"
else:
    flow_name = "@cosmic-labs/resume-analyser"

result = client.flow.execute(flow_name, input_data)
print(result)
print(result)
print(result)
print(result)