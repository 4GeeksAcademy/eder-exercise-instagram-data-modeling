import os
import sys
from sqlalchemy import Column, ForeignKey, Integer, String
from sqlalchemy.orm import relationship, declarative_base
from sqlalchemy import create_engine
from eralchemy2 import render_er

Base = declarative_base()


class Follow(Base):
    __tablename__ = 'follow'
    followID = Column(Integer,primary_key=True)
    init = Column(String(),nullable=False)
    end = Column(String(),nullable=False)
    created = Column(String(),nullable=False)

class User(Base):
    __tablename__='user'
    userID = Column(Integer,primary_key=True)
    profile_photo = Column(String(),nullable=False)
    name = Column(String(),nullable=False)
    type = Column(String(),nullable=False)
    description = Column(String(),nullable=False)
    email = Column(String(),nullable=False)
    phone = Column(String(),nullable=False)
    created = Column(String(),nullable=False)
    privacy = Column(String(),nullable=False)
    follower = Column(String(),nullable=False)
    follow = Column(String(),nullable=False)
    highlight = relationship('Highlight',backref='user',lazy=True)
    reel = relationship('Reel',backref='user',lazy=True)
    post = relationship('Post',backref='user',lazy=True)
    story = relationship('Story',backref='user',lazy=True)
    story_like = relationship('Story_like',backref='user',lazy=True)
    story_comment = relationship('Story_comment',backref='user',lazy=True)
    post_like = relationship('Post_like',backref='user',lazy=True)
    post_comment = relationship('Post_comment',backref='user',lazy=True)
    reel_like = relationship('Reel_like',backref='user',lazy=True)
    reel_comment = relationship('Reel_comment',backref='user',lazy=True)


class Highlight(Base):
    __tablename__ = 'highlight'
    highlightID = Column(Integer,primary_key=True)    
    name = Column(String(),nullable=False)
    thumbnail = Column(String(),nullable=False)
    created = Column(String(),nullable=False)
    storyID = Column(Integer,ForeignKey('story.storyID'),nullable=False)
    userID = Column(Integer,ForeignKey('user.userID'), nullable =False)

class Collection(Base):
    __tablename__ = 'collection'
    collectionID = Column(Integer,primary_key=True)
    name = Column(String(),nullable=False)
    created = Column(String(),nullable=False)
    thumbnail = Column(String(),nullable=False)
    reelID = Column(Integer, ForeignKey('reel.reelID'),nullable=False)
    postID = Column(Integer,ForeignKey('post.postID'),nullable=False)
    userID = Column(Integer,ForeignKey('user.userID'),nullable=False)


class Post(Base):
    __tablename__ = 'post'
    postID = Column(Integer,primary_key=True)
    bgsong = Column(String(),nullable=False)
    audience = Column(String(),nullable=False)
    place = Column(String(),nullable=False)
    draft = Column(String,nullable=False)
    collection = relationship('Collection', backref='post',lazy=True)
    mediaID = Column(Integer,ForeignKey('media.mediaID'),nullable=False)
    post_likeID = Column(Integer,ForeignKey('post_like.post_likeID'),nullable=False)    
    post_commentID = Column(Integer,ForeignKey('post_comment.post_commentID'),nullable=False)
    post_like = relationship('Post_like',backref='post',lazy=True)
    post_comment = relationship('Post_comment',backref='post',lazy=True)
    userID = Column(Integer,ForeignKey('user.userID'),nullable=False)

 

class Reel(Base):
    __tablename__ = 'reel'
    reelID = Column(Integer,primary_key=True)
    bgsong = Column(String(),nullable=False)
    place = Column(String(),nullable=False)
    draft = Column(String,nullable=False)
    mediaID = Column(Integer,ForeignKey('media.mediaID'),nullable=False)
    collection = relationship('Collection',backref='reel',lazy=True)
    reel_likeID = Column(Integer,ForeignKey('reel_like.reel_likeID'),nullable=False)
    reel_commentID = Column(Integer,ForeignKey('reel_comment.reel_commentID'),nullable=False)
    reel_like= relationship('Reel_like',backref='reel',lazy=True)
    reel_comment = relationship('Reel_comment', backref='reel',lazy=True)
    userID = Column(Integer,ForeignKey('user.userID'),nullable=False)




