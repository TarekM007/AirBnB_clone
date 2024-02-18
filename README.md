<h1><img src="https://raw.githubusercontent.com/Ouyei/AirBnB_clone/master/images/hbnb%20img.png" alt="logo python" width="650" height="270"><br/><b>0x00. AirBnB clone - The console</b></h1>

## Getting Started

 
**What’s a command interpreter?**

Do you remember the Shell? It’s exactly the same but limited to a specific use-case. In our case, we want to

be able to manage the objects of our project:

  

- Create a new object (ex: a new User or a new Place)

- Retrieve an object from a file, a database etc…

- Do operations on objects (count, compute stats, etc…)

- Update attributes of an object

- Destroy an object

  

### Learning Objectives

  

## General

 - How to create a Python package
   
  - How to create a command interpreter in Python using the cmd module
   
   - What is Unit testing and how to implement it in a large project
   
   - How to serialize and deserialize a Class
   
   - How to write and read a JSON file
   
   - How to manage datetime
   
   - What is an UUID
   
   - What is *args and how to use it
   
   - What is **kwargs and how to use it
   
   - How to handle named arguments in a function

  
  

## Execution

  
Your shell should work like this in interactive mode:

  
```
$ ./console.py
(hbnb) help

Documented commands (type help <topic>):
========================================
EOF help quit

(hbnb)
(hbnb)
(hbnb) quit
$
```

But also in non-interactive mode: (like the Shell project in C)

```
$ echo "help" | ./console.py

(hbnb)

Documented commands (type help <topic>):
========================================

EOF help quit
(hbnb)
$
$ cat test_help
help
$
$ cat test_help | ./console.py
(hbnb)

  
Documented commands (type help <topic>):
========================================
EOF help quit
(hbnb)
$

```

## Usage Examples

