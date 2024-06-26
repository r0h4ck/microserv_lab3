from flask import Flask, jsonify, request
from random import choice
import requests
import uuid


app = Flask(__name__)

log_service_url = ['http://logging-service-1:9001/',
                   'http://logging-service-2:9001/',
                   'http://logging-service-3:9001/']
msg_service_url =  'http://messages-service:9002/'

class FacadeService:
    @app.route('/', methods=['POST'])
    def log():
        log_message = request.json['message']
        message = {str(uuid.uuid4().hex): log_message}
        log_response = None
        log_service = None

        with requests.Session() as sess:
            mes_response = sess.post(msg_service_url, json=message)
        while not log_response:
            log_service = choice(log_service_url) #select url 1 in 3
            try:
                with requests.Session() as sess:
                    log_response = sess.post(log_service, json=message)
            except Exception as e:
                print(f"Unable to connect to {log_service}, reason = {e.__class__.__name__} : {e}")
                continue
        #output to console 
        out={'msg-resp':mes_response.json(),
             'log-resp':log_response.json(),
             'logger':log_service,}

        return jsonify(out)

    @app.route('/', methods=['GET'])
    def get_messages():
        log_service = None
        log_response = None

        with requests.Session() as sess:
            mes_response = sess.get(msg_service_url)
        while not log_response:
            log_service = choice(log_service_url)
            try:
                with requests.Session() as sess:
                    log_response = sess.get(log_service)
            except Exception as e:
                print(f"Unable to connect to {log_service}, reason = {e.__class__.__name__} : {e}")
                continue
        #output to console 

        out={'msg-resp':mes_response.json(),
             'log-resp':log_response.json(),
             'logger':log_service,}

        return jsonify(out)

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=9000)
