#Using More Routes
from flask import Flask
app = Flask(__name__)

@app.route("/")
def hello():
  return "Hello World!"

@app.route("/John")
def John():
	return "Hello John!"
	
@app.route("/Welcome/<name>") # at the endpoint /<name>
def Welcome_name(name): # call method Welcome_name
	return "Welcome " + name + "!" # which returns "Welcome + name + !

if __name__ == "__main__":
	app.run(debug=True)