from flask import Flask, render_template, redirect, request
import RecSys

# __name__ = __main__
app = Flask(__name__)

@app.route('/')
def hello():
	return render_template('index.html')

@app.route('/',methods=['POST'])
def get_recommendations():
	if request.method=='POST':
		selected_tags=list([request.form['category']])
		movies=RecSys.recommendations(selected_tags)
		
	return render_template('index.html',your_result=True,data=movies.to_dict(orient='records'))


if __name__ == '__main__':
	#Reflects changes when we refresh the page
	#app.debug = True
	app.run(debug=True)
