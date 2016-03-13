from app import app, db
from .models import Post
from datetime import datetime

@app.route("/")
def hello():
    return "Hello World!"

@app.route('/post/username/<uname>/activity/<activity>', methods=['GET'])
def show_post(uname, activity):
    language = ''
    post = Post(body=activity, timestamp=datetime.utcnow(), author=uname)
    db.session.add(post)
    db.session.commit()
    return 'Uname %s activty %s' %( uname, activity )
