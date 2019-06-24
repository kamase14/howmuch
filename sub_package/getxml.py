import datetime
import time
import xml.etree.ElementTree as ET
import hmac
import hashlib
import urllib.parse


def func_getxml(cardname):
    url = 'http://wonder.wisdom-guild.net/api/card-price/v1/'

    api_key = "INSERT_YOUR_APIKEY"
    secret  = "INSERT_SECRET_KEY"
    # send e-mail to wisdom_guild
    
    name = cardname
    now = datetime.datetime.now()
    unix = str(round(time.mktime(now.timetuple())))
    tmp = {
    "api_key" : api_key,
    "card" : cardname,
    "timestamp"  : unix
    }
    query= urllib.parse.urlencode(tmp)


    query_list = query.split('&')
    query_list.sort()
    query_string = '\n'.join(query_list)
    print(query_string)
    sig = hmac.new(b'0123456789', query_string.encode('UTF-8'), hashlib.sha256)
    sig = sig.hexdigest()

    print("#"*50)


    print("\n sig2     :"  + " " + sig)

    all_url = url + "?" + query + "&api_sig=" + sig

    return all_url
