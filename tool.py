import requests
import json
from flask import Flask,jsonify,request
#header1 = {'appid': '1110125831'}
#re = requests.get("https://lottery.zwlhome.com/matrixProgram/qqGuildBot/listExchangeGoods?pageNum=1&pageSize=20&guildId=6138592206477703023",headers=header1).text
#jr = json.loads(re)
#print(jr['data']['rows'][0]['name'])
app = Flask(__name__)
app.config['JSON_AS_ASCII'] = False
@app.route('/', methods=['GET'])
def home():
	mode = request.args.get("mode")
	qq = request.args.get("qq")
	skey = request.args.get("skey")
	pskey = request.args.get("pskey")
	token = request.args.get("token")
	question = request.args.get("question")
	bkn = request.args.get("bkn")
	group_id = request.args.get("groupid")
	slot = request.args.get("slot")
	answer = request.args.get("answer")
	keyword = request.args.get("keyword")
	if(mode == "callback"):
		return(Q_Group_Keeper.CallBack_Message(qq,skey,pskey,token,question,bkn))
	if(mode == "getq"):
		return(Q_Group_Keeper.Get_All_Question(qq,skey,pskey,group_id,bkn))
	if(mode == "setq"):
		return(Q_Group_Keeper.Set_Keeper_Question(qq,skey,pskey,bkn,group_id,slot,question,answer,keyword))
	if(mode == "delq"):
		return(Q_Group_Keeper.Delete_Keeper_Question(qq,skey,pskey,bkn,group_id,slot))
class Q_Group_Keeper:
	def CallBack_Message(QQ,Skey,P_skey,Token,Question,Bkn):#Q群管家回调触发消息
		hedr={
    	"qname-service":"976321:131072",
    	"Content-Type": "application/json",
    	"qname-space": "Production",
    	"Cookie":"uin=o0"+QQ+"; skey="+Skey+"; p_uin=o0"+QQ+"; p_skey="+P_skey+"; qq_locale_id=2052"}
		url = "https://app.qun.qq.com/cgi-bin/guanjia_robot/qna_callback/get_answer?bkn="+Bkn
		js = requests.post(url=url,headers=hedr,json={"token":Token,"question":Question,"anonymous":1}).text
		return(js)
	def Get_All_Question(QQ,Skey,P_skey,Group_id,Bkn):#获取Q群管家所有问题
		hedr={
    	"qname-service":"976321:131072",
    	"Content-Type": "application/json",
    	"qname-space": "Production",
    	"Cookie":"uin=o0"+QQ+"; skey="+Skey+"; p_uin=o0"+QQ+"; p_skey="+P_skey+"; qq_locale_id=2052"}
		url = "https://web.qun.qq.com/qunrobot/proxy/domain/app.qun.qq.com/cgi-bin/guanjia_robot/qna_setting/get_qna?bkn="+Bkn
		js = requests.post(url=url,headers=hedr,json={"bkn":int(Bkn),"group_id":int(Group_id)}).text
		return(js)
	def Set_Keeper_Question(QQ,Skey,P_skey,Bkn,Group_id,Slot,Question,Answer,Keyword):#设置管家的问题
		hedr={
    	"qname-service":"976321:131072",
    	"Content-Type": "application/json",
    	"qname-space": "Production",
    	"Cookie":"uin=o0"+QQ+"; skey="+Skey+"; p_uin=o0"+QQ+"; p_skey="+P_skey+"; qq_locale_id=2052"}
		url = "https://web.qun.qq.com/qunrobot/proxy/domain/app.qun.qq.com/cgi-bin/guanjia_robot/qna_setting/set_qna?bkn="+Bkn
		js = requests.post(url=url,headers=hedr,json={"bkn":int(Bkn),"group_id":int(Group_id),"qna_item":{"slot":int(Slot),"question":Question,"answer":Answer,"keyword":[Keyword]}}).text
		return(js)
	def Delete_Keeper_Question(QQ,Skey,P_skey,Bkn,Group_id,Slot):#删除管家问题
		hedr={
    	"qname-service":"976321:131072",
    	"Content-Type": "application/json",
    	"qname-space": "Production",
    	"Cookie":"uin=o0"+QQ+"; skey="+Skey+"; p_uin=o0"+QQ+"; p_skey="+P_skey+"; qq_locale_id=2052"}
		url = "https://web.qun.qq.com/qunrobot/proxy/domain/app.qun.qq.com/cgi-bin/guanjia_robot/qna_setting/set_qna?bkn="+Bkn
		js = requests.post(url=url,headers=hedr,json={"bkn":int(Bkn),"group_id":int(Group_id),"qna_item":{"slot":int(Slot),"question":"","answer":"","keyword":[""]}}).text
		return(js)
#print(Q_Group_Keeper.Get_All_Question("258909685","MHfZ4QkdO0","q6eevJpEOg0*zIOCEVmqjcTNEHWDXE77FolpQBqbHpw_","293243179","1632755149"))
#HjKWXDaXTQcCwqJy6iNnq40zFpNteqsxG4evTQBBq0c=
print(Q_Group_Keeper.CallBack_Message("258909685","MHfZ4QkdO0","q6eevJpEOg0*zIOCEVmqjcTNEHWDXE77FolpQBqbHpw_","HjKWXDaXTQcCwqJy6iNnq40zFpNteqsxG4evTQBBq0c=","8","1632755149"))
if __name__ == '__main__':
    app.run(host="0.0.0.0", port=2688)