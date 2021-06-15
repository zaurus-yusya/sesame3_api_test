import os
from dotenv import load_dotenv
load_dotenv()

from pysesame3.auth import WebAPIAuth
from pysesame3.lock import CHSesame2

API_KEY = os.environ['API_KEY']
SESAME3_UUID = os.environ['SESAME3_UUID']
SESAME3_SECRET = os.environ['SESAME3_SECRET']

auth = WebAPIAuth(apikey=API_KEY)
sesame3_uuid = SESAME3_UUID
sesame3_secret = SESAME3_SECRET

device = CHSesame2(
	authenticator=auth,
	device_uuid=sesame3_uuid,
	secret_key=sesame3_secret,
)

device.toggle()