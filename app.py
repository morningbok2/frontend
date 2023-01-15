from flask import Flask, render_template, jsonify
app = Flask(__name__)

from pymongo import MongoClient
client = MongoClient('mongodb+srv://test:sparta@cluster0.kprghtj.mongodb.net/Cluster0?retryWrites=true&w=majority')
db = client.dbsparta


@app.route("/test_list", methods=["GET"])
def test_get():
    test_list = list(db.test_list.find({},{'_id':False}))
    return jsonify({'test':test_list})

@app.route("/infoList", methods=["GET"])
def info_get():
    info_list = list(db.infoList.find({},{'_id':False}))
    return jsonify({'info':info_list})

@app.route('/')
def home():
   return render_template('index.html')

@app.route('/result')
def result():
    return render_template('result.html')

@app.route('/test')
def test():
    return render_template('test.html')

if __name__ == '__main__':
   app.run('0.0.0.0', port=5000, debug=True)