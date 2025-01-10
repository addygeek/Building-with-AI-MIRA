from mira_sdk import MiraClient
from mira_sdk.exceptions import FlowError
from dotenv import load_dotenv
import os

# Load environment variables from .env file
load_dotenv()

api_key = os.getenv("MIRA_API_KEY")
flow_name = "your-username/custom-workout-planner"
input_data = {
    "fitness_goal": "strength",
    "available_equipment": "dumbbells, yoga mat",
    "time_available": 30
}
client = MiraClient(config={"API_KEY": api_key})
try:
    result = client.flow.execute(flow_name, input_data)
    print("Execution result:", result)
except FlowError as e:
    print("Execution error:", str(e))
