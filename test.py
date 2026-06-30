# see what is going on in small pages, request and response
# interview does not have any coding part, onlu talking back and forth

# for example related to request and response
# important to understand what are headers and what are useful for
#     knowing all the roles of headers at this part of the course is not necessary
#     knowing all status codes is not necessary, but broadcast status codes are helpful

# picking more in HTTP 1.1 (the others like HTTP 2 are not necessary)

# '''request and response cycle'''
# the request is made by the client and the resonse by the server

# '''email app recieves an important email, can the server send me a request?'''
# No, requests can only be made by the client, there are other tools we can use for this, like long pooling
# Leave a connection open from the server, and once the request from the client we send the info

# '''When the client sends a request, can you tell me about the components of the HTTP request'''
# The components are: request line(method like GET), host headers, and the optional body
# HTTP requests

# '''what is the use of the body in a request HTTP'''
# In the postrequest in the body we can add the query parameters, by adding or updating some of the information

# '''How is the app using the URL path'''
# parts of the URL are:
# scheme
# host
# path
# port (default port 443)

# at the beggining, is what supposed to mirror the file directories with subfolders
# But nowadays we route directly to specific subservers with the resource we want (rather than going subfolder by subfolder)

# '''is there a safe place where I can put my password in a HTTP request'''
# No, HTTP requests are very insecure, using plain text even if we put it in the body (very insecure)
# the right place to add confidential information is int the transport layer with a TLS (using an encripted message)

# '''parts of a HTTP response'''
# status code (like 200 OK), 3 digits number (we dont need to know all the status code, but it is important to know the first digit of our code)
# 200 succesful
# 300 redirection (302)
# 400 error from client side like misspelled
# 500 error from server side, we cannot do anything about it

# headers like `content type`,
# or like set cookies headers (optional)
# and a body containing the actual data, such as displaying a web page with HTML.

# '''what does the browser do when it gets a 300 series response'''
# It takes the new URL direction provided in the location header and creates a new request with the new provided location with the end goal of finally display the body of the server response when we access the right location and we get the HTML body
# This is a quality of the browser, not of HTTP.

# '''difference between 400 and 500 series status code'''
# 400 series an error from the client side (probably something wrong from our side like misspelling)
# 500 series, out of hands (erro on the server side )

# '''what is a cookie'''
# a cookie lives in the browser (in the client side), it is used to store some information from the sites

# '''name of data (attribute) that identifies the client'''
# that is the session ID, and that will happen every single time in a request-response cycle (the client always provides the same session ID for each request)
# This helps us to create a statefulness in a stateless enviroment like HTTP

# '''the extent of security we need to know'''
# ethernet and IP levels dont have any security, TCP is also secureless
# TLS is where we secure our HTTP (the transport layer)
# The important thing we need to know is the 3 ways of securing information (encription, autentification, integrity) and how the TLS handsake happens

# '''**** IMP (encryption) - REVIEW THIS TOPIC - difference between symmetric and asymmetric keys'''
# symmetric key, is when both parties have the same key, the nature of the symmetric key is once you know the key you can encript and unencript messages very fast

# We need both the public and the private key, we always encript things with the public key and to decripted we need the private key that is the real valuable one

# To exchange the private key we need a safe way that is with the asymmetric keys

# asymmetric keys are done only during the TLS handshake, the server gives us a pablick ke and the client encripts the premaster secret with the private key, once the server receives this it can decrepted with its private key and the protocols agreed in the handshake

# is the first step when the client and the server have not exchange keys yet, so they need to do this first step when they dont have a key from the other side

# '''what about authentication'''
# Authentification is to make sure that someone is what they say they are, they verify this with the certificates of the client, that certificate is validates by the certificate authorities, this goes all the way up to the root authorities that are finally based on trust

# '''How do we know if a CAs root can be trusted or not'''
# It is based on an approved list of CAs, this list is manage by people and based on trust

# '''**** REVIEW THIS CONCEPT TOO - How do we implement integrity'''
# We have unencrypted date payload, and the server checks that the message after encription is exactly the same one than the MAC provided by the client