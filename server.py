from flask import Flask
server = Flask(__name__)

@server.route("/")
def hello():
    i=0
    while 1:
       return i+=1

if __name__ == "__main__":
   server.run(host='0.0.0.0', port=1337)
