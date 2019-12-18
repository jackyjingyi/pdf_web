import pandas as pd
import numpy as np
import nltk
from .analyze_class import keyword_modify
import re
import logging
import string
import os


BUG_LOG = []
FAIL_PATTERN = r'[Xx]'
NA_NR_PATTERN = r'(N/A|N/R)'


def predefine_(df):
    """

    :param df: list read from protocol : list
    :return: True if no two test name are identical, False otherwise
    """
  
    # normally if requirement is empty, then its bias

    df = pdf_df_rename(df)
    for i in df[df.requirement == ''].index:
        print(i)
        df = df.drop([i])
    df = df.reset_index(drop=True)
    print("checking if reset index", df.head())
    groupby_name = df.columns[0]
    print(groupby_name)
    # result = pd.concat(g for _,g in df.groupby(groupby_name) if len(g)>1)
    df.insert(loc=0,
              value=df[groupby_name].apply(lambda x: re.sub('[\n\t]', '', ' '.join(keyword_modify(x).lower().split()))),
              column='reitem')

    return df


def split_data_frame(*args, **kwargs):
    """
    split dataframe into two, according to certain value in specific column,
    slicing by row
    :param args:
    :param kwargs:
    :return: df1: true, df2: false
    """
    pass


def pdf_df_rename(df):
    if df.shape[1] == 4:
        df.columns = ['test_item', 'test_method', 'requirement', 'result']
    elif df.shape[1] == 5:
        df.columns = ['test_item', 'requirement', 'pass', 'fail', 'comment']
    elif df.shape[1] == 6:
        df.columns = ['test_item', 'country', 'requirement', 'pass', 'fail', 'comment']
    return df


def get_protocol(p, path, guess=True, customise=False, idx=1):
    """
     select protocol based on FirstPage into attr
    :param p: str: attr['protocol']
    :param path: dir contains all protocol files
    :param guess: if guess true, search for key word if cannot perfect match
    :param customise: if true, let user enter protocol name
    :return: protocol excel file address
    """

    def get_key_word(p: str, idx):
        keyword = re.split('[-_]', p)[idx]
        print(keyword)
        return str(keyword)

    protocols = [i for i in os.listdir(path=path) if i[-4:-1] == 'xls']
    print(protocols)
    candidates = []
    keyword = get_key_word(p, idx)
    if customise:
        p = input("please enter protocol name: ")
        if p in protocols:
            return p
        else:
            print("cannot find entered protocol")
            return get_protocol(p, path=path, guess=True, customise=True)
    for _f in protocols:
        print(re.split('[-_]', _f))
        if _f[:-5] == p:
            # prefectly match
            logging.info("find prefectly matched candidate : %s" %_f)
            return _f
        else:
            if guess:
                if keyword in re.split('[-_]', _f):
                    candidates.append(_f)
                    
            else:
                pass

    return candidates


