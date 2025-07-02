def http_status(status):
    match status:
        case 200:
            return "Ok"
        case 404:
            return "Notfound"
        case 500:
            return "internal error"
        case _: #else
            return "Unknown status"
        
print(http_status(5007))