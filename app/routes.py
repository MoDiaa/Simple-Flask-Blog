from flask import render_template, request, redirect, url_for, Blueprint
from app import db
from app.models import User,Post


bp = Blueprint('main', __name__)

@bp.route('/', methods=['GET', 'POST'])
def index():
    error = None
    if request.method == 'POST':
        name = request.form['name']
        email = request.form['email']
        bio = request.form.get('bio')
        if name and email:
            # Check if the email already exists
            existing_user = User.query.filter_by(email=email).first()
            if existing_user:
                error = f"Email '{email}' is already registered."
            else:
                user = User(name=name, email=email)
                db.session.add(user)
                db.session.commit()
                return redirect(url_for('main.index'))
    users = User.query.all()
    posts = Post.query.order_by(Post.timestamp.desc()).limit(5).all()
    return render_template('index.html', users=users, posts=posts, error=error)  # Pass posts here@bp.route('/add_post', methods=['POST'])
@bp.route('/add_post', methods=['POST'])
def add_post():
    title = request.form['title']
    content = request.form['content']
    user_id = request.form['user_id']
    if title and content and user_id:
        post = Post(title=title, content=content, user_id=user_id)
        db.session.add(post)
        db.session.commit()
    return redirect(url_for('main.index'))