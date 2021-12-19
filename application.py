from flask import Flask

app = Flask(__name__)

@app.route("/")
def hello():
    return "<h1>Hello World!</h1>"

@app.route("/profile/<username>")
def get_profile(username):
    return "profile" + username

@app.route("/first/<username")
def hello_first():
    return "<h3>Hello" + username + "!</h3>"

@app.route("/message/<int:message_id>")
def get_message(message_id):
    return "message id: %d" % message_id   
    # %d 는 int, %f 는 float, %s 는 string

if __name__ == "__main__":
    app.run(host = "0.0.0.0", port = "8080", debug = True)