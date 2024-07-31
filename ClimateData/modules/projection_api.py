from dotenv import load_dotenv
import os
load_dotenv()

api_key = os.getenv("CLIMATE_API_KEY")

print("API_KEY: ", api_key)

# def projectedData(parameters):
#     print()