from flask import Flask,render_template,url_for,request
from flask_bootstrap import Bootstrap
import pandas as pd
import numpy as np
from sklearn.feature_extraction.text import CountVectorizer
from sklearn.externals import joblib


app = Flask(__name__)
Bootstrap(app)
@app.route('/')
def index():
	return render_template('index.html')

@app.route('/predict',methods=['POST'])
def predict():
	'''
	df = pd.read_csv("data/names_dataset.csv")
	df_X = df.name
	df_Y=df.sex
	    # Vectorization
	corpus = df_X
	cv = CountVectorizer()
	X = cv.fit_transform(corpus) 
	# Loading Model
	naivebayes_model = open("models/naivebayesgendermodel.pkl","rb")
	clf = joblib.load(naivebayes_model)
	'''

	if request.method == 'POST':
		hardness = int(request.form['hardness'])
		question_type = request.form['question_type']
		time_limit = int(request.form['time_limit'])
		question_type_hardness = {"mcq": 1, "shuffle": 1, "output": 3, "fill": 5, "snippet": 5}
		max_question_type_hardness = int(request.form['max_question_type_hardness'])
		time_taken=int(request.form['time_taken'])
		answer_status=request.form['answer_status(c/w)']

	print("XXXXXXXXXXXXXXXXXX")

	print(answer_status)
	print("XXXXXXXXXXXXXXXXXX")

    
	if answer_status == 'Correct':
		if time_limit>0:
			cs= (10 * hardness + question_type_hardness[question_type])/(10 * max_question_type_hardness) + ((time_limit - time_taken)/time_limit)/10 + 0.3
			formula="(10 * hardness + question_type_hardness[question_type])/(10 * max_question_type_hardness) + ((time_limit - time_taken)/time_limit)/10 + 0.3"
		else:
			cs= (10 * hardness + question_type_hardness[question_type])/(10 * max_question_type_hardness) + 0
			formula="(10 * hardness + question_type_hardness[question_type])/(10 * max_question_type_hardness)"
	else:
		cs= -(10 * hardness + question_type_hardness[question_type])/(30 * max_question_type_hardness)
		formula="-(10 * hardness + question_type_hardness[question_type])/(30 * max_question_type_hardness)"
	
	print("XXXXXXXXXXXXXXXXXX")

	print(cs)
	print("XXXXXXXXXXXXXXXXXX")

	return render_template('output.html',change = cs,formula=formula)

if __name__ == '__main__':
	app.run(debug=True)