from flask import Flask, request, jsonify
from flask_cors import CORS
from youtube_transcript_api import YouTubeTranscriptApi

app = Flask(__name__)
CORS(app)

def get_transcript(video_id):  
    transcript = YouTubeTranscriptApi.get_transcript(video_id)
    concatenated = []

    for line in transcript:
        concatenated.append(line['text'])

    return ' '.join(concatenated)

# transcript = get_transcript('aKVvdgfbmWw')
# print(transcript)

@app.route('/', methods=['GET'])
def respond():
    # Retrieve the videoID from the url parameter /?video=
    video_id = request.args.get("video", None)

    # For debugging
    print(f"Received: {video_id}")

    response = {}

    # Check if the user sent a name at all
    if not video_id:
        response["ERROR"] = "No video found. Please send a video."
    else:
        response["MESSAGE"] = get_transcript(video_id)

    response = jsonify(response)
    response.headers.add('Access-Control-Allow-Origin', '*')

    # Return the response in json format
    return response

# @app.route('/getmsg/', methods=['GET'])
# def respond():
#     # Retrieve the name from the url parameter /getmsg/?name=
#     name = request.args.get("name", None)

#     # For debugging
#     print(f"Received: {name}")

#     response = {}

#     # Check if the user sent a name at all
#     if not name:
#         response["ERROR"] = "No name found. Please send a name."
#     # Check if the user entered a number
#     elif str(name).isdigit():
#         response["ERROR"] = "The name can't be numeric. Please send a string."
#     else:
#         response["MESSAGE"] = f"Welcome {name} to our awesome API!"

#     # Return the response in json format
#     return jsonify(response)


# @app.route('/post/', methods=['POST'])
# def post_something():
#     param = request.form.get('name')
#     print(param)
#     # You can add the test cases you made in the previous function, but in our case here you are just testing the POST functionality
#     if param:
#         return jsonify({
#             "Message": f"Welcome {name} to our awesome API!",
#             # Add this option to distinct the POST request
#             "METHOD": "POST"
#         })
#     else:
#         return jsonify({
#             "ERROR": "No name found. Please send a name."
#         })


# @app.route('/')
# def index():
#     # A welcome message to test our server
#     return "<h1>Welcome to our medium-greeting-api!</h1>"


if __name__ == '__main__':
    # Threaded option to enable multiple instances for multiple user access support
    app.run(threaded=True, port=5000)