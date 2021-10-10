from flask import Flask, render_template, url_for, request
from forms import DiabetesForm
app = Flask(__name__)

app.config['SECRET_KEY'] = 'd9ef9646e24773bf0e9ee3fa4da5a38d'

def ProcessUserInput(user_input):
    return len(user_input)

@app.route("/home")
@app.route("/")
def home():
    return render_template('home.html')

@app.route("/survey")
def survey():
    form = DiabetesForm()
    return render_template('survey.html', form=form)

@app.route("/results", methods=["POST"])
def results():
    user_input = list(request.form.listvalues())
    clean_results = CleanUserInput(user_input)
    results = PaddedList(clean_results)
    return render_template('results.html', results=results)

def CleanUserInput(results):
    final_results = []
    new_results = results[1:17]
    for x in new_results:
        final_results.append(int(x[0]))

    #Clean age
    raw_age = final_results[0]
    new_age = (raw_age/100)
    final_results[0] = new_age
    return final_results

def PaddedList(results):
    #Take out the age
    new_results = results[1:16]

    return new_results

def LayerReductions(input_vector):
    return

if __name__ == '__main__':
    app.run(debug=True)
