# CUSTOM LOAD BALANCER IMPLEMENTATION

## ICS 4A

## Group Members

1. 138070 Alfred Karanja
2. 138930 Cynthia Kiconco
3. 145402 Kuria Githinji

## Quick Guide

1. Introduction
   - Overview
     - Installation instructions
       - Usage guidelines

2. Project Analysis

# Introduction

## Overview
This project involves creating a load balancer using consistent hashing to manage a set of web server containers. The load balancer is implemented as a Flask application and provides various HTTP endpoints to modify configurations and check the status of the managed web server replicas. The primary function of the load balancer is to distribute client requests evenly across the available replicas to ensure balanced load distribution.

## Installation Instructions

## Requirements

1. Docker Desktop
2. Flask version 3.0.3 or higher
3. Gunicorn version  20.1.0 or higher
4. Python 3.11.4 or higher
5. Windows Operating System

## Installation Instructions

1. Clone the Repository to your machine

   `` git clone https://github.com/kuriofoolio/custom_load_balancer.git ``
   
2. Build the Server containers

   `` docker-compose build ``

3. Run the containers 

   `` docker-compose up -d `` 

## Usage guidelines
Once you have the load balancer and web server containers set up and running, you can interact with them using the defined HTTP endpoints. Here are the detailed usage guidelines for each endpoint:

  1. Checking status of Replicas 

  Endpoint: /rep
  Method: GET
  Description: Returns the current status of the replicas managed by the load balancer.
  
  Example Request : 

     `` curl http://localhost:5000/rep ``

  Example Response : 

 ``` {
    "message": {
        "N": 3,
        "replicas": ["Server 1", "Server 2", "Server 3"]
    },
    "status": "successful"
} 
 ```


2. Adding New replicas

    Endpoint: /add
    Method: POST
    Description: Adds new server instances to scale up the system.

    Request Payload:

    n: The number of new instances to add.
    hostnames (optional): A list of preferred hostnames for the new instances.


    Example Request : 

    ```
    curl -X POST -H "Content-Type: application/json" -d '{
    "n": 2,
    "hostnames": ["S4", "S5"]
    }' http://localhost:5000/add

    ```

    Example Response : 

    ```

    {
    "message": {
        "N": 5,
        "replicas": ["Server 1", "Server 2", "Server 3", "S4", "S5"]
    },
    "status": "successful"
    }

    ```
3. Removing Replicas

    Endpoint: /rm
    Method: DELETE
    Description: Removes server instances to scale down the system.

    Request Payload:

    * n: The number of instances to remove
    * hostnames(optiobal) : A list of preferred hostnames for the instances to remove. 

    Example Request : 

    ``` 
    curl -X DELETE -H "Content-Type: application/json" -d '{
    "n": 2,
    "hostnames": ["S4", "S5"]
    }' http://localhost:5000/rm

    ```

    Example Resposible : 

    ``` 
    {
    "message": {
        "N": 3,
        "replicas": ["Server 1", "Server 2", "Server 3"]
    },
    "status": "successful"
    }

    ```

4. Routing Client Requests

Endpoint: /<path>
Method: GET
Description: Routes requests to a server replica based on the consistent hashing algorithm.

Example Request :

`` curl http://localhost:5000/home ``

Example Response : 

```

{
    "message": "Request routed to Server 1",
    "status": "successful"
}

```

Additional Notes:

Scaling Up: To add more server replicas, ensure that the payload in the POST request to /add accurately specifies the number of new instances and their hostnames if preferred.

Scaling Down: To remove server replicas, ensure that the DELETE request to /rm specifies the correct number of instances to be removed and their hostnames if preferred.

Routing Requests: The endpoint /<path> can be used to route requests. Currently, only the /home path is recognized by the server replicas as per the provided code.


















