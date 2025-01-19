from dotenv import load_dotenv
import os
import pandas as pd
import requests

load_dotenv()

var = os.getenv("API_KEY_NAME")

print(var)