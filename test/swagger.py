import unittest
import json
import os
import sys

with open('../json/test_swagger.json') as f:
  expected = json.load(f)

sys.path.insert(1, '/Users/danielgomez/Documents/GitHub/Generators')
import swagger_gen

description = "This is a simple example NodeJS API project to demonstrate Swagger Documentation"
title = "Tasks API"
email = "abc@gmail.com"
basePath = "/api"
paths = [{
    "path": "/resume/{id}",
    "type": "get",
    "summary": "Get persons resume",
    "description": "Get resume with id",
    "parameters": [
    {
                            "name": "id",
                            "in": "path",
                            "description": "ID of resume",
                            "required": true,
                            "type": "string"
                        }],
    "responses":{
                        "200": {
                            "description": "successful operation",
                            "schema": {
                                "$ref": "#/definitions/resumeResponse"
                            }
                        },
                        "400": {
                            "description": "Invalid status value",
                            "schema": {
                                "$ref": "#/definitions/InvalidResponse"
                            }
                        }
                    }
},
{
    "path": "/resume",
    "type": "post",
    "summary": "Create a resume",
    "description": "Create a resume",
    "parameters": [
        {
            "in": "body",
            "name": "body",
            "description": "search object",
            "required": true,
            "schema": {
                "type": "object",
                "properties": {
                    "resume" : {
                        "type": "object",
                        "$ref": "#/definitions/Create"
                    }
                }
            }
        }
    ],
    "responses":{
                  "200": {
                        "description": "successful operation",
                        "schema": {
                            "type": "array",
                            "items": {
                                "$ref": "#/definitions/resumeResponse"
                            }
                        }
                    },
                    "400": {
                        "description": "Invalid status value",
                        "schema": {
                            "$ref": "#/definitions/InvalidResponse"
                        }
                    }
            }
}]
definitions = [{
    "Search": {
    }
                "type": "object",
                "properties": {
                    "location": {
                        "type": "string"
                    },
                    "experience": {
                        "type": "string"
                    },
                    "education": {
                        "type": "string"
                    }
                }
            },
            {
            "InvalidResponse": {
            "type": "object",
            "properties": {
                "statusCode": {
                    "type": "string"
                },
                "message": {
                    "type": "string"
                }
            }
        }
    }
]

class TestSwagger(unittest.TestCase):
    def test_start(self):
        results = swagger_gen.enter_values(description, title, email, basePath)
        self.assertEqual(results["swagger"], expected["swagger"])

    # Test whole json
    def test_correct(self):
        # email, basePath, paths[{endpoint, requestType, Summary, description, produces, parameters[name, in, description, required, type], responses[{number, description, schema}]}]
        results = swagger_gen.enter_values(description, title, email, basePath)
        self.assertEqual(results, expected)

if __name__ == '__main__':
    unittest.main()