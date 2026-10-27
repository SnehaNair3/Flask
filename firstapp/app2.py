
from flask import Flask, render_template

app=Flask(__name__,template_folder='templates')


@app.route('/')
def index():
    return render_template('index.html')


@app.route('/idx2')
def index2():
    myvalue='NeuralNine'
    myresult=10 + 20
    return render_template(template_name_or_list='index2.html', myvalue=myvalue, myresult=myresult)


@app.route('/idx3')
def index3():
    mylist=[10,20,30,40,50]
    return render_template(template_name_or_list='index3.html',mylist=mylist)



@app.route('/base_idx')
def baseindex():
    mylist=[10,20,30,40,50]
    return render_template(template_name_or_list='index_base.html',mylist=mylist)


@app.route('/other')
def other():
    some_text='Hello World'
    return render_template('filter.html',some_text=some_text)


@app.template_filter('reverse_string')
def reverse_string(s):
    return s[::-1]


@app.template_filter('repeat')
def repeat(s,times=2):
    return s * times
    

@app.template_filter('alternate_case')
def alternate_case(s):
    return ''.join([c.upper() if i%2==0 else c.lower() for i,c in enumerate(s)])

if __name__ == '__main__':
    app.run(host='0.0.0.0',debug=True)