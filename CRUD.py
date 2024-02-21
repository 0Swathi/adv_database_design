#insert one()
from pymongo import MongoClient
from pymongo.server_api import ServerApi
import datetime
import pprint

uri = "mongodb+srv://swathireddy:swathireddy@cluster0.55uldwr.mongodb.net/"

# Create a new client and connect to the server
client = MongoClient(uri, server_api=ServerApi('1'))

try:
    # Send a ping to confirm a successful connection
    client.admin.command('ping')

    # Get reference to 'school' database
    db = client.school

    # Get reference to 'students' collection
    students_collection = db.students

    # Inserting one student record
    new_student = {
        "name": "John Doe",
        "age": 15,
        "grade": 10,
        "attendance": {
            "2024-02-20": True,
            "2024-02-21": False
        },
        "grades": {
            "Math": 85,
            "Science": 90,
            "History": 78
        },
        "registration_date": datetime.datetime.utcnow()
    }

    # Insert the new student document into the 'students' collection
    result = students_collection.insert_one(new_student)

    document_id = result.inserted_id
    pprint(f"_id of inserted document: {document_id}")

except Exception as e:
    print(e)
finally:
  client.close()
#insertmany()
  from pymongo import MongoClient
from pymongo.server_api import ServerApi
import datetime
import pprint

uri = "mongodb+srv://swathireddy:swathireddy@cluster0.55uldwr.mongodb.net/"

# Create a new client and connect to the server
client = MongoClient(uri, server_api=ServerApi('1'))

try:
    # Send a ping to confirm a successful connection
    client.admin.command('ping')

    # Get reference to 'school' database
    db = client.school

    # Get reference to 'students' collection
    students_collection = db.students

    # List of student records to insert
    student_records = [
        {
            "name": "Alice",
            "age": 16,
            "grade": 11,
            "attendance": {
                "2024-02-20": True,
                "2024-02-21": False
            },
            "grades": {
                "Math": 90,
                "Science": 85,
                "History": 88
            },
            "registration_date": datetime.datetime.utcnow()
        },
        {
            "name": "Bob",
            "age": 15,
            "grade": 10,
            "attendance": {
                "2024-02-20": True,
                "2024-02-21": True
            },
            "grades": {
                "Math": 88,
                "Science": 92,
                "History": 80
            },
            "registration_date": datetime.datetime.utcnow()
        }
        # Add more student records as needed
    ]

    # Insert the list of student documents into the 'students' collection
    result = students_collection.insert_many(student_records)

    # Print the IDs of the inserted documents
    pprint(f"_ids of inserted documents: {result.inserted_ids}")

except Exception as e:
    print(e)
finally:
  client.close()

#read()
  from pymongo.mongo_client import MongoClient
from pymongo.server_api import ServerApi
from bson.objectid import ObjectId
import pprint

# URI for MongoDB Atlas connection
uri = "mongodb+srv://swathireddy:swathireddy@cluster0.55uldwr.mongodb.net/"

# Create a new client and connect to the MongoDB server
client = MongoClient(uri, server_api=ServerApi('1'))

try:
    # Sending a ping to confirm a successful connection to the server
    client.admin.command('ping')

    # Reference to the 'school' database
    db = client.school

    # Reference to the 'students' collection
    students_collection = db.students

    # Creating a query to find a specific student by their unique ID
    student_id_to_find = ObjectId("65c2caeaae6140696995984e")

    # Finding the student document with the specified ID in the 'students' collection
    found_student = students_collection.find_one({"_id": student_id_to_find})

    # Printing the found student document
    pprint.pprint(found_student)

except Exception as e:
    # Handling any errors that occur during the process
    print(e)

finally:
    # Closing the connection to the MongoDB server
  client.close()

#readone()
  from pymongo.mongo_client import MongoClient
from pymongo.server_api import ServerApi
import pprint

# MongoDB Atlas URI
uri = "mongodb+srv://swathireddy:swathireddy@cluster0.55uldwr.mongodb.net/"

# Create a new client and connect to the MongoDB server
client = MongoClient(uri, server_api=ServerApi('1'))

try:
    # Send a ping to confirm a successful connection to the server
    client.admin.command('ping')

    # Get reference to the 'school' database
    db = client.school

    # Get reference to the 'students' collection
    students_collection = db.students

    # Defining a query to find students who scored above a certain grade
    query = {"grades.Math": {"$gt": 80}}  # Find students who scored more than 80 in Math

    # Finding the documents matching the query in the 'students' collection
    cursor = students_collection.find(query)

    num_students = 0
    for student in cursor:
        num_students += 1
        pprint.pprint(student)
        print()
    print("# of students found: " + str(num_students))

except Exception as e:
    # Handling any errors that occur during the process
print(e)

#updateone()
from pymongo.mongo_client import MongoClient
from pymongo.server_api import ServerApi
from bson.objectid import ObjectId
import pprint

# MongoDB Atlas URI
uri = ""mongodb+srv://swathireddy:swathireddy@cluster0.55uldwr.mongodb.net/""

