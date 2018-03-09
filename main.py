def handle(event, context):
    return {
        "statusCode": 200,
        "headers": {"Content-Type": "application/json"},
        "body": '{"id":1,"balance":123, "currency":"EUR"}'
    }
