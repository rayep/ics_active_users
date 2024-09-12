"""ICS Active Users"""

import ssl
from src.auth import HTTPAuthMgr
from src.client import RESTClient

# SSL Context for ignoring certificate errors.
try:
    _create_unverified_https_context = ssl._create_unverified_context
except AttributeError:
    # Legacy Python that doesn't verify HTTPS certificates by default
    pass
else:
    # Handle target environment that doesn't support HTTPS verification
    ssl._create_default_https_context = _create_unverified_https_context

HOST = '<VPN-SERVER-HOSTNAME>'
USERNAME = '<USERNAME>'
PASSWORD = '<PASSWORD>'

user_pass_authmanager = HTTPAuthMgr(HOST, USERNAME, PASSWORD)
client_1 = RESTClient(user_pass_authmanager)

api_key = client_1.get(f"https://{HOST}/api/v1/auth")['api_key']

api_authmanager = HTTPAuthMgr(HOST, api_key, '')
client_2 = RESTClient(api_authmanager)

active_users = client_2.get(
    f"https://{HOST}/api/v1/system/active-users?number=100")  # top 100 users
