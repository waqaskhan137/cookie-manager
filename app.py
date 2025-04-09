from flask import Flask, request, jsonify, send_from_directory

app = Flask(__name__)

cookie_recipes = []
guestbook = []

@app.route('/')
def index():
    return send_from_directory('static', 'index.html')

@app.route('/guestbook')
def guestbook_page():
    return send_from_directory('static', 'guestbook.html')

@app.route('/cookie/add', methods=['POST'])
def add_cookie():
    data = request.get_json()
    cookie_recipes.append(data['recipe'])
    return '', 200

@app.route('/cookie/list')
def list_cookies():
    return jsonify(cookie_recipes)

@app.route('/guestbook/add', methods=['POST'])
def add_guest():
    data = request.get_json()
    guestbook.append(data['name'])
    return '', 200

@app.route('/guestbook/list')
def list_guests():
    return jsonify(guestbook)

if __name__ == '__main__':
    app.run(debug=True)