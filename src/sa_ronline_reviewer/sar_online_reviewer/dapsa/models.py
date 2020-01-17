from django.db import models
from django.contrib.auth.models import User
import datetime
from datetime import date
import uuid
import os
import random
import logging

def pl_dirtory_path(instance, filename):

    return "reports/{0}/{1}".format(instance.pl, filename)


class SamplePool(models.Model):
    assign_status = [
        ('1', 'assigned'),
        ('2', 'rejected'),
        ('3', 'waiting'),
        ('4', 'reviewed'),
        ('5', 'complete not reviewed'),
    ]
    asin_types = [
        ('1','SPB'),
        ('2','HPB'),
        ('3','CPB'),
    ]
    parent_asin = models.CharField(max_length=50)
    region_id = models.IntegerField()
    marketplace_id = models.IntegerField()
    asin = models.CharField(max_length=50)
    ifdone = models.CharField(max_length=25, default="fresh")
    brand_code = models.CharField(max_length=25, null=True, blank=True)
    item_name = models.TextField(null=True, blank=True)
    style = models.CharField(max_length=25, null=True, blank=True)
    risk_level = models.IntegerField(null=True, blank=True)
    classification_type = models.CharField(
        max_length=50, null=True, blank=True)
    product_type = models.CharField(max_length=100, null=True, blank=True)
    brand_name = models.CharField(max_length=100, null=True, blank=True)
    product_group_description = models.CharField(
        max_length=100, null=True, blank=True)
    parent_asin_name = models.TextField(null=True, blank=True)
    # asin_creation_date = models.DateTimeField()
    edition = models.CharField(max_length=25)
    max_available_quantity = models.IntegerField(null=True, blank=True)
    min_available_quantity = models.IntegerField(null=True, blank=True)
    eod_available_quantity = models.IntegerField(null=True, blank=True)
    all_vendors = models.TextField(null=True, blank=True)
    first_vendor = models.CharField(max_length=25, null=True, blank=True)
    vendor_name = models.TextField(null=True, blank=True)
    sub_parent_asin_number = models.IntegerField(null=True, blank=True)
    ifpick = models.CharField(max_length=25, default="not pick")
    assign_date = models.DateTimeField(null=True, blank=True)  # 
    assign_status = models.CharField(max_length=25, choices=assign_status)
    assignee = models.CharField(max_length=100, null=True, blank=True)
    asin_type = models.CharField(max_length=25, choices=asin_types, null=True, blank=True)

    def assign_asin(number = 6, **kwargs):
        
        """
        assign asins to user by given number amount
        check if AsinAssign objects assign_date == today is not empty
        if len() == number * user.count: not calling this method
        else:callthis 
        return {
            user.id : [asin, asin, asin]
        }
        """
        _temp = {
            'SPB' : '1',
            'HPB' : '2',
            'CPB' : '3',
        }
        _task_type = kwargs['task_type']
        
        today_min = datetime.datetime.combine(datetime.date.today(), datetime.time.min)
        today_max = datetime.datetime.combine(datetime.date.today(), datetime.time.max)
        try:
            asins = AsinAssign.objects.filter(task_type = _temp[_task_type],assign_date__range=(today_min, today_max))
        except:
            logging.info("no asins for today's tasks")
            asins = []
        
        if not len(asins) == 0:
            # already assigned
            return 
        
        user = User.objects.all()  # filter(tasks = spb |hpb)
 
        asins = SamplePool.objects.filter(ifpick = "pick", assign_status = '3', ifdone = "fresh", asin_type = _temp[_task_type])
       
        idxs = set()
        while len(idxs)!= number * len(user):
            idxs.update([random.randrange(len(asins))])
        results = {}
        asins = [asins[i] for i in idxs]
        for u in user:
            results[u.id] = []
            while len(results[u.id])<number:
                current = asins.pop(0)
                results[u.id].append(current)
                current.assign_status = '1'
                AsinAssign(asin = current, assignee = u,assign_status = '1').save()
                if len(asins) == 0:
                    logging.warning("ASIN list is empty, check if sample size is not large enough")
                    break
        return results
    
    def assign_single(**kwargs):
        user = kwargs['user']
        number = kwargs['number']
        _task_type =kwargs['task_type']
        _temp = {
            'SPB' : '1',
            'HPB' : '2',
            'CPB' : '3',
        }
        asins = SamplePool.objects.filter(ifpick = "pick", assign_status = '3', ifdone = "fresh", asin_type = _temp[_task_type])
       
        idxs = set()
        while len(idxs)!= number:
            idxs.update([random.randrange(len(asins))])
        results = []
        asins = [asins[i] for i in idxs]
        
        while len(results)<number:
            current = asins.pop(0)
            results.append(current)
            current.assign_status = '1'
            AsinAssign(asin = current, assignee = user,assign_status = '1',task_type =_temp[_task_type] ).save()
            if len(asins) == 0:
                logging.warning("ASIN list is empty, check if sample size is not large enough")
                break
        return results

    def replacable(self):
        # check if this ASIN has more than itself's asins same parent asin, fresh, status ==3, 
        p_asin = self.parent_asin
        try:
            l_asins = SamplePool.objects.filter(parent_asin = p_asin, ifdone = "fresh", assign_status = '3',ifpick="not pick")
       
            return l_asins
        except:
            # empty
            return False

    def replace(self):
        # replace asin with anther random asin with same parent asin
        l_asins = self.replacable()
        if l_asins:
            idx = random.randrange(len(l_asins))
            self.assign_status = '2'  # add reject reason in futher
            self.ifpick = "not pick"
            new = l_asins[idx]
            new.ifpick = "pick"
            new.assign_status = '1'
            return new
        else:
            logging.info("No other asin in this parent asin")
            # need assign another aisn from different parent asin group
            return


