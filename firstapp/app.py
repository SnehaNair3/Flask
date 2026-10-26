
from flask import Flask,request,make_response

app=Flask(__name__)

# simple default route/ simple index route 
# we are gonna use the decoraror @
@app.route('/')
def index():
    return "<h1>Hello World!!</h1"


@app.route('/hello',methods=['GET','POST'])
def hello():
    if request.method == 'GET':
        return 'You made a GET request.\n'
    elif request.method == 'POST':
        return 'You made a POST request.\n'
    else:
        return 'You will never see this message.\n'


@app.route('/hello2')
def hello2():
    return "Hello 2\n",202


@app.route('/hello3')
def hello3():
    response=make_response('Hello World!\n')
    response.status_code=202
    response.headers['content-type']='text/plain'
    return response



@app.route('/greet/<name>')
def greet(name):
    return f"Hello {name}"


@app.route('/add/<num1>/<num2>')
def add(num1,num2):
    return f'{num1} + {num2} = {num1+num2}'

@app.route('/add2/<int:num1>/<int:num2>')
def add2(num1,num2):
    return f'{num1} + {num2} = {num1+num2}'


@app.route('/handle_url_params')
def handle_params():
    if 'greeting' in request.args.keys() and 'name' in request.args.keys():
        greeting=request.args['greeting']
        name=request.args.get('name')
        return f'{greeting} , {name}'
    else:
       return 'Some parameters are missing.' 

if __name__ == '__main__':
    app.run(host='0.0.0.0',port=5000,debug=True)

# after deploying the application , chnage debug = False

