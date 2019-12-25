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
from .models import Document, MiningLog, TestDoc
from .forms import DocumentForm, TestDocForm
from django.views.decorators.csrf import csrf_protect
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.decorators import login_required
from django.views.generic import TemplateView
from django.contrib.auth.mixins import LoginRequiredMixin
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
    return render(request, 'dapsa/upload.html')


class SecretPage(LoginRequiredMixin, TemplateView):
    template_name = 'secret_page.html'


def upload(request):
    """
    upload a pdf file, store it into document & mininglog"""
    if request == "POST":
        form = DocumentForm(data=request.POST, files=request.FILES)
        print(request.FILES)
        if form.is_valid():
            new_doc = Document(
                description=request.POST['descrption'], pl=request['pl'], upload=request.FILES['upload'])
            new_doc.save()
            return redirect(reverse('upload'))

    else:
        form = DocumentForm()
    documents = Document.objects.all()
    return render(request, 'dapsa/upload.html', {'documents': documents,
                                                 'form': form
                                                 })


def list(request):
    # Handle file upload
    if request.method == 'POST':
        form = TestDocForm(request.POST, request.FILES)
        if form.is_valid():
            newdoc = TestDoc(docfile=request.FILES['docfile'])
            newdoc.save()

            # Redirect to the document list after POST
            return redirect(reverse('list'))
    else:
        form = TestDocForm()  # A empty, unbound form

    # Load documents for the list page
    documents = TestDoc.objects.all()

    # Render list page with the documents and the form
    return render(request, 'dapsa/list.html', {'documents': documents, 'form': form})


def pdf_analysis_main(docobject):
    # frist create an instance to Mining Queue, if there are workers avaliable, pop queue,
    # delete this records, (or create a status, change that status to mining)
    # => analyse pdf and change the MiningLog status continue to monitoring this record
    # step1 finish => display bascinfo and require users' confirmation
    # start step2, display chosen protocol
    # analyzing and mapping , change the mapped protocol records dynamically
    #
    pass


class PDFExtractionView(View):

    def get(self, request, *args, **kwargs):
        return HttpResponse('Hello world')
