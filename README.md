# Async-Stres-Test

This script is designed to send multiple asynchronous POST requests to a specified URL using the aiohttp library in Python. It measures the execution time of each request and provides a summary of the total time taken to run all the requests.

# Usage
1. Replace the url variable with the desired URL you want to send the POST requests to.  
2. Adjust the n variable to specify the number of asynchronous requests you want to send.  
3. Modify the data dictionary to contain the actual request body you want to send in each request.  
4. Run the script with python script.py

# Requirements
1. Python 3.7 or above  
2. aiohttp library  

# Additional Information
If you want to make GET requests instead of POST requests, you can modify the script by replacing session.post with session.get in the send_request function. Remember to adjust the data parameter accordingly, as GET requests typically don't include a request body.
