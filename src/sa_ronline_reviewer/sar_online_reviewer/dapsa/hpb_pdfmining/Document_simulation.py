import os
from tag_keys import PATH


class Document:
    'A simulation to django model'
    def __init__(self, path, sub_path, doc_id):
        self.path = path
        self.sub_path = sub_path
        self.doc_id = doc_id
        self._file_path = ''

    @property
    def file_path(self):
        return self._file_path

    @file_path.setter
    def file_path(self, arg):
        self._file_path = self.path + self.sub_path + os.listdir(path =(self.path+self.sub_path))[arg]
        print('calling',self._file_path)

    def __call__(self, *args, **kwargs):
        self.file_path = self.doc_id

    def get_file_name(self):
        return os.listdir(path =(self.path+self.sub_path))[self.doc_id][:-4]


if __name__ == '__main__':
    # test
    path = PATH['path']
    sub_path = PATH['sub_path'][4]
    doc_id = 1
    print(path,sub_path)
    print(os.listdir(path=path+sub_path)[doc_id])
    doc = Document(path=path,sub_path=sub_path,doc_id=doc_id)
    doc()
    print(doc.__dict__)


