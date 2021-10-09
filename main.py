from flask import Flask, render_template
from forms import DiabetesForm
app = Flask(__name__)

app.config['SECRET_KEY'] = 'd9ef9646e24773bf0e9ee3fa4da5a38d'

@app.route("/home")
@app.route("/")
def home():
    return render_template('home.html')

@app.route("/survey", methods=['GET', 'POST'])
def survey():
    #Page for filling out form
    form = DiabetesForm()
    return render_template('survey.html', form=form)

@app.route("/results", methods=['GET', 'POST'])
def results():
    #Process Survey results here.. Call a function for algorithm
    ##Pass the algorithm results into the html file
    ###How do we get the user's input?
    return render_template('results.html')

if __name__ == '__main__':
    app.run(debug=True)
