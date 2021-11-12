import time
import hashlib
import requests
import json
from urllib.request import urlopen, Request
from songline import Sendline
from datetime import datetime


# setting the URL you want to monitor
url = Request('https://api.airtable.com/v0/appNMHWvZtHl2NiZf/2564?maxRecords=1&view=Main%20View',
	headers = {
	'Authorization': 'Bearer keyg1sqOJkyHEGQ7A',
	'Cookie': 'brw=brw6LYltop398P5tW'
})

# to perform a GET request and load the
# content of the website and store it in a var
response = urlopen(url).read()


# to create the initial hash
currentHash = hashlib.sha224(response).hexdigest()
print("running")
time.sleep(30)

token = 'ySyeIo0CgrHZBZeWlQfmJfhx8KxWFylayWFRB2driyw'
# token ไปออกเองในเว็บ https://notify-bot.line.me/my/
messenger = Sendline(token)

def _getSendNotify():
	json_data = json.loads(response)

	x = json_data.get('records')

	m = x[0]
	s = m.get('fields')

	key = 'วันที่เติมน้ำมัน'

	id_data = str(s.get('id'))
	licensePlate_data = str(s.get('เลขทะเบียน'))
	start_data = str(s.get('ต้นทาง'))
	end_data = str(s.get('ปลายทาง'))
	distance_data = str(s.get('ระยะทาง'))
	startMilesNum_data = str(s.get('เลขไมล์ต้นทาง'))
	endMilesNum_data = str(s.get('เลขไมล์ปลายทาง'))
	usersCar_data = str(s.get('ผู้ใช้รถ'))
	dateUse_data = s.get('วันที่ใช้รถ')

	dataFilloil_data = str(s.get('วันที่เติมน้ำมัน'))
	milesNumFilloil_data = str(s.get('เลขไมล์เติมน้ำมัน'))
	fillOilLiter_data = str(s.get('จำนวนลิตร'))
	oilPrice_data = str(s.get('ราคา(บาท)'))
	provinceFillOil_data = str(s.get('จังหวัด'))

	dateUse_new = datetime.fromisoformat(dateUse_data[:-1])
	date_time_str = dateUse_new.strftime('%d %B %Y %H:%M:%S')


	# python check if key in dict using "in"
	if key in s:
			dateUse_new_2 = datetime.fromisoformat(dataFilloil_data[:-1])
			date_time_str_fillOil = dateUse_new_2.strftime('%d %B %Y %H:%M:%S')
			print(f"Yes, key: '{key}' มีนะ in dictionary") 
			
	else:
			print(f"No, key: '{key}' ไม่มีนะ in dictionary")
			date_time_str_fillOil = "None"

	# notify
	messenger.sendtext('\n' + '🚗' + 'ข้อมูลการใช้รถยนต์' + '\n' +  '🚗 📊  📈'
				+ '\n' + '\n' + 
	'id: ' + id_data + '\n' +
'เลขทะเบียนรถ : ' + licensePlate_data + '\n' +
'ต้นทาง : ' + start_data + '\n' + 
'ปลายทาง : ' + end_data + '\n' +
'ผู้ใช้รถ : ' + usersCar_data + '\n' +
'เลขไมล์ต้นทาง : ' + startMilesNum_data + '\n' + 
'เลขไมล์ปลายทาง : ' + endMilesNum_data + '\n' + 
'ระยะทาง : ' + distance_data + ' km' + '\n' + 
'วันที่ใช้รถ : ' + date_time_str + '\n' +
	'\n' + '🟢🟢🟢🟢🟢🟢🟢🟢🟢'+ '\n' + '\n' +
'การเติมน้ำมัน ⛽️ ' + '\n' +
'วันที่เติมน้ำมัน : ' + date_time_str_fillOil + '\n' +
'เลขไมล์เติมน้ำมัน : ' + milesNumFilloil_data + '\n' +
'จำนวนลิตร : ' + fillOilLiter_data + ' ลิตร' + '\n'+
'ราคา(บาท) : ' + oilPrice_data + ' บาท' + '\n'+
'จังหวัดที่เติมน้ำมัน : ' + provinceFillOil_data + '\n'
	)

print('api is changed')


while True:
	try:
		# perform the get request and store it in a var
		response = urlopen(url).read()
		
		# create a hash
		currentHash = hashlib.sha224(response).hexdigest()
		
		# wait for 30 seconds
		time.sleep(30)
		
		# perform the get request
		response = urlopen(url).read()
		
		# create a new hash
		newHash = hashlib.sha224(response).hexdigest()

		# check if new hash is same as the previous hash
		if newHash == currentHash:
			continue

		# if something changed in the hashes
		else:
			_getSendNotify()

			# again read the website
			response = urlopen(url).read()

			# create a hash
			currentHash = hashlib.sha224(response).hexdigest()

			# wait for 30 seconds
			time.sleep(10)
			continue
			
	# To handle exceptions
	except Exception as e:
		print('error')



	