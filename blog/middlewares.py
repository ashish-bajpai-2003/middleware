# def my_middleware(get_response):
#     print("One time Initialization")
#     def my_function(request):
#         print("This is before view.")
#         response= get_response(request)
#         print("This is after view..")
#         return response
#     return my_function


# class MyMiddleware:
#     def __init__(self , get_response):
#         self.get_response = get_response
#         print("One time Initialization")

#         def __call__(self, request):
#             print("This is before view")
#             response = self.get_response(request)
#             print("This is after view")
#             return response
        

class BrotherMiddleware:
    def __init__(self , get_response):
        self.get_response = get_response
        print("One time Brother Initialization")

    def __call__(self, request):
        print("This is brother before view")
        response = self.get_response(request)
        print("This is brother after view")
        return response
        


class FatherMiddleware:
    def __init__(self , get_response):
        self.get_response = get_response
        print("One time father Initialization")

    def __call__(self, request):
        print("This is father before view")
        response = self.get_response(request)
        print("This is father after view")
        return response
        


class MotherMiddleware:
    def __init__(self , get_response):
        self.get_response = get_response
        print("One time mother Initialization")

    def __call__(self, request):
        print("This is mother before view")
        response = self.get_response(request)
        print("This is mother  after view")
        return response
