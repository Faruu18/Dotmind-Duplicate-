from flask import Flask, render_template, request
app = Flask(__name__static_url_path='/static')
def index():

     return render_template ('index.html')

@app.route('/about_us')
def about_us():

 return render_template("about_us.html")

 if name == "main":
    app.run(debug=True)
   


