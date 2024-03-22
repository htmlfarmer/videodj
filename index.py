from flask import Flask, render_template

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/example_script')
def example_script():
    import json
    result_data = {"message": "This is the result of the Python script.", "value": 43+2}
    return json.dumps(result_data)

if __name__ == '__main__':
    app.run(debug=True)