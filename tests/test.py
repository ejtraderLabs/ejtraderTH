import ejtraderTH
import requests as req

#the function for processing data
def my_func(data):
    ejtraderTH.console_log(output=True)
    ip = req.request(method='GET',url="http://ipinfo.io/ip")
    
    return ip.content

#sending arguments for asynchronous multi thread processing
processed_data = ejtraderTH.start(my_func, repeat=20, max_threads=20)

#printing the synchronised received results
print()
print(f'>> Result: {processed_data}')
ejtraderTH.elapsed(output=True)