# netmonapi
Backend for AI4NetMon project

Steps:

1. Clone repository

2. Inside netmonapi directory open terminal and run:
  $sudo docker compose up --build -d
  
3. In a browser open: http://localhost:8000/docs

### Endpoints and Parameters

* /asns: choose the number of results per page and which page to show, and the API returns the entire dataframe - all the ASes with their attributes.
* /asn/{ASN}: takes the AS number as parameter and returns all its attributes.
* /bias/: takes multiple AS numbers as parameters, calculates bias across all dimensions for the particular set and returns it.
* /bias/{imp}: takes a particular set as parameter: (Atlas, RIS, RIS&RouteViews, rrc00, rrc01 ... rrc26) and returns the bias of the set across all dimensions.
* /bias_diff/{set}: takes a particular set as parameter (Atlas, RIS). Choose the number of results per page and which page to show, and the API returns the % difference in bias if adding each AS of the set in the infrastructure.    
