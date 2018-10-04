Objectives
**********
Text Analysis using elasticSearch

installation
************
i)Install docker
  **************
ii)pull the elastic image in docker
***********************************
docker pull docker.elastic.co/elasticsearch/elasticsearch:5.5.3

iii)run the elasticsearch within docker
***************************************
docker run -p 9200:9200 -p 9300:9300 -e "discovery.type=single-node" docker.elastic.co/elasticsearch/elasticsearch:5.5.3

iv)Authentications
*********************

default user: elastic
           password: changeme

v)install elasticsearch plugins
*******************************
https://chrome.google.com/webstore/detail/elasticsearch-head/ffmkiejjmecolpfloofpjologoblkegm/

FLow
****
i)scrap data from Amazon.com(here we scrap review of iphone X from amazon.com)
ii)Store the review in elastic search
iii)Query text from ElasticSearch on stored review


significance of python file
***************************
converterFromUnicode.py :-> used to convert the unicode to standard data type
phase1 :-> initial Api to retrieve and put review documents in elastic search
connection.py :-> connect to elasticSearch, query and prepare response


example
********
http://localhost:5000/PUT/Review/iphoneX/From/Amazon/<reviews-count>


http://localhost:5000/GET/Review/By/keywords/<key-words>




match(post)
******
{
  "query": {
    "match": {
      "review": "I just love this phone"
    }
  }
}

term(post)
*****
{
  "query": {
    "term": {
      "review": "nice phone"
    }
  }
}


wildcard
***
{
  "query": {
    "wildcard": {
      "review": "*1.0*"
    }
  }
}
