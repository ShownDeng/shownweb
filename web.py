from flask import Flask, render_template, request

app = Flask(__name__)

@app.route('/')
def hello_world():
    return render_template('index.html')

@app.route('/test')
def index():
    return render_template('test_index.html')

@app.route('/post',methods=['POST'])
def post_register():
    user=request.form.get('user')
    password=request.form.get('pwd')
    gender=request.form.get('gender')
    place_list=request.form.getlist('place')
    print(user,password,gender,place_list)
    return '注册成功'

if __name__ == '__main__':
    app.run(debug=True)

