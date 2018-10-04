import urllib2,ast
import solr_query_builder
import ConfigParser

# Reading solr config
Config = ConfigParser.ConfigParser()
Config.read("main.ini")
hostName=Config.get('Solr','hostName')
port=Config.get('Solr','port')
core=Config.get('Solr','core')
number_of_search_result=Config.get('Solr','number_of_search_result')


boost_topic=Config.get('Solr','boost_topic')
boost_main_content=Config.get('Solr','boost_main_content')
boost_fileName=Config.get('Solr','boost_fileName')
# query_expansion_flag=Config.get('Solr','query_expansion_flag')

reRankDocs=Config.get('Query-Re-Ranking','reRankDocs')
reRankWeight=Config.get('Query-Re-Ranking','reRankWeight')
number_of_search_result_after_QR=Config.get('Query-Re-Ranking','number_of_search_result_after_QR')

base_url='http://'+hostName+':'+port+'/solr/'+core+'/'

# to preapare a string of keywords from a list
def prepare_query_keywords(list_of_keywords):
    key=''
    for each in list_of_keywords:
        key+=each+"+"
    return key[:-1]

# to execute general query
def query_expansion_without_initial_query(list_of_keywords):
    keys = prepare_query_keywords(list_of_keywords)
    url = base_url+"select?q="+keys+"&defType=edismax&qf=topic^"+boost_topic+"+main^"+boost_main_content+"+fileName^"+boost_fileName+"&wt=json&fl=*,score&rows="+number_of_search_result
    print(url)
    content = urllib2.urlopen(url).read()
    return (ast.literal_eval(content))['response']


# to get all the topic for a specific query
def main_query_for_getting_topic(url):
    content = urllib2.urlopen(url).read()
    solr_response=ast.literal_eval(content)['response']

    topic_from_main_query=[]
    doc=solr_response['docs']
    for each_doc in doc:
        for each_topic in each_doc['topic']:
            topic_from_main_query.append(each_topic)

    final_topic_after_removing_duplicates=list(set(topic_from_main_query))
    return (final_topic_after_removing_duplicates)

# depending upon the user solr config. it will execute query expansion after getting all the topic from a general query
def query_re_ranking_with_initial_query(query_keywords):

    # getting the string query_keywords from a user defined function
    key=prepare_query_keywords(query_keywords)

    # general query request for getting Nth result from a query
    main_url = base_url+"select?q="+key+"&defType=edismax&qf=topic^" + boost_topic + "+Pdf_extraction^" + boost_main_content + "+fileName^" + boost_fileName + "&wt=json&fl=*,score&rows="+number_of_search_result

    # gettting all the union of topic from the general_url
    topic_list=main_query_for_getting_topic(main_url)

    # preparing the query keywords for Query_Re-Ranking
    sub_query_keywords=prepare_query_keywords(topic_list)

    # preparing the query url for query_re_ranking
    query_url=base_url+'select?q='+key+'&defType=edismax&qf=topic^'+boost_topic+'+Pdf_extraction^'+boost_main_content+'+fileName^'+boost_fileName+'&rq=%7B!rerank%20reRankQuery=$rqq%20reRankDocs='+reRankDocs+'%20reRankWeight='+reRankWeight+'%7D&rqq=topic:'+sub_query_keywords+'&fl=*,score&rows='+number_of_search_result_after_QR

    # reading the content from the solr
    content = urllib2.urlopen(query_url).read()
    solr_response = ast.literal_eval(content)['response']
    return solr_response


