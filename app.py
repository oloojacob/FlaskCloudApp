from flask import Flask, render_template

app = Flask(__name__)

@app.route('/')
def home():
    return '''
    <h1>Hello, World!</h1>
    <p><a href="/second">Click here to view the second file</a></p>
    '''

@app.route('/second')
def second():
    return '''
    <h1>Welcome to the Second Page</h1>
    <p>This is the second file linked to the first page.</p>
    <p><a href="/">Go back to Home</a></p>
    '''

if __name__ == '__main__':
    app.run(debug=True)