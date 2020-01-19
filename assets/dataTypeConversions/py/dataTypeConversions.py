from xml.etree.ElementTree import Element, SubElement, Comment, tostring
import json
import csv

# XML - > CSV
def xmlToCsv():
    pass

# XML - > JSON
def xmlToJson():
    pass

# CSV - > JSON
def csvToJson():
    csvfile = open("./csv.csv", 'r')
    jsonfile = open("./csvtojson.json", 'w')

    reader = csv.DictReader( csvfile)
    jsonfile.write('[')

    for row in reader:
        json.dump(row, jsonfile)
        jsonfile.write(',\n')
    jsonfile.write(']')

# CSV - > XML
def csvToXml():
    pass 

# JSON - > CSV
def jsonToCsv():
    with open('./json.json', 'r') as read_file:
        data = read_file.read()

    jsonobj = json.loads(data)

    keylist = []
    for key in jsonobj[0]:
        keylist.append(key)
        f = csv.writer(open('./csv.csv', "w"))
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
            print(line)


# JSON - > XML
def jsonToXml():
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
        print(tree_out)

# jsonToXml()       #complete
# jsonToCsv()       #complete
csvToJson()       # half complete, fix trailing comma