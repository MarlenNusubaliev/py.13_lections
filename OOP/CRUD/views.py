# CRUD - Create Read(listning, detail) Update Delete
import json
from search import search_obj


class CRUD:
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
    
    def list(self):
        res = [{'id': x['id'], 'title': x['title'], 'price': x['price']} 
               for x in self._objects]
        
        return {'Status': '200 OK', 'msg': res}
    

    @search_obj
    def detail(self, id, **kwargs):
        product = kwargs['object_']
        return {'Status': '200 OK', 'msg': product}
    
    @search_obj
    def update(self, id, **kwargs):
        product = kwargs.pop('object_')
        product.update(**kwargs)
        self._save()

        return {'Status': '206 Updated'}
    
    @search_obj
    def delete(self, id, **kwargs):
        product = kwargs['object_']
        self._objects.remove(product)
        self._save()
        return {'Status': '204 No Content'}
    

    def _save(self):
        with open('data.json', 'w') as file:
            json.dump(self._objects, file, indent=4)
        return 'Saved'




obj = CRUD()
obj.create(title='Redmi Note 10',
           description='The best phone',
           qty=10, price=200)

obj.create(title='Redmi Note 20',
           description='The best phone 1212',
           qty=3, price=500)

obj.create(title='Iphone 14 Pro Max',
           description='New The best phone',
           qty=5, price=1000)

obj.create(title='Samsung S22 Ultra',
           description='The best Android phone',
           qty=8, price=900)



print('==============================list================================================')

print(obj.list())
print('=============================detail================================================')

print(obj.detail(3))
print(obj.detail(4))
print(obj.detail(16))
print('=============================update================================================')
print(obj.detail(2))
print(obj.update(2, title='Redmi Note 30 Ultra Max Plus'))
print(obj.detail(2))
print(obj.update(16, title='Redmi', print=900))
print('=============================delete================================================')
print(obj.list())
print(obj.delete(1))
print(obj.detail(14))
print(obj.list())

# print(obj.save())
obj.create(title='Samsung Z Flip 20',
           description='The best Android Flip phone',
           qty=3, price=1000)







