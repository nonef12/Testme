from flask import Flask
server = Flask(__name__)

@server.route("/")
def hello():
    a = 0
    while 1:
        return f"Hello {a}"
    

if __name__ == "__main__":
   server.run(host='0.0.0.0', port=1337)
