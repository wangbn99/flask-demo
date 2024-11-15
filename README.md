### test health 
 ```sh
 curl -i -X GET http://127.0.0.1:5000
 ```


### send data in query string 
 ```sh
 curl -i -X GET "http://127.0.0.1:5000/test?q=query&s=search"
 ```

 
### send json data 
 ```sh
 curl -i -X POST -H "Contnt-Type: application/json" --json '{"q":"query","s":"search"}' http://127.0.0.1:5000/test
 ```


 ### send form data 
 ```sh
 curl -i -X POST -H "Contnt-Type: application/x-www-form-urlencoded" --data "q=query&s=search" http://127.0.0.1:5000/test
 ```

