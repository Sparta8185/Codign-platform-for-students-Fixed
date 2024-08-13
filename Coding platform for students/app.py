from flask import Flask, render_template, request, jsonify
import subprocess

app = Flask(__name__)

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
        subprocess.run(['gcc', 'temp.c', '-o', 'temp'], check=True)
        result = subprocess.run(['./temp'], input=input_values, text=True, capture_output=True, check=True)
        output = result.stdout
    except subprocess.CalledProcessError as e:
        output = e.stderr or str(e)

    return jsonify({'output': output})

if __name__ == '__main__':
    app.run(debug=True, host='127.0.0.1', port=5000)
