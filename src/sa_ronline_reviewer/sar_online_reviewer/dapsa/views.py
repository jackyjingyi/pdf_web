import re
import os
import time
import logging
import pandas as pd
import string
import pdfminer
from pdfminer.pdfparser import PDFParser
from pdfminer.pdfdocument import PDFDocument
from pdfminer.pdfpage import PDFTextExtractionNotAllowed
from pdfminer.pdfinterp import PDFResourceManager
from pdfminer.pdfinterp import PDFPageInterpreter
from pdfminer.layout import LAParams, LTChar, LTCurve, LTTextLine, LTText, LTTextBox, LTLine, LTRect, LTImage, \
    LTTextBoxHorizontal, LTPage
from pdfminer.converter import PDFPageAggregator
from pdfminer.pdfpage import PDFPage
from datetime import datetime
from openpyxl import Workbook, load_workbook
from openpyxl.utils import get_column_letter
from django.shortcuts import render

from hpb_pdfmining.pdf_layouts import Point, Cluster, Cell, Table, approxiamtion, inside
from hpb_pdfmining.tag_keys import SKIP_KEYS, BEGIN_KEYS, INFO_KEYS, DATE_PATTERN, MONTH
from hpb_pdfmining.mapper import predefine_, pdf_df_rename, get_protocol, Mapper
from hpb_pdfmining.analyze_class import check_dict, keyword_modify, keyword_contains_in, resove_dict
from hpb_pdfmining.main_decorators import timeout, check_first_page_with_dict, check_not_first_page_with_dict, controller
from hpb_pdfmining.extractors import FirstPageInfo, user_select_from_list, PDFExtractor, PageExtractor, checkpointsvaliadation, append_df_to_excel, find_key, find_right_neightbors


