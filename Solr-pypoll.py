#!/usr/bin/python
# -*- encoding: utf-8 -*-

import urllib
import xml.etree.ElementTree as ET
import json

fqdn = 'http://127.0.0.1:8888/'
uri = 'solr4/admin/cores?action=STATUS'

def main():
    
    data = []
    
    resp=urllib.urlopen(fqdn+uri).read()
    tree = ET.fromstring(resp)
    for lst in tree.findall("lst"):
        for lst2 in lst.findall("lst"):
            core={"{#CORENAME}":lst2.attrib['name']}
            data.append(core)
   
    print  json.dumps({"data": data})


if __name__ == "__main__":
    main() 
