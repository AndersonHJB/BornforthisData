from flask import Flask, request, jsonify
from PIL import Image
import io

app = Flask(__name__)


@app.route('/')
def index():
    return """
    Welcome to the Image Conversion API!
    POST to /convert with 'image' (file) and 'output_type' (e.g., 'jpeg', 'png') to convert images.
    POST to /analyze with 'text' to analyze sentiment of the text using TextBlob.
    """


@app.route('/convert', methods=['POST'])
def convert_image():
    if 'image' not in request.files:
        return jsonify({"error": "No image part"}), 400
    file = request.files['image']
    output_type = request.form.get('output_type', 'png')
    if not file or file.filename == '':
        return jsonify({"error": "No selected file"}), 400
    try:
        image = Image.open(file.stream)
        img_byte_arr = io.BytesIO()
        image.save(img_byte_arr, format=output_type.upper())
        img_byte_arr = img_byte_arr.getvalue()
        return jsonify({"status": "success", "image_bytes": len(img_byte_arr)}), 200
    except Exception as e:
        return jsonify({"error": str(e)}), 500


@app.route('/analyze', methods=['POST'])
def analyze_text():
    from textblob import TextBlob
    text = request.form.get('text', '')
    if not text:
        return jsonify({"error": "No text provided"}), 400
    sentiment = TextBlob(text).sentiment
    return jsonify({"polarity": sentiment.polarity, "subjectivity": sentiment.subjectivity}), 200


if __name__ == '__main__':
    app.run(debug=True)
