Shad
----

Small framework for building RESTful API wrappers.

Install
-------


Usage
-----

Define your base API class

    from shad import BaseAPI, APIFunction, bind
    
    class MyAPI(BaseAPI):
        def __init__(self, api_key, base_url="http://example.com/"):
           self.api_key = api_key
           self.base_url = base_url
        
   		def update_parameters(self, params):
   		   params["key"] = self.api_key
   		   return params
   		   
`base_url` is required, and used by the method `get_base_url` to build the requests url. You can override `get_base_url` if you want to include variable constants in your base url in every request.

Next define your end points

    @bind
    class mycall(APIFunction):
        path = "accounts/login/"
        method = "GET"
        
Then a user of your wrapper can do this:

    api = MyAPI('THISISMYAPIKEY')
    api.mycall(format='json')
    
 
        