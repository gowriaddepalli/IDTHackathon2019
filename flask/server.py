from flask import Flask, jsonify, render_template, request, Response
import hw

app = Flask(__name__)

@app.route('/')
def static_page():
    return render_template('idt2.html')

@app.route('/IDT' )
def dynamic_page():
    return (render_template('idt.html'))


if __name__== "__main__":
    app.run(debug=True)

