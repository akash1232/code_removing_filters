

#For Production you need to include authorisation also   (url,auth=("username","password"))
import requests
import json

update_url="http://45.33.101.163:8983/solr/collection1/update"     


headers={'content-type':'application/json'}
	
params = {"commit" : "true" }



r=requests.get("http://45.33.101.163:8983/solr/collection1/select?q=*%3A*&fq=filters%3A%22Screen+Size%3B4.6+inches+-+5.0+inches%22&start=0&rows=0&wt=json&indent=true")
r=json.loads(r.text)
numfound=r["response"]["numFound"]
start=0
end=5000

while start <  numfound:
	final_data=[]
	r=requests.get("http://45.33.101.163:8983/solr/collection1/select?q=*%3A*&fq=filters%3A%22Screen+Size%3B4.6+inches+-+5.0+inches%22&start="+str(start)+"&rows="+str(end)+"&fl=id%2Cfilters&wt=json&indent=true")
	r=json.loads(r.text)

	for data in r["response"]["docs"]:

		print (data["filters"])
	
		id=data["id"]
		print id
		try:
			data["filters"].remove("Screen Size;4.6 inches - 5.0 inches")    
			print (data["filters"])
			final_data.append({'id':str(id),'filters':{'set':(data["filters"])}})
		except:
			pass
	

	print final_data



	r=requests.post(update_url,headers=headers,params=params,data=json.dumps(final_data))
	print r.text

	start=start+end
	end=end+5000
	
	
	
	
