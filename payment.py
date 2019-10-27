from flask import render_template, Flask, request, jsonify
import tempfile
# from payment import create_app
# app = create_app()
app = Flask(__name__)


@app.route('/')
def hello_world():
    return 'Hello World!'


@app.route('/order_info')
def index():
    return render_template('order_info.html')


@app.route('/prepare_pay', methods=['POST'])
def prepare_pay():
    if request.method == "POST":
        amount = request.form.get("amount")
        account = request.form.get("account")
        """
        1.创建保存二维码的临时文件
        2.获取临时文件名作为二维码的文件名
        3.构造支付信息
        4.将支付信息拼接成支付url
        5.以支付url生成二维码
        6.构造二维码url
        7.返回支付金额及二维码url
        """
        return jsonify(account, amount)

    return "error request method"


@app.route('/pay', methods=['POST'])
def pay():
    pass

if __name__ == '__main__':
    print(app.url_map)
    print(app.static_folder)
    print(app.static_url_path)
    app.run(debug=True)

