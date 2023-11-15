def search_obj(func):
    def wrapper(*args, **kwargs):
        self = args[0]
        id = args[1]
        for product in self._objects:
            if id == product['id']:
                kwargs.update(object_=product)
                return func(*args, **kwargs)
        return {'Status': '404 Not Found'}
    return wrapper
        