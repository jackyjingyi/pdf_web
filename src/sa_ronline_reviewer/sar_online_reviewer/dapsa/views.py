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
from django.shortcuts import render, redirect
from django.urls import reverse
from django.http import HttpResponse
from django.views import View
from .models import Protocols
from .hpb_pdfmining.pdf_layouts import Point, Cluster, Cell, Table, approxiamtion, inside
from .hpb_pdfmining.tag_keys import SKIP_KEYS, BEGIN_KEYS, INFO_KEYS, DATE_PATTERN, MONTH
from .hpb_pdfmining.mapper import predefine_, pdf_df_rename, get_protocol, Mapper
from .hpb_pdfmining.analyze_class import check_dict, keyword_modify, keyword_contains_in, resove_dict
from .hpb_pdfmining.main_decorators import timeout, check_first_page_with_dict, check_not_first_page_with_dict, controller
from .hpb_pdfmining.extractors import FirstPageInfo, user_select_from_list, PDFExtractor, PageExtractor, checkpointsvaliadation, append_df_to_excel, find_key, find_right_neightbors
from .models import MiningLog, TestDoc, SamplePool, Protocols, Protocol
from .forms import TestDocForm
from django.views.decorators.csrf import csrf_protect
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.decorators import login_required
from django.views.generic import TemplateView
from django.contrib.auth.mixins import LoginRequiredMixin
from openpyxl import load_workbook
import uuid
"""
class to render or serilize the output to json and then pass it to frontend
1. input :  pdf address reference
2. 
"""


def home(request):
    count = User.objects.count()
    return render(request, 'home.html', {
        'count': count
    })


def signup(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('home')
    else:
        form = UserCreationForm()
    return render(request, 'registration/signup.html', {
        'form': form
    })


@login_required
def secret_page(request):
    asins = SamplePool.objects.filter(ifpick="pick")

    return render(request, 'secret_page.html', {'asins': asins})


class SecretPage(LoginRequiredMixin, TemplateView):
    template_name = 'secret_page.html'


def tasks(request):
    # Handle file upload
    if request.method == 'POST':

        form = TestDocForm(request.POST, request.FILES)
        if form.is_valid():
            temp_caseid = str(uuid.uuid4())

            newdoc = TestDoc(caseid=temp_caseid, pl=request.POST['pl'],
                             docfile=request.FILES['docfile'], uploaded_by=request.user)  # .save()

            newdoc.save()
            #excel_file = request.FILES['docfile']
            #wb = load_workbook(excel_file)
            #ws = wb.worksheets[0]
            #f = open('log.txt', 'w')
            # for row in ws.iter_rows(min_row=2, max_row=ws.max_row):
            #Protocols(protocol_name=row[0].value, short_cut=row[1].value, amazon_number=row[3].value,uploaded_by = request.user).save()

            # SamplePool(parent_asin=row[0].value, region_id=row[1].value, marketplace_id=row[2].value, asin=row[3].value,
            #           ifdone=row[4].value, brand_code=row[5].value, item_name=row[6].value, style=row[7].value, risk_level=row[8].value,
            #           classification_type=row[9].value, product_type=row[10].value, brand_name=row[
            #               11].value, product_group_description=row[12].value,
            #           parent_asin_name=row[13].value, edition=row[14].value,
            #           max_available_quantity=row[15].value, min_available_quantity=row[
            #               16].value, eod_available_quantity=row[17].value,
            #           all_vendors=row[18].value, first_vendor=row[19].value, vendor_name=row[
            #               20].value, sub_parent_asin_number=row[21].value,
            #           ifpick=row[22].value, assign_status='3').save()

            # Redirect to the document list after POST
            # try:
            #    current_protocol = Protocols.objects.get(
            #        protocol_name=row[1].value)
            #    idx = row[0].value
            #    if idx > len(Protocol.objects.all()):
            #        Protocol(protocol_name=current_protocol, speck_number=row[2].value, regulation=row[3].value,
            #                 requirement_title=row[4].value, link=row[5].value, region=row[6].value,  test_method=row[7].value,
            #                 requirement=row[8].value, protduct_scope=row[9].value, exemption=row[
            #                     10].value, protocol_section=row[11].value,
            #                 mandatory_voluntary=row[12].value, reationale=uuid.uuid4(), inner_id=row[13].value, is_cornerstone=True, uploaded_by_1=request.user, last_updated_by_1=request.user).save()
            #        print("saving")
            #    else:
            #        print("not saving")
            #    print(len(Protocol.objects.all()))
            # except:
            #    f.writelines([str(i.value)+',' for i in row]+['\n'])
            return redirect(reverse('tasks'))
    else:
        form = TestDocForm()  # A empty, unbound form

    # Load documents for the list page
    documents = TestDoc.objects.all()

    # Render list page with the documents and the form
    return render(request, 'dapsa/tasks.html', {'documents': documents, 'form': form})


def pdfmain(request, **kargs):
    caseid = request.path.split('/')[-2]
    print(caseid)
    document = TestDoc.objects.get(caseid=caseid)
    print(document)
    if document:
        results = pdf_analysis_main(document)
        print(results)
        if results['protocol']:
            current_protocol = results['protocol']
            # check if the protocol in db
            if current_protocol in [str(i.protocol_name) for i in Protocols.objects.all()]:
                p_obj = Protocols.objects.get(protocol_name=current_protocol)
                # corresponding protocol items
                protcol_item = Protocol.objects.filter(protocol_name_id=p_obj)
            else:
                # for check
                p_obj = Protocols.objects.get(amazon_number=21)
                protcol_item = Protocol.objects.filter(protocol_name_id=p_obj)
            return render(request, 'dapsa/analysis.html', {'document': document, 'dict': results, 'p_name':p_obj,'items': protcol_item})
        # return render(request, 'dapsa/analysis.html', {'document': document, 'dict': results})
    return render(request, 'dapsa/analysis.html', {'document': document})


def secret_page_protocol_audit(request):
    protocols = Protocols.objects.all()

    protocol_detail = Protocol.objects.filter(id__lt=10)
    print(protocol_detail)
    return render(request, 'secret_page_protocol.html', {'protocols': protocols, 'protocol_detail': protocol_detail})

    # return render(request, 'secret_page_protocol.html', {'protocols': protocols})


def pdf_analysis_main(doc):
    # frist create an instance to Mining Queue, if there are workers avaliable, pop queue,
    # delete this records, (or create a status, change that status to mining)
    # => analyse pdf and change the MiningLog status continue to monitoring this record
    # step1 finish => display bascinfo and require users' confirmation
    # start step2, display chosen protocol
    # analyzing and mapping , change the mapped protocol records dynamically
    #
    fp = doc.docfile.open('rb')
    pdf = PDFExtractor(fp)
    basicinfor = pdf.collect_first_page_info()
    return basicinfor


class PDFExtractionView(View):

    def get(self, request, *args, **kwargs):
        return HttpResponse('Hello world')
