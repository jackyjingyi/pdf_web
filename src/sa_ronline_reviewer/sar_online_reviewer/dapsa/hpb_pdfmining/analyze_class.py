import re
import nltk
from nltk.stem.wordnet import WordNetLemmatizer
import string
import copy


def keyword_modify(a_string, special=False):
    'lower letter, no head or tail whitespace, return string without punctuations'
    a_string = re.sub(r'[\n\t]', '', re.sub(r'[\t\n]', '', a_string.strip()))
    temp = re.sub('_', '', re.sub('-', '', string.punctuation))
    if special:
        return a_string.translate(str.maketrans('', '', temp))
    else:
        return a_string.translate(str.maketrans('', '', string.punctuation)).strip()


def keyword_nltk(a_sting):
    'very slow'
    l = [WordNetLemmatizer().lemmatize(word.lower(), 'v') for word in nltk.word_tokenize(a_sting)]
    return l


def str_contains(target_str, check_str):
    """
    check if check str contains in target_str
    :param target_str: mother str
    :param check_str: child str
    :return: boolean
    """

    pass


def keyword_contains_in(keyword, target_str, split_mark=None, position=2, title=False):
    """
    Vendor Name: xyz.co,.ltd
    :param keyword: Vendor Name
    :param target_str: Vendor Name: xyz.co,.ltd
    :param split_mark: :
    :param position: 1 return before, 2 return after,
    :param position: True return title()
    :return: xyz.co,.ltd
    """

    def _modify(word, split_mark, title):
        if split_mark:
            if title:
                word = word.strip(split_mark).strip()
            else:
                word = word.strip()
        if title:
            return word.title()
        else:
            return word

    before_keyword, keyword, after_keyword = target_str.strip().lower().partition(keyword.lower())

    if position == 1:
        return _modify(before_keyword, split_mark=split_mark, title=title)
    elif position == 2:
        return _modify(after_keyword, split_mark=split_mark, title=title)


def resove_dict(*args, **kwargs):
    """
    i totally forgot how this works, but
    :param args:
    :param kwargs:
    :return:
    """
    try:
        if isinstance(kwargs['the_dict'], dict):
            if len(args) >= kwargs['start']:
                print('current args are {} and at level {}:', args, kwargs['start'])
                return resove_dict(the_dict=kwargs['the_dict'][args[kwargs['start']]], *args, start=kwargs['start'] + 1)
            else:
                return kwargs['the_dict']
        else:
            return kwargs['the_dict']
    except KeyError:
        print('the key <{}> is not in {}, {} level'.format(
            args[kwargs['start']], kwargs['the_dict'], kwargs['start']
        ))
        return


def check_dict(*args, **kwargs):
    k = resove_dict(*args, **kwargs)
    if k:
        m = copy.deepcopy(k)
    else:
        return k
    if m:
        while len(m) > 0:
            current = m.pop(0)
            yield (current, kwargs['item'], current == kwargs['item'])


if __name__ == '__main__':

    from tag_keys import INFO_KEYS

    test_dict = {
        'key1': {'key2': {1: 'find me'}, },
        'keyx': [1, 2, 3],
    }

    kktest = resove_dict('key1', 'key2', 1, the_dict=test_dict, start=0)
    print(kktest)  # find me
    kktest1 = resove_dict('keyx', the_dict=test_dict, start=0)
    print(kktest1)  # [1,2,3]

    done = check_dict('vendor name', item='Vender Name', the_dict=INFO_KEYS, start=0)
    for do in done:
        print(do)
    print(keyword_modify('Language -\n Quebec'))
    print(re.sub('[\n\t]', '', ' '.join(keyword_modify('Language -\n Quebec').lower().split())))
    sh = keyword_contains_in(keyword='vEnder name', target_str='Vender Name: Beifa Group Co.,Ltd \n \n \n \n \n \n \n',
                             split_mark=":", title=True)
    print(sh)
