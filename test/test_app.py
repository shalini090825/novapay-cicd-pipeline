import sys
sys.path.append(".")
from app import app
def test_home():
    client = app.test_client()
    response = client.get("/")
    if response.status_code != 200:
        raise Exception ("Home page failed")
def test_health():
    client = app.test_client()
    response = client.get("/health")
    if response.status_code != 200:
        raise Exception ("Health check failed")
