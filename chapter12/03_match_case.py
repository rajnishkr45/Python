def http_status(status):
    match status:
        case 200:
            return "OK"
        case 404:
            return "NOT FOUND"
        case 500:
            return "INTERNAL SERVER ERROR"
        case _:
            return "Invalid Case"


print(http_status(500))