class AsinAssign(models.Model):
    assign_status = [
        ('1', 'assigned'),
        ('2', 'rejected'),
        ('3', 'complete'),
    ]
    asin_types = [
        ('1','SPB'),
        ('2','HPB'),
        ('3','CPB'),
    ]
    asin = models.ForeignKey(SamplePool, on_delete=models.CASCADE)
    assignee = models.ForeignKey(User, on_delete=models.CASCADE)
    assign_date = models.DateTimeField(auto_now_add=True)
    update_time = models.DateTimeField(auto_now=True)
    assign_status = models.CharField(max_length=25, choices=assign_status)
    task_type = models.CharField(max_length=25, choices=asin_types, null=True, blank=True)

     
    def complete(self):
        self.assign_status = '3'
        asin = self.asin
        asin.assign_status = '4'
        p_asin = asin.parent_asin
        l_asins = SamplePool.objects.filter(parent_asin = p_asin)
        for a in l_asins:
            a.assign_status = '5'
            a.ifdone = "done"
        return

    def reject(self):
        self.assign_status = '2'
        asin = self.asin
        asin.assign_status = '2'
        pass


class TestDoc(models.Model):
    caseid = models.CharField(max_length=255)
    pl = models.CharField(max_length=255)
    docfile = models.FileField(upload_to=pl_dirtory_path)
    uploaded_at = models.DateTimeField(auto_now_add=True)
    uploaded_by = models.ForeignKey(
        User, on_delete=models.CASCADE, to_field="username")
    asin = models.CharField(max_length=25, null=True, blank=True)

    def filename(self):
        return os.path.basename(self.docfile.name)


class Protocols(models.Model):
    caseid = models.CharField(max_length=255, null=True, blank=True)
    protocol_name = models.CharField(
        max_length=200, verbose_name='Protocol Name', unique=True)
    short_cut = models.CharField(max_length=50, null=True, blank=True)
    version = models.CharField(max_length=25, null=True, blank=True)
    amazon_number = models.IntegerField(null=True, blank=True)
    uploaded_by = models.ForeignKey(User, on_delete=models.CASCADE)
    uploaded_date = models.DateTimeField(auto_now_add=True)
    updated_date = models.DateTimeField(auto_now=True)

    def __repr__(self):
        return self.protocol_name


