import urllib2,ast


url='http://localhost:8983/solr/core_1/select?q={!mlt%20qf=topic%20mintf=1%20mindf=1}1'

content = urllib2.urlopen(url).read()
solr_response = ast.literal_eval(content)['response']
print(solr_response)


