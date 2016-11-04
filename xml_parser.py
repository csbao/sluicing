import xml.etree.cElementTree as ET
import itertools, re
import sys, unicodedata, os, gzip, json

class custom_xml_parser(ET.XMLParser):

    rx = re.compile("&[^\s]*;")
    def feed(self,data):
        # m = self.rx.search(data)
        mydata = data
        for i in self.rx.finditer(data):
            mstart, mend = i.span()
            mydata = mydata[:mstart] + i.group().lower() + mydata[mend:]


        super(custom_xml_parser,self).feed(mydata)



def process_filename(stringname):
    """ takes: stringname to be processed as a file
        ret:  string
    """
    #process string to filename
    filename = stringname.split("/")[2].split(".")[0]
    return "../nyt_eng/"+filename+".gz"

def clean_text(text):
    return text.replace("\n", " ").replace(" ", "").strip()

def list_of_file(filename):
    with gzip.open (filename, "r") as f:
        parser = custom_xml_parser(encoding='utf-8')
        l = f.readlines()

        it = itertools.chain('<root>', [i.decode('utf-8') for i in l], '</root>')
        root = ET.fromstringlist(it, parser=parser)

    lists = []
    doc_id = ""
    for element in root:
        headline = ""
        list1=[]
        doc_id = element.attrib["id"]
        # print(element.attrib["id"])
        for e in element:
            if (e.tag == 'HEADLINE'):
                headline = e.text.strip()

            list2 = [clean_text(i.text) for i in e if e.tag=='TEXT']
            if len(list2) > 0:
                # lists.append(doc_id, list2)
                lists.append((headline, list2)) if len(headline) > 0 else lists.append((doc_id, list2))

        # if len(list1) > 0:
        #     lists.append((headline, list1)) if len(headline) > 0 else lists.append((doc_id, list1))
    return lists

def jsonConvert(jsonFileName):
    # requires json format, a la allSluices.jsons
    f = jsonFileName
    jsonContent = []
    with open(f, 'r') as fd:
        jsonContent = fd.readlines()

    contents = []
    for l in jsonContent:
        obj = json.loads(l)
        # "metadata": {
        #                 "line": 3855,
        #                 "file": "Treebanks/NYT-Parsed/nyt_eng_199407.tgrep2",
        #                 "treeNode": 12
        #             },

        index = obj["metadata"]["file"] + "_" + str(obj["metadata"]["line"])
        file = obj["metadata"]["file"]
        sluice = obj["match"]["sluice"]["string"]  # should we add the tree too?
        sent = obj["match"]["sentence"]["string"]
        govVP = obj["match"]["govVP"]["string"]
        # before = ""
        # after = ""
        # for i in obj["before"]:
        #     before += i["string"]
        # for i in obj["after"]:
        #     after += i["string"]
        record = (file, sent, sluice, govVP)
        contents.append(record)
    return contents



def main():
    # Now we would like to iterate through database and search for sentence in lists
    #conn = sqlite3.connect('nyt.db')
    #c = conn.cursor()

    #c.execute(''' select line, sentence, file from sluices order by file asc''')
    #rows = c.fetchall()
    begin = int(sys.argv[1])
    end = int(sys.argv[2])
    begin = 0
    cwd = "/campusdata/csbao/sluicing/scripts/"
    rows = jsonConvert(cwd+"allSluices.jsons")
    end = len(rows)
    file1 = rows[0][0]
    print(file1)
    contents = list_of_file(process_filename(file1))
    for iter in rows[begin:end]:
        removedSpaces = iter[1].replace(" ", "")
        # Now we need to make iter[2] search through everything lol
        if file1 != iter[0]:
            file1 = iter[0]
            filename = process_filename(file1)
            # update contents
            contents = list_of_file(filename)
        # if (iter[2]=="Treebanks/NYT-Parsed/nyt_eng_199407.tgrep2"):

        for i in contents:
            # print(removedSpaces)
            find = False
            for sent in i[1]:
                if (removedSpaces in sent):
                    print (i[0])
                    find = True
                    break
            if find: break



if __name__ == "__main__":
    main()

