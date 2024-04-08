Explanation on NoSQL Wide-Column Store Model 

In this new era, the fast growth of technologies and cloud applications has changed the direction 
of data stored that containing transactions, social media information, online payments and 
researchers have developed the NoSQL model due to the relational database model scalability 
issues that introduces a unique and new data storage technique rather than the relational 
database model (Shehata & Abed , 2020). NoSQL is primarily concerned with query processing, 
and there are numerous implementations, technologies, and techniques for creating a NoSQL 
database system (Shehata & Abed , 2020). The main difference between NoSQL databases and 
SQL databases is how data is stored and authenticated. There are many varieties of NoSQL 
databases such as wide-column stores, document stores, and value stores, each of which has its 
own set of characteristics, and these three categories cover the majority of the techniques 
involved (Shehata & Abed , 2020). The data reading performance of Column Store is optimized. 
For the architecture of the NoSQL Wide-Column Store, the traditional business divide 
into online analytical processing (OLAP) and online transaction processing (OLTP) is justified 
by the different workloads in both systems (OLTP) (Viswanathan, Mishra, & Srividya, 2020). 
Whereas the online transaction processing (OLTP) applications are defined by complex read 
operations such as joins and large sample scans encompassing only a few columns but several 
database rows, online analytical processing (OLAP) applications are defined by complicated 
read processes such as joins and large longitudinal scans spanning only a few columns but a 
few database rows. Both 2 tasks are often handled by these different systems which are data 
warehousing systems, business intelligence (BI) systems and transaction processing systems 
(TPS) (Viswanathan, Mishra, & Srividya, 2020). 
The Wide Column Store refers to the fact that it stores data in columns compared to 
rows in a relational database due to the column being the smallest and lowest data manner’s 
instance (Shehata & Abed , 2020). It also saves several values that belong to the same column 
in a contiguous, compressed, and densely packed manner, unlike typical database systems that 
store main records as rows after each other in a continuous fashion. The columns are realized 
and decided in relevant to each row in a state initially defined by the table organization owned 
uniform-sized columns for each tuple in this type of NoSQL database. As a result, these stores 
establish a two-dimensional aggregate organization with a key and a row aggregate specified 
as a collection of columns (Shehata & Abed , 2020). This permits any column to be added to 
any row, and the rows in this example can have a lot of different columns. To put it another 
1 
way, each row has a variety of various columns that were kept and stored. It can also store data 
in tables such as data column segments (Shehata & Abed , 2020). 
In the nutshell, the primary goal of using a wide column store database is to achieve 
high performance in the operations of reading and writing data from and to stored data, as well 
as to speed up the process of returning query results (Shehata & Abed , 2020). The wide column 
store database has a wide range of applications, including CRM systems, data warehouses, and 
other inquiry systems (Shehata & Abed , 2020). Wide column store databases as well as in
memory features were introduced to bring about a shift in how we think about how data should 
be managed (Viswanathan, Mishra, & Srividya, 2020). Varied systems have different needs, 
but none can deny the numerous benefits that wide column store databases give. Since wide 
column store databases understand only the columns required by users' requests, they respond 
faster than row-oriented databases, which interpret all rows and columns in the list. A row
oriented strategy is the ideal answer for applications that write and update a lot of data in the 
OTLP systems. From the other side, OLAP systems are designed to perform significant 
dynamic querying on vast amounts of data, making wide column store databases a viable option 
(Shehata & Abed , 2020). In order to maintain the longevity game, the market is gravitating 
toward these new advancements. Eventually time will prove if wide column-store architecture 
may one day entirely dominate traditional designs due to technological improvement 
(Viswanathan, Mishra, & Srividya, 2020). 

CAP Theorem for Cassandra

