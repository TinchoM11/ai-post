from flask import request, jsonify
from firebase_actions import get_transaction, save_new_post
from main import main


def new_post():
    if request.method == 'POST':
        initial_message = request.json.get('initial_message')
        # If not initial_message is provided or shorter than 10 characters, return an error
        if not initial_message or len(initial_message) < 10:
            return jsonify({'message': 'Initial Message too short or not sent'}), 400
        try:
            post_content = main(initial_message)
            res = save_new_post(post_content)
            return res, 201
        except ValueError as e:
            return str(e), 400


def get_post(post_id):
    if request.method == 'GET':
        post = get_transaction(post_id)
        if post != "Post not found":
            return jsonify(post), 200
        else:
            return jsonify({'message': 'Post not found'}), 404
