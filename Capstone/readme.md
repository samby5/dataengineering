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

Static Data :
business.json - Contains business data including location data, attributes, and categories
review.json - Contains full review text data including the user_id that wrote the review and the business_id the review is written for.
user.json - User data including the user's friend mapping and all the metadata associated with the user.
checkin.json - Checkins on a business.
tip.json - Tips written by a user on a business. Tips are shorter than reviews and tend to convey quick suggestions.
dont use photo data 
=================================================================================
API Data:
Business Search	/businesses/search	Search for businesses by keyword, category, location, price level, etc.
Phone Search	/businesses/search/phone	Search for businesses by phone number.
Transaction Search	/transactions/{transaction_type}/search	Search for businesses which support food delivery transactions.
Business Details	/businesses/{id}	Get rich business data, such as name, address, phone number, photos, Yelp rating, price levels and hours of operation.
Business Match	/businesses/matches	Find the Yelp business that matches an exact input location. Use this to match business data from other sources with Yelp businesses.
Reviews	/businesses/{id}/reviews	Get up to three review excerpts for a business.
Autocomplete	/autocomplete	Provide autocomplete suggestions for businesses, search keywords and categories.

Event Endpoint: This endpoint returns the detailed information of a Yelp event. You can get the event ID from /events or /events/featured.
