from flask import request, jsonify
from firebase_actions import get_transaction, save_new_post
from main import main


def new_post():
    if request.method == 'POST':
        initial_message = request.json.get('initial_message')
        # Asegúrate de tener acceso a main() desde aquí
        post_content = main(initial_message)
        res = save_new_post(post_content)
        return res, 201


def get_post(post_id):
    if request.method == 'GET':
        post = get_transaction(post_id)
        if post != "Post not found":
            return jsonify(post), 200
        else:
            return jsonify({'message': 'Post not found'}), 404
