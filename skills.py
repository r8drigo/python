from flask_restful import Resource

skills_list = ['Python', 'Java', 'Flask', 'PHP']
class Skills(Resource):
    def get(self):
        return skills_list