#!/usr/bin/python
from random import randint
import requests
import time
import urllib

def sign_request(key, raw):
    from hashlib import sha1
    import hmac

    hashed = hmac.new(key, raw, sha1)
    return hashed.digest().encode("base64").rstrip('\n')



consumer_key = 'd7usle9dl46noe5rsqjx1ejsitt9c404'
consumer_secret = 'a970hlce8b3uq0s4opoesxglg2wsetex'
consumer_key_token = '%s&' % (consumer_secret)

print consumer_key_token
print '\n'

version = '1.0'
http_method = 'POST'
url = 'http://justdoit.com/oauth/token/request'
signature_method = 'HMAC-SHA1'
timestamp = int(time.time())
rand_value = randint(1000000, 7777777)

ob_signature = [ 
	('oauth_consumer_key', consumer_key),
	('oauth_nonce', rand_value),
	('oauth_signature_method', signature_method),
	('oauth_timestamp', timestamp),
	('oauth_version', version)  
]

str_signature = '%s&%s&%s' % (
	http_method,
	urllib.quote_plus(url),
	urllib.quote_plus(urllib.urlencode(ob_signature))
)
signature = sign_request(consumer_key_token, str_signature)

print str_signature
print '\n'
print signature

headers = {
	'Authorization': "OAuth oauth_nonce=%d,oauth_consumer_key=%s,oauth_signature=%s,oauth_signature_method=%s,oauth_timestamp=%d,oauth_version=%s" % (rand_value, consumer_key, signature, signature_method, timestamp, version)
}

data={
	'oauth_nonce': rand_value,
	'oauth_consumer_key': consumer_key,
	'oauth_signature' : signature,
	'oauth_signature_method': signature_method,
	'oauth_timestamp': timestamp,
	'oauth_version': version
}

r = requests.post(url, data=data, headers=headers)

print r.status_code, r.reason, r.text







