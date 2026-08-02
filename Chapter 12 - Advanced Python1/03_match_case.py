def http_server(status):
    match status:
        case 200:
            return "Ok"
        case 404:
            return "Not Found"
        case 500:
            return "Internal Server Error"
        case _:
            return "Unknown Status"    
            
print (http_server(200))
print (http_server(404))
print (http_server(500))
print (http_server(7800))