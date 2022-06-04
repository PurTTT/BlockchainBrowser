
import requests
import json
from flask import Flask,request,make_response
from flask_cors import *
app = Flask(__name__)
cors = CORS(app,supports_credentials=True)
app.config['CORS_HEADERS'] = 'Content-Type'

@app.route('/',methods=['GET','POST'])
@cross_origin(origin='*')
def index():
    print("********************************************************被调用了*************************")
    url="https://api.testnet.eos.io/v1/chain/get_info"
    resp =requests.post(url)
    res = json.loads(resp.text)
    inta=res['head_block_num']# 最新块号
    if request.method == 'POST':
        postdata = json.loads(request.get_data(as_text=True))
        inta = postdata['num'] 
        print(inta)
    url="https://api.testnet.eos.io/v1/chain/get_block"
    headers={"Content-Type": "application/json"}
    flag = True
    while flag:
        payload= {"block_num_or_id": str(inta)}
        resp =requests.post(url,headers=headers,data=json.dumps(payload))
        res = json.loads(resp.text)
        if "transactions" in res and res["transactions"] != []:
            flag = False
            print(res)
        else:
            inta -= 1
            print(inta)
    resp = make_response(res)  # 响应体数据
    return resp


@app.route('/info',methods=['GET','POST'])
@cross_origin(origin='*')
def info():
    url="https://api.testnet.eos.io/v1/chain/get_info"
    resp =requests.post(url)
    res = json.loads(resp.text)
    print(res)
    resp = make_response({'num':res['head_block_num']})  # 返回最新块号
    return resp


@app.route('/bitInfo',methods=['GET','POST'])
@cross_origin(origin='*')
def bitInfo():
    url="https://blockchain.info/latestblock"
    resp = requests.get(url, verify=False)
    res = json.loads(resp.text)
#    print(res)
    resp = make_response({'num':res['height']})  # 返回最新块号
    return resp


@app.route('/block',methods=['GET','POST'])
@cross_origin(origin='*')
def block():
    inta = 127168196
    if request.method == 'POST':
        postdata = json.loads(request.get_data(as_text=True))
        inta = postdata['num'] 
        print(inta)
    url="https://api.testnet.eos.io/v1/chain/get_block"
    headers={"Content-Type": "application/json"}
    payload= {"block_num_or_id": str(inta)}
    resp =requests.post(url,headers=headers,data=json.dumps(payload))
    res = json.loads(resp.text)
    #print("HAPPEN")
    #print(res)
    resp = make_response(res)  # 返回指定块 2区块消息block3基本信息info

    return resp
    
@app.route('/bitBlock',methods=['GET','POST'])
@cross_origin(origin='*')
def bitBlock():
    inta = 127168196
    if request.method == 'POST':
        postdata = json.loads(request.get_data(as_text=True))
        inta = postdata['num']
        print(inta)
    url="https://blockchain.info/block-height/" + str(inta) + "?format=json"
#    headers={"Content-Type": "application/json"}
#    payload= {"block_num_or_id": str(inta)}
#    resp =requests.post(url,headers=headers,data=json.dumps(payload))
    resp = requests.get(url)
    res = json.loads(resp.text)
    #print("HAPPEN")
#    print("**************************", res)
    resp = make_response(res)  # 返回指定块 2区块消息block3基本信息info

    return resp
    

@app.route('/tx',methods=['GET','POST'])
@cross_origin(origin='*')
def tx():
    url="https://api.testnet.eos.io/v1/chain/get_info"
    resp =requests.post(url)
    res = json.loads(resp.text)
    inta=res['head_block_num']# 最新块号
    url="https://api.testnet.eos.io/v1/chain/get_block"
    headers={"Content-Type": "application/json"}
    flag = 0
    count = 0
    txs = []
    #删除inta = 127295878
    while flag<2:
        payload= {"block_num_or_id": str(inta)}
        resp =requests.post(url,headers=headers,data=json.dumps(payload))
        res = json.loads(resp.text)
        if "transactions" in res and res["transactions"] != []:
            print(res)
            txs.append(res)
            flag += 1
        else:
            print(flag,inta,count)
        inta -= 1
        count += 1

    resp = make_response({'re':txs})  # 响应体数据
    print({'re':txs})
    return resp
    
    
@app.route('/bitTx',methods=['GET','POST'])
@cross_origin(origin='*')
def bitTx():
    url="https://blockchain.info/unconfirmed-transactions?format=json"
    resp = requests.get(url)
    res = json.loads(resp.text)
    resp = make_response(res)  # 响应体数据
#    print({'re':txs})
    return resp


if __name__ == '__main__':
    app.run(debug=True)
