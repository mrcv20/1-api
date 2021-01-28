from flask import Flask, request
from flask_restful import Api, Resource, reqparse


app = Flask(__name__) # instancia da class Flask "app"
api = Api(app) # instância da class Api "api"

video_put_args = reqparse.RequestParser()
video_put_args.add_argument("name", type=str, help="Name of the video is required", required=True)
video_put_args.add_argument("views", type=str, help="Views of the videois requried", required=True)
video_put_args.add_argument("likes", type=str, help="Likes of the video is required", required=True)
videos = {}

class Video(Resource):
    def get(self, video_id):
        return videos[video_id]

    def put(self, video_id):
        args = video_put_args.parse_args()
        return {video_id: args}

api.add_resource(Video, "/video/<int:video_id>")


if __name__ == '__main__':
    app.run(debug=True)