from flask import Flask, jsonify
from diskcache import Cache
import requests

app = Flask(__name__)

cache = Cache(directory="cache/", size_limit=int(4e9))


@app.route("/")
def index():
    return "welcome to ipfs-cdn!"

@app.route("/ipfs/<key>")
def ipfs(key: str):
    if key not in cache:
        resp = requests.get(f"https://dweb.link/ipfs/{key}")
        assert resp.status_code==200
        cache.set(key=key, value=resp.content)
    return cache.get(key=key)

@app.route("/ipfs/db/stats")
def ipfs_db_stats():
    keys = list(cache.iterkeys())
    size = cache.volume()
    max_size = cache.size_limit
    percent = size / max_size * 100
    return jsonify({
        "keys": len(keys),
        "size": f"{round(size/1024/1024, 2)} MB ({round(percent, 2)}%)",
    })