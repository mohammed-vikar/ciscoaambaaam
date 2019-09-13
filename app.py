import os
from flask import Flask, request, render_template, url_for, redirect
import pandas as pd
from pandas import ExcelWriter
from pandas import ExcelFile
import json


#ALLOWED_EXTENSIONS = set(['txt', 'pdf', 'png', 'jpg', 'jpeg', 'gif'])
ALLOWED_EXTENSIONS = set(['csv', 'xlsx'])

app = Flask(__name__)


@app.route("/")
def indexPage():
    return render_template('index.html')

@app.route("/loadCab")
def loadCab():
    return render_template('cab.html')

@app.route("/handleUpload", methods=['POST'])
def handleFileUpload():
    if 'baaamFile' in request.files:
    	print("Posted file: {}".format(request.files['baaamFile']))
    	_baaamFile = request.files['baaamFile']
    	#print "_baaamFile.read() ", _baaamFile.read()
        #print "os.path ", os.path
        #print "app.instance_path ", app.instance_path
        if _baaamFile.filename != '':
        	print "Did i get the uploaded file? ", _baaamFile.filename
        	_fileExtension = _baaamFile.filename.rsplit('.', 1)[1].lower()
        	print " file extension is ", _fileExtension
        	if allowed_file(_baaamFile.filename) and _fileExtension == 'csv':
        		print("Process CSV file")
        		#processCsvFile(_baaamFile)
        	elif allowed_file(_baaamFile.filename) and _fileExtension == 'xlsx':
        		print("Process Excel file")
        		#processExcelFile(_baaamFile)
        	else:
				print("The file type is not supported")
				return json.dumps({'Alert':'<span>The file type is not supported. Please upload either .csv or .xlsx !! <a href=/loadCab> Go Back</a></span>'})
				
    return redirect(url_for('loadCab'))

def allowed_file(_filename):
	#print("--------------------")
	#print("Verify the Extension")
	#print(_filename.rsplit('.', 1)[1].lower())
	#print("--------------------")
	return '.' in _filename and _filename.rsplit('.', 1)[1].lower() in ALLOWED_EXTENSIONS

def processExcelFile(_baaamFile):
	print("--------------------")
	print("---------")
	df = pd.read_excel(_baaamFile)
	print(df.columns)
	for i in df.index:
		print("Folder Id ", df['FolderId'][i])
		print("Name ", df['Name'][i])
		print("Description ", df['Description'][i])
		print("Expression ", df['Expression'][i])
	print("---------")
	print("--------------------")

def processCsvFile(_baaamFile):
	print("--------------------")
	print("---------")
	for x in _baaamFile:
		print "x ", x
		self._folderId = x.split(',')[0]
		self._traitName = x.split(',')[1]
		self._traitDescription = x.split(',')[2]
		self._traitExpresssion =  x.strip().split(',')[3]
		print self._folderId , self._traitDescription , self._traitName , self._traitExpresssion
	print("---------")
	print("--------------------")


if __name__ == '__main__':
    app.run() 