class GenericView:
    def __init__(self, methods=('GET',)):
        self.methods = methods

    def get(self, request):
        return ""

    def post(self, request):
        print("POOST")
        print(request)
        # pass

    def put(self, request):
        pass

    def delete(self, request):
        pass


class DetailView(GenericView):
    def __init__ (self,methods=('GET',)):
        super().__init__(methods)
    
    def render_request(self, request, method):
        if method not in self.methods:
            raise TypeError('данный запрос не может быть выполнен')
        get_method=getattr(self,method.lower())
        return get_method(request)


    def get(self, request):
        if not type(request)==dict:
            raise TypeError('request не является словарем')
        if "url" not in request:
            raise TypeError('request не содержит обязательного ключа url')
        return f"url: { request['url'] }"


dv = DetailView()
html = dv.render_request({'url': 'https://site.ru/home'}, 'GET') 
print(html)


# dv = DetailView(methods=('PUT', 'POST'))
# html = dv.render_request({'url': 'https://site.ru/home'}, 'POST')