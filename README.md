# GarvitBhardwaj-File-Key-Value-Store

# This project is built on Flask.
#There is 4 endpoint here. 1) / 2) create 3) read 4) delete
You can either change the input parameter is home endpoint to run CRD functions 
Or you can go to individual endpoint to run the corresponding functionaliy

Here is sample input correspoding to each endpoints

1) endpoint-> "/"
  Input -> { "input" : 1, "key": "name", "value": "Garvit","time":10}
  
2) endpoint-> "/create"
  Input -> {"key": "name", "value": "Garvit","time":10}  
 
3) endpoint-> "/read"
  Input -> {"key": "name"}
  
4) endpoint-> "/delete"
  Input -> {"key": "name"}  
  
How to run the project:

1) run the CRD.py file using "py CRD.py" command
2) Now start postman app and give input in body.