**Launching the console**
```
$ ./console.py
(hbnb) 
```
**Creating a new object**
```
(hbnb) create
** class name missing **
(hbnb) create User
7b8c7a8b-f45a-4484-b6e2-aaed70cdac61
```
**Show an object**
```
(hbnb) show User
** instance id missing **
(hbnb) show User 7b8c7a8b-f45a-4484-b6e2-aaed70cdac61
[User] (7b8c7a8b-f45a-4484-b6e2-aaed70cdac61) {'updated_at': datetime.datetime(2022, 3, 6, 14, 3, 12, 433468), 'id': '7b8c7a8b-f45a-4484-b6e2-aaed70cdac61', 'created_at': datetime.datetime(2022, 3, 6, 14, 3, 12, 433433)}
```
**Update an object**
```
(hbnb) all
[[BaseModel] (27f7849d-1bb9-4cce-9e1e-3d933b2e882d) {'updated_at': datetime.datetime(2022, 3, 4, 5, 40, 47, 215829), 'id': '27f7849d-1bb9-4cce-9e1e-3d933b2e882d', 'created_at': datetime.datetime(2022, 3, 4, 5, 40, 47, 215822), 'name': 'My_First_Model', 'my_number': 89}, [BaseModel] (fc9c4248-2f98-4603-a716-27806a356b78) {'updated_at': datetime.datetime(2022, 3, 4, 5, 41, 28, 920273), 'id': 'fc9c4248-2f98-4603-a716-27806a356b78', 'created_at': datetime.datetime(2022, 3, 4, 5, 41, 28, 920267), 'name': 'My_First_Model', 'my_number': 89}, [BaseModel] (27dd53e5-e308-4bed-ac3d-eaa2ab4e941d) {'updated_at': datetime.datetime(2022, 3, 4, 5, 43, 54, 796849), 'id': '27dd53e5-e308-4bed-ac3d-eaa2ab4e941d', 'created_at': datetime.datetime(2022, 3, 4, 5, 43, 54, 796818)}, [User] (d6ded2d9-8cf9-4c44-8ab0-d47fa9a89a9f) {'updated_at': datetime.datetime(2022, 3, 4, 5, 46, 43, 114823), 'id': 'd6ded2d9-8cf9-4c44-8ab0-d47fa9a89a9f', 'created_at': datetime.datetime(2022, 3, 4, 5, 46, 43, 114813), 'first_name': 'Betty', 'last_name': 'Bar', 'email': 'airbnb@mail.com', 'password': 'root'}, [User] (8ce747cb-ce8e-498f-a493-ce415b8a6e6c) {'updated_at': datetime.datetime(2022, 3, 4, 5, 46, 43, 115617), 'id': '8ce747cb-ce8e-498f-a493-ce415b8a6e6c', 'created_at': datetime.datetime(2022, 3, 4, 5, 46, 43, 115610), 'first_name': 'John', 'email': 'airbnb2@mail.com', 'password': 'root'}, [User] (7b8c7a8b-f45a-4484-b6e2-aaed70cdac61) {'updated_at': datetime.datetime(2022, 3, 6, 14, 3, 12, 433468), 'id': '7b8c7a8b-f45a-4484-b6e2-aaed70cdac61', 'created_at': datetime.datetime(2022, 3, 6, 14, 3, 12, 433433)}]
(hbnb) update
** class name missing **
(hbnb) update User
** instance id missing **
(hbnb) update User 7b8c7a8b-f45a-4484-b6e2-aaed70cdac61
** attribute name missing **
(hbnb) update User 7b8c7a8b-f45a-4484-b6e2-aaed70cdac61 Age "42"
(hbnb) all
[[BaseModel] (27f7849d-1bb9-4cce-9e1e-3d933b2e882d) {'updated_at': datetime.datetime(2022, 3, 4, 5, 40, 47, 215829), 'id': '27f7849d-1bb9-4cce-9e1e-3d933b2e882d', 'created_at': datetime.datetime(2022, 3, 4, 5, 40, 47, 215822), 'name': 'My_First_Model', 'my_number': 89}, [BaseModel] (fc9c4248-2f98-4603-a716-27806a356b78) {'updated_at': datetime.datetime(2022, 3, 4, 5, 41, 28, 920273), 'id': 'fc9c4248-2f98-4603-a716-27806a356b78', 'created_at': datetime.datetime(2022, 3, 4, 5, 41, 28, 920267), 'name': 'My_First_Model', 'my_number': 89}, [BaseModel] (27dd53e5-e308-4bed-ac3d-eaa2ab4e941d) {'updated_at': datetime.datetime(2022, 3, 4, 5, 43, 54, 796849), 'id': '27dd53e5-e308-4bed-ac3d-eaa2ab4e941d', 'created_at': datetime.datetime(2022, 3, 4, 5, 43, 54, 796818)}, [User] (d6ded2d9-8cf9-4c44-8ab0-d47fa9a89a9f) {'updated_at': datetime.datetime(2022, 3, 4, 5, 46, 43, 114823), 'id': 'd6ded2d9-8cf9-4c44-8ab0-d47fa9a89a9f', 'created_at': datetime.datetime(2022, 3, 4, 5, 46, 43, 114813), 'first_name': 'Betty', 'last_name': 'Bar', 'email': 'airbnb@mail.com', 'password': 'root'}, [User] (8ce747cb-ce8e-498f-a493-ce415b8a6e6c) {'updated_at': datetime.datetime(2022, 3, 4, 5, 46, 43, 115617), 'id': '8ce747cb-ce8e-498f-a493-ce415b8a6e6c', 'created_at': datetime.datetime(2022, 3, 4, 5, 46, 43, 115610), 'first_name': 'John', 'email': 'airbnb2@mail.com', 'password': 'root'}, [User] (7b8c7a8b-f45a-4484-b6e2-aaed70cdac61) {'updated_at': datetime.datetime(2022, 3, 6, 14, 5, 57, 527661), 'id': '7b8c7a8b-f45a-4484-b6e2-aaed70cdac61', 'created_at': datetime.datetime(2022, 3, 6, 14, 3, 12, 433433), 'Age': '42'}]
```
**Destroy an object**
```
(hbnb) destroy
** class name missing **
(hbnb) destroy User
** instance id missing **
(hbnb) destroy User 7b8c7a8b-f45a-4484-b6e2-aaed70cdac61
(hbnb)
```

## Authors:

* **Tarek Mahmoud** - [Linkedin](https://www.linkedin.com/in/tarek-m-moustafa/)
