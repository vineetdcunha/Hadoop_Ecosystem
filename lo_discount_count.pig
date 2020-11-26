a1 = LOAD '/user/ec2-user/lineorder.tbl' using PigStorage('|') AS (lo_orderkey:int, lo_linenumber:int, lo_custkey:int, lo_partkey:int, lo_suppkey:int, lo_orderdate:int, lo_orderpriority:chararray, lo_shippriority:chararray, lo_quantity:int, lo_extendedprice:int, lo_ordertotalprice:int, lo_discount:long, lo_revenue:int, lo_supplycost:int, lo_tax:int, lo_commitdate:int, lo_shipmode:chararray); 
a2 = GROUP a1 BY lo_discount;
a5 = foreach a2 generate group as lo_discount, COUNT(a1.lo_extendedprice) as cnt;
result = FOREACH a5 GENERATE lo_discount, cnt;
dump result;