from flask import Flask, render_template

app = Flask(__name__)


@app.route('/')
def hello_world():  # put application's code here
    return 'Hello World!'


@app.route('/deaf_guide')
def deaf_guide():
    guides = [
        {
            'title': '您好',
            'num': 2,
        },
        {
            'title': '请坐',
            'num': 2,
        },
        {
            'title': '请问您办理什么业务',
            'num': 6,
        },
        {
            'title': '好的，请稍等',
            'num': 3,
        },
        {
            'title': '存款',
            'num': 1,
        },
        {
            'title': '取款',
            'num': 1,
        },{
            'title': '定期存款',
            'num': 2,
        },
        {
            'title': '办理银行卡',
            'num': 1,
        },
        {
            'title': '激活信用卡',
            'num': 2,
        },
        {
            'title': '打印交易明细',
            'num': 3,
        },
        {
            'title': '修改重置密码',
            'num': 2,
        }, {
            'title': '修改客户信息',
            'num': 3,
        },
        {
            'title': '请问您还有其他业务吗？',
            'num': 6,
        },
        {
            'title': '请带好随身物品，再见，请慢走！',
            'num': 4,
        },

    ]
    return render_template('deaf_guide.html', guides=guides)


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5100)
