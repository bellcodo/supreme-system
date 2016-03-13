from flask import Flask
import os
app = Flask(__name__)

@app.route("/")
def hello():
    return "Hello World!"

@app.route('/post/username/<string:uname>/activity/<string:activity>')
def show_post(post_id):
    # show the post with the given id, the id is an integer
    return 'Post %d' % post_id

if __name__ == "__main__":
    port = int(os.environ.get("PORT", 5000))
    app.run(host='0.0.0.0', port=port)
