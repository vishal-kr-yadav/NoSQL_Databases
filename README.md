
**Install Cassandra and Run a Single-Node Cluster on Ubuntu**  
Reference link: https://www.digitalocean.com/community/tutorials/how-to-install-cassandra-and-run-a-single-node-cluster-on-ubuntu-14-04

**Installation for python** 
 
pip install cassandra-driver  
reference_link : https://datastax.github.io/python-driver/installation.html

**Cassandra cqlsh coomand:**  
Reference link: https://dzone.com/articles/cassandra-data-modeling-primary-clustering-partiti
  
**Create keyspace**
- CREATE KEYSPACE testing
    WITH replication = {'class':'SimpleStrategy', 'replication_factor' : 1};
    use testing;

**Create table**
- CREATE Table employees(id uuid,name varchar,PRIMARY KEY(id));
- create table marks(id int,exam_date timestamp,marks float, exam_name text,
                   primary key (stuid,exam_date));

**Insert into table:**
- insert into employees (id,name) values (now(),'Jon Don');
- insert into employees (id,name) values (now(),'john cena');

**EXPAND ON** (Not compulsory)


**Some useful commands**
                   
- DESCRIBE tables;
- DROP TABLE employees;
- SELECT * FROM system.schema_keyspaces ;

**Model in cassandra:**  
Reference link: https://cqlengine.readthedocs.io/en/latest/