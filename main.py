from flask import Flask, render_template

app = Flask(__name__)


@app.route('/', methods=['GET'])
def index():
    return 'Hello There whats up? if you want to chat with random people put chat after the 500 using / '

@app.route('/chat')
def chatRoom():
    return render_template('chat.html')

if __name__ == "__main__":
    app.run(debug=True)


