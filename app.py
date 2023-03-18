#!/usr/bin/env python

import os

from flask import Flask, jsonify, request
from sentence_transformers import SentenceTransformer
from waitress import serve
from flask_cors import CORS
from time import strftime
import logging
import traceback

logger = logging.getLogger('waitress')
logger.setLevel(logging.INFO)

app = Flask(__name__)
CORS(app)

model_name = os.environ.get('MODEL')
port = os.environ.get('PORT', 5000)

@app.route('/', methods=['POST'])
def encode():
    data = request.get_json(force=True)

    sentences = data.get("sentences", [])
    batch_size = int(data.get("batch_size", 8))

    embeddings = encoder.encode(sentences, batch_size=batch_size)

    return jsonify({ "embeddings": embeddings.tolist(), "count": len(embeddings) })

@app.route('/health')
def health():
    return "OK"

@app.after_request
def after_request(response):
    timestamp = strftime('[%Y-%b-%d %H:%M]')
    logger.error('%s %s %s %s %s %s', timestamp, request.remote_addr, request.method, request.scheme, request.full_path, response.status)
    return response

@app.errorhandler(Exception)
def exceptions(e):
    tb = traceback.format_exc()
    timestamp = strftime('[%Y-%b-%d %H:%M]')
    logger.error('%s %s %s %s %s 5xx INTERNAL SERVER ERROR\n%s', timestamp, request.remote_addr, request.method, request.scheme, request.full_path, tb)
    return e, 500

if __name__ == '__main__':
    logger.info(f"Using model {model_name}")
    encoder = SentenceTransformer(model_name)

    serve(app, host="0.0.0.0", port=port)