from flask import Flask
import bugsnag
from bugsnag.flask import handle_exceptions

bugsnag.configure(
    api_key= "f799e66123ca4de64f87aaf00f7137c0" ,
    project_root="."
)

app = Flask(__name__)
handle_exceptions(app)

@app.route("/")
def index():
    return "Hello from Flask DevOps project!"

@app.route("/error")
def error():
    raise Exception("Crash test for Bugsnag")

if __name__ == '__main__':
    app.run(host="0.0.0.0", port=5000)

