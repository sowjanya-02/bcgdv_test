# Backend API using Flask

## Flask
    It is microframework and doesn't have a lot of overhead, Flask is very performant. Extensions could impact performance negatively.
    Very flexible
    ORM used in current api is mongoengine
    Flask documentation is comprehensive, full of examples and well structured.
    It is super easy to deploy Flask in production 
    High Flexibility
    Easy to divide the code in to multiple chunks
    Easy installation
    Flask ORM frame works supports SQL and NOSQL
    Data Validation
    Built in unittest library


## Project Structure
The Python Flask based backend api
   * models(predefining the fields in db for data validation)
   * db(initiating the db for creating the collection object)
   * routes(Endpoint)
   * appfun(Main function to integrate with flask server)
   * test (to automate the api with unittest)
     
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
   #### Response
    {"total_cost":value}
   

   
   
   
   
   
 





