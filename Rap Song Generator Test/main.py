from mira_sdk import MiraClient, Flow
import os
from dotenv import load_dotenv
load_dotenv()
# Initialize the client
client = MiraClient(config={"API_KEY": os.getenv("MIRA_API_KEY")})

version = "0.0.2"
input_data = {
    "style": "West",
    "topic": "hard life"
}


# If no version is provided, latest version is used by default
if version:
    flow_name = f"@venmus/rap-song-generator/{version}"
else:
    flow_name = "@venmus/rap-song-generator"

result = client.flow.execute(flow_name, input_data)
print(result)