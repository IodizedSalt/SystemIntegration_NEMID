from xml.etree.ElementTree import Element, SubElement, Comment, tostring, fromstring, ElementTree
import json
import csv

# XML - > CSV
def xmlToCsv():
    pass

# XML - > JSON
def xmlToJson():
    xmlFile = open('xml.xml', 'r')

    tree = ElementTree(fromstring(xmlFile))
    print(tree)


# CSV - > JSON
def csvToJson():
    csvFile = open('csv.csv', 'r')
    jsonFile = open('./csvTo/csvtojson.json', 'w')

    data = []
    for row in csv.DictReader(csvFile):
        data.append(row)

    jsonFile.write(json.dumps(data))

# CSV - > XML
def csvToXml():
    csvFile = open('csv.csv', 'r') 
    xmlFile = open('./csvTo/csvtoxml.xml', 'wb')

    
    for row in csv.DictReader(csvFile):
        top = Element('DATA')
        body = SubElement(top, 'User')
        uls = SubElement(body, 'Balance')

        body.text = row['user']
        uls.text =  row['balance']
        
        tree_out = tostring(top, encoding="UTF-8")
        xmlFile.write(tree_out)
        xmlFile.write(b'\n')
        print(tree_out)


# JSON - > CSV
def jsonToCsv():

    csvFile = open('./jsonTo/jsontocsv.csv', 'w')

    with open('./json.json', 'r') as read_file:
        data = read_file.read()

    jsonobj = json.loads(data)

    keylist = []

    for key in jsonobj[0]:
        keylist.append(key)
        f = csv.writer(csvFile)

    f.writerow(keylist)
    
    for record in jsonobj:
        currentrecord = []
        for key in keylist:
            currentrecord.append(record[key])
        f.writerow(currentrecord)

    with open('./csv.csv') as f:
        line = f.readline()
        while line:
            line = f.readline()
            # csvFile.write(line)
            print(line)


# JSON - > XML
def jsonToXml():
    xmlFile = open('./jsonTo/jsontoxml.xml', 'wb')
    with open('./json.json', 'r') as read_file:
        data = json.load(read_file)

    top = Element('DATA')
    body = SubElement(top, 'Users')
    uls = SubElement(body, 'Balance')

    for i in data:
        top = Element('DATA')
        body = SubElement(top, 'Users')
        uls = SubElement(body, 'Balance')
        
        body.text = i['user']
        uls.text =  str(i['balance'])

        tree_out = tostring(top, encoding="UTF-8")
        xmlFile.write(tree_out)
        xmlFile.write(b'\n')
        print(tree_out)

# csvToXml()
# csvToJson()

# jsonToXml()
# jsonToCsv()


xmlToJson()