# NEO4J Notebook

## SYNTAX

| Symbol  | Description              | Usage                                                |
| --------  | ------------------       | -----------                                            |
| ()        | Node                     | `(person1)`                                            |
| :         | Variable-label separator | `(person1:John)` <br> `(:John)`  # label-only <br> `(person1)`   # variable-only <br> `-[relationship1:KNOWS]->` <br>  `-[:KNOWS]->`  # label-only <br> `-[relationship1]->`  # variable-only                         |
| -[]-      | Undirected relationship  | `(person1)-[relationship1:KNOWS]-(person2)`            |
| -[]-> <br> <-[]-  | Directed relationship    | `(person1)-[relationship1:KNOWS]->(person2)`   |
| {}        | Property                 | `CREATE (person1:John {age: 32, height: 182})` <br> `MATCH (s)-[{since:2010}]->(o)`       |
| .         | Property call prefix     | `RETURN person1.age, person1.height`                   |
| ""        | String                   | `WHERE person1.name = "John"`                          |

### Comparison and Logic operators

Comparison operators:

| Operator   | Description                   | Usage                      |
| ---------- | ------------------            | ---------------------------   |
| =          | Equal to                      | `WHERE person1.name > 'John'` |
| <>         | Not equal to                  | `WHERE person1 <> person2`    |
| > <br> <   | Greater/less than             | `WHERE person1.age > 30` <br> `number = 15 OR (number > 20 AND number < 10)`     |
| >= <br> <= | Greater/less than or equal to | `WHERE person1.age >= 30`     |
| IS NULL <br> IS NOT NULL | - | ``                            |
| CONTAINS | String-specific | `WHERE candidate CONTAINS 'Jane'`                            |
| STARTS WITH | String-specific | `WHERE candidate STARTS WITH 'Ja'`                            |
| ENDS WITH | String-specific | `WHERE candidate ENDS WITH 'ne'`                            |l

Boolean operators:

| Operator | Description        | Example                       |
| -------- | ------------------ | ---------------------------   |
| AND       | -                 | `WHERE person.name = "John" AND person.from = "Netherlands"`   |
| OR        | -                | `WHERE number = 4 OR (number > 6 AND number < 10)`                              |
| XOR        | -                | `WHERE number = 4 OR (number > 6 AND number < 10)`                              |
| NOT        | -                | `WHERE number = 4 OR (number > 6 AND number < 10)`                              |

## COMMANDS

### General
| Command  | Description               | Usage                    |
| -------- | ------------------        | --------------------------- |
| :help    |                           | `:help` <br> `:help create` |
| :clear   | Clears the output stream  |                             |

## QUERY CLAUSES, OPERATORS, AND FUNCTIONS

### Query Clauses

| Clause  | Description        | Usage |
| -------- | ------------------ | -------- |
| CREATE   | Creates data | `CREATE (node1:Person {name: "John", from: "Netherlands"}),` <br> `(node2:Person {name: "Jane", pet: "Cat"}),` <br> `(node1)-[:KNOWS {since: 2001}]->(node2)` |
| MATCH    | Specifies a pattern of nodes or relationships | `MATCH (:Person)--(:Pet)` <br>  `MATCH (node1:Person)-[relationship1:HAS_PET]->(node2:Pet)` |
| WHERE    | Constrains the results | `WHERE person.name = "John" AND person.from = "Netherlands"` |
| RETURN   | Requests particular results | `RETURN person.name, person.from, type(person)` |
| DISTINCT | Omits repeating values from results | `RETURN DISTINCT person.name, person.from` |
| WITH     | Assigns variable to another variable | `WITH person as p` |
| LIMIT    | Limits the number of results returned | `RETURN s,o LIMIT 10` |
| PROFILE <br> EXPLAIN  | Explains how the results are reached (added before query) | `PROFILE MATCH (s)--(o) RETURN s,o` <br> `EXPLAIN MATCH (s)--(o) RETURN s,o`        |
| DELETE    | Removes a pattern from data | `MATCH ()-[r:ACTED_WITH]->() DELETE r` |

### Query Operators and Special Characters
| Operator          | Description        | Usage |
| ----------------  | ------------------ | -------- |
| *  | Any | `MATCH p=shortestPath( (john:Person {name:"John Smith"})-[*]-(lincoln:Person {name:"Abraham Lincoln"}) ) RETURN p` |
| *N  <br> *N1..N2  | Connections from N1th degree to N2th degree | `MATCH (john:Person {name:"John"})-[*1..2]-(n) RETURN DISTINCT john, n` # Return all nodes that are up to 2 hops away from john |
| \|       | Or                 | `-[:myLabel1|:myLabel2]->`   |

### Query Functions
| Function          | Description        | Usage |
| ----------------  | ------------------ | -------- |
| shortestPath()    | Outputs shortest path between nodes | `MATCH p=shortestPath( (john:Person {name:"John Smith"})-[*]-(lincoln:Person {name:"Abraham Lincoln"}) ) RETURN p` |

### Neo4j Data Model (Subject -Relationship-> Object, and Properties for all)

`s`: subject, `r`: relationship, `o`: object, `pN`: property, `vN`: value:

    CREATE (s {p1: v1}) -[:r {p2: v2}]-> (o {p3:v3})

`Type(p)` is equal to `r`. `s`, `o`, and `r` has all their properties. `p` refers to all properties of `r`:

    MATCH (s)-[p]-(o)
    RETURN s, Type(p), o, s.propery1, p, o.property2

### 'CREATE' Keyword


### MATCH Keyword

General syntax for MATCH-WHERE-RETURN:

    MATCH (node1:Label1)-[relationship1:Label1]->(node2:Label2)
    WHERE relationship1.property1 > {value1}
    RETURN relationship1.property1, type(relationship1)

Match specific node:

    MATCH (person1:John)

Match any relationships

    MATCH (person1:John)--(person2:Jane)  # any relationship
    MATCH (person1:John)-->(person2:Jane)  # any relationship in one direction

Match specific relationships

    MATCH (person1:John)-[:KNOWS]-(person2:Jane) # both directions
    MATCH (person1:John)-[:KNOWS]->(person2:Jane)  # one directional


### WHERE Keyword

Constrain with a property value:

    MATCH (person1:John)-->(person2)
    WHERE person2.from = "US"

WHERE keyword can be omitted from many queries:

    # This query...:
    MATCH (person1:John)-->(person2)
    WHERE person2.from = "US"

    # ...can also be written as:
    MATCH (person1:John)-->(person2 {from: "US"})

But WHERE keyword is still needed for creating complex constraints:

    MATCH (eightiesMovie:Movie)
    WHERE eightiesMovie.released >= 1980 AND eightiesMovie.released <= 1990
    RETURN eightiesMovie.title

### RETURN Keyword
    
### Complex Pattern Matching

Extended social network of a user:

    MATCH (user)-[:KNOWS]-(friend)-[:KNOWS]-(friendOfAFriend)

	# 'friend' can also be just ignored
    MATCH (user)-[:KNOWS]-()-[:KNOWS]-(friendOfAFriend) 

Users who bought this also bought:

	MATCH (user)-[:PURCHASED]->(product)<-[:PURCHASED]-()-[:PURCHASED]->(otherProduct)

## PROCEDURES

### Importing Data 

## Csv
https://neo4j.com/blog/importing-data-neo4j-via-csv/
