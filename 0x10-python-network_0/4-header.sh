#!/bin/bash
# takes an argument, sends a GET request displays the body of the response
curl -sX GET $1 -H "X-HolbertonSchool-User-Id: 98" -L
