from flask import Flask, render_template, request, jsonify, send_from_directory

app = Flask(__name__)
UPLOAD_FOLDER = 'static/upload/'
app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER

@app.route("/get-image/<image_name>")
def get_image(image_name):

    try:
        return jsonify("{}")
    except FileNotFoundError:
        abort(404)
		
if __name__ == '__main__':
   app.run(debug = True)