from flask import Flask, send_from_directory, render_template
app = Flask(__name__)

@app.route("/")
def home():
    return render_template('index.html')
 
@app.route("/pics/<filename>")
def files(filename):
    return send_from_directory('detected_image', filename)


 
if __name__ == "__main__":
    app.run(host='0.0.0.0', port=8000)