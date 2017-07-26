from django.db import models

# Create your models here.
class Machine_type(models.Model):
	name = models.CharField(max_length=50,primary_key=True)
	description = models.CharField(max_length=255,blank=True, null=True)
	created_date = models.DateTimeField(auto_now_add=True)
	modified_date = models.DateTimeField(blank=True, null=True,auto_now=True)
	user = models.ForeignKey('auth.User',blank=True,null=True)

	def __str__(self):
		return self.name

class Machine(models.Model):
	USED = 'USED'
	REPAIR ='REPAIR'
	PM = 'PM'
	STATUS_CHOICES = (
        (USED, 'Using'),
        (REPAIR, 'Repairing'),
        (PM,'Preventive Maintenance')
    )
	name = models.CharField(max_length=50,primary_key=True)
	model = models.CharField(verbose_name ='Model Name',max_length=50,blank=True, null=True)
	description = models.CharField(max_length=255,blank=True, null=True)
	machine_type = models.ForeignKey('Machine_type',
		on_delete = models.CASCADE, related_name='machine_list')
	status = models.CharField(max_length=10 ,choices=STATUS_CHOICES,default=USED)
	created_date = models.DateTimeField(auto_now_add=True)
	modified_date = models.DateTimeField(blank=True, null=True,auto_now=True)
	user = models.ForeignKey('auth.User',blank=True,null=True)

	def __str__(self):
		return self.name

class Ticket(models.Model):
	P = 'PENDING'
	A = 'ACK'
	W = 'WORKING'
	C ='CLOSED'
	STATUS_CHOICES = (
        (P, 'Pending'),
        (A, 'Acknowledge'),
        (W, 'Working'),
        (C, 'Closed'),
    )
	machine = models.ForeignKey('Machine', related_name='tickets')
	symptom =  models.CharField(max_length=255)
	description = models.TextField(max_length=255,blank=True, null=True)
	status = models.CharField(max_length=10 ,choices=STATUS_CHOICES,default=P)
	created_date = models.DateTimeField(auto_now_add=True)
	ack_date = models.DateTimeField(blank=True, null=True)
	target_date = models.DateTimeField(blank=True, null=True)
	finished_date = models.DateTimeField(blank=True, null=True)
	modified_date = models.DateTimeField(blank=True, null=True,auto_now=True)
	user = models.ForeignKey('auth.User',blank=True,null=True)

	def __str__(self):
		return ('%s -- %s' % (self.machine,self.symptom))


class Log(models.Model):
	C = 'CREATE'
	A = 'ACK'
	S = 'START'
	F = 'FINISH'
	P = 'POSTPONE'
	N = 'NOTE'
	LOG_CHOICES = (
        (C, 'Create'),
        (A,'Acknowledge'),
        (S,'Start'),
        (F, 'Finish'),
        (P, 'Postpone'),
        (N,'Notice'),
    )
	ticket = models.ForeignKey('Ticket', related_name='logs')
	log_type = models.CharField(max_length=10 ,choices=LOG_CHOICES,default=N)
	comment = models.TextField(blank=True, null=True)
	modified_date = models.DateTimeField(blank=True, null=True,auto_now=True)
	user = models.ForeignKey('auth.User',blank=True,null=True)

class Pm(models.Model):
	P = 'PENDING'
	C ='CLOSED'
	STATUS_CHOICES = (
        (P, 'Pending'),
        (C, 'Closed'),
    )
	machine = models.ForeignKey('Machine', related_name='pms')
	description = models.TextField(blank=True, null=True)
	planed_date = models.DateTimeField(blank=True, null=True)
	finished_date = models.DateTimeField(blank=True, null=True)
	created_date = models.DateTimeField(auto_now_add=True)
	status = models.CharField(max_length=10 ,choices=STATUS_CHOICES,default=P)
	modified_date = models.DateTimeField(blank=True, null=True,auto_now=True)
	user = models.ForeignKey('auth.User',blank=True,null=True)



