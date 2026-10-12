from flask import Flask, render_template, request, redirect, url_for
from flask_sqlalchemy import SQLAlchemy
from geopy.geocoders import Nominatim
from flask_uploads import UploadSet, configure_uploads, IMAGES


app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///photos.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
app.config['UPLOADED_PHOTOS_DEST'] = 'uploads'

db = SQLAlchemy(app)
photos = UploadSet('photos', IMAGES)
configure_uploads(app, photos)


class Photo(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    filename = db.Column(db.String(255))
    location = db.Column(db.String(255))


@app.route('/')
def index():
    photos = Photo.query.all()
    return render_template('index.html', photos=photos)


@app.route('/upload', methods=['POST'])
def upload():
    if 'photo' in request.files:
        file = request.files['photo']
        if file:
            filename = photos.save(file)
            location = get_geolocation(filename)
            new_photo = Photo(filename=filename, location=location)
            db.session.add(new_photo)
            db.session.commit()
    return redirect(url_for('index'))


def get_geolocation(filename):
    locator = Nominatim(user_agent="fight-for-life-demo")
    location = locator.geocode("uploads/" + filename)
    if location:
        return f"{location.latitude}, {location.longitude}"
    return "Location not available"


if __name__ == '__main__':
    db.create_all()
    app.run(debug=True)
