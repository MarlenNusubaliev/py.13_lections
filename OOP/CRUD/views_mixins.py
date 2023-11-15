from .search import search_obj
import json

class CreateMixin:

    def _get_or_set_obj(self):
        try:
            if self._objects and self._id:
                pass
        except (NameError, AttributeError):
            self._objects = []
            self._id = 0


    def __init__(self) -> None:
        self._get_or_set_obj()

    def create(self, **kwargs):
        self._id += 1
        obj = dict(id=self._id, **kwargs)
        self._objects.append(obj)
        print({'status': '201 Created', 'msg': obj['title']})
        self._save()

        return {'status': '201 Created', 'msg': obj['title']}
    


class ReadMixin:
    def list(self):
        res = [{'id': x['id'], 'title': x['title'], 'price': x['price']} 
                for x in self._objects]
        
        return {'Status': '200 OK', 'msg': res}
    

    @search_obj
    def detail(self, id, **kwargs):
        product = kwargs['object_']
        return {'Status': '200 OK', 'msg': product}


class UpdateMixin:
    @search_obj
    def update(self, id, **kwargs):
        product = kwargs.pop('object_')
        product.update(**kwargs)
        self._save()

        return {'Status': '206 Updated'}
    
class DeleteMixin:
    @search_obj
    def delete(self, id, **kwargs):
        product = kwargs['object_']
        self._objects.remove(product)
        self._save()
        return {'Status': '204 No Content'}
    
class SaveMixin:
    def _save(self):
        with open('data.json', 'w') as file:
            json.dump(self._objects, file, indent=4)
        return 'Saved'