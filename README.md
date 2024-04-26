# Miscellaneous db performance testing experiments

Currently, and for the immediate future, solely focused on experiments related to Rucio (https://github.com/rucio/rucio).

<br> <br>

## Performance of retrieving different 'Result'-esque types - PSQL/SQLAlchemy
<p float="left">
  <img src="images/types_perf_comparison_bar.png" alt="Data retrieval perf comparison" width="45%"/>
  <img src="images/types_perf_comparison_line.png" alt="Data retrieval perf comparison" width="45%"/>
</p>

<br> <br>

## Complex query vs. two simpler queries - PSQL/SQLALCHEMY
<p float="left">
  <img src="images/complex_or_multiple_5_batchsize_log.png" alt="Data retrieval perf comparison" width="45%"/>
  <img src="images/complex_or_multiple_2_batchsize.png" alt="Data retrieval perf comparison" width="45%"/>
</p>

### (EXPLAIN ANALYZE VERBOSE) Simple queries 
<img src="images/simple_q2.png" alt="Simple query 1" height="150px">
<img src="images/simple_q1.png" alt="Simple query 2" height="200px">

### (EXPLAIN ANALYZE VERBOSE) Complex query
<img src="images/complex_q.png" alt="Complex query" height="400px">