class Protocol(models.Model):
    # if spec number, this can be a key identifier
    # else use {requirement_title , region, protocol_section}
    
    protocol_name = models.ForeignKey(
        Protocols, on_delete=models.CASCADE, to_field="protocol_name")
    
    speck_number = models.CharField(
        max_length=300, verbose_name='Speck Number', null=True, blank=True)
    regulation = models.TextField(
        verbose_name='Regulation', null=True, blank=True)
    requirement_title = models.TextField(
        verbose_name='Requirement title', null=True, blank=True)
    link = models.TextField(null=True, blank=True)
    region = models.TextField(verbose_name='Region',blank=True, null=True)
    test_method = models.TextField(
        verbose_name='Test Method', null=True, blank=True)
    requirement = models.TextField(
        verbose_name='Requirement', null=True, blank=True)
    protduct_scope = models.TextField(
        verbose_name='Product Scope', null=True,blank=True)
    exemption = models.TextField(default='NA', blank=True, null=True)
    protocol_section = models.TextField( null=True, blank=True)
    mandatory_voluntary = models.TextField(blank=True, null=True)
    is_cornerstone = models.BooleanField(
        verbose_name='Is Cornerstone', default=False)
    new_voluntary_safety_standard = models.TextField(
        verbose_name='New Voluntary Safety Standard', null=True, blank=True)
    reationale = models.CharField(
        verbose_name='Reationale', max_length=50, null=True, blank=True)
    inner_id = models.IntegerField(null=True, blank=True)
    upload_date = models.DateTimeField(auto_now_add=True)
    latest_update_date = models.DateTimeField(auto_now=True)
    uploaded_by_1 = models.ForeignKey(
        User, on_delete=models.CASCADE, related_name="uploaded")
    last_updated_by_1 = models.ForeignKey(
        User, on_delete=models.CASCADE, related_name="last_updated")

    def get_protocol_name(self):
        return self.protocol_name.protocol_name

class MiningQueue(models.Model):
    """
    For multithreading, only store caseid, 
    controller will delete one record once hit start processing

    """
    sessionid = models.UUIDField(
        primary_key=True, default=uuid.uuid4, editable=False)
    caseid = models.ForeignKey(TestDoc, on_delete=models.CASCADE)


class MiningLog(models.Model):
    status = [
        ('1', 'Processing'),
        ('2', 'Success'),
        ('3', 'Fail'),
        ('4', 'Stop')
    ]
    caseid = models.UUIDField(
        primary_key=True, default=uuid.uuid4, editable=False)
    doc_id = models.ForeignKey(
        TestDoc, related_name="+", on_delete=models.SET_NULL, null=True)
    start_time = models.DateTimeField(auto_now_add=True, blank=True)
    stage1 = models.CharField(max_length=3, choices=status)
    stage2 = models.CharField(max_length=3, choices=status)
    end_time = models.DateTimeField(auto_now=True, blank=True)

    def restart(self):
        # if sucess for both stage => set stage1 & 2 =>(2) then reassign this doc to ExQ
        # elif Processing => set current stage to (4) then reassign
        # elif Fail => set current stage to (3) then reassign
        pass


class BasicInfo(models.Model):
    """
    caseid:ExtractionLog id

    """
    caseid = models.ForeignKey(MiningLog, on_delete=models.CASCADE)
    asin = models.CharField(max_length=50)
    protocol = models.CharField(max_length=200)
    extract_report_date = models.CharField(max_length=100)
    vendor = models.CharField(max_length=200)
    factory = models.CharField(max_length=200)


class ConlusionInfo(models.Model):
    """
    use requirement_title + region should locate unique targe in protocol
    displaying final output (after mapping)
    """
    Scenarios = [
        ('1', 'Missing'),
        ('2', 'Pass'),
        ('3', 'Fail')
    ]
    caseid = models.ForeignKey(MiningLog, on_delete=models.CASCADE)
    frequence = models.IntegerField(default=0)
    phased_requirement_title = models.CharField(max_length=200)
    requirement_title = models.ForeignKey(
        Protocol, related_name='requirement_title_r', on_delete=models.CASCADE)
    region = models.ForeignKey(
        Protocol, related_name='region_r', on_delete=models.CASCADE)
    protocol_section = models.ForeignKey(
        Protocol, related_name="protocol_section_r", on_delete=models.CASCADE)
    scenario = models.CharField(max_length=3, choices=Scenarios)
    page = models.IntegerField(default=0)
    reasons = models.TextField()  # reasons from pdf report
    comments = models.TextField()  # editable for user adds on


class ExtractionLog(models.Model):
    """
    Processing log: in extraction stage"""
    pass


class MappingLog(models.Model):
    """
    Logs of Mapping stage =>(stage2)"""
    pass
