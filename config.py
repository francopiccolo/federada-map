import os
from dotenv import load_dotenv

load_dotenv()

GOOGLE_MAPS_GEOCODING_API_KEY = os.environ.get('GOOGLE_MAPS_GEOCODING_API_KEY')