class Mapper:
    def __init__(self, df):
        """

        :param df: dataframe extracted from protocol
        """
        self.df = df
        self._col = None
        self._row = None
        self.shape = df.shape
        self.is_predo = False
        self.df.columns = ['test_item', 'country', 'test_method', 'requirement', 'section']

    @property
    def col(self):
        return self.df.shape[1]

    @property
    def row(self):
        return self.df.shape[0]

    def duplicate_data_frame(self):
        pass

    def pre_do(self):
        self.df[self.df.columns[0]] = self.df[self.df.columns[0]].apply(
            lambda x: ' '.join(keyword_modify(x).lower().split()))

    def predefine_checker_list(self, idx=0, merge=False, merge_idx=None):
        """

        :param idx: groupby columns and insert it into second col with name reitem
        :param merge: if True, concat merge_idx column then clean the str, insert this into second col with name reitem
        :param merge_idx: mainly (0,1)
        :return: df
        """
        if merge:
            try:
                assert isinstance(merge_idx, (list, tuple)), "merge_idx should be iterable not {%s}" % type(merge_idx)
            except AssertionError as e:
                BUG_LOG.append(e)
                print("merge_idx should be iterable not {%s}" % type(merge_idx))
                return
            if isinstance(merge_idx, (list, tuple)):
                self.df.insert(loc=0, value=self.df[self.df.columns[merge_idx[0]]].astype(str) + ' ' + self.df[
                    self.df.columns[merge_idx[1]]],
                               column='reitem')
                self.df.reitem = self.df.reitem.apply(
                    lambda x: re.sub('[\n\t]', '', ' '.join(keyword_modify(x).lower().split())))
                self.df.insert(loc=0, column='counts', value=0)
                self.df.insert(loc=self.col, column='scenario', value=None)
                self.df.insert(loc=self.col, column='page', value=0)
                self.df.insert(loc=self.col, column='comments', value=0)
                self.is_predo = True
                print("pre do is done", self.df.head())
        else:
            _name = self.df.columns[idx]
            print(_name)
            # result = pd.concat(g for _,g in df.groupby(groupby_name) if len(g)>1)
            self.df.insert(loc=0, value=self.df[_name].apply(lambda x: ' '.join(keyword_modify(x).lower().split())),
                           column='reitem')
            self.df.reitem = self.df.reitem.apply(
                lambda x: re.sub('[\n\t]', '', ' '.join(keyword_modify(x).lower().split())))
            self.df.insert(loc=0, column='counts', value=0)
            self.df.insert(loc=self.col, column='scenario', value='Missing')
            self.df.insert(loc=self.col, column='page', value=0)
            self.df.insert(loc=self.col, column='comments', value=0)
            self.is_predo = True
            print("pre do is done", self.df.head())
            print(self.df.reitem[:8].tolist())
        return self.df

    def verify_item(self, page_number, pdf_df, idx=0, ):
        """
        compare pdf_df column = idx with  reitem,
        :param page_number:
        :param pdf_df:
        :param idx:
        :return:
        """
        if not self.is_predo:
            if pdf_df.shape[1] == 5:
                self.predefine_checker_list()  # (merge=True, merge_idx=(0, 2))
            else:
                self.predefine_checker_list()
        # counts_before_verfiy
        c = self.df.counts.sum()
        print("current sum of protocol is ", c)
        print("checking", pdf_df.head())
        # check if pdf_df contains fail
        if pdf_df.shape[1] == 5:
            # 4 column last column contains "fail"
            check_items = pdf_df.reitem.tolist()
            print(check_items, type(check_items))
            pdf_df.insert(loc=pdf_df.shape[1], column='result_map', value=None)
            # result_map clean result column data
            pdf_df.result_map = pdf_df.result.apply(lambda x: ' '.join(keyword_modify(str(x)).lower().split()))
            print(pdf_df.result_map[:])
            check_fail = np.transpose(np.nonzero(pdf_df.result_map.str.contains('fail').tolist()))
            # check_fail is a numpy array in one dimension
            print(check_fail)
            if check_fail.size > 0:
                print("this is check item", check_items)
                # this page's data frame contains failures,
                fail_list = []
                un_fail_list = []
                for i in range(len(check_items)):
                    if i in check_fail:
                        fail_list.append(check_items[i])
                    else:
                        un_fail_list.append(check_items[i])
                print(type(fail_list[0]), un_fail_list)
                print("test ing")

                # due to unknown issue in pandas isin(),
                # it wont work when checking list too long or others? use str.contains do iteration,
                # however str.contains sacrifice efficiency, and take risk
                for i in fail_list:
                    _temp1 = self.df.reitem.isin([i])  # list [True, False]
                    print(_temp1)
                    self.df.loc[_temp1, 'counts'] += 1
                    self.df.loc[_temp1, 'scenario'] = 'fail'
                    logging.debug(" ")
                    print("should add this", i)
                    print(type(pdf_df.result[pdf_df['result_map'] == i]), pdf_df['result'])
                    print(pdf_df[pdf_df['reitem'].isin([i])].result)
                    try:
                        self.df.loc[_temp1, 'comments'] = pdf_df[pdf_df['reitem'].isin([i])].result.item()
                    except:
                        # duplicate error
                        c = pdf_df.index[pdf_df['reitem'].isin([i])].tolist()[0]
                        self.df.loc[_temp1, 'comments'] = pdf_df.result[c]
                    self.df.loc[_temp1, 'counts'] += 1
                    self.df.loc[_temp1, 'page'] = page_number
                for j in un_fail_list:
                    _temp2 = self.df.reitem.isin([j])  # list [True, False]
                    self.df.loc[_temp2, 'scenario'] = 'pass'
                    self.df.loc[_temp2, 'page'] = page_number
                    try:
                        self.df.loc[_temp2, 'comments'] = pdf_df[pdf_df['reitem'].isin([j])].result.item()
                    except:
                        # duplicate error
                        c = pdf_df.index[pdf_df['reitem'].isin([j])].tolist()[0]
                        self.df.loc[_temp2, 'comments'] = pdf_df.result[c]
                    self.df.loc[_temp2, 'counts'] += 1
            else:
                for j in check_items:
                    _temp2 = self.df.reitem.isin([j])  # list [True, False]
                    self.df.loc[_temp2, 'counts'] += 1
                    self.df.loc[_temp2, 'scenario'] = 'pass'
                    self.df.loc[_temp2, 'page'] = page_number
                    try:
                        self.df.loc[_temp2, 'comments'] = pdf_df[pdf_df['reitem'].isin([j])].result.item()
                    except:
                        # duplicate error
                        c = pdf_df.index[pdf_df['reitem'].isin([j])].tolist()[0]
                        self.df.loc[_temp2, 'comments'] = pdf_df.result[c]
        elif pdf_df.shape[1] == 6 or pdf_df.shape[1] == 7:
            # 5 columns and 6 columns, column is fail contains fail information and col comment contains failure reason
            check_items = pdf_df.reitem.tolist()  # checking items
            print("this is check item")
            print(check_items, type(check_items))
            print(pdf_df.fail.str.contains(FAIL_PATTERN).tolist())
            check_fail = np.transpose(np.nonzero(pdf_df.fail.str.contains(FAIL_PATTERN, na=False).tolist()))
            # check_fail is a numpy array
            print(check_fail)
            if check_fail.size > 0:
                print("this is check item", check_items)
                # this page's data frame contains failures,
                fail_list = []
                un_fail_list = []
                for i in range(len(check_items)):
                    if i in check_fail:
                        fail_list.append(check_items[i])
                    else:
                        un_fail_list.append(check_items[i])
                print(type(fail_list[0]), un_fail_list)
                print("test ing")
                # due to unknown issue in pandas isin(),
                # it wont work when checking list too long or others? use str.contains do iteration,
                # however str.contains sacrifice efficiency, and take risk
                for i in fail_list:
                    _temp1 = self.df.reitem.isin([i])  # list [True, False]
                    self.df.loc[_temp1, 'counts'] += 1
                    self.df.loc[_temp1, 'scenario'] = 'fail'
                    print("should add this", pdf_df.comment[pdf_df['reitem'] == i])
                    try:
                        self.df.loc[_temp1, 'comments'] = pdf_df[pdf_df['reitem'].isin([i])].comment.item()
                    except:
                        # duplicate error
                        c = pdf_df.index[pdf_df['reitem'].isin([i])].tolist()[0]
                        self.df.loc[_temp1, 'comments'] = pdf_df.comment[c]
                    self.df.loc[_temp1, 'page'] = page_number
                for j in un_fail_list:
                    _temp2 = self.df.reitem.isin([j])  # list [True, False]
                    self.df.loc[_temp2, 'counts'] += 1
                    self.df.loc[_temp2, 'scenario'] = 'pass'
                    self.df.loc[_temp2, 'page'] = page_number
                    try:
                        self.df.loc[_temp2, 'comments'] = pdf_df[pdf_df['reitem'].isin([j])].result.item()
                    except:
                        # duplicate error
                        c = pdf_df.index[pdf_df['reitem'].isin([j])].tolist()[0]
                        self.df.loc[_temp2, 'comments'] = pdf_df.comment[c]
            else:
                print(check_items)
                loc_number = {}
                for j in check_items:
                    print(j)
                    _temp2 = self.df.reitem.isin([j])  # list [True, False]
                    print("%%^^&checking_temp2", j, np.transpose(np.nonzero(_temp2)))
                    self.df.loc[_temp2, 'counts'] += 1
                    self.df.loc[_temp2, 'scenario'] = 'pass'
                    self.df.loc[_temp2, 'page'] = page_number
                    idx = pdf_df[pdf_df['reitem'] == j].index
                    print(idx)
                    if len(idx) > 1:
                        print(loc_number)
                        if j in loc_number.keys():
                            loc_number[j] += 1
                        else:
                            loc_number[j] = 0
                        print("idx is here")
                        print(idx, loc_number)
                        print(idx[loc_number[j]], pdf_df.loc[idx[loc_number[j]]].comment)
                        self.df.loc[_temp2, 'comments'] = pdf_df.loc[idx[loc_number[j]]].comment
                    else:
                        self.df.loc[_temp2, 'comments'] = pdf_df[pdf_df['reitem'] == j].comment.item()
        return self.df
