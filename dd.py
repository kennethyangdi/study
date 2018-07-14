
#load picture
import requests
import datetime,time
from bs4 import BeautifulSoup

try:
  htmlurl = "http://s2.lulujjs.club/pw/thread.php?fid=14&page=3"
  res = requests.get(htmlurl)
except Exception as e:
  print (e)
else:
  print("parse "+htmlurl+" success")
finally:
  print("continue to read html summary")

html = BeautifulSoup(res.text,'lxml')
print(html)
seq=1
for link in html.find_all('a'):
	print(seq)
	#if seq == 10:
	#	break
	id = link.get('id')
	if(id):
		if id.startswith('a_ajax'):
			seq += 1
			hre = link.get('href')
			try:
			 picsurl = 'http://s2.lulujjs.club/pw/'+hre
			 res = requests.get(picsurl)
			except Exception as e:
			 print(e)
			else:
			 print("parse "+res+" success")
			finally:
			 print("continue to read html detail")
			#read pic
			html = BeautifulSoup(res.text,'lxml')
			for index, each in enumerate(html.select('#read_tpc img')):
				d = time.strftime("%Y%m%d%H%M%S", time.localtime())
				with open('{}.jpg'.format(d), 'wb') as jpg:
					starttime = datetime.datetime.now()
					jpg.write(requests.get(each.attrs['src'], stream=True).content)
					endtime = datetime.datetime.now()
					print (endtime - starttime).seconds
