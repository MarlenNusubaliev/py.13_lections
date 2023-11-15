from views_mixins import *


class Post(CreateMixin, ReadMixin, UpdateMixin, DeleteMixin, SaveMixin):
    pass

class Comment(CreateMixin, ReadMixin, DeleteMixin, SaveMixin):
    pass

class Like(CreateMixin, ReadMixin, DeleteMixin, SaveMixin):
    pass

