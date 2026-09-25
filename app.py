from flask import Flask
app = Flask(__name__)
@app.route("/")
def home():
    return """
    <h1>NovaPay Digital Bank</h1>
    <p>Application is running successfully!</p>
    <p>Version: 1.0 blue</p>
    """
@app.route("/health")
def health():
    return "Healthy"

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)  # nosec B104
