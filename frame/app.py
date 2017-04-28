from flask import Flask
app = Flask("frame")


@app.route('/')
def hello_frame():
    return 'Hello, Frame!'

