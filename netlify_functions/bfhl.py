from app import bfhl as handler

def lambda_handler(event, context):
    return handler(event, context)
