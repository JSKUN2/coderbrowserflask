from flask import Flask, render_template
import os

app = Flask(__name__, template_folder='templates', static_folder='static')

IMG_FOLDER = os.path.join('static', 'IMG')

app.config['UPLOAD_FOLDER'] = IMG_FOLDER


@app.route("/")
def index():
    logo = os.path.join(app.config['UPLOAD_FOLDER'], 'logo.png')
    bg = os.path.join(app.config['UPLOAD_FOLDER'], 'bg1.png')
    img1 = os.path.join(app.config['UPLOAD_FOLDER'], 'search.png')
    img2 = os.path.join(app.config['UPLOAD_FOLDER'], 'opensource.png')
    img3 = os.path.join(app.config['UPLOAD_FOLDER'], 'discord.png')
    img4 = os.path.join(app.config['UPLOAD_FOLDER'], 'bootstrap.png')
    img5 = os.path.join(app.config['UPLOAD_FOLDER'], 'github.png')
    img6 = os.path.join(app.config['UPLOAD_FOLDER'], 'stack.png')
    img7 = os.path.join(app.config['UPLOAD_FOLDER'], 'youtube.png')

    return render_template("index.html", logo=logo ,img1=img1,img2=img2,img3=img3,img4=img4,img5=img5,img6=img6,img7=img7,bg=bg)


if __name__=='__main__':
    app.run(debug=True)