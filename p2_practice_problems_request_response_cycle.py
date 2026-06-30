'''1. What are the required components of an HTTP request? What are the additional optional components?'''

# The required components of a HTTP request are:
# -HTTP method (in this case is GET)
# -header host (required since HTTP/1.1)
# -path

# The optional components are:
# -port
# -query parameters
# -message body

'''2. What are the required components of an HTTP response? What are the additional optional components?'''

# the required response components are:
#  -status(like 200 ok)

# The rest are optional:
# -header
# -body

'''3. What determines whether a request should use GET or POST as its HTTP method?'''

# We use the HTTP method `GET` when we want to retrieve information from the server, and we use the HTTP method `POST` when we want to upload data into the server.

### LS solution

# GET requests should only retrieve content from the server. They can generally be thought of as "read only" operations, however, there are some subtle exceptions to this rule. For example, consider a webpage that tracks how many times it is viewed. GET is still appropriate since the main content of the page doesn't change.

# POST requests involve changing values that are stored on the server. Most HTML forms that submit their values to the server will use POST. Search forms are a noticeable exception to this rule: they often use GET since they are not changing any data on the server, only viewing it.