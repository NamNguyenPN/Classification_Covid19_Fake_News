import backend # Import the python file containing the ML model
from flask import Flask, request, render_template,jsonify # Import flask libraries

app = Flask(__name__,template_folder="templates",static_folder='assets')

@app.route("/")
def home():
    return render_template('index.html',label="LABEL")   

@app.route("/classify",methods=['POST','GET'])
def classify_type():
    try:
        sentence = request.args.get('txt') # Get parameters for sentence

        # Get the output from the classification model
        if(len(sentence)!=0):
            label = backend.classify(sentence).upper()
        
        #CSS for output
        if len(sentence) == 0:
            label_class = "input alert-warning"
            return render_template('index.html', label='',sentence='', label_class=label_class)
        if label == "FAKE":
            label_class = "fake"
        else:
            label_class = "real"

        # Render the output in new HTML page
        return render_template('index.html', label=label,sentence=sentence, label_class=label_class)
    except:
        return 'Error'

def retry():
    exam = request.args.get('txt') # Get parameters for sentence

    # Get the output from the classification model
    label = backend.classify(exam)
    
    return render_template('index.html', label='',sentence='', label_class='')

if __name__ == "__main__":
    app.run(debug=True)