![image](https://github.com/yeejing0822/-CassandraWide-ColumnStoreNoSQLDB/assets/86753374/acbe6ca5-b19d-4344-9bd3-2d4f0d3c0230)

In the CAP theorem, it is stated that it is impossible to provide all three of the following 
guarantees at the same time in a distributed system.  
• C = Consistency (Where all nodes see the same data simultaneously) 
• A = Availability (A guarantee where every request sent will receive a response about 
whether it was successful or failed) 
• P = Partition-tolerance (The system should continue to operate despite arbitrary 
message loss or failure in part of the system) 
According to the theorem, a distributed system cannot satisfy all three of these 
guarantees at the same time. 
Cassandra is usually known as an AP system which means that availability and 
partition-tolerance are more important than the consistency. But Cassandra can be tuned with 
replication factor and consistency level to also meet consistency. 

In the CAP theorem, it is stated that it is impossible to provide all three of the following 
guarantees at the same time in a distributed system.  
• C = Consistency (Where all nodes see the same data simultaneously) 
• A = Availability (A guarantee where every request sent will receive a response about 
whether it was successful or failed) 
• P = Partition-tolerance (The system should continue to operate despite arbitrary 
message loss or failure in part of the system) 
According to the theorem, a distributed system cannot satisfy all three of these 
guarantees at the same time. 
Cassandra is usually known as an AP system which means that availability and 
partition-tolerance are more important than the consistency. But Cassandra can be tuned with 
replication factor and consistency level to also meet consistency. 

![image](https://github.com/yeejing0822/-CassandraWide-ColumnStoreNoSQLDB/assets/86753374/c36bd5fc-f7fa-431e-a02b-2db2b8d399e4)

The main schemes for the concurrency control in NoSQL can be categorised into two 
parts: pessimistic concurrency control and optimistic concurrency control. Pessimistic 
concurrency control assumes that the same record will be updated concurrently at the same 
time. Therefore, pessimistic concurrency control reduces the possibility of the concurrency 
problem by locking the record to guarantee exclusive access to a single operation. For instance, 
readers-writer locks are implemented in MongoDB and BerkeleyDB so that only one user can 
modify the data while multiple users can access the data (Grolinger, Higashino, Tiwari, & 
Capretz , 2013). On the contrary, optimistic concurrency control checks the data at the end of 
the operation to see if any concurrent updates on the same record, instead of locking the record 
for a single modification. One of the optimistic concurrency control strategies that are 
employed in the NoSQL database models is multi-version concurrency control (MVCC).   
14 
According to Kanungo and Morena (2018), MVCC creates a new version with every 
transaction commit, instead of overwriting the old values. Therefore, it contains a list of 
different versions of the data with the values history and there is only one value marked as the 
current or newest value for usage. In other concurrency controls, a read would normally be 
rejected when the data value is being overwritten. However, MVCC avoids rejecting the 
operations that arrive too late by versioning the data value. Some examples of NoSQL database 
applications including Voldemort, HBase, NuoDB, CouchDB, Riak and Clustricx are 
implementing their optimistic concurrency control with MVCC (Grolinger, Higashino, Tiwari, 
& Capretz , 2013). 
In this report, we will focus on the transaction handling in Apache Cassandra, an open
source Wide-Column Store NoSQL database. As Cassandra is one of the NoSQL databases, it 
does not support the ACID transaction model with rollback and locking protocol for 
concurrency control. Rather, it provides atomic, isolated and durable transactions with tunable 
consistency. With tunable consistency, the user can rule on how eventual they wish the 
consistency of transaction to be (DataStax, How are Cassandra transactions different from 
RDBMS transactions?, 2021). To ensure that the transactions are atomic, the write and delete 
operations are atomic at the partition level. This means that any insertion or update of two or 
more rows in the same partition is served as a write operation. Besides, Cassandra performs 
row-level isolation. This indicates that the results of the transaction which is performing the 
write operation will not be visible to the other transactions. In terms of durability, Cassandra 
saves all the updates to a replica node in the memory as well as a commit log on the disk before 
they are granted as a successful commit. By doing so, any loss on the updates during the server 
failure can be recovered through the commit log. 
One of the techniques used by Cassandra in solving the concurrency problem is its 
lightweight transactions with linearizable consistency. To handle the concurrent operations, 
Cassandra used the Paxos consensus protocol to implement its lightweight transactions. 
According to DataStax (2021), Cassandra implements Paxos consensus protocol with 
linearizable consistency. Linearizable consistency is a sequential consistency containing real
time constraints. It guarantees that the isolation of each transaction is alike with the serializable 
level provided by RDBMS. Therefore, the lightweight transaction implemented by Cassandra 
is also known as compare and set (CAS). There are a total of four phases that occurred in Paxos 
protocol: 

1.     Prepare /Promise 
2.     Read/Results 
3.     Propose/Accept 
4.  Commit/Acknowledge
   
In the prepare/promise phase, a node prepares by sending a message containing a 
proposal number to other nodes. The other nodes promise to accept the proposal provided that 
the proposal number of the received message is the highest as compared to the other messages 
received. In the read/results phase, the node that sent the message will make a read request to 
the other nodes while the other nodes will respond with the data. In the propose/accept phase, 
the node that sent the message will send the proposed write to the other nodes and the other 
nodes will accept the proposed write. In the commit/acknowledge phase, the value will be 
committed and acknowledged as a write operation provided that it meets all the criteria 
(Parham, 2018). 
To use lightweight transactions in Apache Cassandra version 3.0 above, we can use the 
IF clause with the INSERT and UPDATE statements. It is recommended to use lightweight 
transactions only when necessary because they will cause latency in the operations to increase 
fourfold due to the round-trips between the CAS coordinators (DataStax, Using lightweight 
transactions, 2021). One of the examples of performing the light transaction in Cassandra is to 
ensure that the insertion of the new data is unique. For example, if a user wants to make sure 
that the slot of booking is reserved, the user can use the IF NOT EXISTS clause as follows: 

![image](https://github.com/yeejing0822/-CassandraWide-ColumnStoreNoSQLDB/assets/86753374/b390faef-ebca-4003-a175-40c859946597)

Otherwise, the Cassandra database will overwrite the data when booking the reserved 
slot without using lightweight transactions as follows:

![image](https://github.com/yeejing0822/-CassandraWide-ColumnStoreNoSQLDB/assets/86753374/0d27221c-9925-4dd9-bfd5-071ffc4d359b)

To provide a better understanding of transaction handling in the Cassandra database, 
we will implement the lightweight transactions in our prototype application which is created 
using the Cassandra Wide-Column Store NoSQL database.
