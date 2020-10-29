from flask import Flask, render_template, redirect, request
import RecSys
import emoji

# __name__ = __main__
app = Flask(__name__)

@app.route('/')
def hello():
	return render_template('index.html')

@app.route('/',methods=['POST'])
def get_recommendations():
	if request.method=='POST':
		name=request.form['username']
		selected_tags=request.form.getlist('tags')
		print(selected_tags)
		print(type(selected_tags))
		#selected_tags=request.form['category'].split(',')
		movies=RecSys.recommendations(selected_tags)
		print(type(movies))
	return render_template('index.html',your_result=True,your_name=name,data=movies.to_dict(orient='records'))


if __name__ == '__main__':
	#Reflects changes when we refresh the page
	#app.debug = True
	app.run(debug=True)
