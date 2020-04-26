from flask import Flask, render_template,url_for,request, redirect, session,send_file, jsonify
import modeltest
from werkzeug.utils import secure_filename
import modeltest
import json
import os
port = int(os.environ.get("PORT",5000))
jsonfilepath = "./static/sample.json"


app = Flask(__name__)
@app.route('/')
def root():
	return render_template("index.html")
@app.route('/results', methods = ['GET','POST'])
def results():
	predicted = ""
	actual = ""
	try:
		request_text = request.form['posturl']
		#request_text = requests.get(url)
		print(request_text)
		actual = str(modeltest.actual(request_text))
		predicted = str(modeltest.predict(request_text))
		print(predicted)
		print(actual)
	except:
		print("Couldn't get a url")
	
	return render_template('index.html', predicted = predicted,actual = actual)

"""@app.route('/upload', methods=['GET', 'POST'])
def upload():
    return render_template('upload.html')"""

@app.route('/automated_testing', methods = ['GET', 'POST'])
def automated_testing():
	#content = ""
	l= ""
	lis = []
	lis_predicted = []
	lis_actual = []
	l = {}
	size = 0
	name = ""
	if request.method == 'POST':
		f = request.files["upload_file"]
		#print(f)
		#print(f.read())
		lines = f.readlines()
		print(lines)
		for line in lines:
			line = line.strip()
			line = str(line)
			line = line[2:]
			line = line[:-1]
			print(line)
			lis.append(line)
			actual = str(modeltest.actual(line))
			predicted = str(modeltest.predict(line))
			print(actual,predicted)
			lis_actual.append(actual)
			lis_predicted.append(predicted)
			size = size+1
			l[line] = predicted
			"""dictionary ={line:predicted}
												l = l+ str(dictionary)"""
		print(size)
		json_object = json.dumps(l) 			  
		with open(jsonfilepath, "w") as outfile: 
		    outfile.write(json_object)
		outfile.close()
		with open('./static/sample.json') as f:
			data = json.load(f)
		print(data)
		return jsonify(l)
	else:
		return render_template("automated.html")

	"""else:
					return render_template('upload.html')"""
	#return render_template("book.html", lis=lis, lis_predicted = lis_predicted,lis_actual = lis_actual,size = size)

@app.route('/download')
def download_file():
	path = "./static/sample.json"
	return send_file(path, as_attachment=True)
@app.route('/main', methods=['GET', 'POST'])
def main():
	return render_template("index.html")






@app.errorhandler(404)
def page_not_found(error):
    return 'This page does not exist', 404




if __name__ == '__main__':
    app.run(debug=True)

