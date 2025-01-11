from mira_sdk import MiraClient, Flow

import os
from dotenv import load_dotenv
load_dotenv()
# Initialize the client
client = MiraClient(config={"API_KEY": os.getenv("MIRA_API_KEY")})

# Load the flow configuration
flow = Flow(source="flow.yaml")

# Define test inputs
input_dict = {
    "user_age": "25",
    "user_gender": "male",
    "fitness_goal": "weight loss",
    "fitness_level": "beginner",
    "preferred_workout_types": "cardio, strength training",
    "available_equipment": "dumbbells, resistance bands",
    "workout_duration": "45",
    "days_per_week": "5",
    "user_feedback": "too intense",
    "progress_metrics": "weight: 70, body_fat_percentage: 20"
}

# Test the flow
response = client.flow.test(flow, input_dict)
print("Test Response:", response)
