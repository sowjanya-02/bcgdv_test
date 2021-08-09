# bcgdv_test


## Project Structure
The Python Flask based backend api
      1) models(predefining the fields in db)
      2) db(initiating the db)
      3) routes(Endpoint function checkout)
      4) appfun(main application functions)
      5) test (to automate the api with pytest)
     
## Backend Api Description
  * /check out is single endpoint and it takes a list of ids and return the total cost.
  ### APi constarints:
     1) check whether offer exists or not depending on query parameters of watchids
     2) In containarized application initially data has been written to db 

## Backed Setup and Configuration with Docker

### Step 1.
   * mkdir sample
   * git init .
   * git pull  https://github.com/sowjanya-02/bcgdv_test.git
   
### step2
 * docker-compose up -d (to run in background)

### step3 test with curl
   * curl --request GET  http://0.0.0.0:8000/checkout?ids=1,2,3,1,1
   

   
   
   
   
   
 





