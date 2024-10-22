from flask import Flask, render_template, request, jsonify, send_from_directory
import subprocess
import os

app = Flask(__name__)
CODES_DIR = 'codes'

@app.route('/')
def index():
    return render_template('main.html')

@app.route('/run_code', methods=['POST'])
def run_code():
    data = request.json
    code = data.get('code')
    input_values = data.get('input')

    with open('temp.c', 'w') as f:
        f.write(code)

    try:
        subprocess.run(['gcc', 'temp.c', '-o', 'temp.exe'], check=True)
        result = subprocess.run(['./temp.exe'], input=input_values, text=True, capture_output=True, check=True)
        output = result.stdout
    except subprocess.CalledProcessError as e:
        output = e.stderr or str(e)

    return jsonify({'output': output})

@app.route('/open_file', methods=['GET'])
def open_file():
    filename = request.args.get('filename')
    if not filename.endswith('.c'):
        return 'Invalid file type', 400
    
    file_path = os.path.join(CODES_DIR, filename)
    if os.path.exists(file_path):
        with open(file_path, 'r') as f:
            content = f.read()
        return content
    return 'File not found', 404

@app.route('/save_file', methods=['POST'])
def save_file():
    data = request.json
    filename = data.get('filename')
    code = data.get('code')
    
    if not filename.endswith('.c'):
        return jsonify({'message': 'Invalid file type, must be a .c file'}), 400
    
    file_path = os.path.join(CODES_DIR, filename)

    try:
        with open(file_path, 'w') as f:
            f.write(code)
        return jsonify({'message': 'File saved successfully'})
    except Exception as e:
        return jsonify({'message': str(e)}), 500

if __name__ == '__main__':
    app.run(debug=True, host='127.0.0.1', port=5000)
