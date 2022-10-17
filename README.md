# netmonapi
### Backend for AI4NetMon project

Steps:

1. Clone repository

2. Inside netmonapi directory open terminal and run:
  $sudo docker compose up --build -d
  
3. In a browser open: http://localhost:8000/docs

### Endpoints and Parameters

* /asns: choose the number of results per page and which page to show, and the API returns the entire dataframe - all the ASes with their attributes.
  e.g: http://localhost:8000/asns?page=1&size=50 for showing the first page of results and 50 ASNs per page.
  
* /asn/{ASN}: takes the AS number as parameter and returns all its attributes.
  e.g: http://localhost:8000/asn/10 to get results for the AS number 10.
  
* /bias/: takes multiple AS numbers as parameters, calculates bias across all dimensions for the particular set and returns it.
  e.g: http://localhost:8000/bias/?asn=12&asn=178&asn=1500 to get bias for the set consisting of AS numbers: {12, 178, 1500}.
  
* /bias/{imp}: takes a particular set as parameter: (Atlas, RIS, RIS&RouteViews, rrc00, rrc01 ... rrc26) and returns the bias of the set across all dimensions.
  e.g: http://localhost:8000/bias/Atlas to get the precalculated bias for the `Atlas` set.
  
* /bias_diff/{set}: takes a particular set as parameter (Atlas, RIS). Choose the number of results per page and which page to show, and the API returns the % difference in bias if adding each AS of the set in the infrastructure.    
  e.g: http://localhost:8000/bias_diff/RIS?page=1&size=50 to get the bias difference for the `RIS` set, showing the first page of results and 50 results per page.
