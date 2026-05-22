from flask import Flask

app = Flask(__name__)

def welcome():
    print("Welcome")
    return "Welcome"
  
def click():
    print("Click")
    return "Click"

@app.route("/")
def home():
    return "Hello from Python!"

if __name__ == "__main__":
    app.run(port=5000)

