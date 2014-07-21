import riak
myClient = riak.RiakClient(pb_port=8087, protocol='pbc')
bucket = myClient.bucket('contacts')
bucket.enable_search()
for doc in bucket.search('state:Tennessee')['docs']:
	print doc
#for key in bucket.get_keys():
#	print bucket.get(key).data['state']
