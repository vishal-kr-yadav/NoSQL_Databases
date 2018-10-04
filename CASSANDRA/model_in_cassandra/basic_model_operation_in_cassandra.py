from cassandra.cqlengine import columns
from cassandra.cqlengine.models import  Model
from cassandra.cqlengine.management import sync_table
from cassandra.cqlengine import connection
import uuid
from datetime import datetime

#connection
connection.setup(['127.0.0.1'], "testing")

#model class
class ExampleModel(Model):
    example_id      = columns.UUID(primary_key=True, default=uuid.uuid4)
    example_type    = columns.Integer(index=True)
    created_at      = columns.DateTime()
    description     = columns.Text(required=False)


# create a table within the keyspace
def create(ExampleModel,example_type,description):

    sync_table(ExampleModel)
    em1 = ExampleModel.create(example_type=example_type, description=description, created_at=datetime.now())

#a simple query for getting the count
def get_count(model):
    total_count=model.objects.count()
    return total_count

#  a simple query for getting where example_type=any_value
def get_example_type(model,example_type):
    q=model.objects(example_type=example_type)
    for instance in q:
        print(instance.description)

#function call
print(get_count(ExampleModel))
get_example_type(ExampleModel,1)
create('ExampleModel','example_type',"description")
