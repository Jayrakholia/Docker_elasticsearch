from elasticsearch import Elasticsearch
es = Elasticsearch([{'host': 'localhost', 'port': 9200, 'scheme':'http'}])


"""
create index
    """
index_name = 'elastic_index'
es.indices.create(index=index_name)

"""
add document to the index
    """
    
index_name = 'elastic_index'

document1 = {
    'name':'jay',
    'age': 20,
    'gender': 'Male'
}

document2 = {
    'name':'vyom',
    'age': 20,
    'gender':'Male'
}

document3 = {
    'name':'X',
    'age': 22,
    'gender':'Male'
}

document4= {
    'name':'Raj',
    'age': 20,
    'gender':'Male'
}

res = es.index(index=index_name,id = "1",body=document1)
print(res)
res2 = es.index(index=index_name,id="2",body=document2)
print(res2)
res3=es.index(index=index_name,id="3",body=document3)
print(res3)
res4=es.index(index=index_name,id="4",body=document4)
print(res4)

"""
Update document
    """
index_name = 'elastic_index'
doc_id = '1'

#define query
update_query = {
    'doc':{
        'title':'New',
        'content':'updated'
    }
}
es.update(index=index_name,id = "1", body=update_query)

"""
Search document(get)
    """
index_name = 'elastic_index'
resp=es.get(index=index_name,id=1)
query=print(resp['_source'])

"""
Delete
    """
index_name = 'elastic_index'
es.delete(index=index_name,id=2)

"""
 Search by name
    """
index_name = 'elastic_index'
search_term = 'jay'

query = {
    'query': {
        'match': {
            'name': search_term
        }
    }
}

results = es.search(index=index_name, body=query)

for result in results['hits']['hits']:
    print(result['_source'])
