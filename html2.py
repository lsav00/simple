
from flask import Flask
app = Flask(__name__)

def factors(num):
	return [x for x in range (1, num+1) if num%x==0]
  
@app.route('/')
def home():
	return '<a href="/factor_raw/100"> click here for an example</a>'
  
@app.route('/factor_raw/<int:n>')


def factors_display_raw_html(n):
	list_factor = factors(int(n))
	# adding "n" and placed at the top
	
	html = "<h1> Factors of "+str(n)+" are</h1>"+"\n"+"<ul>"
	# make a <li> item for every output (factor)
	
	for f in list_factor:
		html += "<li>"+str(f)+"</li>"+"\n"
	html += "</ul> </body>" # closes tag at the end
	return html
  
if __name__ == '__main__':
	app.run(host='0.0.0.0')