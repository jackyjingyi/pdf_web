from django.db import models
import uuid

class Document(models.Model):
    caseid = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    description = models.CharField(max_length=255,blank=True)
    doc = models.FileField(upload_to='reports/%Y/%m/%d')
    uploaded_at = models.DateTimeField(auto_now_add=True)

class Protocols(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    protocol_name = models.CharField(max_length=200,verbose_name='Protocol Name',unique=True)
    short_cut = models.CharField(max_length=50)
    version = models.CharField(max_length=25)
    amazon_number = models.CharField(max_length=25)

class Protocol(models.Model):
    # if spec number, this can be a key identifier
    # else use {requirement_title , region, protocol_section}
    protocol_name = models.ForeignKey(Protocols, on_delete = models.CASCADE)
    speck_number = models.CharField(max_length=30, verbose_name='Speck Number', null=True)   
    regulation = models.TextField(verbose_name='Regulation')
    requirement_title = models.TextField(verbose_name='Requirement title')
    link = models.URLField(max_length=200)
    region = models.CharField(verbose_name='Region', max_length=100)
    test_method = models.TextField(verbose_name='Test Method')
    requirement = models.TextField(verbose_name='Requirement')
    protduct_scope = models.CharField(verbose_name='Product Scope',max_length=100)
    exemption = models.CharField(max_length=30, default='NA')
    protocol_section = models.CharField(max_length=100, null=False)
    mandatory_voluntary = models.CharField(max_length=30)
    is_cornerstone = models.BooleanField(verbose_name='Is Cornerstone', default=False)
    new_voluntary_safety_standard = models.TextField(verbose_name='New Voluntary Safety Standard',null=True)
    reationale = models.CharField(verbose_name='Reationale',max_length=50, null=True)
    upload_date = models.DateField(auto_now_add=True)


class MiningQueue(models.Model):
    """
    For multithreading, only store caseid, 
    controller will delete one record once hit start processing
    
    """
    sessionid = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    caseid = models.ForeignKey(Document, on_delete = models.CASCADE)


class MiningLog(models.Model):
    status = [
        ('1', 'Processing'),
        ('2', 'Success'),
        ('3', 'Fail'),
        ('4', 'Stop')
    ]
    caseid =models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    doc_id = models.ForeignKey(Document, related_name= "+",on_delete = models.SET_NULL, null= True)
    start_time = models.DateTimeField(auto_now_add=True, blank = True)
    stage1 = models.CharField(max_length=3, choices=status)
    stage2 = models.CharField(max_length=3, choices=status)
    end_time = models.DateTimeField(auto_now=True, blank = True)

    def restart(self):
        # if sucess for both stage => set stage1 & 2 =>(2) then reassign this doc to ExQ
        # elif Processing => set current stage to (4) then reassign 
        # elif Fail => set current stage to (3) then reassign
        pass 


class BasicInfo(models.Model):
    """
    caseid:ExtractionLog id

    """
    caseid = models.ForeignKey(MiningLog, on_delete = models.CASCADE)
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
    caseid = models.ForeignKey(MiningLog, on_delete = models.CASCADE)
    frequence = models.IntegerField(default = 0)
    phased_requirement_title = models.CharField(max_length = 200)
    requirement_title = models.ForeignKey(Protocol,related_name='requirement_title_r',on_delete = models.CASCADE)
    region = models.ForeignKey(Protocol,related_name='region_r',on_delete = models.CASCADE)
    protocol_section = models.ForeignKey(Protocol, related_name="protocol_section_r", on_delete= models.CASCADE)
    scenario = models.CharField(max_length = 3 , choices=Scenarios)
    page = models.IntegerField(default = 0)
    reasons = models.TextField()  # reasons from pdf report
    comments = models.TextField() # editable for user adds on
    
class ExtractionLog(models.Model):
    """
    Processing log: in extraction stage"""
    pass


class MappingLog(models.Model):
    """
    Logs of Mapping stage =>(stage2)"""
    pass



