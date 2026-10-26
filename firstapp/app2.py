
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



if __name__ == '__main__':
    app.run(host='0.0.0.0',debug=True)