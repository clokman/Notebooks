#  NEO4J/Cypher GLOSSARY OF USAGE SCENARIOS
This reference sheet is a collection of examples that are representative of various usage scenarios of each listed keyword.

## USEFUL RESOURCES
- [Cypher reference card](https://neo4j.com/docs/cypher-refcard/current/)
- [Cypher manual](https://neo4j.com/docs/developer-manual/current/)

## DATA MODEL

Data model of Neo4j:

    (Subject:LABEL {Property:Value} ) -[Relationship:LABEL {Property: Value}]-> (Object{Property: Value})

More succinctly, and with an example clause: `s`=subject, `r`=relationship, `o`=object, `pN`=property, `vN`=value:

    CREATE (s {p1: v1}) -[:r {p2: v2}]-> (o {p3:v3})

General syntax for MATCH-WHERE-RETURN:

    MATCH (node1:Label1)-[relationship1:Label1]->(node2:Label2)
    WHERE relationship1.property1 > {value1}
    RETURN relationship1.property1, type(relationship1)

## SYNTAX

| Symbol  | Description & links        | Usage examples                                                |
| --------  | ------------------       | -----------                                            |
| ()        | Node                     | `(person1)`                                            |
| :         | Variable-label separator | `(person1:John)` <br> `(:John)`  # label-only <br> `(person1)`   # variable-only <br> `-[relationship1:KNOWS]->` <br>  `-[:KNOWS]->`  # label-only <br> `-[relationship1]->`  # variable-only   <br> `RETURN labels(n) AS labels` # return all labels of  a node                      |
| -[]-      | Undirected relationship  | `(person1)-[relationship1:KNOWS]-(person2)`            |
| -[]-> <br> <-[]-  | Directed relationship    | `(person1)-[relationship1:KNOWS]->(person2)`   |
| {}        | Property                 | `CREATE (person1:John {age: 32, height: 182})` <br> `MATCH (s)-[{since:2010}]->(o)` <br> `WHERE (n)-[:KNOWS]-({ name: 'Jane' })`  <br><br> `MATCH (n)-[r:KNOWS]->(n2) WHERE r.since < 2000 RETURN n2.name`   |
| .         | Property call prefix     | `RETURN person1.age, person1.height`                   |
| ""        | String                   | `WHERE person1.name = "John"`                          |

## OPERATORS

Comparison operators:

| Operator   | Description & links           | Usage examples                      |
| ---------- | ------------------            | ---------------------------   |
| =          | Equal to                      | `WHERE person1.name > 'John'` |
| <>         | Not equal to                  | `WHERE person1 <> person2`    |
| > <br> <   | Greater/less than             | `WHERE person1.age > 30` <br> `number = 15 OR (number > 20 AND number < 10)`     |
| >= <br> <= | Greater/less than or equal to | `WHERE person1.age >= 30`     |
| IS NULL <br> IS NOT NULL | - | ``                            |
| CONTAINS | String-specific | `WHERE candidate CONTAINS 'Jane'`                            |
| STARTS WITH | String-specific | `WHERE candidate STARTS WITH 'Ja'`                            |
| ENDS WITH | String-specific | `WHERE candidate ENDS WITH 'ne'`                            |
| =~ | Regex (string-specific) See [Java regex](https://docs.oracle.com/javase/7/docs/api/java/util/regex/Pattern.html) for regex syntax | `WHERE n.name =~ 'http.*'` # This is a dot with special meaning of 'any character', and '*' means 'all following' <br> `WHERE n.email =~ '.*\\.org'` # Escapes in regex is done with double backslash <br> `WHERE n.name =~ '(?i)jane.*'` # '?i' makes the whole expresion case-insensitive|

Boolean operators:

| Operator | Description & links     | Usage examples                       |
| -------- | ------------------      | ----------------------------------   |
| AND       | -                 | `WHERE person.name = "John" AND person.from = "Netherlands"`   |
| OR        | -                | `WHERE number = 4 OR (number > 6 AND number < 10)`                              |
| XOR        | -                | `WHERE number = 4 XOR (number > 6 AND number < 10)`                              |
| NOT        | -                | `WHERE NOT number = 4 OR NOT (number > 6 AND number < 10)` <br> `WHERE NOT (persons)-->(jane)` |

Query operators and special characters:

| Operator          | Description & links           | Usage examples |
| ----------------  | ------------------ | -------- |
| \|       | Or                 | `MATCH (n1)-[:myLabel1|:myLabel2]->(n2)`   |
| *  | Any | `MATCH p=shortestPath( (john:Person {name:"John Smith"})-[*]-(lincoln:Person {name:"Abraham Lincoln"}) ) RETURN p` |
| *N  <br> *N1..N2  | Connections from N1th degree to N2th degree | `MATCH (john:Person {name:"John"})-[*1..2]-(n) RETURN DISTINCT john, n` # Return all nodes that are up to 2 hops away from john |

## NEO4J COMMANDS

General

| Command  | Description & links       | Usage examples                    |
| -------- | ------------------        | --------------------------- |
| :help    |                           | `:help` <br> `:help create` |
| :clear   | Clears the output stream  |                             |

## CLAUSES

| Clause   | Description & links           | Usage examples |
| -------- | ------------------ | -------- |
| CREATE   | Creates data | `CREATE (node1:Person {name: "John", from: "Netherlands"}),` <br> `(node2:Person {name: "Jane", pet: "Cat"}),` <br> `(node1)-[:KNOWS {since: 2001}]->(node2)` <br><br> `CREATE (swbook:Book { title: 'A Semantic Web Primer',                    authors: ['Antoniou, G', 'Harmelen, F'] })`|
| MERGE   | Creates data where absent, merges with existing data in case of already existing entities | `MERGE (jane:Person {name:"Jane"})` <br><br> `FOREACH (namesList in ["John","Bob"] | MERGE (jane)-[:KNOWS]->(:Person {name:namesList}))` <br><br> `LOAD CSV WITH HEADERS FROM "file:///directory/file.csv" AS each_row MERGE (u:Person { name: each_row.name, email: each_row.email });` # direct enrichment from file |
| LOAD   | Retrieves and parses data from a specified source. All fields are parsed as string. | `LOAD CSV WITH HEADERS FROM  http://data.neo4j.com/northwind/products.csv" AS each_row CREATE (n) SET n = each_row RETURN n` # simple load <br><br> `LOAD CSV WITH HEADERS FROM http://data.neo4j.com/northwind/products.csv" AS each_row CREATE (n:Product) SET n = each_row, n.unitPrice = toFloat(each_row.unitPrice)` # complex load <br><br> `LOAD CSV WITH HEADERS FROM "file:///directory/file.csv" AS each_row FIELDTERMINATOR ';' MERGE (u:Person { name: each_row.name, email: each_row.email });` # direct enrichment from file using custom delimiter <br><br> `LOAD CSV FROM  "http://data.neo4j.com/examples/person.csv" AS eachLine MERGE (n:Person {id: toInteger  eachLine[0])}) SET n.name = eachLine[1] RETURN n` # Use header index position in the file to assign properties (instead of using headers) |
| SET   | Updates properties and labels. Can also be used to copy variables (only works with maps) | `MATCH (jane { name: 'Jane Smith' }) SET jane:Person:Female`  # set (multiple) labels <br><br> `MATCH (jane { name: 'Jane Smith' }) SET jane.country = 'US', jane.height = 180`  # set properies <br><br> `MATCH (jane { name: 'Jane Smith', age: 28 }) SET jane.age = NULL`  # remove property <br><br> `MATCH (jane { name: 'Jane Smith' }) SET jane += { hungry: FALSE , position: 'Programmer' }`  # '+=' style of adding properties <br><br> `LOAD CSV WITH HEADERS FROM http://data.neo4j.com/northwind/products.csv" AS each_row CREATE (n:Product) SET n = each_row, n.unitPrice = toFloat(each_row.unitPrice), n.discontinued = (row.discontinued <> "0")`  # Copy each_row to n variable, and make transformations. The last n.discontinued = (row.discontinued <> "0") part sets "0" and "1" strings to TRUE and FALSE by first evaluating the contents of the parentheses, and then setting the n.discountinued to the result of this evaluation. |
| REMOVE    | Removes properties or labels graph elements | `MATCH (jane { name: 'Jane Smith' }) REMOVE jane.age` # remove property <br><br> `MATCH (n { name: 'Jane Smith' }) REMOVE n:Female:Programmer` # remove (multiple) labels |
| DELETE    | Removes nodes, relationships, or paths from data | `MATCH (n) DETACH DELETE n` # delete all <br> `MATCH ()-[r:ACTED_WITH]->() DELETE r` # delete all instances of a specificic relationship |
| MATCH    | Specifies a pattern of nodes or relationships | `MATCH (n) RETURN n` # return everything <br> `MATCH (per:Person),(pet:Pet)` <br> `MATCH (:Person)--(:Pet)`  # any relationship  <br> `MATCH (node1:Person)-[relationship1:HAS_PET]->(node2:Pet)` <br> `MATCH (supp:Supplier)-->(prod:Product)-->(cat:Category)` # complex inter-node pattern regardless of relationship type <br> `MATCH (node1:Person)-[:KNOWS]-(node2:Person)` # any direction <br> `MATCH (s)-[{since:2010}]->(o)` |
| OPTIONAL MATCH    | Specify the patterns to search for in the database while using nulls for missing parts of the pattern. | `MATCH (mr:Movie { title: 'Moulin Rouge' }) OPTIONAL MATCH (mr)-->(x) RETURN x, x.name` <br><br> `OPTIONAL MATCH (jane)-[r:KNOWS]->()` |
| WHERE    | Constrains/filters the results. Conceptually similar to and 'if' statement. | `MATCH (n) WHERE n:Dutch RETURN n.name` # filter on label <br><br> `WHERE person.name = "John" AND person.from = "Netherlands"` # filter on property <br> `WHERE NOT (persons)-->(jane)` # filter on relationship <br> `WHERE (n)-[:KNOWS]-({ name: 'Jane' })` # filter on relationship and property <br><br> `MATCH (john { name: 'John' }), (targets) WHERE targets.name IN ['Jane', 'Bob'] AND (john)<--(targets) RETURN targets.name,targets.age` # complex filtering <br><br> WHERE keyword can be omitted from many queries: <br> # This query...: <br> `MATCH (person1:John)-->(person2) WHERE person2.from = "US"` <br> # ...can also be written as: <br> `MATCH (person1:John)-->(person2 {from: "US"})` <br><br> But WHERE keyword is still needed for creating complex constraints: <br> `MATCH (eightiesMovie:Movie) WHERE eightiesMovie.released >= 1980 AND eightiesMovie.released <= 1990 RETURN eightiesMovie.title` |
| RETURN <br><br> [DISTINCT] [AS]  | Requests particular results | `RETURN person.name, person.from, type(person)` <br> `RETURN labels(n) AS labels` # return all labels of  a node <br> `RETURN DISTINCT persons` |
| DISTINCT | Omits repeating values from results. <br><br> Important note: DISTINCT is essentially an aggregation operation, and when it is used, any integer and float variables that are set to return must also be aggregated. (See the example in the right column.) | `RETURN DISTINCT person.name, person.from` <br><br> Example: 'DISTINCT is aggregation': <br>`MATCH (per:Person)-[:ORDERED]->(:Shipment)-[ord:CONTAINS]->(item:Item) RETURN DISTINCT per.name, SUM(ord.quantity) AS TotalProductsOrdered` # If what is returned was not `SUM(ord.quantity)` but was only `ord.quantity`, then the query would return only one of the order quantitities, instead of a sum of order quantities per each person!  |
| WITH  ... [AS]  | Allows manipulation of the output before it is passed on to the following query parts | `WITH person as p` <br><br> `MATCH (jane { name: 'Jane' })--(otherPerson)-->() WITH otherPerson, count(*) AS foaf WHERE foaf > 1 RETURN otherPerson.name` # make a cutoff <br><br> `MATCH (n) WITH n ORDER BY n.name DESC LIMIT 5 RETURN collect(n.name)` # order results|
| IN       | Checks if an element exists in a list | `MATCH (john { name: 'John' }), (targets) WHERE targets.name IN ['Jane', 'Bob'] AND (john)<--(targets) RETURN targets.name,targets.age` |
| FOREACH       | Iterates over a list. '\|' character must be used after FOREACH clause. | `FOREACH (eachName in ["John","Bob"] | MERGE (jane)-[:KNOWS]->(:Person {name:eachName}))` # iterate over a list <br><br>  `MATCH p = (begin)-[*]->(end) WHERE begin.name = 'A' AND end.name = 'D' FOREACH (n IN nodes(p)| SET n.marked = TRUE )` # iterate over a subset of nodes |
| LIMIT    | Limits the number of results returned | `RETURN s,o LIMIT 10` |
| INDEX  | Indexes the provided graph elements. ([Docs](https://neo4j.com/docs/developer-manual/current/cypher/schema/index/)) | `CREATE INDEX ON :Product(id)` # index single property <br> `CREATE INDEX ON :Product(id, name)` # multiple property index (composite) <br> `CALL db.indexes` # list all indexes      |
| PROFILE <br> EXPLAIN  | Explains how the results are reached (added before query) | `PROFILE MATCH (s)--(o) RETURN s,o` <br> `EXPLAIN MATCH (s)--(o) RETURN s,o`        |

## FUNCTIONS

| Function          | Description & links           | Usage examples |
| ----------------  | ------------------ | -------- |
| nodes()    | Lists nodes in a variable | `MATCH p =(begin)-[*]->(end) WHERE begin.name = 'A' AND end.name = 'D' FOREACH (n IN nodes(p)| SET n.marked = TRUE )` |
| relationships()   | Lists relationships in a variable | `MATCH v =(n1)-->(r)-->(n2) WHERE n1.name = 'Jane' AND n2.name = 'Bob' RETURN relationships(v)` |
| labels()   | Lists all labels | `MATCH (n) RETURN n, labels(n)` <br><br> `MATCH (s)-[p]-(o) RETURN Type(p)` # alternative way to get labels using Type() |
| properties()   | Lists all properties | `MATCH (n) RETURN n, properties(n)` |
| Type()   | Get type of variable | `MATCH (s)-[p]-(o) RETURN Type(p)` |
| toString() <br> toInteger() <br> toFloat() <br> toBoolean() <br>  | Convert to type | `MATCH (supplier:Supplier) SET supplier.supplierID = toInteger(supplier.supplierID)` |
| collect() <br> collect(DISTINCT)    | Collects specified values and stores them as a list | `MATCH  (prod:Product) RETURN collect(prod.price)` # returns: `[12,53,57]` # directly using `RETURN prod.price` would have returned `12, 53, 57` as separate rows, not as a list <br><br> `MATCH  (prod:Product) RETURN prod.name, collect(DISTINCT prod.ingredients) AS ingredients`  # group all unique ingredients as a list and return them as one row |
| exists()    | Checks if the given pattern is in data | `WHERE exists(n.property)` |
| shortestPath()    | Outputs shortest path between nodes | `MATCH p=shortestPath( (john:Person {name:"John Smith"})-[*]-(lincoln:Person {name:"Abraham Lincoln"}) ) RETURN p` |
| count()    | Counts number of occurrences | `MATCH (jane { name: 'Jane' })--(otherPerson)-->() WITH otherPerson, count(*) AS foaf WHERE foaf > 1 RETURN otherPerson.name` |

# NOTES

## INDEXING
In Neoj, nodes and relationships are indexed automatically, but not properties. Properties must be indexed manually by using INDEX keyword. Index should be kept as small as possible for performance concerns.

The properties that are indexed often are identifiers for each dataset imported (e.g., orderID, customerID, articleID, etc), so that efficient matching can be made between their entities (e.g., while creating relationships between nodes created from two distinct datasets).

# PROCEDURES AND SCENARIOS

## INTERESTING EXAMPLE QUERIES

Extended social network of a user:

    MATCH (user)-[:KNOWS]-(friend)-[:KNOWS]-(friendOfAFriend)

	# 'friend' can also be just ignored
    MATCH (user)-[:KNOWS]-()-[:KNOWS]-(friendOfAFriend) 

Users who bought this also bought:

	MATCH (user)-[:PURCHASED]->(product)<-[:PURCHASED]-()-[:PURCHASED]->(otherProduct)

## DATA IMPORT

Useful resources:

- [Neo4J importing guide](https://neo4j.com/developer/guide-importing-data-and-etl/)
- [Importing data via CSV](https://neo4j.com/blog/importing-data-neo4j-via-csv/)

## Link two imported datasets by a shared ID column

CategoryID exists in both category and product nodes. Pair nodes in each group based on this:

    MATCH (part:Part),(functionCategory:Function_Category)
    WHERE part.functionID = functionCategory.functionID
    CREATE (part)-[:HAS_FUNCTION]->(functionCategory)

## Use a join dataset to create relationships

(...and add relationship properties)

    LOAD CSV WITH HEADERS FROM "http://data.example.com/shipment-details.csv" AS eachRow
    MATCH (item:Item), (shi:Shipment)
    WHERE item.itemID = eachRow.itemID AND shi.shipmentID = eachRow.shipmentID // match ids
    CREATE (shi)-[shipmentDetails:CONTAINS]->(item)  // add csv cells as relationship properties 
    SET shipmentDetails = eachRow