from django.shortcuts import render
# from django.http import HttpResponse
from django.http import HttpResponse, HttpResponseRedirect, Http404
from django.contrib import messages

from .forms import TicketRequestForm,TicketAckForm,TicketStartForm,TicketFinishForm,TicketCommentForm
from .models import Ticket
from .models import Log
from .models import Machine,Machine_type

import datetime
from django.db.models import Count,Sum,Value

# Create your views here.

def index(request):
	machine_obj =Machine_type.objects.all()
	s = Machine.objects.all().values('machine_type','status').annotate(number=Count('name'))
	return render(request, 'index.html', {'objs': machine_obj,'machines':s})
	# return HttpResponse("Hello I am Machine Man")

def pending(request):
	pending_obj =Ticket.objects.filter(status='PENDING').order_by('created_date')
	return render(request, 'pending.html', {'obj': pending_obj})

def pending_repair(request):
	pending_obj =Ticket.objects.all().order_by('created_date')
	return render(request, 'pending_repair.html', {'obj': pending_obj})

def acknowledge(request,id):
	obj =Ticket.objects.get(id=id)
	# 'print (obj)
	if request.method == 'POST':
		form = TicketAckForm(request.POST)
		if form.is_valid():
			details = form.cleaned_data['details']
			# next_page = form.cleaned_data['next_page']


			obj.status='ACK'
			obj.ack_date = datetime.datetime.now()
			obj.save()

			mc = Machine.objects.get(name=obj.machine.name)
			mc.status='REPAIR'
			mc.save()

			
			# obj.update(status='ACK',ack_date=datetime.datetime.now())
			# Update Logs
			Log.objects.create(ticket=obj,log_type='ACK',comment=details,user=request.user)

			print(request.META.get('HTTP_REFERER'))

			return HttpResponseRedirect('../repair')
	else:
		next_page = request.META.get('HTTP_REFERER')
		form = TicketAckForm()

	return render(request, 'acknowledge.html', {'form': form,'obj':obj,'next_page':next_page})

def startRepair(request,id):
	obj =Ticket.objects.get(id=id)
	# 'print (obj)
	if request.method == 'POST':
		form = TicketStartForm(request.POST)

		if form.is_valid():
			details = form.cleaned_data['details']
			target = form.cleaned_data['target']
			
			obj.status='WORKING'
			obj.target_date = target
			obj.save()

			# mc = Machine.objects.get(name=machine)
			# mc.status='REPAIR'
			# mc.save()

			
			# obj.update(status='ACK',ack_date=datetime.datetime.now())
			# Update Logs
			Log.objects.create(ticket=obj,log_type='START',comment=details,user=request.user)


			return HttpResponseRedirect('../repair')
	else:
		form = TicketStartForm()

	return render(request, 'startRepair.html', {'form': form,'obj':obj})


def finishRepair(request,id):
	obj =Ticket.objects.get(id=id,status='WORKING')
	# 'print (obj)
	if request.method == 'POST':
		form = TicketFinishForm(request.POST)

		if form.is_valid():
			details = form.cleaned_data['details']
			
			obj.status='CLOSED'
			obj.finished_date = datetime.datetime.now()
			obj.save()

			mc = Machine.objects.get(name=obj.machine)
			mc.status='USED'
			mc.save()

			# Update Logs
			Log.objects.create(ticket=obj,log_type='FINISH',comment=details,user=request.user)


			return HttpResponseRedirect('../../repair')
	else:
		form = TicketFinishForm()

	return render(request, 'finishRepair.html', {'form': form,'obj':obj})

def commentRepair(request,id):
	obj =Ticket.objects.get(id=id,status='WORKING')
	log = Log.objects.filter(ticket=obj).order_by('modified_date')
	# 'print (obj)
	if request.method == 'POST':
		form = TicketCommentForm(request.POST)

		if form.is_valid():
			details = form.cleaned_data['details']

			# Update Logs
			Log.objects.create(ticket=obj,log_type='NOTE',comment=details,user=request.user)


			# return HttpResponseRedirect('.')
	else:
		form = TicketCommentForm()

	return render(request, 'commentRepair.html', {'form': form,'obj':obj,'logs':log})

def machineDetails(request,machine,id = None):

	log =None
	obj = None
	if id :
		m = Ticket.objects.get(id=id)
		obj =Ticket.objects.filter(machine__name=m.machine).order_by('created_date')
		r = obj.get(id=id)
		log = Log.objects.filter(ticket = r).order_by('modified_date')
	else :
		m = Ticket.objects.get(id=machine)
		obj =Ticket.objects.filter(machine__name=m.machine).order_by('created_date')
		log = Log.objects.filter(ticket = obj.last()).order_by('modified_date')
	return render(request, 'machine_details.html', {'objs':obj,'logs':log,'current_id':m})

def create(request):
	if request.method == 'POST':
		print ('User request is : %s' % request.user)
		form = TicketRequestForm(request.POST)
		# check whether it's valid:
		if form.is_valid():
			machine = form.cleaned_data['machine']
			symptom = form.cleaned_data['symptom']
			description = form.cleaned_data['details']

			obj =Ticket.objects.create(machine=machine,description=description,symptom=symptom,user=request.user)

			mc = Machine.objects.get(name=machine)
			mc.status='REPAIR'
			mc.save()
			
			# Update Logs
			Log.objects.create(ticket=obj,log_type='CREATE',comment=symptom,user=request.user)
			# # messages.error(request, 'Container : %s is upload successful' % obj.container_no)
			messages.success(request, 'Ticket created successful')

			return HttpResponseRedirect('/machine/repair')
	else:
		form = TicketRequestForm()

	return render(request, 'ticket.html', {'form': form})

