# {{TABLE NAME}} Model and Repository Classes Design Recipe

_Copy this recipe template to design and implement Model and Repository classes for a database table._

## 1. Design and create the Table

If the table is already created in the database, you can skip this step.

Otherwise, [follow this recipe to design and create the SQL schema for your table](./single_table_design_recipe_template.md).

*In this template, we'll use an example table `users`*

```
# EXAMPLE

Table: users

Columns:
id | name | cohort_name
```

## 2. Create Test SQL seeds

Your tests will depend on data stored in PostgreSQL to run.

If seed data is provided (or you already created it), you can skip this step.

```sql
-- EXAMPLE
-- (file: spec/seeds_{table_name}.sql)

-- Write your SQL seed here. 

-- First, you'd need to truncate the table - this is so our table is emptied between each test run,
-- so we can start with a fresh state.
-- (RESTART IDENTITY resets the primary key)

TRUNCATE TABLE users RESTART IDENTITY; -- replace with your own table name.

-- Below this line there should only be `INSERT` statements.
-- Replace these statements with your own seed data.

INSERT INTO users (name, cohort_name) VALUES ('David', 'April 2022');
INSERT INTO users (name, cohort_name) VALUES ('Anna', 'May 2022');
```

Run this SQL file on the database to truncate (empty) the table, and insert the seed data. Be mindful of the fact any existing records in the table will be deleted.

```bash
psql -h 127.0.0.1 your_database_name < seeds_{table_name}.sql
```

## 3. Define the class names

Usually, the Model class name will be the capitalised table name (single instead of plural). The same name is then suffixed by `Repository` for the Repository class name.

```python
# EXAMPLE
# Table name: users

# Model class
# (in lib/user
#.py)
class User


# Repository class
# (in lib/user
#_repository.py)
class UserRepository

```
# Model class
# (in lib/user.py)
class Peep


# Repository class
# (in lib/user_repository.py)
class PeepRepository

## 4. Implement the Model class

Define the attributes of your Model class. You can usually map the table columns to the attributes of the class, including primary and foreign keys.

```python
# EXAMPLE
# Table name: users

# Model class
# (in lib/user
#.py)

class User:
    def __init__(self):
        self.id = 0
        self.name = ""
        self.password = ""

        # Replace the attributes by your own columns.


class Peep:
    def __init__(self):
        self.id = 0
        self.title = ""
        self.content = ""
        self.time = ""
```

*You may choose to test-drive this class, but unless it contains any more logic than the example above, it is probably not needed.*

## 5. Define the Repository Class interface

Your Repository class will need to implement methods for each "read" or "write" operation you'd like to run against the database.

Using comments, define the method signatures (arguments and return value) and what they do - write up the SQL queries that will be used by each method.

```python
# EXAMPLE
# Table name: users

# Repository class
# (in lib/user
#_repository.py)

class UserRepository():

    # Selecting all records
    # No arguments
    def all():
        # Executes the SQL query:
        # SELECT id, name, cohort_name FROM users;

        # Returns an array of user
        # objects.

        # Gets a single record by its ID
        # One argument: the id (number)
    def find(id):
        # Executes the SQL query:
        # SELECT id, name, cohort_name FROM users WHERE id = $1;

        # Returns a single user
        # object.

        # Add more methods below for each operation you'd like to implement.

    def create(user):

    #)
    # 

    # def update(user
    #)
    # 

    # def delete(user
    #)
    # 


class PeepRepository():

    def all():
    #in reverse chronological order

    def create():

    def 
 
,,,
    
## 6. Write Test Examples

Write Python code that defines the expected behaviour of the Repository class, following your design from the table written in step 5.

These examples will later be encoded as Pytest tests.

```python
# EXAMPLES

# 1
# Get all users

repo = UserRepository()

users = repo.all()

len(users) # =>  2

users[0].id # =>  1
users[0].name # =>  'John Doe'
users[0].password # =>  'pass123'

users[1].id # =>  2
users[1].name # =>  'Jane Smith'
users[1].password # =>  'password12'

# 2
# Get a single user

repo = userRepository()

user = repo.find(1)

user.id # =>  1
user.name # =>  'John Doe'
user.password # =>  'pass123'

# Add more examples for each method

repo = PeepRepository()

peeps = repo.all()

len(peeps) # =>  2

peeps[0].id # =>  1
peeps[0].title # =>  'John Doe'
peeps[0].content # =>  'pass123'
peeps[0].time 

peeps[1].id # =>  2
peeps[1].title # =>  'Jane Smith'
peeps[1].content # =>  'password12'
peeps[1].time 
# 2
# Get a single user

repo = PeepRepository()

peep = repo.find(1)

peep.id # =>  1
peep.title # =>  'John Doe'
peep.content # =>  'pass123'

```

Encode this example as a test.

User:
def test_user_variables():
    user = User(1, test username, test password)
    

## 7. Test-drive and implement the Repository class behaviour

_After each test you write, follow the test-driving process of red, green, refactor to implement the behaviour._

<!-- BEGIN GENERATED SECTION DO NOT EDIT -->

---

**How was this resource?**  
[😫](https://airtable.com/shrUJ3t7KLMqVRFKR?prefill_Repository=makersacademy%2Fdatabases-in-python&prefill_File=resources%2Frepository_class_recipe_template.md&prefill_Sentiment=😫) [😕](https://airtable.com/shrUJ3t7KLMqVRFKR?prefill_Repository=makersacademy%2Fdatabases-in-python&prefill_File=resources%2Frepository_class_recipe_template.md&prefill_Sentiment=😕) [😐](https://airtable.com/shrUJ3t7KLMqVRFKR?prefill_Repository=makersacademy%2Fdatabases-in-python&prefill_File=resources%2Frepository_class_recipe_template.md&prefill_Sentiment=😐) [🙂](https://airtable.com/shrUJ3t7KLMqVRFKR?prefill_Repository=makersacademy%2Fdatabases-in-python&prefill_File=resources%2Frepository_class_recipe_template.md&prefill_Sentiment=🙂) [😀](https://airtable.com/shrUJ3t7KLMqVRFKR?prefill_Repository=makersacademy%2Fdatabases-in-python&prefill_File=resources%2Frepository_class_recipe_template.md&prefill_Sentiment=😀)  
Click an emoji to tell us.

<!-- END GENERATED SECTION DO NOT EDIT -->