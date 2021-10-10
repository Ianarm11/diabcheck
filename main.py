from flask import Flask, render_template, url_for, request
from forms import DiabetesForm
import math
app = Flask(__name__)

#Needed for the Flask form, not sure why
app.config['SECRET_KEY'] = 'd9ef9646e24773bf0e9ee3fa4da5a38d'

#Global variables for calculations
best_chromosome = [4.3638, -0.5550, -4.6910, -2.5606, 4.1476, -3.1029, -1.5852, 1.7923, -0.4648, 1.5244, -2.2239,
                   1.2143, -2.3946, 3.1617, 0.9508, -0.1914]
chromosome_weights = best_chromosome[0:-2]
k = best_chromosome[-2]
x0 = best_chromosome[-1]

#Home page
@app.route("/home")
@app.route("/")
def home():
    return render_template('home.html')

#Survey page
@app.route("/survey")
def survey():
    form = DiabetesForm()
    return render_template('survey.html', form=form)

#Results Page
@app.route("/results", methods=["POST"])
def results():
    user_input = list(request.form.listvalues())
    clean_list = GetCleanList(user_input)
    age = clean_list[0]
    padded_list = GetPaddedList(clean_list)
    new_layer = LayerReductions(padded_list)
    new_layer.insert(0,age)
    final_layer = new_layer
    sum_of_products = FindSumOfProducts(final_layer)
    sum_of_weights = FindWeightSum()
    x = (sum_of_products/sum_of_weights)
    raw_prediction = LogisticFunction(x, k, x0)
    diabetes_predication = round(raw_prediction)
    return render_template('results.html', results=diabetes_predication)

def GetCleanList(x):
    clean_list = []
    temp_list = x[1:17]
    for x in temp_list:
        clean_list.append(int(x[0]))

    #Clean age
    raw_age = clean_list[0]
    new_age = (raw_age/100)
    clean_list[0] = new_age
    return clean_list

def GetPaddedList(x):
    #Take out the age
    no_age_list = x[1:16]
    #Add a 0 to the front and end
    no_age_list.insert(0,0)
    no_age_list.insert(len(no_age_list), 0)
    #Set padded list to no_age_list
    padded_list = no_age_list
    return padded_list

def LayerReductions(padded_list):
    v_out = []
    v_previous = []
    v_next = []
    layers = 4
    v_input = padded_list
    v_previous = v_input
    for layer in range(0, layers):
        v_next = []
        for i in range(0, (len(v_previous) - 1)):
            v_next.append((v_previous[i] + v_previous[i+1])/2)
        v_previous = v_next
    v_out = v_next
    return v_out

def LogisticFunction(x, k, x0):
    raw_prediction = 1/(1+math.exp(-k*(x-x0)))
    return raw_prediction

def FindSumOfProducts(final_layer):
    for i in range(0, len(final_layer)):
        summed_products = 0
        patient_val = final_layer[i]
        weight_val = chromosome_weights[i]
        product_of_values = patient_val * weight_val
        summed_products = summed_products + product_of_values
    return summed_products

def FindWeightSum():
    weight_sum = 0
    for i in range(0, len(chromosome_weights)):
        weight_value = chromosome_weights[i]
        weight_sum = weight_sum + weight_value
    return weight_sum



if __name__ == '__main__':
    app.run(debug=True)
