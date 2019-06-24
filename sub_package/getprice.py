import json
import xmljson
import urllib.request
from lxml.etree import parse

import xml.etree.ElementTree as ET

def func_getprice(url,cardname):
    result_message = ""
    price_list = []
    req = urllib.request.Request(url)

    with urllib.request.urlopen(req) as response:
        xmldata = response.read()

    root  = ET.fromstring(xmldata)

    for value in root.iter('value'):
        price_list.append(str(round(float(value.text))))

    print(price_list)

    result_message = "**" + cardname + "**の金額一覧(wisdom_guild調べ)\n最安値　　 :  **"+ price_list[0] + "円**\n平均値　　 :  **" + price_list[1] + "円**\nトリム平均 :  **" + price_list[2] + "円**\n中央値　　 :  **" + price_list[3] + "円**"

    return  result_message
