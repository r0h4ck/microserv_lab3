from flask import Flask, jsonify

app = Flask(__name__)

class MessagesService:
    @app.route('/', methods=['GET'])
    def get_messages():
        return jsonify('This is static message')


    @app.route('/', methods=['POST'])
    def post_messages():
        return jsonify("Message sent to logging service")

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=9002)
