import sys
import numpy as np
from lxml import etree
from io import StringIO
import xml.etree.cElementTree as ET

xml_string = open('bookstore.xml')
bookstore = etree.fromstring(xml_string.read())
query = sys.argv[1]
if(query == "query1"):
    path = bookstore.xpath('//book/title | //book/price')
    for element in path:
        print(element.text)
elif(query == "query2"):
    path = bookstore.xpath('//title | //price')
    for element in path:
        print(element.text)
elif(query == "query3"):
    path = bookstore.xpath('/bookstore/book/title | //price')
    for element in path:
        print(element.text)