class Story(Base):
    __tablename__ = 'story'
    storyID = Column(Integer,primary_key=True)
    bgsong = Column(String(),nullable=False)
    place = Column(String(),nullable=False)
    audience = Column(String(),nullable=False)   
    draft = Column(String,nullable=False)
    highlight = relationship('Highlight', backref='story',lazy=True)
    mediaID = Column(Integer,ForeignKey('media.mediaID'),nullable=False)
    story_likeID= Column(Integer,ForeignKey('story_like.story_likeID'),nullable=False)
    story_commentID = Column(Integer,ForeignKey('story_comment.story_commentID'),nullable=False)
    story_like = relationship('Story_like',backref='story',lazy=True)
    story_comment = relationship('Story_comment',backref='story',lazy=True)
    userID = Column(Integer,ForeignKey('user.useriD'),nullable=False)



class Media(Base):
    __tablename__ = 'media'
    mediaID = Column(Integer,primary_key=True)
    fileref = Column(String(),nullable=False)
    type = Column(String(),nullable=False)
    created = Column(String(),nullable=False)
    post = relationship('Post',backref='media',lazy=True)
    reel = relationship('Reel',backref='media', lazy=True)
    story = relationship('Story',backref='media',lazy=True)
    



class Post_like(Base):
    __tablename__ = 'post_like'
    post_likeID = Column(Integer,primary_key=True)
    created = Column(String(),nullable=False)
    post = relationship('Post',backref='post_like',lazy=True)
    postID = Column(Integer,ForeignKey('post.postID'),nullable=False)
    userID = Column(Integer,ForeignKey('user.userID'),nullable=False)
    


class Reel_like(Base):
    __tablename__ = 'reel_like'
    reel_likeID = Column(Integer,primary_key=True)
    created = Column(String(),nullable=False)
    reel = relationship('Reel',backref='media',lazy=True)
    reelID = Column(Integer,ForeignKey('reel.reelID'),nullable=False)
    userID = Column(Integer,ForeignKey('user.userID'),nullable=False)
   

class Story_like(Base):
    __tablename__ = 'story_like'
    story_likeID = Column(Integer,primary_key=True)
    created = Column(String(),nullable=False)
    story= relationship('Story',backref='story_like',lazy=True)
    storyID = Column(Integer,ForeignKey('story.storyID'),nullable=False)
    userID = Column(Integer,ForeignKey('user.userID'),nullable=False)

   
    


class Post_comment(Base):
    __tablename__ = 'post_comment'
    post_commentID = Column(Integer,primary_key=True)
    created = Column(String(),nullable=False)
    post = relationship('Post',backref='post_comment', lazy=True)
    postID = Column(Integer,ForeignKey('post.postID'),nullable=False)
    userID = Column(Integer,ForeignKey('user.userID'),nullable=False)
    
   

class Reel_comment(Base):
    __tablename__ = 'reel_comment'
    reel_commentID = Column(Integer,primary_key=True)
    created = Column(String(),nullable=False)
    reel = relationship('Reel',backref='reel_comment',lazy=True)
    reelID = Column(Integer,ForeignKey('reel.reelID'),nullable=False)
    userID = Column(Integer,ForeignKey('user.userID'),nullable=False)
    
    
    

class Story_comment(Base):
    __tablename__ = 'story_comment'
    story_commentID = Column(Integer,primary_key=True)
    created = Column(String(),nullable=False)
    story = relationship('Story',backref='story_comment',lazy=True)
    storyID = Column(Integer,ForeignKey('story.storyID'),nullable=False)
    userID = Column(Integer,ForeignKey('user.userID'),nullable=False)
  













""" class Person(Base):
    __tablename__ = 'person'
    # Here we define columns for the table person
    # Notice that each column is also a normal Python instance attribute.
    id = Column(Integer, primary_key=True)
    name = Column(String(250), nullable=False)

class Address(Base):
    __tablename__ = 'address'
    # Here we define columns for the table address.
    # Notice that each column is also a normal Python instance attribute.
    id = Column(Integer, primary_key=True)
    street_name = Column(String(250))
    street_number = Column(String(250))
    post_code = Column(String(250), nullable=False)
    person_id = Column(Integer, ForeignKey('person.id'))
    person = relationship(Person)

    def to_dict(self):
        return {} """

## Draw from SQLAlchemy base
try:
    result = render_er(Base, 'diagram.png')
    print("Success! Check the diagram.png file")
except Exception as e:
    print("There was a problem genering the diagram")
    raise e
