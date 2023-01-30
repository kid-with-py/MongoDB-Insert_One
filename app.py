

import pymongo

client=pymongo.MongoClient('mongodb://localhost:27017/')

mydatabase=client['Students']

info=mydatabase.studentsinfo

records={
    'firstname':'Jhon',
    'lastname':'Wick',
    'rollnumber':'01'
}

data=info.insert_one(records)

print(data.inserted_id)
