from flask import Flask, render_template, request

app = Flask(__name__)

# Caesar Cipher function
def caesar(text, shift, direction):
    result = ""
    if direction == "decode":
        shift = -shift
    for letter in text:
        if letter.isalpha():
            if letter.isupper():
                result += chr((ord(letter) - 65 + shift) % 26 + 65)
            else:
                result += chr((ord(letter) - 97 + shift) % 26 + 97)
        else:
            result += letter
    return result

# Serve index.html
@app.route('/')
def home():
    return render_template('index.html')

# Encode route
@app.route('/encode', methods=['POST'])
def encode():
    message = request.form['message']
    shift = int(request.form['shift'])
    return caesar(message, shift, "encode")

# Decode route
@app.route('/decode', methods=['POST'])
def decode():
    message = request.form['message']
    shift = int(request.form['shift'])
    return caesar(message, shift, "decode")

if __name__ == "__main__":
    app.run(debug=True)