import urllib2

def upload_pdf(file_path):


    fileTitle="my_file_name"
    with open('file_path', 'rb') as data:
        result = data.read()
        req = urllib2.Request(url='http://localhost:8983/solr/core_1/update/extract?literal.id='+fileTitle+'&commit=true',data=result)
        req.add_header('Content-type', 'application/pdf')
        urllib2.urlopen(req)


