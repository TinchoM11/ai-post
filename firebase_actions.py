from firebase import db
from flask import jsonify
import uuid


def get_transaction(id):
    collection_ref = db.collection("posts")

    doc_ref = collection_ref.document(id)

    try:
        doc = doc_ref.get()
        print("Document data: ", doc.to_dict())

        if doc.exists:
            return doc.to_dict()
        else:
            return "Post not found"
    except Exception as e:
        print("Error:", e)
        return "Error occurred while retrieving post data"


def save_new_post(post_content):
    # If no ID is provided, Firestore will generate a random one
    print("Saving new Post...", post_content)
    collection_ref = db.collection("posts")

    try:
        # Create a dictionary to save the post data
        post_data = {
            "content": post_content
        }

        id = str(uuid.uuid4())
        # Save the data to Firestore with the id provided
        doc_ref = collection_ref.document(id)
        doc_ref.set(post_data)

        return jsonify({
            "message": "New Post Saved successfully.",
            "post_details": {
                "id": id,
                "content": post_content
            }
        })
    except Exception as e:
        print("Error:", e)
        return "Error occurred while saving new post"
