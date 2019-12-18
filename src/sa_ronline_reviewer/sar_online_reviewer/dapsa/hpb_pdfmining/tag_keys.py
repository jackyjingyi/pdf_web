import os
BEGIN_KEYS = [
    'Parts Inventory',
]

END_KEYS = {
    'positive': [

    ],
    'negative': [

    ]
}

SKIP_KEYS = [
    'General Terms and Conditions of Business of TÜV Rheinland in Greater China \n',
]

INFO_KEYS = {
    'report number': ['PrüfberichtNr Test Report No', 'PrüfberichtNr Test Report  No', 'Test Report No'],
    'protocol': ['Prüfgrundlage Test specification', 'Test specification'],
    'vendor name': ['Vender Name'],
    'factory name': ['Factory Name', 'Factory  Name'],
    'lab': ['TUV Rheinland', 'TÜV Rheinland'],
}

DATE_PATTERN = {
    'mm/dd/yyyy': "([1-9]|1[0-9]|2[0-9]|3[0-1])(.|-)(0[1-9]|1[0-2])(.|-|)(20[0-9][0-9])",
    'dd/mm/yyyy': "([1-9]|1[0-9]|2[0-9]|3[0-1])(.|-)([1-9]|1[0-2])(.|-|)(20[0-9][0-9])",
    'yyyy/mm/dd': "([0-9]{4})(-|/|.)(0[1-9]|1[0-2])(-|/|.)(0[1-9]|[1-2][0-9]|3[0-1])",
    'oo/dd/yyyy': "([a-zA-z]{3})(-|/|.)([1-9]|1[0-9]|2[0-9]|3[0-1])(-|/|.)([0-9]{4})",
}

FAILURE_SUMMARY= [
    'details of failure', 'failure summary',
]

FAILURE_KEYS = [
    'fail'
]

MONTH = {
    'Jan': 1,
    'Feb': 2,
    'Mar': 3,
    'Apr': 4,
    'May': 5,
    'Jun': 6,
    'Jul': 7,
    'Aug': 8,
    'Sep': 9,
    'Oct': 10,
    'Nov': 11,
    'Dec': 12,
}

PROTOCOLS = os.path.join(os.getcwd(),'hpb_pdfmining/documents/protocols/tt1/')

LAB_INFO = {
    'TUV': {},
    'ITS': {},
    'BV': {},
}

TARGET_KEYS = [
    "child vendor code",
    "amazon style id",
    'parent asin',
    'acc trf#',
    "testing stage",
    "stage of testing",
    "report number",
    "test report number",
    "report no",
    "test report no",
    "number"
]

