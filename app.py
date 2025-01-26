from flask import Flask, render_template, send_from_directory
import os

app = Flask(__name__)

# Define the folder where your images are stored
IMAGE_FOLDER = 'static/images'

# Route to display the gallery
@app.route('/')
def index():
    # List of image file names (you can add more images here)
    image_names = ['image1.jpg', 'image2.jpg', 'image3.jpg']
    return render_template('index.html', image_names=image_names)

# Route to serve the full image when clicked
@app.route('/image/<image_name>')
def show_image(image_name):
    # Return the image file from the images folder
    return send_from_directory(IMAGE_FOLDER, image_name)

if __name__ == '__main__':
    # Run the Flask app
    app.run(debug=True)
