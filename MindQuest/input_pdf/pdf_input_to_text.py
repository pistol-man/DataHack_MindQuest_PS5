from flask import Flask, render_template, request, send_file
import PyPDF2
import io

app = Flask(__name__)


@app.route('/')
def home():
    return render_template('index.html')


@app.route('/upload', methods=['POST', 'GET'])
def upload():
    if request.method == 'POST':
        # Handle the uploaded resume here
        uploaded_file = request.files['resume']
        if uploaded_file:
            # Read the PDF content
            pdf_content = uploaded_file.read()

            # Create a PDF file object using PdfReader
            pdf_reader = PyPDF2.PdfReader(io.BytesIO(pdf_content))

            # Extract text from the PDF (assuming it's a text-based PDF)
            pdf_text = ""
            for page in pdf_reader.pages:
                pdf_text += page.extract_text()

            return pdf_text

    return render_template('upload.html')


if __name__ == '__main__':
    app.run(debug=True)