PATH = {
    'path': os.path.join(os.getcwd(),'hpb_pdfmining/documents/reports/'),
    'sub_path': {4: '4columns/', 5: '56columns/', 6: '56columns/', 'cornerstone': 'others/', 'check': 'check/'},
}
# all country combinations in all tuv protocols
COUNTRY_LIST = ['US, CA', 'EU', 'United States/ Canada', 'United States; Mexico; Canada; European Union, Japan, India',
                'United States; Mexico; India; Canada; Japan; European Union; China', 'EU,US,CAN',
                'United States; Mexico; Canada; Japan; European, India', 'US', 'United States;',
                'France; Germany; Italy; Spain; United Kingdom',
                'United States; Mexico; Canada; Japan; European Union; India; Turkey',
                'United States; Mexico; Canada; Japan; European Union; India;', 'European Union', 'EU,US,CA',
                'United States; Mexico; Canada; Japan; European Union; India;  Turkey',
                'United States; Mexico; Canada; Japan; European Union; India',
                'United States; Mexico; Canada; Japan; European Union; India; Singapore, Australia', 'Canada', 'GE',
                'United States; Mexico; Canada; Japan; European Union; India; ,',
                'United States; Canada; European Union, Mexico, Japan, India', 'US, CA, JP, EU, IN',
                'United States (California market only)', 'EU, IN, US', 'FR', 'United States',
                'United States; Mexico; Canada;',
                'United States; Mexico; Canada; Japan; European Union; India; China, Turkey', 'DE',
                'United States; Mexico; Canada; Japan; European Union; India; , Turkey', 'US, CA, MX',
                'Canada; European Union', 'United Kingdom',
                'United States; Mexico; Canada; Japan; European Union; India; China;Turkey',
                'CA, CN, EU, IN, JP, MX, US', 'EU, CA, US, JP, MX, IN', 'United States; Canada',
                'United States-California', 'US,CAN,MX', 'United States; Mexico; Canada; ; European Union; India;',
                'Canada; European Union; Japan; Mexico; United States', 'United States; Mexico; Canada; European Union',
                'England', 'United States; Mexico; Canada; Japan; European Union;',
                'United States; Mexico; Canada, European union, India, Japan',
                'United States; Mexico; Canada; Japan; European Union; India; ; Turkey',
                'United States; Mexico; Canada; Japan; European Union; India; china',
                'Canada; European Union; India; Mexico; Japan; United States',
                'Canada; European Union; Japan; United States', 'CA, US, MX, JP',
                'Mexico, Japan, India, Canada, European Union', 'IT', 'All',
                'United States; Mexico; Canada; Japan; European Union; India; ;',
                'United States; Mexico; Canada; Japan; European Union; China', 'Germany', 'European Union, Turkey',
                'CA', 'UK', 'EU, JP, MX, US', 'United States; Mexico; Canada;  European Union;', 'EU, IN, JP', 'EU, IN',
                'EU/JP/MX', 'United States; Mexico; India; Canada; Japan; European Union;',
                'United States, Canada, Mexico', 'United States; Canada; Japan; European Union;', 'US/CA',
                'United States; Mexico; Canada; Japan; European Union; India,', 'EU, JP, MX', 'US/Canada',
                'United States; Mexico; Canada; Japan; European Union; India; china; Turkey',
                'United States (California)', 'European Union,', 'United States; Canada; European Union; UK',
                'United States; Mexico; Canada; Japan; European Union; India; China;',
                'United States; Mexico; Canada; Japan; European Union;India; Turkey', 'Italy',
                'Canada (British Columbia)', 'Canada; European Union; India; Japan; Mexico; United States',
                'Canada; China; European Union; India; Japan; Mexico; United States', 'Canada; Mexico; United States']


