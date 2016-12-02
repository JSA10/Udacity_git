

select animals.name, animals.species, diet.food
       from animals join diet
       on animals.species = diet.species;


QUERY = '''
select name, birthdate from animals
      where (not species = 'gorilla') and (not name = 'Max');
'''
select name, birthdate from animals
      where not(species = 'gorilla' or name = 'Max');

Can also do:
select name, birthdate from animals
      where species != 'gorilla' and name != 'Max';

# Find all the llamas born between January 1, 1995 and December 31, 1998.
# Fill in the 'where' clause in this query.

QUERY = '''
select name from animals where
    species = 'llama' and
    birthdate >= '1995-1-1' and
    birthdate <= '1998-12-31';
'''

The One Thing SQL Is Terrible At  == displaying existing names of tables and columns.
Hampered by being built in 80s when direct interaction with programmes wasn't common and needed to structured using flow diagrams


And here are the SQL commands that were used to create those tables.
We won't cover the create table command until lesson 4, but it may be interesting to look at:

 create table animals (
        name text,
        species text,
        birthdate date);

 create table diet (
        species text,
        food text);

 create table taxonomy (
        name text,
        species text,
        genus text,
        family text,
        t_order text);

 create table ordernames (
        t_order text,
        name text);

 ***Remember: In SQL, we always put string and date values inside single quotes.***


 # Uncomment one of these QUERY variables at a time and use "Test Run" to run it.
 # You'll see the results below.  Then try your own queries as well!
 #

 QUERY = "select max(name) from animals;"

 QUERY = "select * from animals limit 10;"

 QUERY = "select * from animals where species = 'orangutan' order by birthdate;"

 QUERY = "select name from animals where species = 'orangutan' order by birthdate desc;"

 QUERY = "select name, birthdate from animals order by name limit 10 offset 20;"

 QUERY = "select species, min(birthdate) from animals group by species;"

 QUERY = '''
 select name, count(*) as num from animals
     group by name
     order by num desc
     limit 5;
 '''

 QUERY = "select * from animals"

 QUERY = "select * from animals where species = 'gorilla';"


 Quiz: Select Clauses
 Here are the new select clauses introduced in the previous video:

 ... limit count
 Return just the first count rows of the result table.

 ... limit count offset skip
 Return count rows starting after the first skip rows.

 ... order by columns
 ... order by columns desc
 Sort the rows using the columns (one or more, separated by commas) as the sort key. Numerical columns will be sorted in numerical order; string columns in alphabetical order. With desc, the order is reversed (desc-ending order).

 ... group by columns
 Change the behavior of aggregations such as max, count, and sum. With group by, the aggregation will return one row for each distinct value in columns.

 QUERY = ''' select species, count(*) as num from animals
                  group by species
                  order by num desc'''


  #
  # Insert a newborn baby opossum into the animals table and verify that it's been added.
  # To do this, fill in the rest of SELECT_QUERY and INSERT_QUERY.
  #
  # SELECT_QUERY should find the names and birthdates of all opossums.
  #
  # INSERT_QUERY should add a new opossum to the table, whose birthdate is today.
  # (Or you can choose any other date you like.)
  #
  # The animals table has columns (name, species, birthdate) for each individual.
  #

  SELECT_QUERY = "select name, birthdate from animals where species = 'opossum';"

  INSERT_QUERY = "insert into animals values ('Rohan', 'opossum','2015-10-10');"

Could also explicitly mention the column names to insert into, however if new data is in right order
and covers all columns (starting at 1), then don't need to explicitly mention col names.

ALTERNATE_INSERT_QUERY = "insert into animals(name, species, birthdate) values ('Rohan', 'opossum','2015-10-10');"

#Insert queries much simpler than select, they only work on one table at a time and just add rows to tables



# Find the names of the individual animals that eat fish.
#
# The animals table has columns (name, species, birthdate) for each individual.
# The diet table has columns (species, food) for each food that a species eats.

QUERY = '''
select animals.name
    from animals,diet
    where animals.species = diet.species and diet.food = 'fish'
'''
#above is example of a simplified join, selecting names from one table based on a criteria in another
#could also do:

QUERY = '''
    select animals.name
    from animals join diet
    on animals.species = diet.species and diet.food = 'fish'
'''


After aggregating

Be careful with 'where', which runs before the rest of the query and is a restriction on the source tables

'having' is an alternative conditional statement that runs after the query and applies it's restriction on
the result after aggregation

