Yelp Reviews for restuarants pulled from various APIs and loaded into a hybrid model(On Prem and Cloud).

Key Considerations
1) When moving to cloud implement Airflow scheduling. Redshift can be used for Cloud Database storage(for Yelp Warehouse)
2) Initially this is just going to be in local
3) Data flows from Yelp APIs and Static dataset to FileShare and SQL Server
4) Data Analysis will be done in SQL Server db and based on findings data refinement will be done 
5) Spark jobs will do cleaning transformations while moving from Landing to Processed Zone
6) Spark jobs will be used to move data from Processed zone to Stage in Yelp datawarehouse 
7) Required data is migrated to DatamArt based on use case
8) ETL job execution is completed once the Data Warehouse is updated.
9) File Share will be replaced with Amazon S3 Buckets. Use boto3 to move files between s3 buckets
 
BI Tools can point to data marts for meaningful insights