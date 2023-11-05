import os

import redis
from flask import Flask
from prometheus_client import Counter, make_wsgi_app
from werkzeug.middleware.dispatcher import DispatcherMiddleware

app = Flask(__name__)

# Add prometheus wsgi middleware to route /metrics requests
app.wsgi_app = DispatcherMiddleware(app.wsgi_app, {"/metrics": make_wsgi_app()})

# Init prometheus counter outside of index function
visit_count = Counter('visits', 'Number of visits to this app since it started')

@app.route("/")
def index():
    username = os.environ["REDIS_USERNAME"]
    password = os.environ["REDIS_PASSWORD"]
    host = os.environ["REDIS_HOST"]
    port = os.environ["REDIS_PORT"]
    db = os.environ["REDIS_DB"]
    client = redis.Redis(
        username=username, password=password, host=host, port=port, db=db
    )
    key = "HIT_COUNT"
    count = int(client.get(key) or 0)
    response = f"Hello FELFEL. The count is: {count}"
    client.set(key, count + 1)
    # This increments the counter separate from the redis count which could cause discrepancies.
    # Another solution would be to set it to the value of the redis count with:
    # visit_count._value.set(count + 1)
    visit_count.inc()

    return response


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=8080)
