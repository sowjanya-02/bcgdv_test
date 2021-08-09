# bcgdv_test


## Project Structure
The Python Flask based backedn api
  * models(predefining the fields in db)
  * db(initiating the db)
  * routes(Endpoint function checkout)
  * appfun(main application functions)

## Backed Setup and Configuration with Docker

### Step 1.
   * mkdir sample
   * git init .
   * git pull  https://github.com/sowjanya-02/bcgdv_test.git
   
### step2
 * docker-compose up -d (to run in background)

### step3 test with curl
   *curl --request GET  http://0.0.0.0:8000/checkout?ids=1,2,3,1,1
   
## Backed Setup and Configuration with pythonenv

### Step 1.
   * mkdir sample
   * git init .
   * git pull  https://github.com/sowjanya-02/bcgdv_test.git
   
### step2
 *  python3 -m venv ./venv
 *  source ./venv/bin/activate
 *  pip install -r requirements.txt

### step3 test api end point with pytest/unittest
   *  pytest test.py (total 4 tests included)
   
   
   
   
   
   
 





