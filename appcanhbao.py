# import requests

# def url_ok(url):
#     r = requests.head(url)
#     return r.status_code == 200

# a = url_ok("http://naptien.thanhtoan247.vn:8082/CDV_Partner_Services_V1.0/services/Interfaces?wsdl")

# print(a)



#import eventlet
# import eventlet
import time
import requests
# import eventlet
# import eventlet
import time
import cx_Oracle
import requests
# import pyodbc
import threading

danh_sach= [
			"http://naptien.thanhtoan247.vn:8082/CDV_Partner_Services_V1.0/services/Interfaces?wsdl",
			"https://thanhtoan247.net.vn",
			"http://thanhtoan365.vn",
			"https://megacard.vn"
			]
timeout = 60

So_nhan_canh_bao= ["0888354345",
				   "0964058355",
]

# Cấu hình DB
ip = '127.0.0.1'
port = 1521
SID = 'XE'
useridOra ='PYTHON_DEV'
passwdOra = '123@123a'
connstrOra = '127.0.0.1'
dsn_tns = cx_Oracle.makedsn(ip, port, SID)
connect_stringDB = cx_Oracle.connect(useridOra, passwdOra, dsn_tns)
curs = connect_stringDB.cursor()

def check_web(web):
	try:
		r = requests.get(web, timeout = timeout)
		ma_loi = r.status_code
		return ma_loi
	except requests.ConnectionError:
		ma_loi = "Disconnected"
		return ma_loi

def insert_db(nguoi_nhan,noi_dung):
	try:
		sql_cmd = "INSERT INTO TBL_SMS_TRANSACTION (TRANS_ID, REQUEST_ID, REQUEST_TIME, STATUS, SMS_CONTENT, SMS_RECEIVER) VALUES (SEQ_SMS_TRANSACTION.NEXTVAL, SEQ_SMS_TRANSACTION.NEXTVAL, SYSDATE, 1, '"+noi_dung+"', '"+nguoi_nhan+"')"
		ket_qua = curs.execute(sql_cmd)
		connect_stringDB.commit()
		connect_stringDB.close()
		return "Insert OK"
	except:
		return "fail"

#Check tình trạng link vô hạn

for wep in range(len(danh_sach)):
	threading.Thread(target=check_web,args=danh_sach[wep]).start

#insert_db("0888354345","thu thoi nhaz")

# def main():
# 	while True:
# 		for i in range(0, len(danh_sach)):
# 			code = check_web(danh_sach[i])
# 			if code	!= 200:
# 				noi_dung_sms = "Webservice is die:\r\n"+danh_sach[i]+"\r\nMa Loi:"+str(code)
# 				for m in range(0, len(So_nhan_canh_bao)):
# 					insert_db(So_nhan_canh_bao[m],noi_dung_sms)
# 					print(noi_dung_sms)
# 					time.sleep(1)
# #			print(code)
# 			time.sleep(1)

if __name__ == "__main__":
	main()
#print(check_web("https://thanhtoan247.net.vn"))
#print(len(danh_sach))

# for i in range(0,len(danh_sach)):
# 	code = check_web(danh_sach[i])
# 	print("Ma loi tra ve",danh_sach[i],code)
# 	time.sleep(1)
#test = check_web(link)
#print(test)


#sql_cmd = "INSERT INTO SOFTPIN_SOLD (PROVIDER,SERIAL,NGAY_BAN) values ('VTT', '016838645qA', sysdate)"
## tnsOra = useridOra + "/" + passwdOra + "@" + connstrOra
## conOra = cx_Oracle.connect(tnsOra)
#curs = db.cursor()
#ket_qua = curs.execute(sql_cmd)
## ket_qua = curs.parse(sql_cmd)
#db.commit()
#db.close()
##rows = curs.fetchone()
#print(ket_qua)