from mira_sdk import MiraClient, Flow
from dotenv import load_dotenv
import os

# Load environment variables from .env file
load_dotenv()

api_key = os.getenv("MIRA_API_KEY")
if not api_key:
    raise ValueError("MIRA_API_KEY is not set in the environment variables.")

# Initialize the client
client = MiraClient(config={"API_KEY": api_key})

flow = Flow(source="flow.yaml")

#Hard coded for "topic" and "style"
input_dict = {"topic": "Easy Life", "style": "Lil Wayne"}

response = client.flow.test(flow, input_dict)
# print(response)
#responce in \n, \\ & \\n sepearted values

# Extract the result and remove unwanted characters
output = response.get("result", "No output generated.")
formatted_output = output.replace("\\n", "\n").replace("\\'", "'")

print("Generated Rap Song:\n")
print(formatted_output)