QUERY = '''
select diet.food, count(*) as num
    from animals,diet
    where animals.species = diet.species
    group by diet.food
    having num = 1
'''
#could drop the diet. from last statement
The having clause works like the where clause, but it applies after group by
aggregations take place. The syntax is like this:

select columns from tables group by column having condition ;

Usually, at least one of the columns will be an aggregate function such as count,
max, or sum on one of the tables' columns. In order to apply having to an aggregated column,
you'll want to give it a name using as.

For more on having: http://www.postgresql.org/docs/9.4/static/sql-select.html#SQL-HAVING



#
# List all the taxonomic orders, using their common names, sorted by the number of
# animals of that order that the zoo has.
#
# The animals table has (name, species, birthdate) for each individual.
# The taxonomy table has (name, species, genus, family, t_order) for each species.
# The ordernames table has (t_order, name) for each order.
#
# Be careful:  Each of these tables has a column "name", but they don't have the
# same meaning!  animals.name is an animal's individual name.  taxonomy.name is
# a species' common name (like 'brown bear').  And ordernames.name is the common
# name of an order (like 'Carnivores').

#PROBLEM SOLVING
#inputs three tables, animals, taxonomy and ordernames
#output common names for taxonomic orders, sorted by no of animals in that order

QUERY = '''
select ordernames.name, count(*) as num
    from animals,taxonomy,ordernames
    where animals.species = taxonomy.name and
        taxonomy.t_order = ordernames.t_order
    group by ordernames.name
    order by num Desc
'''

And here's another, this time using the explicit join style:

###***not as nice - stick to simplified version above***

select ordernames.name, count(*) as num
  from (animals join taxonomy
                on animals.species = taxonomy.name)
                as ani_tax
        join ordernames
             on ani_tax.t_order = ordernames.t_order
  group by ordernames.name
  order by num desc

"""I think the upper version is much more readable than the lower one, because in
the explicit join style you have to explicitly tell the database what order to join
the tables in — ((a join b) join c) — instead of just letting the database worry
about that. ***NOTE: If you're using a more barebones database (like SQLite) there can be a
performance benefit to the explicit join style. But in PostgreSQL, the more
server-oriented database system we'll be using next lesson, the query planner should
optimize away any difference.***"""


*** Python DB-API ***
--> Using python code to connect to SQL database and query using embedded SQL code


# To see how the various functions in the DB-API work, take a look at this code,
# then the results that it prints when you press "Test Run".
#
# Then modify this code so that the student records are fetched in sorted order
# by student's name.
#

import sqlite3

# Fetch some student records from the database.
db = sqlite3.connect("students")
c = db.cursor()
query = "select name, id from students order by name;"
c.execute(query)
rows = c.fetchall()

# First, what data structure did we get?
print "Row data:"
print rows

# And let's loop over it too:
print
print "Student names:"
for row in rows:
  print "  ", row[0]

db.close()


## commit is needed to actually action the SQL query using DB-API. This is a
## safeguard against mistakes and inconsistent updating of multiple tables.
### each command is known as a transaction, that will 'roll-back' if process
### interrupted before commit statement.
# process called 'atomicity' = either a change happens as a whole, or not at all

# This code attempts to insert a new row into the database, but doesn't
# commit the insertion.  Add a commit call in the right place to make
# it work properly.
#

import sqlite3

db = sqlite3.connect("testdb")
c = db.cursor()
c.execute("insert into balloons values ('blue', 'water') ")
db.commit()
db.close()

"""
Before:
+-------+----------+
| color | contents |
+=======+==========+
|   red |      air |
| green |   helium |
+-------+----------+

After:
+-------+----------+
| color | contents |
+=======+==========+
|   red |      air |
| green |   helium |
|  blue |    water |
+-------+----------+
"""



### vagrant command line

vagrant up
vagrant ssh
cd /vagrant/forum
ls
python forum.py
ctrl-c #to break
exit

"""
Hello PostgreSQL
The psql command-line tool is really powerful. There's a complete reference to it in the PostgreSQL documentation.

To connect psql to a database running on the same machine (such as your VM), all you need to give it is the database name. For instance, the command psql forum will connect to the forum database.

From within psql, you can run any SQL statement using the tables in the connected database. Make sure to end SQL statements with a semicolon, which is not always required from Python.

You can also use a number of special psql commands to get information about the database and make configuration changes. The \d posts command shown in the video is one example — this displays the columns of the posts table.

Some other things you can do:

\dt — list all the tables in the database.

\dt+ — list tables plus additional information (notably, how big each table is on disk).

\H — switch between printing tables in plain text vs. HTML.
"""
