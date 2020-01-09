from tag_keys import BasicDict, BASIC_INFO

class TestBasicDict(BasicDict):
    def __init__(self, idx, key):
        super().__init__(idx = idx, key = key)

    def test_item(self):
        print(self.item)
        return 


if __name__ == "__main__":
    for i in range(5):
        tbd = TestBasicDict(idx = i, key = None)
   
        tbd.__iter__()