COUNTRY_DICT = {'US, CA': ['CA', 'US'], 'EU': ['UK', 'DE', 'FR', 'IT', 'ES'], 'United States/ Canada': ['CA', 'US'],
                'United States; Mexico; Canada; European Union, Japan, India': ['UK', 'DE', 'FR', 'IT', 'ES', 'CA',
                                                                                'US'],
                'United States; Mexico; India; Canada; Japan; European Union; China': ['UK', 'DE', 'FR', 'IT', 'ES',
                                                                                       'CA', 'US'],
                'EU,US,CAN': ['UK', 'DE', 'FR', 'IT', 'ES', 'CA', 'US'],
                'United States; Mexico; Canada; Japan; European, India': ['UK', 'DE', 'FR', 'IT', 'ES', 'CA', 'US'],
                'US': ['US'], 'United States;': ['US'],
                'France; Germany; Italy; Spain; United Kingdom': ['UK', 'DE', 'FR', 'IT', 'ES'],
                'United States; Mexico; Canada; Japan; European Union; India; Turkey': ['UK', 'DE', 'FR', 'IT', 'ES',
                                                                                        'CA', 'US'],
                'United States; Mexico; Canada; Japan; European Union; India;': ['UK', 'DE', 'FR', 'IT', 'ES', 'CA',
                                                                                 'US'],
                'European Union': ['UK', 'DE', 'FR', 'IT', 'ES'],
                'EU,US,CA': ['UK', 'DE', 'FR', 'IT', 'ES', 'CA', 'US'],
                'United States; Mexico; Canada; Japan; European Union; India;  Turkey': ['UK', 'DE', 'FR', 'IT', 'ES',
                                                                                         'CA', 'US'],
                'United States; Mexico; Canada; Japan; European Union; India': ['UK', 'DE', 'FR', 'IT', 'ES', 'CA',
                                                                                'US'],
                'United States; Mexico; Canada; Japan; European Union; India; Singapore, Australia': ['UK', 'DE', 'FR',
                                                                                                      'IT', 'ES', 'CA',
                                                                                                      'US'],
                'Canada': ['CA'], 'GE': ['DE'],
                'United States; Mexico; Canada; Japan; European Union; India; ,': ['UK', 'DE', 'FR', 'IT', 'ES', 'CA',
                                                                                   'US'],
                'United States; Canada; European Union, Mexico, Japan, India': ['UK', 'DE', 'FR', 'IT', 'ES', 'CA',
                                                                                'US'],
                'US, CA, JP, EU, IN': ['UK', 'DE', 'FR', 'IT', 'ES', 'CA', 'US'],
                'United States (California market only)': ['US'], 'EU, IN, US': ['UK', 'DE', 'FR', 'IT', 'ES', 'US'],
                'FR': ['FR'], 'United States': ['US'], 'United States; Mexico; Canada;': ['CA', 'US'],
                'United States; Mexico; Canada; Japan; European Union; India; China, Turkey': ['UK', 'DE', 'FR', 'IT',
                                                                                               'ES', 'CA', 'US'],
                'DE': ['DE'],
                'United States; Mexico; Canada; Japan; European Union; India; , Turkey': ['UK', 'DE', 'FR', 'IT', 'ES',
                                                                                          'CA', 'US'],
                'US, CA, MX': ['CA', 'US'], 'Canada; European Union': ['UK', 'DE', 'FR', 'IT', 'ES', 'CA'],
                'United Kingdom': ['UK'],
                'United States; Mexico; Canada; Japan; European Union; India; China;Turkey': ['UK', 'DE', 'FR', 'IT',
                                                                                              'ES', 'CA', 'US'],
                'CA, CN, EU, IN, JP, MX, US': ['UK', 'DE', 'FR', 'IT', 'ES', 'CA', 'US'],
                'EU, CA, US, JP, MX, IN': ['UK', 'DE', 'FR', 'IT', 'ES', 'CA', 'US'],
                'United States; Canada': ['CA', 'US'], 'United States-California': ['US'], 'US,CAN,MX': ['CA', 'US'],
                'United States; Mexico; Canada; ; European Union; India;': ['UK', 'DE', 'FR', 'IT', 'ES', 'CA', 'US'],
                'Canada; European Union; Japan; Mexico; United States': ['UK', 'DE', 'FR', 'IT', 'ES', 'CA', 'US'],
                'United States; Mexico; Canada; European Union': ['UK', 'DE', 'FR', 'IT', 'ES', 'CA', 'US'],
                'England': ['UK'],
                'United States; Mexico; Canada; Japan; European Union;': ['UK', 'DE', 'FR', 'IT', 'ES', 'CA', 'US'],
                'United States; Mexico; Canada, European union, India, Japan': ['UK', 'DE', 'FR', 'IT', 'ES', 'CA',
                                                                                'US'],
                'United States; Mexico; Canada; Japan; European Union; India; ; Turkey': ['UK', 'DE', 'FR', 'IT', 'ES',
                                                                                          'CA', 'US'],
                'United States; Mexico; Canada; Japan; European Union; India; china': ['UK', 'DE', 'FR', 'IT', 'ES',
                                                                                       'CA', 'US'],
                'Canada; European Union; India; Mexico; Japan; United States': ['UK', 'DE', 'FR', 'IT', 'ES', 'CA',
                                                                                'US'],
                'Canada; European Union; Japan; United States': ['UK', 'DE', 'FR', 'IT', 'ES', 'CA', 'US'],
                'CA, US, MX, JP': ['CA', 'US'],
                'Mexico, Japan, India, Canada, European Union': ['UK', 'DE', 'FR', 'IT', 'ES', 'CA', 'US'],
                'IT': ['IT'], 'All': ['UK', 'DE', 'FR', 'IT', 'ES', 'CA', 'US'],
                'United States; Mexico; Canada; Japan; European Union; India; ;': ['UK', 'DE', 'FR', 'IT', 'ES', 'CA',
                                                                                   'US'],
                'United States; Mexico; Canada; Japan; European Union; China': ['UK', 'DE', 'FR', 'IT', 'ES', 'CA',
                                                                                'US'], 'Germany': ['DE'],
                'European Union, Turkey': ['UK', 'DE', 'FR', 'IT', 'ES'], 'CA': ['CA'], 'UK': ['UK'],
                'EU, JP, MX, US': ['UK', 'DE', 'FR', 'IT', 'ES', 'US'],
                'United States; Mexico; Canada;  European Union;': ['UK', 'DE', 'FR', 'IT', 'ES', 'CA', 'US'],
                'EU, IN, JP': ['UK', 'DE', 'FR', 'IT', 'ES'], 'EU, IN': ['UK', 'DE', 'FR', 'IT', 'ES'],
                'EU/JP/MX': ['UK', 'DE', 'FR', 'IT', 'ES'],
                'United States; Mexico; India; Canada; Japan; European Union;': ['UK', 'DE', 'FR', 'IT', 'ES', 'CA',
                                                                                 'US'],
                'United States, Canada, Mexico': ['CA', 'US'],
                'United States; Canada; Japan; European Union;': ['UK', 'DE', 'FR', 'IT', 'ES', 'CA', 'US'],
                'US/CA': ['CA', 'US'],
                'United States; Mexico; Canada; Japan; European Union; India,': ['UK', 'DE', 'FR', 'IT', 'ES', 'CA',
                                                                                 'US'],
                'EU, JP, MX': ['UK', 'DE', 'FR', 'IT', 'ES'], 'US/Canada': ['CA', 'US'],
                'United States; Mexico; Canada; Japan; European Union; India; china; Turkey': ['UK', 'DE', 'FR', 'IT',
                                                                                               'ES', 'CA', 'US'],
                'United States (California)': ['US'], 'European Union,': ['UK', 'DE', 'FR', 'IT', 'ES'],
                'United States; Canada; European Union; UK': ['UK', 'DE', 'FR', 'IT', 'ES', 'CA', 'US'],
                'United States; Mexico; Canada; Japan; European Union; India; China;': ['UK', 'DE', 'FR', 'IT', 'ES',
                                                                                        'CA', 'US'],
                'United States; Mexico; Canada; Japan; European Union;India; Turkey': ['UK', 'DE', 'FR', 'IT', 'ES',
                                                                                       'CA', 'US'], 'Italy': ['IT'],
                'Canada (British Columbia)': ['CA'],
                'Canada; European Union; India; Japan; Mexico; United States': ['UK', 'DE', 'FR', 'IT', 'ES', 'CA',
                                                                                'US'],
                'Canada; China; European Union; India; Japan; Mexico; United States': ['UK', 'DE', 'FR', 'IT', 'ES',
                                                                                       'CA', 'US'],
                'Canada; Mexico; United States': ['CA', 'US']}

if __name__ == '__main__':

    import re

    date = 'this is date 23/10/2019, 10.23.2019, 2019/10.23,sas '
    xref = "this is k Prüfgrundlage Test specification 16.01.2019"
    x = re.findall("([1-9]|1[0-9]|2[0-9]|3[0-1])(.|-)(0[1-9]|1[0-2])(.|-|)(20[0-9][0-9])", xref)
    print(x)
    y = re.findall("([0-9]{4})(-|/|.)(0[1-9]|1[0-2])(-|/|.)(0[1-9]|[1-2][0-9]|3[0-1])", xref)
    print(y)
    z = re.findall("([1-9]|1[0-9]|2[0-9]|3[0-1])(.|-)([1-9]|1[0-2])(.|-|)(20[0-9][0-9])", xref)
    print(z)
