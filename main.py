from flask import Flask, request, render_template
import os


app = Flask(__name__)

@app.route('/')
def index():
    return "this is the home " + request.method
    
@app.route('/tuna')
def tuna():
    return "<h3> TUNA </h3>"
    
@app.route('/test/<int:variable>')
def test(variable):
    return "this is the home " + str(variable)
    
@app.route('/temp/<variable>')
def temp(variable):
    return render_template("temp.html", var = variable)
    
if __name__ == "__main__":
    app.run(debug=True,host = os.getenv('HOST', '0.0.0.0'), port = int(os.getenv('PORT',8080)))