from flask import Flask
from prometheus_client import Counter, generate_latest

app = Flask(__name__)

visit_counter = Counter("visit_count", "Number of visits to the homepage")

@app.route("/")
def hello():
    visit_counter.inc()
    return "<h2>Welcome to Mini Project!</h2>"

@app.route("/metrics")
def metrics():
    return generate_latest(), 200, {"Content-Type": "text/plain; charset=utf-8"}

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)