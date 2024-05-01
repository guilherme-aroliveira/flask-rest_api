# Flask - REST API Project

[![License](https://img.shields.io/badge/License-MIT-blue.svg)](https://opensource.org/license/mit)

This is a project of the course "Application Development using Microservices and Serverless" by IBM as part of IBM DevOps Certificate.

### Description

This project consists of creating a Product list using a Flask Server. 
The application executes CRUD operations (Create, Retrieve, Update, and Delete), through the REST API endpoints in the Flask server.

### Usage

To execute this application install the necessary packages to run it:

```python
$ python3 -m pip install flask flask_cors

# run the python server
$ python3 products.py
```

Use curl to serve the REST API endpoints:
```bash
$ curl http://localhost:5000/products
```

To add a product (POST request) curl can also be used:
```bash
$ curl -X POST -H "Content-Type: application/json" \
    -d '{"id": 145, "name": "Pen", "price": 2.5}' \
    http://localhost:5000/products
```

To verify the added product:
```bash
$ curl http://localhost:5000/products/145
```

Another way to use this application is to run the Python server and use the Postman app to execute the CRUD operations on the REST API.

### License

Copyright (c) 2024, Guilherme Oliveira. All rights reserved.

Licensed under the Apache License. See [LICENSE](LICENSE)
