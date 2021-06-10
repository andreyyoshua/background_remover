from flask import Flask, render_template, request, jsonify, send_from_directory
from flask.helpers import send_file
from werkzeug.utils import secure_filename
from werkzeug.datastructures import  FileStorage
import pixellib
from pixellib.tune_bg import alter_bg


app = Flask(__name__)
UPLOAD_FOLDER = 'static/upload/'
app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER
	
change_bg = alter_bg()
change_bg.load_pascalvoc_model("deeplabv3_xception_tf_dim_ordering_tf_kernels.h5")

@app.route('/uploader', methods = ['GET', 'POST'])
def upload_file():
    if request.method == 'POST':
        files = request.files.getlist("file")
        new_files = []
        for file in files:
            secure_name = secure_filename(file.filename)
            new_filename = UPLOAD_FOLDER + secure_name
            file.save(new_filename)
            change_bg.color_bg(new_filename, colors = (255, 255, 255), output_image_name=new_filename)
            new_files.append(secure_name)
        return jsonify(new_files)

@app.route("/get-image/<image_name>")
def get_image(image_name):

    try:
        return send_file(UPLOAD_FOLDER + image_name)
    except FileNotFoundError:
        abort(404)
		
if __name__ == '__main__':
   app.run(debug = True)