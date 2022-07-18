from flask import Flask, render_template, url_for,request,redirect
import csv
#Flask class
app = Flask(__name__)
print(__name__)
#we are using a decorator. It will give extra tools to build the server.
#render_template looks automatically for a folder called templates. so the html files shuld be in this folder
#print(url_for('static',filename='alien.ico'))
#Lets try to use a variable to be given:

@app.route("/")
def my_home():
    return render_template('index.html')

@app.route('/<string:page_name>')
def html_page(page_name):
    return render_template(page_name)

#@app.route('/submit_form',methods=['POST','GET'])
#def login():
#    return 'form submitted ip iai ei'
#    return render_template('login.html',error=error)  
# 
def write_to_file(data):
    with open('database.txt',mode='a') as database:
        email = data["email"]
        subject =data["subject"]
        message=data["message"]
        file = database.write(f'\n{email},{subject},{message}')    

def write_to_csv(data):
    with open('database.csv',newline='',mode='a') as database2:
        email = data["email"]
        subject =data["subject"]
        message=data["message"]
        csv_writer = csv.writer(database2,delimiter=',',quotechar='"',quoting=csv.QUOTE_MINIMAL)
        csv_writer.writerow([email,subject,message])

@app.route('/submit_form',methods=['POST','GET'])
def submit_form():
    if request.method == 'POST':
        try:
            data = request.form.to_dict()
            write_to_csv(data)
            print(data)
            return redirect('/thankyou.html')
        except:
            return 'did not save to database'
                
    else: return 'something went wrong. try again'     
