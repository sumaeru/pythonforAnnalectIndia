from flask import Flask, request, jsonify
from flask_sqlalchemy import SQLAlchemy
from flask_marshmallow import Marshmallow,fields
from marshmallow import Schema,fields,validate,validates,validates_schema,ValidationError


import os
 
 
 
#initliazing our flask app, SQLAlchemy and Marshmallow
app = Flask(__name__)
 
basedir = os.path.abspath(os.path.dirname(__file__))
app.config['SQLALCHEMY_DATABASE_URI'] = \
      'sqlite:///'+ os.path.join(basedir,'freak.db')
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
 
 
db = SQLAlchemy(app)
ma = Marshmallow(app)
 
 
#this is our database model
class Post(db.Model):
    id = db.Column(db.Integer, primary_key = True)
    title = db.Column(db.String(100))
    description = db.Column(db.String(200))
    author = db.Column(db.String(50))
 
 
    def __init__(self, title, description, author):
        self.title = title
        self.description = description
        self.author = author

 
#we are drowned in opinions those who byheart all the best.

class PostValidation(ma.Schema):
    title=fields.Str(required=True)
    author=fields.Email(required=True)
    description=fields.String(required=True)

 
# class PostSchema(ma.Schema):

#     class Meta:
#         fields = ("title", "author", "description")
 
 
#post_schema = PostSchema()#observe where it is used
#posts_schema = PostSchema(many=True)#observe where it is used

post_schema=PostValidation()
posts_schema=PostValidation(many=True)
validation=PostValidation()








#with app.app_context():
 #   db.create_all()



 
#adding a post
@app.route('/post', methods = ['POST'])
def add_post():
        errors = validation.validate(request.json)
        if(errors):
             return errors,422
        title = request.json['title']
        description = request.json['description']
        author = request.json['author']
        my_posts = Post(title, description, author)
        db.session.add(my_posts)
        db.session.commit()
        return validation.jsonify(my_posts)
    
    
    
 
 
 
 
#getting posts
@app.route('/get', methods = ['GET'])
def get_post():
    all_posts = Post.query.all()
    result = posts_schema.dump(all_posts)
 
    return jsonify(result)
 
 
#getting particular post
@app.route('/post_details/<id>/', methods = ['GET'])
def post_details(id):
    post = Post.query.get(id)
    return post_schema.jsonify(post)
 
 
#updating post
@app.route('/post_update/<id>/', methods = ['PUT'])
def post_update(id):
    post = Post.query.get(id)
 
    title = request.json['title']
    description = request.json['description']
    author = request.json['author']
 
 
    post.title = title
    post.description = description
    post.author = author
 
    db.session.commit()
    return post_schema.jsonify(post)
 
 
 
#deleting post
@app.route('/post_delete/<id>/', methods = ['DELETE'])
def post_delete(id):
    post = Post.query.get(id)
    db.session.delete(post)
    db.session.commit()
 
    return post_schema.jsonify(post)
 
 
 

if __name__ == "__main__":
    app.run(debug=True)