from flask_restful import Api
from flask import Blueprint


from .meetup import Meetup
from .user import User
from .question import Question
from .get_all_meetups import Meetups
from .get_all_questions import Questions
from .get_all_users import Users

version1=Blueprint("api",__name__, url_prefix="/api/v1")
api=Api(version1)
api.add_resource(User,'/user/<username>')
api.add_resource(Meetup,'/meetup/<topic_name>')
api.add_resource(Question,'/question/<title_name>')
api.add_resource(Meetups,'/meetups')
api.add_resource(Questions,'/questions')
api.add_resource(Users,'/users')

