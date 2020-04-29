from flask import Flask, request, jsonify, send_file, render_template
#from werkzeug.utils import secure_filename
#import question_gen_run as qgen

app = Flask(__name__)
#app.config['UPLOAD_FOLDER'] = './uplad/'
"""
mail_settings = {
    "MAIL_SERVER": 'smtp.gmail.com',
    "MAIL_PORT": 465,
    "MAIL_USE_TLS": False,
    "MAIL_USE_SSL": True,
    "MAIL_USERNAME": os.environ['EMAIL_USER'],
    "MAIL_PASSWORD": os.environ['EMAIL_PASSWORD']
}

app.config.update(mail_settings)
mail = Mail(app)
"""

@app.route("/")
def index():
    return render_template('index.html')
"""
@app.route("/form",methods=["POST"])
def form():
	name = request.form['name']
	email = request.form['email']
	subject = request.form['subject']
	message = request.form['message']


@app.route("/generatequiz", methods =["POST"])
def gen():
    #start = time.time()

    file = request.files['file']
    file.save(secure_filename('input.txt'))

    infile = 'input.txt'
    #outfile = 'output.txt'
    file = open(infile, 'r', encoding='utf-8')
    text = file.read()
    n=int(request.form['num_of_ques'])
    # n=3
    questions = qgen.generateQuestions(text,n)
    #end = time.time()
    #final_time = end - start
    #print(final_time)
    return jsonify(questions)
"""

if __name__ == '__main__':
    app.run(debug=True)