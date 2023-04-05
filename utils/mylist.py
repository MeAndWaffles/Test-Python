

class MyList:
    def __init__(self):
        self.items = []

    def add_item(self, item):
        self.items.append(item)

    def create_new_list(self):
        return MyList()

    def test_create_new_list(self):
        new_list = self.create_new_list()
        new_list.add_item(1)
        assert len(new_list.items) == 1

        new_list = self.create_new_list()
        new_list.add_item(2)
        assert len(new_list.items) == 1