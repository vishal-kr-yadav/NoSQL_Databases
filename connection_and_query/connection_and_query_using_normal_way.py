from cassandra.cluster import Cluster
cluster = Cluster() #for connecting on localhost

# cluster = Cluster(['192.168.0.1', '192.168.0.2'])
session = cluster.connect('testing')


# rows = session.execute('SELECT id, name FROM employees')
# for user_row in rows:
#     print user_row.name, user_row.id

def create_namespace(keyspace_name,keyspace_class,keyspace_replication_factor):
    query="""
        CREATE KEYSPACE %s
        WITH replication = { 'class': %s, 'replication_factor': %s }
        """ % keyspace_name % keyspace_class % keyspace_replication_factor
    return query

print(create_namespace('keyspace_name','keyspace_class','keyspace_replication_factor'))