LineOrder1 = LOAD '/user/ec2-user/lineorder.tbl' using PigStorage('|') AS (lo_orderkey:int, lo_linenumber:int, lo_custkey:int, lo_partkey:int, lo_suppkey:int, lo_orderdate:int, lo_orderpriority:chararray, lo_shippriority:chararray, lo_quantity:int, lo_extendedprice:int, lo_ordertotalprice:int, lo_discount:long, lo_revenue:int, lo_supplycost:int, lo_tax:int, lo_commitdate:int, lo_shipmode:chararray); 
LineRevenue = FILTER LineOrder1 BY lo_discount > 6;
a2 = GROUP LineRevenue BY lo_quantity;
a5 = foreach a2 generate group as lo_quantity, SUM(LineRevenue.lo_revenue) as total_revenue;
sum_result = FOREACH a5 GENERATE lo_quantity, total_revenue;
dump sum_result;