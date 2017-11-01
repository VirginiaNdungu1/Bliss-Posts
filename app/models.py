from . import db
from werkzeug.security import generate_password_hash, check_password_hash
from flask_login import UserMixin
from . import login_manager


@login_manager.user_loader
def load_user(id):
    '''
    callback function that retrieves a user
    when a unique identifier is passed in it

    The function queries the database and gets
    a User with that ID
    '''
    return User.query.get(int(id))


class Role(db.Model):
    '''
    Create new roles
    Pass in db.Model as Arg

    Reason:
    Connect this class to our db and allow communication
    '''
    __tablename__ = 'roles'
    role_id = db.Column(db.Integer, primary_key=True)
    role = db.Column(db.String(255))
    users = db.relationship('User', backref='role', lazy='dynamic')

    def __repr__(self):
        return f'Role {self.role}'


class User(UserMixin, db.Model):
    '''
    Create new users
    Pass in db.Model as Arg

    Reason:
    Connect this class to our db and allow communication
    '''
    __tablename__ = 'users'
    id = db.Column(db.Integer, primary_key=True)
    fullname = db.Column(db.String(255))
    username = db.Column(db.String(255))
    email = db.Column(db.String(255), unique=True, index=True)
    password_hash = db.Column(db.String(255))
    profession = db.Column(db.String(255))
    quote = db.Column(db.String(255))
    roles = db.Column(db.Integer, db.ForeignKey('roles.role_id'))
    posts = db.relationship('Post', backref='user', lazy="dynamic")
    comments = db.relationship(
        'Comment', backref='user', lazy="dynamic")

    @property
    def password(self):
        raise AttributeError('You cannot read the password attribute')

    @password.setter
    def password(self, password):
        self.password_hash = generate_password_hash(password)

    def verify_password(self, password):
        return check_password_hash(self.password_hash, password)

    def __repr__(self):
        return f'User {self.username}'


class Category(db.Model):
    '''
    Create new categories
    Pass in db.Model as Arg

    Reason:
    Connect this class to our db and allow communication
    '''
    __tablename__ = 'categories'
    category_id = db.Column(db.Integer, primary_key=True)
    topic = db.Column(db.String(255))
    category_post = db.relationship(
        'Post', backref='category', lazy='dynamic')

    def save_category(self):
        db.session.add(self)
        db.session.commit()

    @classmethod
    def get_category(self, id):
        category = Category.query.filter_by(category_id=id).all()
        return category

    def __repr__(self):
        return f'Category {self.topic}'


class Post(db.Model):
    '''
    Create new posts
    Pass in db.Model as Arg

    Reason:
    Connect this class to our db and allow communication
    '''
    __tablename__ = 'posts'
    post_id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String())
    description = db.Column(db.String())
    votes = db.Column(db.Integer)
    category_id = db.Column(
        db.Integer, db.ForeignKey('categories.category_id'))
    user_id = db.Column(db.Integer, db.ForeignKey('users.id'))
    comment_id = db.Column(db.Integer, db.ForeignKey('comments.comments_id'))

    def save_post(self):
        '''
        method that saves an instance of the Review Model
        to session and commits it to the database
        '''
        db.session.add(self)
        db.session.commit()

    @classmethod
    def get_post(cls, category_id, user_id):
        posts = Post.query.filter_by(
            category_id=id, user_id=postsuser_id).all()
        return posts

    def __repr__(self):
        return f'Post {self.title}'


class Comment(db.Model):
    '''
    Create new comments
    Pass in db.Model as Arg

    Reason:
    Connect this class to our db and allow communication
    '''
    __tablename__ = 'comments'
    comments_id = db.Column(db.Integer, primary_key=True)
    comment_description = db.Column(db.String())
    users_id = db.Column = db.Column(db.Integer, db.ForeignKey('users.id'))

    def save_comment(self):
        '''
        method that saves an instance of the Review Model
        to session and commits it to the database
        '''
        db.session.add(self)
        db.session.commit()

    @classmethod
    def get_comment(cls, post_id, user_id):
        comments = Post.query.filter_by(post_id=id, alluser_id=user_id).all()
        return comments

    def __repr__(self):
        return f'Comment {self.comment_description}'
