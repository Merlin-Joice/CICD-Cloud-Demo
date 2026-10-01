from flask import Flask

app = Flask(__name__)

@app.route("/")
def home():
    return """
    <h1>CI/CD Pipeline Successful!</h1>
    <p>Application deployed using GitHub and Cloud Platform.</p>
    <p>Build → Test → Deploy</p>
    """

if __name__ == "__main__":
    app.run(debug=True, port=5000)