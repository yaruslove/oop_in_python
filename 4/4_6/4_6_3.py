class RetriveMixin:
    def get(self, request):
        return "GET: " + request.get('url')


class CreateMixin:
    def post(self, request):
        return "POST: " + request.get('url')


class UpdateMixin:
    def put(self, request):
        return "PUT: " + request.get('url')


class GeneralView:
    allowed_methods = ('GET', 'POST', 'PUT', 'DELETE')
    def render_request(self, request):
        if request['method'] in self.allowed_methods:
            method_request = request.get('method').lower()
            return getattr(self, method_request)(request)  # f"{request.get('method')}: {request.get('url')}"
        else:
            raise TypeError(f"Метод {request.get('method')} не разрешен.")


class DetailView(RetriveMixin, GeneralView):
    allowed_methods = ('GET', 'PUT', )

view = DetailView()
html = view.render_request({'url': 'https://stepik.org/course/116336/', 'method': 'GET'})
print(html)

# html = view.render_request({'url': 'https://stepik.org/course/116336/', 'method': 'PUT'})

