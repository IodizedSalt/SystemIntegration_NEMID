# from xml.etree.ElementTree import Element, SubElement, Comment, tostring, fromstring, ElementTree
import xml.etree.ElementTree as ET
import json
import csv

# XML - > CSV
def xmlToCsv():
    csvFile = open('./xmlTo/xmltocsv.csv', 'w')
    tree = ET.parse('xml.xml')
    root = tree.getroot()

    userList = list(root.iter('user'))
    balanceList = list(root.iter('balance'))
    keyList = ['user', 'balance']
    userBalanceDict = {}
    
    for data in userList:
        balanceList = data.getchildren()
        for balance in balanceList:
            userTextStripped = data.text.replace('\n', '').replace('\t', '')
            userBalanceDict[userTextStripped] = int(balance.text)

    print(userBalanceDict)
    
    writer = csv.writer(csvFile)
    writer.writerow(keyList)
    for key, value in userBalanceDict.items():
       writer.writerow([key, value])


# XML - > JSON
def xmlToJson():
    jsonFile = open('./xmlTo/xmltojson.json', 'w')
    tree = ET.parse('xml.xml')
    root = tree.getroot()

    userList = list(root.iter('user'))
    balanceList = list(root.iter('balance'))

    userBalanceDict = {}
    
    for data in userList:
        balanceList = data.getchildren()
        for balance in balanceList:
            userTextStripped = data.text.replace('\n', '').replace('\t', '')
            userBalanceDict[userTextStripped] = int(balance.text)

    # print(userBalanceDict)
    jsonFile.write(json.dumps(userBalanceDict))

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
        top = ET.Element('DATA')
        body = ET.SubElement(top, 'User')
        uls = ET.SubElement(body, 'Balance')

        body.text = row['user']
        uls.text =  row['balance']
        
        tree_out = ET.tostring(top, encoding="UTF-8")
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

    top = ET.Element('DATA')
    body = ET.SubElement(top, 'Users')
    uls = ET.SubElement(body, 'Balance')

    for i in data:
        top = ET.Element('DATA')
        body = ET.SubElement(top, 'Users')
        uls = ET.SubElement(body, 'Balance')
        
        body.text = i['user']
        uls.text =  str(i['balance'])

        tree_out = ET.tostring(top, encoding="UTF-8")
        xmlFile.write(tree_out)
        xmlFile.write(b'\n')
        print(tree_out)

# csvToXml()
# csvToJson()

# jsonToXml()
# jsonToCsv()


# xmlToJson()
# xmlToCsv()