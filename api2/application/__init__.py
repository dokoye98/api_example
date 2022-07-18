from flask import Flask, render_template
import requests

app = Flask(__name__)

@app.route('/', methods=['GET'])
def get_noise():
    animal = (requests.get('http://service1:5001/get/animal')).text
    if animal == 'Dog':
        noise = 'Bark'
    elif animal == 'Cat':
        noise = 'Meow'
    else:
        noise = 'Neigh'
    return render_template('home.html', animal=animal, noise=noise)

if __name__ == '__main__':
    app.run(port=5000, debug=True, host='0.0.0.0')