from flask import Flask
import requests
server = Flask(__name__)

@server.route("/")
def hello():
    a=requests.get("https://www.google.com").text
    return a
if __name__ == "__main__":
   server.run(host='0.0.0.0', port=1337)
