from flask import Flask, request, redirect, jsonify
import redis
import hashlib
import os
from flask_cors import CORS

# Initialize Flask app
app = Flask(__name__)
CORS(app)  # Enable CORS for frontend access

# Get Redis connection details from environment variables
REDIS_HOST = os.getenv("REDIS_HOST", "redis")
REDIS_PORT = int(os.getenv("REDIS_PORT", 6379))

# Connect to Redis with error handling
try:
    redis_client = redis.StrictRedis(host=REDIS_HOST, port=REDIS_PORT, decode_responses=True)
    redis_client.ping()  # Check if Redis is reachable
except redis.ConnectionError:
    print("Error: Unable to connect to Redis. Ensure Redis is running.")
    redis_client = None  # Set to None so app doesn't crash

def shorten_url(long_url):
    """Generate a short URL using MD5 hash (first 6 characters)."""
    short_hash = hashlib.md5(long_url.encode()).hexdigest()[:6]
    if redis_client:
        redis_client.set(short_hash, long_url)
    return short_hash

@app.route('/shorten', methods=['POST'])
def shorten():
    """API to shorten a long URL."""
    if not redis_client:
        return jsonify({"error": "Redis is unavailable"}), 500

    data = request.get_json()
    long_url = data.get("url")
    if not long_url:
        return jsonify({"error": "URL required"}), 400

    short_url = shorten_url(long_url)
    return jsonify({"short_url": f"http://localhost:5000/{short_url}"})

@app.route('/<short_url>')
def redirect_to_long_url(short_url):
    """Redirect to the original long URL using the shortened hash."""
    if not redis_client:
        return jsonify({"error": "Redis is unavailable"}), 500

    long_url = redis_client.get(short_url)
    if long_url:
        return redirect(long_url)
    return jsonify({"error": "Short URL not found"}), 404

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
