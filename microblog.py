from flask import Flask

app = Flask("microblog")

@app.route("/")
def index():
    return "Hello world"

app.run()