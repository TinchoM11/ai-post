from flask import Flask
from routes import new_post, get_post

app = Flask(__name__)

app.route('/new_post', methods=['POST'])(new_post)
app.route('/post/<string:post_id>', methods=['GET'])(get_post)

if __name__ == '__main__':
    app.run(debug=True)
