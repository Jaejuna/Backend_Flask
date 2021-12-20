from flask import Flask, jsonify

app = Flask(__name__)

def add_file(data):
    return data + 5

@app.route("/")
def hello():
    return "<h1>Hello World!</h1>"

@app.route("/profile/<username>")
def get_profile(username):
    return "profile" + username

@app.route("/first/<int:messageid>")
def get_first(messageid):
    data = add_file(messageid)
    return "<h1>%d</h1>" % (data)

@app.route("/message/<int:message_id>")
def get_message(message_id):
    return "message id: %d" % message_id   
    # %d 는 int, %f 는 float, %s 는 string

@app.route('/json_test')
def hello_json():
    data = {'name' : '김대리', 'family' : 'Byun'}
    return jsonify(data)

@app.route('/server_info')
def server_json():
    data = { 'server_name' : '0.0.0.0', 'server_port' : '8080' }
    return jsonify(data)
    #flask jsonify(): 리턴 데이터를 JSON 포맷으로 제공
    
if __name__ == "__main__":
    app.run(host = "0.0.0.0", port = "8080", debug = True)
    
    
#HTTpie installed!