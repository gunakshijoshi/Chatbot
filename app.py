from flask import Flask, render_template, jsonify, request
import processor


app = Flask(__name__)

app.config['SECRET_KEY'] = 'enter-a-very-secretive-key-3479373'


@app.route('/', methods=["GET", "POST"])
def index():
    return render_template('index.html', **locals())



@app.route('/bot', methods=["GET", "POST"])
def botResponse():

    if request.method == 'POST':
        the_question = request.form['question']

        response = processor.bot_response(the_question)

    return jsonify({"response": response })



if __name__ == '__main__':
    app.run(port="8000",debug=True)
