from flask import Flask, render_template, url_for, request
import sqlite3
import shutil
import os
from werkzeug.utils import secure_filename


connection = sqlite3.connect('user_data.db')
cursor = connection.cursor()

command = """CREATE TABLE IF NOT EXISTS user(name TEXT, password TEXT, mobile TEXT, email TEXT)"""
cursor.execute(command)

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/recognise', methods=['POST'])
def recognise():
    if 'img' not in request.files:  # Check if 'img' is in the request
        return "No file part in the request", 400

    file = request.files['img']
    if file.filename == '':  # Check if a file is selected
        return "No selected file", 400

    # Define upload folder
    upload_folder = os.path.join('static', 'test')
    os.makedirs(upload_folder, exist_ok=True)  # Create the directory if it doesn't exist

    # Save the uploaded file securely
    file_name = secure_filename(file.filename)
    file_path = os.path.join(upload_folder, file_name)
    file.save(file_path)

    print(f"File saved at: {os.path.abspath(file_path)}")  # Debugging log

    # Call the OCR function from EasyOCRTest
    try:
        from EasyOCRTest import recognition  # Import OCR function
        #cal recognition function for extracting text from image that function contain CNN model gives output text and accuracy

        text, accuracy = recognition(file_path)
    except Exception as e:
        print(f"Error in OCR function: {e}")
        return "An error occurred while processing the image!", 500

    # Read the recognized text from 'qw.txt'
    

    # Return the result to the `index.html` template
    return render_template(
        'index.html',
        text=text,
        accuracy=accuracy,
        ImageDisplay=f"/{file_path.replace(os.sep, '/')}"  # Ensure correct path format for HTML
    )

if __name__ == "__main__":
    app.run(debug=True, use_reloader=True)
