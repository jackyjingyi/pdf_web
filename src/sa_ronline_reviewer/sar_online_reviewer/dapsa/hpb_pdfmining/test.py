from tag_keys import BasicDict, BASIC_INFO

class TestBasicDict(BasicDict):
    def __init__(self, idx, key):
        super().__init__(idx = idx, key = key)

    def test_item(self):
        print(self.item)
        return 

from fuzzywuzzy import fuzz
from fuzzywuzzy import process

print(fuzz.ratio("""Directives. It is acceptable if the standards are not listed or not
complete 6. 3rd Party Testing lab/ Certification body info incl.
name, address of testing location, test report # and issuing
date. IF vendor has EU AR, 3rd party not required. 7. Sole
Responsibility Statement of EU Representative - Must be
present 8. Authorized Signature and Job Title - Must be
present 9. Date of Signed Declaration - MM/DD/YYYY. Must
be present, no expiration date unless there are changes to the
product or directives/test standards.""","""Directives.  if the standards are not listed or not
complete 6. rtification body info incl.
name, address of testing location, test report # and issuing
date. IF vendor has EU AR, 3rd party not required. 7. Sole
Responsibility Statement of EU Representative - Must be
present 8. Authorized Signature and Job Title - Must be
present 9. Date of Signed Declaration - MM/DD/YYYY. Must
be present, no expiration date unless there are changes to the
product or """ ))

if __name__ == "__main__":
    for i in range(5):
        tbd = TestBasicDict(idx = i, key = None)
   
        tbd.__iter__()
