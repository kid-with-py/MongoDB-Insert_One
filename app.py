### pymongo is the library which helps to interact with MongoDB using Python ###

import pymongo

### Creating URI for MongoDB ###

client=pymongo.MongoClient('mongodb://localhost:27017/')

### Setting DB's Name ###

mydatabase=client['Students']

### Setting collection's(studentsinfo) Name ###

info=mydatabase.studentsinfo

### Creating data for Collection ###

records={
    'firstname':'Jhon',
    'lastname':'Wick',
    'rollnumber':'01'
}

### Inserting The Data into the database-collection ###

data=info.insert_one(records)

print(data.inserted_id)
