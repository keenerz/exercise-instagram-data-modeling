import os
import sys
from sqlalchemy import Column, ForeignKey, Integer, String
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import relationship
from sqlalchemy import create_engine
from eralchemy import render_er

Base = declarative_base()

class User(Base):
    __tablename__ = 'user'
    id = Column(Integer, primary_key=True)
    name = Column(String(250), nullable=False)
    username = Column(String(250), nullable=False, unique=True)
    email = Column(String(250), nullable=False, unique=True)
    password = Column(String(250), nullable=False)

class Followers(Base):
    __tablename__ = 'followers'
    id = Column(Integer, primary_key=True)
    user_id = Column(String(250), ForeignKey('user.id'), nullable=False)
    follower_id = Column(String(250), ForeignKey('user.id'), nullable=False)

class Post(Base):
    __tablename__ = 'post'
    id = Column(Integer, primary_key=True)
    user_id = Column(String(250), ForeignKey('user.id'), nullable=False)
    username = Column(String(250), ForeignKey('user.username'), nullable=False)
    total_likes = Column(Integer, ForeignKey('user.total_likes'), nullable=True)
    total_comments = Column(Integer, ForeignKey('user.total_comments'), nullable=True)

class Media(Base):
    __tablename__ = 'media'
    id = Column(Integer, primary_key=True)
    url = Column(String(250), nullable=False)
    post_id = Column(Integer, ForeignKey('post.id'), nullable=False)

class Comment(Base):
    __tablename__ = 'comment'
    id = Column(Integer, primary_key=True)
    comment_text = Column(String(250), nullable=True)
    user_id = Column(Integer, ForeignKey('user.id'), nullable=False)
    post_id = Column(Integer, ForeignKey('post.id'), nullable=False)

class Likes(Base):
    __tablename__ = 'likes'
    id = Column(Integer, primary_key=True)
    like_count = Column(Integer, nullable=False)
    post_id = Column(Integer, ForeignKey('post.id'), nullable=False)
    user_id = Column(Integer, ForeignKey('user.id'), nullable=False)

class Hashtag_Comment(Base):
    __tablename__ = 'hashtag_comment'
    id = Column(Integer, primary_key=True)
    hashtag_id = Column(Integer, ForeignKey('comment.id'), nullable=False)
    hashtag_text = Column(String(250), nullable=False)

    def to_dict(self):
        return {}

## Draw from SQLAlchemy base
try:
    result = render_er(Base, 'diagram.png')
    print("Success! Check the diagram.png file")
except Exception as e:
    print("There was a problem genering the diagram")
    raise e