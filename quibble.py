class Quibble:
    def __init__(self, text=None, category=None):
        self._id = None
        self._text = text
        self._category = category

    @property
    def id(self):
        """:return: id: int - quibble identifier"""
        return self._id

    @id.setter
    def id(self, value):
        """:param value: int - assigned to id property"""
        self._id = value

    @property
    def text(self):
        """:return: text: str - quibble text"""
        return self._text

    @text.setter
    def text(self, value):
        """:param value: str - assigned to text property"""
        self._text = value

    @property
    def category(self):
        """:return: category: str - quibble category"""
        return self._category

    @category.setter
    def category(self, value):
        """:param value: str - assigned to category property"""
        self._category = value

    def __str__(self):
        return f'[<Quibble> id:{self._id}) text:{self._text} - category:{self._category}]'
        # return u'[<Quibble> text:%s category:%s]' % (self._text, self._category)