# Create a new client and connect to the MongoDB server
client = MongoClient(uri, server_api=ServerApi('1'))

try:
    # Send a ping to confirm a successful connection to the server
    client.admin.command('ping')

    # Get reference to the 'school' database
    db = client.school

    # Get reference to the 'students' collection
    students_collection = db.students

    # Filter for the student to update (assuming we're updating based on their unique ID)
    student_to_update = {"_id": ObjectId("65c2cb3a004800a420ffc3dd")}

    # Update operation: adding 1 to the student's age
    increment_age = {"$inc": {"age": 1}}

    # Print the original student document
    pprint.pprint(students_collection.find_one(student_to_update))

    # Update the target student document by incrementing their age
    result = students_collection.update_one(student_to_update, increment_age)
    print("Documents updated: " + str(result.modified_count))

    # Print the updated student document
    pprint.pprint(students_collection.find_one(student_to_update))

except Exception as e:
    # Handling any errors that occur during the process
    print(e)

finally:
    # Closing the connection to the MongoDB server
 client.close()

#updatemany()
from pymongo.mongo_client import MongoClient
from pymongo.server_api import ServerApi
from bson.objectid import ObjectId
import pprint

# MongoDB Atlas URI
uri = "mongodb+srv://swathireddy:swathireddy@cluster0.55uldwr.mongodb.net/"

# Create a new client and connect to the MongoDB server
client = MongoClient(uri, server_api=ServerApi('1'))

try:
    # Send a ping to confirm a successful connection to the server
    client.admin.command('ping')

    # Get reference to 'school' database
    db = client.school

    # Get reference to 'students' collection
    students_collection = db.students

    # Filter: Selecting students with a certain grade level
    select_students = {"grade": 10}

    # Update: Setting a field for selected students (e.g., assigning a homeroom)
    set_field = {"$set": {"homeroom": "10A"}}

    # Update documents matching the filter criteria
    result = students_collection.update_many(select_students, set_field)

    # Print the number of documents matched and updated
    print("Documents matched: " + str(result.matched_count))
    print("Documents updated: " + str(result.modified_count))

    # Print one of the updated documents to verify the changes
    pprint.pprint(students_collection.find_one(select_students))

except Exception as e:
    # Handle any errors that occur during the process
    print(e)

finally:
    # Close the connection to the MongoDB server
  client.close()

#deleteone()
  from pymongo.mongo_client import MongoClient
from pymongo.server_api import ServerApi
from bson.objectid import ObjectId
import pprint

# MongoDB Atlas URI
uri = "mongodb+srv://swathireddy:swathireddy@cluster0.55uldwr.mongodb.net/"

# Create a new client and connect to the MongoDB server
client = MongoClient(uri, server_api=ServerApi('1'))

try:
    # Send a ping to confirm a successful connection to the server
    client.admin.command('ping')

    # Get reference to the 'school' database
    db = client.school

    # Get reference to the 'students' collection
    students_collection = db.students

    # Filter by ObjectId
    student_to_delete = {"_id": ObjectId("65c2caeaae6140696995984f")}

    # Search for the student document before deletion
    print("Searching for target student document before deletion: ")
    pprint.pprint(students_collection.find_one(student_to_delete))

    # Write an expression that deletes the target student document
    result = students_collection.delete_one(student_to_delete)

    # Search for the student document after deletion
    print("Searching for target student document after deletion: ")
    pprint.pprint(students_collection.find_one(student_to_delete))

    print("Documents deleted: " + str(result.deleted_count))

except Exception as e:
    # Handle any errors that occur during the process
    print(e)

finally:
    # Close the connection to the MongoDB server
  client.close()

#deletemany()
  from pymongo.mongo_client import MongoClient
from pymongo.server_api import ServerApi
from bson.objectid import ObjectId
import pprint

# MongoDB Atlas URI
uri = "mongodb+srv://swathireddy:swathireddy@cluster0.55uldwr.mongodb.net/"

# Create a new client and connect to the MongoDB server
client = MongoClient(uri, server_api=ServerApi('1'))

try:
    # Send a ping to confirm a successful connection to the server
    client.admin.command('ping')

    # Get reference to the 'school' database
    db = client.school

    # Get reference to the 'students' collection
    students_collection = db.students

    # Filter students based on a condition (e.g., age less than 18)
    students_to_delete = {"age": {"$lt": 18}}

    # Search for sample student document before deletion
    print("Searching for sample target student document before deletion: ")
    pprint.pprint(students_collection.find_one(students_to_delete))

    # Write an expression that deletes the target student documents
    result = students_collection.delete_many(students_to_delete)

    # Search for sample student document after deletion
    print("Searching for sample target student document after deletion: ")
    pprint.pprint(students_collection.find_one(students_to_delete))

    print("Documents deleted: " + str(result.deleted_count))

except Exception as e:
    # Handle any errors that occur during the process
    print(e)

finally:
    # Close the connection to the MongoDB server
  client.close()





