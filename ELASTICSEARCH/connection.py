import elasticsearch as es
import unicodedata
import json, ast
res=es.Elasticsearch(["localhost:9200"], http_auth="elastic:changeme")
import collections
from converterFromUnicode import convert


def createBackup(review,userId):
    backupData=['Rehaan1.0 out of 5 starsEarPods are missing16 February 2018Colour', 'sahil anand1.0 out of 5 starsThe apple product is damaged after one day the display ...20 February 2018Colour', 'Prashun1.0 out of 5 starsOne Star14 February 2018Colour', 'Chandeep Kaur5.0 out of 5 starsFive Stars13 February 2018Colour', 'atul1.0 out of 5 starsOne Star14 February 2018Colour', 'dr hameem meeran pillai5.0 out of 5 starsExcellent phone27 January 2018Colour', 'ABBHI RATHORE5.0 out of 5 starsI phone X is totally dfrnt12 February 2018Colour', 'kushal jain5.0 out of 5 starsBest iphone ever31 January 2018Colour', 'Karan5.0 out of 5 starsBest ever product from amazonBeautiful phone from amazon I love it n best part is that I got a excellent service from amazon Published 48 minutes ago', 'junaid5.0 out of 5 starsI got my order yesterday no damage with all accessories ...I got my order yesterday no damage with all accessories with screen protector inside thank you amazon for offering me in offer price Published 16 hours ago', 'Arvinder Singh5.0 out of 5 starsi phone x the dream phonehi it is almost everybodies dream today to buy this iphone.it is really the nice phone with a lot of features some of the features are -14.73 centimeters (5.Read more Published 3 days ago', 'na3892.0 out of 5 starsNot happy with the purchaseMissing headphones from inside a packed box.Didnt expect that. Published 3 days ago', 'Vijay Nimmagadda5.0 out of 5 starsFive StarsGood Published 5 days ago', 'Smar1.0 out of 5 starsDumbest phoneDumb Published 7 days ago', 'Amazon Customer5.0 out of 5 starsThis is love.. <3 I just love this phoneThis is love.. <3 I just love this phone, excellent features, cameras everything. Must go for this.. Amazon services are excellent too. Published 7 days ago', "Satyaki Chakraborti1.0 out of 5 starsNothing Special and goodYou have better option than an iPhone X . The face ID which is a supreme feature doesn't work that good. And apple is not the first company to bring bezeless display.Read more Published 7 days ago", 'Santosh Ambekar 5.0 out of 5 starsAmazing product and great deliveryUndoubtedly its a great piece of innovation. iPhone X is not only a premium mobile but a great product. Thanks to amazon for making an on time delivery and great packing. Published 8 days ago']
    while userId >1:

        doc = {
            "review": backupData[userId]
            # "review": The apple product is damaged after one day the display
        }
        res.index(index="customer", doc_type='iphoneX', id="user"+str(userId), body=doc)
        userId-=1




def createDocument(review,userId):
    while userId >0 :

        doc = {
            "review": review[userId]
            # "review": The apple product is damaged after one day the display
        }
        res.index(index="customer", doc_type='iphoneX', id="user"+str(userId), body=doc)
        userId-=1

#search if you know the id within ELASTICSEARCH
# result=res.get(index='customer', doc_type='amazon', id='review1')

#match query will show all result depend upon the score .higher the score ,higher the chance to apper in the top

def executeQuery(queryBody):
    output=res.search(index="customer", body=queryBody)
    score=''
    textReview={}
    result=convert(output)
    totalHit=convert(output['hits']['total'])
    i=0
    list=[]
    dict = {}


    while i <totalHit:
            score=result['hits']['hits'][i]['_score']
            id=result['hits']['hits'][i]['_id']
            type=result['hits']['hits'][i]['_type']
            textReview=result['hits']['hits'][i]['_source']

            dict['score']=score
            dict['id']=id
            dict['type'] = type
            dict['textReview'] = textReview
            list.append(dict)
            dict = {}

            i += 1
    list.append({'totalHit':totalHit})

    return json.dumps(list)

# createDocument('q',1)







# term query will show if the match will be exact matching
# output=res.search(index="customer", body={"query": {"term": {'Review15':'nice phone ,good one'}}})
