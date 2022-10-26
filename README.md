# mq_smf_formatter

The 'GENERIC' python program enables a user examining their own SMF data to categorize their queries into appropriately named directories with correctly modified SQL given their respective LPARs and Queue Manager names.

For example, if you have 1 LPAR named PROD, and 2 queue managers on it, named QM1 and QM2, The GENERIC program would let you to create customized queries for running against your data and organize the queries into appropriately named directories on your workstation. Meaning, by running GENERIC, you would end up with 2 directories, PRODQM1 and PRODQM2, and in each of those directories, you will have customized SQL with correct variable names to run against your SMF data.

In order to use this program:
1) Construct a directory on your workstation with all of the content of this github repo. 
2) Generic SQL programs will need to be added to the directory with the first 7 characters being 'generic'. For example, generic_blob_use.txt. 
3) All SQL queries must be in .txt format. 
4) Modify Distinct_LPAR_QM.txt to have the names of your queue managers and LPARs.
5) The python program will recognize LPAR and QM variables in your SQL queries that have ++LPAR and ++QMGR as temporary variables in need of being customized by the program
  For example, "EXPORT TO "E:\**CustomerPath**\++LPAR\MQ115\Query_Results\++QMGR_BLOBUse.csv" OF DEL MODIFIED BY COLDEL, DECPT." _See the Generic_BlOBUSE.txt as an example.

This program is most useful when you have to create a large amount of custom queries to run against your SMF data with many LPARs and QMs involved. 
