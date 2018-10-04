from pysolr import Solr
conn = Solr('http://localhost:8983/solr/core_1')

# select * from core_1 where topic=collect;
# It will return all the documents where "field->topic=collect"
results = conn.search("topic:collect")
print(results)

#iterate through results object and print each document
for result in results:
    print(result)


def add_documents_in_solr():
    docs = [
         {'id': 1,  'topic': ["topic1","topic2"], 'main': '["All the content of the file.txt file is present here" ]','fileName':["File.txt"]},
      ]
    conn.add(docs)

def delete_all_documents_from_solr():

    conn.delete(q='*:*')
