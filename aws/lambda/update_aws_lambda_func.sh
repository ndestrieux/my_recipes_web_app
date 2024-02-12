#!/bin/sh

zip lambda_function.zip lambda_function.py

aws lambda update-function-code \
    --function-name  createThumbnail \
    --zip-file fileb://lambda_function.zip