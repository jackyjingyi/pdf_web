import functools
from threading import Thread
import time


def check_first_page_with_dict(dict):
    def check_first_page(f):
        def first_page(*args, **kwargs):
            print(args, kwargs)
            try:
                assert args[0].pageid == dict[
                    1], 'Decorator Assertion Error: {} Not First Page, Not calling "{}"'.format(args[0], f.__name__)
                return f(*args, **kwargs)
            except AssertionError as e:
                print(e)

        return first_page

    return check_first_page


def check_not_first_page_with_dict(dict):
    def check_not_first_page(f):
        def not_first_page(*args, **kwargs):
            try:
                assert args[0].pageid != dict[
                    1], 'Decorator Assertion Error: {} This is First Page, Not calling "{}"'.format(args[0], f.__name__)
                return f(*args, **kwargs)
            except AssertionError as e:
                print('this is ', e)

        return not_first_page

    return check_not_first_page


def timeout(timeout):
    def deco(func):
        @functools.wraps(func)
        def wrapper(*args, **kwargs):
            res = [Exception('function [%s] timeout [%s seconds] exceeded!' % (func.__name__, timeout))]

            def newFunc():
                try:
                    res[0] = func(*args, **kwargs)
                except Exception as e:
                    res[0] = e

            t = Thread(target=newFunc)
            t.daemon = True
            try:
                t.start()
                t.join(timeout)
            except Exception as je:
                print('error starting thread')
                raise je
            ret = res[0]
            if isinstance(ret, BaseException):
                raise ret
            return ret

        return wrapper

    return deco


def controller():
    def build_controller(f):
        def build(**kwargs):
            """
            please select proper {args[0}
                1. item1;
                2. item2;
                3. item3;
            :param args:
            :param kwargs: item : list
            :return: selected item
            """
            if isinstance(kwargs['item'], list):
                if len(kwargs['item']) > 1:
                    print("please select prpoer %s, \n" % kwargs['name'])
                    for i in range(len(kwargs['item'])):
                        print(" \t %s. %s " % (i, kwargs['item'][i]))
                    result = input()
                    try:
                        assert isinstance(int(result), int)
                    except AssertionError:
                        return build(**kwargs)
                    kwargs['item'] = kwargs['item'][int(result)]
                    return f(**kwargs)
                else:
                    print(kwargs)
                    kwargs['item'] = kwargs['item'][0]
                    return f(**kwargs)
            elif isinstance(kwargs['item'], str):
                return f(**kwargs)
            return f(**kwargs)

        return build

    return build_controller


if __name__ == '__main__':
    @timeout(5)
    def test():
        print("start")
        for i in range(1, 6):
            time.sleep(1)
            print('{} has passed'.format(i))


    try:
        test()
    except:
        print('exceed')

    l = ['i love python', 'this is trick']


    @controller()
    def get_fuck(s, item=None, t=1):
        print(s)
        print(item)
        print(t)


    get_fuck('protocol', item=l)
