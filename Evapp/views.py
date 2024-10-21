from django.http import HttpResponse, JsonResponse
from django.shortcuts import render

# Create your views here.
from .models import *
import datetime
import base64

def login(request):
    return render(request,'Login.html')
def login_post(request):
    username=request.POST["username"]
    password=request.POST["password"]
    obj=Login.objects.filter(username=username,password=password)
    if obj.exists():
        obj=Login.objects.get(username=username,password=password)
        if obj.type=='Admin':
            request.session['lid']=obj.id
            return HttpResponse('''<script>alert('login successfully');window.location='/Evapp/Admin_home/'</script>''')
        elif obj.type=='Evstation':
            request.session['lid']=obj.id
            return HttpResponse('''<script>alert('login successfully');window.location='/Evapp/Evstnhome/'</script>''')

    return HttpResponse('''<script>alert('Invalid username or password');window.location='/Evapp/login/'</script>''')

def logout(request):
    request.session['lid']=''
    return HttpResponse('''<script>alert('You  Logout Successfully');window.location='/Evapp/login/'</script>''')
def change_password(request):
    res=Login.objects.get(id=request.session['lid'])
    if request.session['lid']=='':
        return HttpResponse('''<script>alert('You  Logout Successfully');window.location='/Evapp/login/'</script>''')

    return render(request, 'Admin/changepassword.html', {'data':res})
def change_pswd_post(request):
    if request.session['lid']=='':
        return HttpResponse('''<script>alert('You  Logout Successfully');window.location='/Evapp/login/'</script>''')

    pass1 = request.POST["frstpwd"]
    pass2 = request.POST["currentpswd"]
    obj = Login.objects.get(id=request.session['lid'])
    # print(pass1)
    # print(obj.password)
    if obj.password == pass2:
        obj.password = pass1
        obj.save()
        return HttpResponse("<script>alert('You changed password');window.location='/Evapp/login/'</script>")
    else:
        return HttpResponse(
            "<script>alert('You cannot change password!!!!!!!!!!!!');window.location='/Evapp/change_password/'</script>")



############################################################Admin###################################################
def Admin_home(request):
    if request.session['lid']=='':
        return HttpResponse('''<script>alert('You  Logout Successfully');window.location='/Evapp/login/'</script>''')

    return render(request,'Adminindexhome.html')


def Add_category(request):
    if request.session['lid']=='':
        return HttpResponse('''<script>alert('You  Logout Successfully');window.location='/Evapp/login/'</script>''')

    return render(request,'Admin/Add category.html')
def Add_cate_post(request):
    if request.session['lid']=='':
        return HttpResponse('''<script>alert('You  Logout Successfully');window.location='/Evapp/login/'</script>''')

    category=request.POST["cname"]
    obj=Category()
    obj.categoryname=category
    obj.save()
    return HttpResponse("<script>alert('You Added a category');window.location='/Evapp/Add_category/'</script>")
def view_category(request):
    if request.session['lid']=='':
        return HttpResponse('''<script>alert('You  Logout Successfully');window.location='/Evapp/login/'</script>''')
    res=Category.objects.all()
    return render(request,'Admin/view category.html',{'data':res})
def search_category(request):
    if request.session['lid']=='':
        return HttpResponse('''<script>alert('You  Logout Successfully');window.location='/Evapp/login/'</script>''')

    srch=request.POST["search"]
    res=Category.objects.filter(categoryname__icontains=srch)
    return render(request,'Admin/view category.html',{'data':res})
def EditCategory(request,did):
    if request.session['lid']=='':
        return HttpResponse('''<script>alert('You  Logout Successfully');window.location='/Evapp/login/'</script>''')

    res=Category.objects.get(id=did)
    return render(request,'Admin/Edit category.html',{'data':res})
def edit_cate_post(request):
    if request.session['lid']=='':
        return HttpResponse('''<script>alert('You  Logout Successfully');window.location='/Evapp/login/'</script>''')

    category = request.POST["cname"]
    did=request.POST["did"]
    obj = Category.objects.get(id=did)
    obj.categoryname = category
    obj.save()
    return HttpResponse("<script>alert('You Updated the category');window.location='/Evapp/View_category/'</script>")
def Delete_category(request,did):
    res=Category.objects.get(id=did).delete()
    return HttpResponse("<script>alert('You Deleted the category');window.location='/Evapp/View_category/'</script>")



def manage_evStations(request):
    if request.session['lid']=='':
        return HttpResponse('''<script>alert('You  Logout Successfully');window.location='/Evapp/login/'</script>''')

    res=Evstation.objects.filter(status='pending')
    return render(request,'Admin/managestations.html',{'data':res})
def search_Ev(request):
    if request.session['lid']=='':
        return HttpResponse('''<script>alert('You  Logout Successfully');window.location='/Evapp/login/'</script>''')

    srch=request.POST["search"]
    res=Evstation.objects.filter(stationname__icontains=srch,status='pending')

    return render(request,'Admin/managestations.html',{'data':res})
def Approve_ev(request,did):
    if request.session['lid']=='':
        return HttpResponse('''<script>alert('You  Logout Successfully');window.location='/Evapp/login/'</script>''')

    res=Evstation.objects.filter(LOGIN=did).update(status='Approved')
    res=Login.objects.filter(id=did).update(type='Evstation')

    return HttpResponse("<script>alert('You Approved the Evstation');window.location='/Evapp/manage_ev/'</script>")
def Approved_stations(request):
    if request.session['lid']=='':
        return HttpResponse('''<script>alert('You  Logout Successfully');window.location='/Evapp/login/'</script>''')

    res=Evstation.objects.filter(status='Approved')
    return render(request,'Admin/view_Approved_stations.html',{'data':res})
def Search_Apprved_ev(request):
    if request.session['lid']=='':
        return HttpResponse('''<script>alert('You  Logout Successfully');window.location='/Evapp/login/'</script>''')

    srch = request.POST["search"]
    res = Evstation.objects.filter(stationname__icontains=srch,status='Approved')
    return render(request, 'Admin/view_Approved_stations.html', {'data': res})
def Reject_ev(request,did):
    if request.session['lid']=='':
        return HttpResponse('''<script>alert('You  Logout Successfully');window.location='/Evapp/login/'</script>''')

    res=Evstation.objects.filter(id=did).update(status='Rejected')
    return HttpResponse("<script>alert('You Rejected the Evstation');window.location='/Evapp/manage_ev/'</script>")
def RejectedStations(request):
    if request.session['lid']=='':
        return HttpResponse('''<script>alert('You  Logout Successfully');window.location='/Evapp/login/'</script>''')

    res=Evstation.objects.filter(status='Rejected')
    return render(request,'Admin/view_Rejected_stations.html',{'data':res})
def Search_Rjctd_ev(request):
    if request.session['lid']=='':
        return HttpResponse('''<script>alert('You  Logout Successfully');window.location='/Evapp/login/'</script>''')

    srch = request.POST["search"]
    res = Evstation.objects.filter(stationname__icontains=srch,status='Rejected')
    return render(request, 'Admin/view_Rejected_stations.html', {'data': res})




def manage_workers(request):
    if request.session['lid']=='':
        return HttpResponse('''<script>alert('You  Logout Successfully');window.location='/Evapp/login/'</script>''')

    res=Workers.objects.filter(status='Pending')
    return render(request,'Admin/manage_workers.html',{'data':res})
def Search_workers(request):
    if request.session['lid']=='':
        return HttpResponse('''<script>alert('You  Logout Successfully');window.location='/Evapp/login/'</script>''')

    srch = request.POST["search"]
    res = Workers.objects.filter(wname__icontains=srch,status='Pending')
    return render(request, 'Admin/manage_workers.html', {'data': res})
def verify_worker(request,did):
    if request.session['lid']=='':
        return HttpResponse('''<script>alert('You  Logout Successfully');window.location='/Evapp/login/'</script>''')

    res=Workers.objects.filter(id=did).update(status='Verified')
    return HttpResponse("<script>alert('You Verified the Worker');window.location='/Evapp/manage_workers/'</script>")
def verifyed_workers(request):
    if request.session['lid']=='':
        return HttpResponse('''<script>alert('You  Logout Successfully');window.location='/Evapp/login/'</script>''')

    res=Workers.objects.filter(status='Verified')
    return render(request,'Admin/View_verified_workers.html',{'data':res})
def Search_vrfyd_workers(request):
    srch = request.POST["search"]
    res = Workers.objects.filter(wname__icontains=srch,status='Verified')
    return render(request, 'Admin/View_verified_workers.html', {'data': res})
def reject_worker(request,did):
    if request.session['lid']=='':
        return HttpResponse('''<script>alert('You  Logout Successfully');window.location='/Evapp/login/'</script>''')

    res=Workers.objects.filter(id=did).update(status='Rejected')
    return HttpResponse("<script>alert('You Rejected the Worker');window.location='/Evapp/manage_workers/'</script>")
def Rejected_workers(request):
    if request.session['lid']=='':
        return HttpResponse('''<script>alert('You  Logout Successfully');window.location='/Evapp/login/'</script>''')

    res=Workers.objects.filter(status='Rejected')
    return render(request,'Admin/View_rejected_workers.html',{'data':res})
def Search_Rjctd_workers(request):
    if request.session['lid']=='':
        return HttpResponse('''<script>alert('You  Logout Successfully');window.location='/Evapp/login/'</script>''')

    srch = request.POST["search"]
    res = Workers.objects.filter(wname__icontains=srch,status='Rejected')
    return render(request, 'Admin/View_rejected_workers.html', {'data': res})


def view_users(request):
    if request.session['lid']=='':
        return HttpResponse('''<script>alert('You  Logout Successfully');window.location='/Evapp/login/'</script>''')

    res=Users.objects.all()
    return render(request,'Admin/view_users.html',{'data':res})
def Search_User(request):
    if request.session['lid']=='':
        return HttpResponse('''<script>alert('You  Logout Successfully');window.location='/Evapp/login/'</script>''')

    srch = request.POST["search"]
    res = Users.objects.filter(uname__icontains=srch)
    return render(request, 'Admin/view_users.html', {'data': res})


def view_feedback(request):
    if request.session['lid']=='':
        return HttpResponse('''<script>alert('You  Logout Successfully');window.location='/Evapp/login/'</script>''')

    res=Feedback.objects.all()
    return render(request,'Admin/view_feedback.html',{'data':res})
def Search_Feedback(request):
    if request.session['lid']=='':
        return HttpResponse('''<script>alert('You  Logout Successfully');window.location='/Evapp/login/'</script>''')

    fromd= request.POST["fromdate"]
    tod=request.POST["todate"]
    res = Feedback.objects.filter(date__range=[fromd,tod])
    return render(request, 'Admin/view_feedback.html', {'data': res})


def view_user_complaint_nd_reply(request):
    if request.session['lid']=='':
        return HttpResponse('''<script>alert('You  Logout Successfully');window.location='/Evapp/login/'</script>''')

    res=Complaints.objects.filter(type='User')
    return render(request,'Admin/View_user_complaint_nd_reply.html',{'data':res})
def Search_User_comp(request):
    if request.session['lid']=='':
         return HttpResponse('''<script>alert('You  Logout Successfully');window.location='/Evapp/login/'</script>''')

    fromd= request.POST["fromdate"]
    tod=request.POST["fromdate"]
    res = Complaints.objects.filter(date__range=[fromd,tod],type='User')
    return render(request, 'Admin/View_user_complaint_nd_reply.html', {'data': res})
def reply_user_com(request,did):
    if request.session['lid']=='':
        return HttpResponse('''<script>alert('You  Logout Successfully');window.location='/Evapp/login/'</script>''')

    res=Complaints.objects.get(id=did)
    return render(request,'Admin/Send_reply_user.html',{'data':res})
def send_reply_post_user(request):
    if request.session['lid']=='':
        return HttpResponse('''<script>alert('You  Logout Successfully');window.location='/Evapp/login/'</script>''')

    did=request.POST["did"]
    reply=request.POST["reply"]
    obj=Complaints.objects.get(id=did)
    obj.reply=reply
    obj.status='Replyed'
    obj.save()
    return HttpResponse("<script>alert('You Replyed to User Successfully');window.location='/Evapp/view_user_complaint_nd_reply/'</script>")

def view_worker_complaint_nd_reply(request):
    if request.session['lid']=='':
        return HttpResponse('''<script>alert('You  Logout Successfully');window.location='/Evapp/login/'</script>''')

    res=Complaints.objects.filter(type='Worker')
    return render(request,'Admin/View_worker_complait_nd_re[ly.html',{'data':res})
def Search_Worker_comp(request):
    if request.session['lid']=='':
        return HttpResponse('''<script>alert('You  Logout Successfully');window.location='/Evapp/login/'</script>''')

    fromd= request.POST["fromdate"]
    tod=request.POST["todate"]
    res = Complaints.objects.filter(date__range=[fromd,tod],type='Worker')
    return render(request, 'Admin/View_worker_complait_nd_re[ly.html', {'data': res})
def reply_worker_com(request,did):
    if request.session['lid']=='':
        return HttpResponse('''<script>alert('You  Logout Successfully');window.location='/Evapp/login/'</script>''')

    res=Complaints.objects.get(id=did)
    return render(request,'Admin/Send_reply_worker.html',{'data':res})
def send_reply_post_worker(request):
    if request.session['lid']=='':
        return HttpResponse('''<script>alert('You  Logout Successfully');window.location='/Evapp/login/'</script>''')

    did = request.POST["did"]
    reply = request.POST["reply"]
    obj = Complaints.objects.get(id=did)
    obj.reply = reply
    obj.status = 'Replyed'
    obj.save()
    return HttpResponse(
        "<script>alert('You Replyed to Worker Successfully');window.location='/Evapp/view_workers_complaint_nd_reply/'</script>")

def view_station_complaint_nd_reply(request):
    if request.session['lid']=='':
        return HttpResponse('''<script>alert('You  Logout Successfully');window.location='/Evapp/login/'</script>''')

    res = Complaints.objects.filter(type='Evstation')
    return render(request, 'Admin/View_Evcomplaints_nd_reply.html', {'data': res})

def Search_staion_comp(request):
    if request.session['lid']=='':
        return HttpResponse('''<script>alert('You  Logout Successfully');window.location='/Evapp/login/'</script>''')

    fromd = request.POST["fromdate"]
    tod = request.POST["todate"]
    res = Complaints.objects.filter(date__range=[fromd, tod], type='Evstation')
    return render(request, 'Admin/View_Evcomplaints_nd_reply.html', {'data': res})

def reply_Station_com(request, did):
    if request.session['lid']=='':
        return HttpResponse('''<script>alert('You  Logout Successfully');window.location='/Evapp/login/'</script>''')

    res = Complaints.objects.get(id=did)
    return render(request, 'Admin/Send_reply_ev.html', {'data': res})

def send_reply_post_station(request):
    if request.session['lid']=='':
        return HttpResponse('''<script>alert('You  Logout Successfully');window.location='/Evapp/login/'</script>''')

    did = request.POST["did"]
    reply = request.POST["reply"]
    obj = Complaints.objects.get(id=did)
    obj.reply = reply
    obj.status = 'Replyed'
    obj.save()
    return HttpResponse("<script>alert('You Replyed to Ev Station Successfully');window.location='/Evapp/view_Station_complaint_nd_reply/'</script>")

##################################################Evstation#######################################################

def home(request):
    if request.session['lid']=='':
        return HttpResponse('''<script>alert('You  Logout Successfully');window.location='/Evapp/login/'</script>''')

    return render(request,"EvstationHomeindex.html")


def signin(request):
    return render(request,"Evstation/Regindex.html")
def Signin_post(request):
    name=request.POST["evstn"]
    licno=request.POST["licno"]
    phn=request.POST["phone"]
    mail=request.POST["mail"]
    passwd=request.POST["passwd"]
    place=request.POST["place"]
    district=request.POST["district"]
    state=request.POST["state"]
    pincode=request.POST["pincode"]
    ob=Login()
    ob.username=mail
    ob.password=passwd
    ob.type="Pending"
    ob.save()
    obj=Evstation()
    obj.stationname=name
    obj.licenseno=licno
    obj.phone=phn
    obj.email=mail
    obj.place=place
    obj.district=district
    obj.state=state
    obj.pincode=pincode
    obj.LOGIN_id=ob.id
    obj.status="Pending"
    obj.save()
    return HttpResponse("<script>alert('You Registered Successfully...');window.location='/Evapp/login/'</script>")

def change_password_ev(request):
    if request.session['lid']=='':
        return HttpResponse('''<script>alert('You  Logout Successfully');window.location='/Evapp/login/'</script>''')

    res = Login.objects.get(id=request.session['lid'])
    return render(request, 'Evstation/change password.html', {'data': res})

def change_pswd_post_ev(request):
    if request.session['lid']=='':
        return HttpResponse('''<script>alert('You  Logout Successfully');window.location='/Evapp/login/'</script>''')

    pass1 = request.POST["frstpwd"]
    pass2 = request.POST["currentpswd"]
    obj = Login.objects.get(id=request.session['lid'])

    if obj.password == pass2:
        obj.password = pass1
        obj.save()
        return HttpResponse("<script>alert('You changed password');window.location='/Evapp/login/'</script>")
    else:
       return HttpResponse("<script>alert('You cannot change password!!!!!!!!!!!!');window.location='/Evapp/change_password_ev/'</script>")

def Addslot(request):
    if request.session['lid']=='':
        return HttpResponse('''<script>alert('You  Logout Successfully');window.location='/Evapp/login/'</script>''')

    res=Evstation.objects.all()
    return render(request,"Evstation/Add Slot.html",{'data':res})
def Addslot_post(request):
    if request.session['lid']=='':
        return HttpResponse('''<script>alert('You  Logout Successfully');window.location='/Evapp/login/'</script>''')

    time=request.POST["time"]
    date=request.POST["date"]
    obj=Slots()
    obj.EVSTATIONS=Evstation.objects.get(LOGIN_id=request.session['lid'])
    obj.time=time
    obj.date=date
    obj.save()
    return HttpResponse("<script>alert('You Added a Slot...');window.location='/Evapp/Addslot/'</script>")
def View_slot(request):
    if request.session['lid']=='':
        return HttpResponse('''<script>alert('You  Logout Successfully');window.location='/Evapp/login/'</script>''')

    res=Slots.objects.filter(EVSTATIONS__LOGIN_id=request.session['lid'])
    return render(request,"Evstation/view slot.html",{'data':res})
def Search_slots(request):
    if request.session['lid']=='':
        return HttpResponse('''<script>alert('You  Logout Successfully');window.location='/Evapp/login/'</script>''')

    fromd = request.POST["from"]
    tod = request.POST["to"]
    res = Slots.objects.filter(date__range=[fromd, tod],EVSTATIONS__LOGIN_id=request.session['lid'])
    return render(request,"Evstation/view slot.html",{'data':res})
def delete_slot(request,did):
    res=Slots.objects.get(id=did).delete()
    return HttpResponse("<script>alert('You Deleted a Slot...');window.location='/Evapp/View_slot/'</script>")
def edit_slot(request,did):
    if request.session['lid']=='':
        return HttpResponse('''<script>alert('You  Logout Successfully');window.location='/Evapp/login/'</script>''')

    res=Slots.objects.get(id=did)
    mm=Evstation.objects.all()
    return render(request,"Evstation/Edit slot.html",{'data':res,'data1':mm})
def Edit_slot_post(request):
    if request.session['lid']=='':
        return HttpResponse('''<script>alert('You  Logout Successfully');window.location='/Evapp/login/'</script>''')

    time = request.POST["time"]
    date = request.POST["date"]
    did=request.POST["id1"]
    obj = Slots.objects.get(id=did)
    obj.EVSTATIONS_id = Evstation.objects.get(LOGIN_id=request.session['lid'])
    obj.date = date
    obj.time = time
    obj.save()
    return HttpResponse("<script>alert('You Updated a Slot...');window.location='/Evapp/View_slot/'</script>")
def view_slot_booked(request):
    if request.session['lid']=='':
        return HttpResponse('''<script>alert('You  Logout Successfully');window.location='/Evapp/login/'</script>''')

    res=Slotbooking.objects.filter(status='Pending',SLOTS__EVSTATIONS__LOGIN_id=request.session['lid'])
    return render(request,"Evstation/view_slot_booking.html",{'data':res})
def approve_slots(request,did):
    if request.session['lid']=='':
        return HttpResponse('''<script>alert('You  Logout Successfully');window.location='/Evapp/login/'</script>''')

    res=Slotbooking.objects.filter(id=did).update(status='Approved')
    return HttpResponse("<script>alert('You Verified the Worker');window.location='/Evapp/view_slot_booked/'</script>")

def reject_slots(request,did):
    if request.session['lid']=='':
        return HttpResponse('''<script>alert('You  Logout Successfully');window.location='/Evapp/login/'</script>''')

    res=Slotbooking.objects.filter(id=did).update(status='Rejected')
    return HttpResponse("<script>alert('You Verified the Worker');window.location='/Evapp/view_slot_booked/'</script>")
def Search_booked_slots(request):
    if request.session['lid']=='':
        return HttpResponse('''<script>alert('You  Logout Successfully');window.location='/Evapp/login/'</script>''')

    fromd = request.POST["from"]
    tod = request.POST["to"]
    res = Slotbooking.objects.filter(SLOTS__date__range=[fromd, tod],SLOTS__EVSTATIONS__LOGIN_id=request.session['lid'])
    return render(request,'Evstation/view_slot_booking.html',{'data':res})
def View_Approved_slots(request):
    if request.session['lid']=='':
        return HttpResponse('''<script>alert('You  Logout Successfully');window.location='/Evapp/login/'</script>''')
    res=Slotbooking.objects.filter(status='Approved')
    return render(request,"Evstation/view_approved_slots.html",{'data':res})
def Approved_slot_search(request):
    if request.session['lid']=='':
        return HttpResponse('''<script>alert('You  Logout Successfully');window.location='/Evapp/login/'</script>''')

    fromd = request.POST["from"]
    tod = request.POST["to"]
    res = Slotbooking.objects.filter(SLOTS__date__range=[fromd, tod],status='Approved')
    return render(request,"Evstation/view_approved_slots.html",{'data':res})
def View_Rejected_slots(request):
    if request.session['lid']=='':
        return HttpResponse('''<script>alert('You  Logout Successfully');window.location='/Evapp/login/'</script>''')

    res=Slotbooking.objects.filter(status='Rejected')
    return render(request,"Evstation/view_rejected_slots.html",{'data':res})
def Rejected_slot_search(request):
    if request.session['lid']=='':
        return HttpResponse('''<script>alert('You  Logout Successfully');window.location='/Evapp/login/'</script>''')

    fromd = request.POST["from"]
    tod = request.POST["to"]
    res = Slotbooking.objects.filter(SLOTS__date__range=[fromd, tod],status='Rejected')
    return render(request,"Evstation/view_rejected_slots.html",{'data':res})
def View_users(request):
    if request.session['lid']=='':
        return HttpResponse('''<script>alert('You  Logout Successfully');window.location='/Evapp/login/'</script>''')

    res=Users.objects.all()
    return render(request,'Evstation/view_users.html',{'data':res})
def search_view_users(request):
    if request.session['lid']=='':
        return HttpResponse('''<script>alert('You  Logout Successfully');window.location='/Evapp/login/'</script>''')

    srch=request.POST["search"]
    res=Users.objects.filter(uname__icontains=srch)
    return render(request,'Evstation/view_users.html',{'data':res})
def Send_complaints(request):
    if request.session['lid']=='':
        return HttpResponse('''<script>alert('You  Logout Successfully');window.location='/Evapp/login/'</script>''')

    return render(request,"Evstation/Send_complaints.html")
def Send_comp_post(request):
    if request.session['lid']=='':
        return HttpResponse('''<script>alert('You  Logout Successfully');window.location='/Evapp/login/'</script>''')

    lid=request.session['lid']
    comp=request.POST["complaint"]
    from datetime import datetime
    date=datetime.now().date().today()
    obj=Complaints()
    obj.complaint=comp
    obj.date=date
    obj.status='Pending'
    obj.reply='Pending'
    obj.type='Evstation'
    obj.LOGIN=Login.objects.get(id=lid)
    obj.save()
    return HttpResponse("<script>alert('You Complainted Successfully...');window.location='/Evapp/Send_complaints/'</script>")
def View_reply(request):
    if request.session['lid']=='':
        return HttpResponse('''<script>alert('You  Logout Successfully');window.location='/Evapp/login/'</script>''')

    lid=request.session['lid']
    res=Complaints.objects.filter(LOGIN_id=lid)
    return render(request,"Evstation/view_reply.html",{'data':res})
def Search_View_reply(request):
    if request.session['lid']=='':
        return HttpResponse('''<script>alert('You  Logout Successfully');window.location='/Evapp/login/'</script>''')

    lid=request.session["lid"]
    fromd = request.POST["from"]
    tod = request.POST["to"]
    res = Complaints.objects.filter(date__range=[fromd, tod],LOGIN_id=lid)
    return render(request,"Evstation/view_reply.html",{'data':res})
def View_general_feedback(request):
    if request.session['lid']=='':
        return HttpResponse('''<script>alert('You  Logout Successfully');window.location='/Evapp/login/'</script>''')

    res=Feedback.objects.filter(type='general')
    return render(request,"Evstation/view_general_feedback.html",{'data':res})
def Search_general_feed(request):
    if request.session['lid']=='':
        return HttpResponse('''<script>alert('You  Logout Successfully');window.location='/Evapp/login/'</script>''')

    fromd = request.POST["from"]
    tod = request.POST["to"]
    res = Feedback.objects.filter(date__range=[fromd, tod],type='general')
    return render(request,"Evstation/view_general_feedback.html",{'data':res})
def view_user_feedback(request):
    if request.session['lid']=='':
        return HttpResponse('''<script>alert('You  Logout Successfully');window.location='/Evapp/login/'</script>''')

    lid=request.session['lid']
    res=Feedback.objects.filter(type='User',EVSTATIONS__LOGIN_id=lid)
    return render(request,"Evstation/view_user_feedback.html",{'data':res})
def Search_user_feed(request):
    if request.session['lid']=='':
        return HttpResponse('''<script>alert('You  Logout Successfully');window.location='/Evapp/login/'</script>''')

    lid=request.session['lid']
    fromd = request.POST["from"]
    tod = request.POST["to"]
    res = Feedback.objects.filter(date__range=[fromd, tod], type='Evstation',EVSTATIONS__LOGIN_id=lid)
    return render(request,"Evstation/view_user_feedback.html",{'data':res})
##################################chat##############################################################


def chat(request, toid):
    qry = Users.objects.get(LOGIN__id=toid)
    return render(request, "Evstation/Chat.html", {'photo': qry.photo, 'name': qry.uname, 'toid': toid})


def chat_view(request, tid):
    fromid = request.session["lid"]
    toid = tid
    qry = Users.objects.get(LOGIN__id=toid)
    from django.db.models import Q
    res = Chat.objects.filter(Q(FROMID=fromid, TOID=toid) | Q(FROMID=toid, TOID=fromid))
    l = []
    for i in res:
        l.append({"id": i.id, "message": i.message,"date": i.date, "from": i.FROMID.id})

    return JsonResponse({'photo': qry.photo, "data": l, 'name': qry.uname, 'toid': tid})


def chat_send(request, msg, tid):
    lid = request.session["lid"]
    toid = tid
    message = msg

    import datetime
    d = datetime.datetime.now().date()
    chatobt = Chat()
    chatobt.message = message
    chatobt.TOID_id = toid
    chatobt.FROMID_id = lid
    chatobt.date = d
    chatobt.save()

    return JsonResponse({"status": "ok"})
###################################################Workers########################################################
def signupworker_post(request):
    name = request.POST['name']
    dob = request.POST['dob']
    gender = request.POST['gender']
    email = request.POST['email']
    phone = request.POST['phone']
    experience = request.POST['experience']
    qualification = request.POST['qualification']
    place = request.POST['place']
    district = request.POST['district']
    state = request.POST['state']


    photo = request.POST['photo']

    import datetime
    import base64
    date = datetime.datetime.now().strftime("%Y%m%d-%H%M%S")
    a = base64.b64decode(photo)
    fh = open(r"C:\Users\Microsoft\PycharmProjects\Evcharging\media\photo\\" + date + ".jpg", "wb")
    path = "/media/photo/" + date + ".jpg"
    fh.write(a)
    fh.close()

    certificate = request.POST['certificate']
    import datetime
    import base64
    date1 = datetime.datetime.now().strftime("%Y%m%d-%H%M%S")
    b = base64.b64decode(certificate)
    fn = open(r"C:\Users\Microsoft\PycharmProjects\Evcharging\media\certi\\" + date1 + ".jpg", "wb")
    path1 = "/media/certi/" + date1 + ".jpg"
    fn.write(b)
    fn.close()

    password = request.POST['password']
    cpassword = request.POST['cpassword']

    if password == cpassword:
        lobj = Login()
        lobj.username = email
        lobj.password = cpassword
        lobj.type = 'Worker'
        lobj.save()

        uobj = Workers()
        uobj.wname = name
        uobj.dob = dob
        uobj.gender = gender
        uobj.phone = phone
        uobj.email = email
        uobj.experience=experience
        uobj.qualification=qualification
        uobj.photo = path
        uobj.certificate = path1
        uobj.place = place
        uobj.state = state
        uobj.district=district
        uobj.LOGIN = lobj
        uobj.status='pending'
        uobj.save()
        return JsonResponse({'status': 'ok'})
    else:
        return JsonResponse({'status': 'no'})
def login_worker_user_post(request):
    username = request.POST['username']
    password = request.POST['password']
    lobj = Login.objects.filter(username=username, password=password)
    if lobj.exists():
        lobjj = Login.objects.get(username=username, password=password)
        if lobjj.type == 'Worker':
            lid = lobjj.id

            return JsonResponse({'status': 'ok', 'lid': str(lid),'type':lobjj.type})
        elif lobjj.type == 'User':
            lid = lobjj.id

            return JsonResponse({'status': 'ok', 'lid': str(lid),'type':lobjj.type})
        else:
            return JsonResponse({'status': 'no'})
    else:
        return JsonResponse({'status': 'no'})
def change_password_worker_post(request):
    lid = request.POST["lid"]
    cpassword = request.POST["currentpassword"]
    npassword = request.POST["newpassword"]
    if Login.objects.filter(id=lid, password=cpassword).exists():

        obj = Login.objects.get(id=lid)
        obj.password = npassword
        obj.save()
        return JsonResponse({'status': 'ok'})
    else:
        return JsonResponse({'status': 'no'})
def add_service_post(request):
    lid=request.POST['lid']
    from datetime import datetime
    date=datetime.now().date().today()
    service=request.POST["service"]
    charge=request.POST["charge"]
    location=request.POST["location"]
    obj=Services()
    obj.service=service
    obj.servicecharge=charge
    obj.date=date
    obj.location=location
    obj.WORKER=Workers.objects.get(LOGIN_id=lid)
    obj.save()
    return JsonResponse({'status':'ok'})
def view_service_post(request):
    lid=request.POST['lid']
    res=Services.objects.filter(WORKER__LOGIN_id=lid)
    print(lid)
    l=[]
    for i in res:
        l.append({'id':i.id,'service':i.service,'charge':i.servicecharge,'date':i.date,'location':i.location})
        print(l)
    return JsonResponse({'status':'ok','data':l})
def edit_service_post(request):
    sid = request.POST['sid']
    i = Services.objects.get(id=sid)
    return JsonResponse({'status':'ok','id': i.id, 'service': i.service, 'servicecharge': i.servicecharge, 'date': i.date,
                  'location': i.location})
def updaate_service_post(request):
    lid=request.POST['lid']
    sid = request.POST['sid']
    from datetime import datetime
    date = datetime.now().date().today()
    service = request.POST["service"]
    charge = request.POST["charge"]
    location = request.POST["location"]
    obj = Services.objects.get(id=sid)
    obj.service = service
    obj.servicecharge = charge
    obj.date = date
    obj.location = location
    obj.WORKER = Workers.objects.get(LOGIN_id=lid)
    obj.save()
    return JsonResponse({'status': 'ok'})
def delete_service_post(request):
    sid=request.POST["sid"]
    res=Services.objects.get(id=sid).delete()
    return JsonResponse({'status':'ok'})

def view_profile_post(request):
    lid=request.POST['lid']
    i=Workers.objects.get(LOGIN_id=lid)

    return JsonResponse({'status':'ok','wname': i.wname,'gender':i.gender,'dob':i.dob,
              'email':i.email,'phone':i.phone,'place':i.place,
              'district':i.district,'state':i.state,'experience':i.experience,
              'qualification':i.qualification,
              'certificate':i.certificate,'photo':i.photo})
def update_workerprof(request):
    lid = request.POST['lid']
    i = Workers.objects.get(LOGIN_id=lid)

    return JsonResponse({'status': 'ok', 'wname': i.wname, 'gender': i.gender, 'dob': i.dob,
                         'email': i.email, 'phone': i.phone, 'place': i.place,
                         'district': i.district, 'state': i.state, 'experience': i.experience,
                         'qualification': i.qualification,
                         'certificate': i.certificate, 'photo': i.photo})

def edit_profile_post(request):
    lid = request.POST['lid']
    name = request.POST['name']
    dob = request.POST['dob']
    gender = request.POST['gender']
    email = request.POST['email']
    phone = request.POST['phone']

    experience = request.POST['experience']
    qualification = request.POST['qualification']
    place = request.POST['place']
    district = request.POST['district']
    state = request.POST['state']

    photo = request.POST['photo']

    print(photo, "hellloooooooo", "")
    if len(photo) > 0:



        a = base64.b64decode(photo)
        date = datetime.datetime.now().strftime("%Y%m%d-%H%M%S")
        fh = open(r"C:\Users\Microsoft\PycharmProjects\Evcharging\media\photo\\" + date + ".jpg", "wb")
        path = "/media/photo/" + date + ".jpg"
        fh.write(a)
        fh.close()
        res = Workers.objects.filter(LOGIN=lid).update(wname = name, dob=dob, gender=gender, phone=phone, email=email,
                                                       experience = experience,qualification = qualification,photo=path, place=place,state = state,  district=district)
        # return JsonResponse({'status': "ok"})
    certificate = request.POST['certificate']
    print(certificate,"heyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyy")
    if len(certificate) > 0:
        # import datetime
        # import base64


        print(certificate,"cerificate")
        date1 = datetime.datetime.now().strftime("%Y%m%d-%H%M%S")
        b = base64.b64decode(certificate)
        fn = open(r"C:\Users\Microsoft\PycharmProjects\Evcharging\media\certi\\" + date1 + ".jpg", "wb")
        path1 = "/media/certi/" + date1 + ".jpg"
        fn.write(b)
        fn.close()
        res = Workers.objects.filter(LOGIN=lid).update(wname = name, dob=dob, gender=gender, phone=phone, email=email,
                                                       experience = experience,qualification = qualification,certificate=path1, place=place,state = state,  district=district)
        # return JsonResponse({'status': "ok"})

    else:
         res = Workers.objects.filter(LOGIN=lid).update(wname = name, dob=dob, gender=gender, phone=phone, email=email,
                                                       experience = experience,qualification = qualification, place=place,state = state,  district=district)
    return JsonResponse({'status': "ok"})


def view_servicebooking_post_ndverify(request):
    lid=request.POST['lid']
    sid=request.POST['sid']
    res=Service_booking.objects.filter(WORKER__LOGIN=lid,status='pending')
    l=[]
    for i in res:
        l.append({'id':i.id,'service':i.SERVICE.service,'charge':i.SERVICE.servicecharge,'username':i.USER.uname})
    return JsonResponse({'status':'ok','data':l})
def Approve_booking_post(request):
    Sbid=request.POST['sid']
    res=Service_booking.objects.filter(id=Sbid).update(status='Approved')
    return JsonResponse({'status':'ok'})
def Reject_booking_post(request):
    Sbid=request.POST['sid']
    res=Service_booking.objects.filter(id=Sbid).update(status='Rejected')
    return JsonResponse({'status':'ok'})
def view_Approved_booking_post(request):
    lid=request.POST['lid']
    res = Service_booking.objects.filter(WORKER__LOGIN=lid, status='Approved')
    l = []
    for i in res:
        l.append({'id': i.id, 'service': i.SERVICE.service, 'charge': i.SERVICE.servicecharge, 'username': i.USER.uname,
                  })
    return JsonResponse({'status':'ok','data':l})
def view_rejected_booking_post(request):
    lid=request.POST['lid']
    res = Service_booking.objects.filter(WORKER__LOGIN=lid, status='Rejected')
    l = []
    for i in res:
        l.append({'id': i.id, 'service': i.SERVICE.service, 'charge': i.SERVICE.servicecharge, 'username': i.USER.uname,
                  })
    return JsonResponse({'status':'ok','data':l})

def view_user_doubts_post(request):
    lid=request.POST['lid']
    res=Doubt.objects.filter(WORKER__LOGIN_id=lid)
    l=[]
    for i in res:
        l.append({'id':i.id,'doubt':i.doubt,'user':i.USER.uname,'userid':i.USER.id,'reply':i.reply})
    return JsonResponse({'status':'ok','data':l})
def send_reply_doubts_post(request):
    lid=request.POST['lid']
    uid=request.POST['uid']
    did=request.POST['did']
    reply=request.POST['reply']
    obj=Doubt.objects.get(id=did)
    obj.reply=reply
    obj.USER=Users.objects.get(id=uid)
    obj.WORKER=Workers.objects.get(LOGIN_id=lid)
    obj.save()
    return JsonResponse({'status':'ok'})




#####################################################Users#########################################################
def signup_user_post(request):
    name = request.POST['name']
    email = request.POST['email']
    phone = request.POST['phone']

    pincode = request.POST['pincode']
    place = request.POST['place']
    district = request.POST['district']
    state = request.POST['state']

    photo = request.POST['photo']

    import datetime
    import base64
    #
    date = datetime.datetime.now().strftime("%Y%m%d-%H%M%S")
    a = base64.b64decode(photo)
    fh = open("C:\\Users\\Microsoft\\PycharmProjects\\AI_menu\\media\\" + date + ".jpg", "wb")
    path = "/media/" + date + ".jpg"
    fh.write(a)
    fh.close()



    password = request.POST['password']
    cpassword = request.POST['cpassword']

    if password == cpassword:
        lobj = Login()
        lobj.username = email
        lobj.password = cpassword
        lobj.type = 'User'
        lobj.save()

        uobj = Users()
        uobj.uname = name
        uobj.phone = phone
        uobj.email = email
        uobj.photo = path
        uobj.place = place
        uobj.state = state
        uobj.district = district
        uobj.pincode=pincode
        uobj.LOGIN = lobj
        uobj.save()
        return JsonResponse({'status': 'ok'})
    else:
        return JsonResponse({'status': 'no'})
def change_password_user_post(request):
    lid = request.POST["lid"]
    cpassword = request.POST["currentpassword"]
    npassword = request.POST["newpassword"]
    if Login.objects.filter(id=lid, password=cpassword).exists():

        obj = Login.objects.get(id=lid)
        obj.password = npassword
        obj.save()
        return JsonResponse({'status': 'ok'})
    else:
        return JsonResponse({'status': 'no'})
def view_profile_user_post(request):
    lid = request.POST['lid']
    i = Users.objects.get(LOGIN_id=lid)
    return JsonResponse({'status':'ok','uname':i.uname,
                         'email': i.email, 'phone': i.phone, 'place': i.place,
                         'district': i.district, 'state': i.state,
                         'pincode': i.pincode,
                          'photo': i.photo})
def update_User_profile(request):
    lid = request.POST['lid']
    i = Users.objects.get(LOGIN_id=lid)

    return JsonResponse({'status': 'ok', 'uname': i.uname,
                         'email': i.email, 'phone': i.phone, 'place': i.place,
                         'district': i.district, 'state': i.state,
                         'pincode': i.pincode,
                         'photo': i.photo})
def edit_profile_user_post(request):
    lid=request.POST['lid']
    name = request.POST['uname']
    email = request.POST['email']
    phone = request.POST['phone']

    pincode = request.POST['pincode']
    place = request.POST['place']
    district = request.POST['district']
    state = request.POST['state']

    photo = request.POST['photo']
    if len(photo) > 0:



        a = base64.b64decode(photo)
        date = datetime.datetime.now().strftime("%Y%m%d-%H%M%S")
        fh = open(r"C:\Users\Microsoft\PycharmProjects\Evcharging\media\photo\\" + date + ".jpg", "wb")
        path = "/media/photo/" + date + ".jpg"
        fh.write(a)
        fh.close()
        res = Users.objects.filter(LOGIN=lid).update(uname = name, pincode=pincode,  phone=phone, email=email,
                                                       photo=path, place=place,state = state,  district=district)
        # return JsonResponse({'status': "ok"})
    else:
        res = Users.objects.filter(LOGIN=lid).update(uname=name, pincode=pincode,  phone=phone, email=email,
                                                        place=place,
                                                       state=state, district=district)
    return JsonResponse({'status': "ok"})


def view_service_user_post(request):
    res = Services.objects.all()
    l = []
    for i in res:
        for i in res:
            l.append(
                {'id': i.id, 'service': i.service, 'charge': i.servicecharge, 'date': i.date, 'location': i.location})
    return JsonResponse({'status':'ok','data':l})
def view_worker_nd_bookservice_user_post(request):
    res = Workers.objects.filter(status='Verified')
    l = []
    for i in res:
        l.append(
            {'id': i.id, 'wname':i.wname,'photo':i.photo,'email':i.email,
             'place':i.place,'district':i.district,
             })

    return JsonResponse({'status':'ok','data':l})
def User_view_workerService_post(request):
    wid=request.POST['wid']
    print(wid)
    res = Services.objects.filter(WORKER_id=wid)
    l = []
    for i in res:
        l.append({'id': i.id, 'service': i.service, 'charge': i.servicecharge, 'date': i.date, 'location': i.location,'wkid':i.WORKER.id})
    return JsonResponse({'status':'ok','data':l})
def book_service_user_post(request):
    lid=request.POST['lid']
    sid=request.POST['sid']
    wid=request.POST['wkid']
    # type=request.POST['typeofservice']
    obj=Service_booking()
    obj.type_of_service=type
    obj.status='pending'
    obj.WORKER=Workers.objects.get(id=wid)
    obj.SERVICE=Services.objects.get(id=sid)
    obj.USER=Users.objects.get(LOGIN_id=lid)
    obj.save()
    return JsonResponse({'status':'ok'})

def view_worker_nd_service_status_user_post(request):
    lid = request.POST['lid']
    res = Service_booking.objects.filter(USER__LOGIN_id=lid)
    l = []
    for i in res:
        l.append({'id': i.id, 'service': i.SERVICE.service,
                  'charge': i.SERVICE.servicecharge, 'Worker': i.WORKER.wname,'wid':i.WORKER.id,
                  'date':i.SERVICE.date,'location':i.SERVICE.location,
                  'status':i.status})
    return JsonResponse({'status':'ok','data':l})

def add_doubts_user_post(request):
    lid=request.POST['lid']
    wid=request.POST['wid']
    doubt=request.POST['doubt']
    obj=Doubt()
    obj.USER=Users.objects.get(LOGIN_id=lid)
    obj.WORKER=Workers.objects.get(id=wid)
    obj.doubt=doubt
    obj.reply='Pending'
    obj.save()
    return JsonResponse({'status':'ok'})
def view_solution_doubt_user_post(request):
    lid = request.POST['lid']
    res = Doubt.objects.filter(USER__LOGIN_id=lid)
    l = []
    for i in res:
        l.append({'id': i.id, 'doubt': i.doubt,'worker':i.WORKER.wname,'reply':i.reply})
    return JsonResponse({'status': 'ok','data':l})

def upload_post_user_post(request):
    lid=request.POST['lid']
    post=request.POST['post']
    from datetime import datetime
    date1 = datetime.now().date().today()
    image=request.POST['photo']
    import datetime
    import base64
    #
    date = datetime.datetime.now().strftime("%Y%m%d-%H%M%S")
    a = base64.b64decode(image)
    fh = open(r"C:\Users\Microsoft\PycharmProjects\Evcharging\media\photo\\" + date + ".jpg", "wb")
    path = "/media/photo/" + date + ".jpg"
    fh.write(a)
    fh.close()
    obj=Post()
    obj.post=post
    obj.image=path
    obj.date=date1
    obj.USER=Users.objects.get(LOGIN_id=lid)
    obj.save()
    return JsonResponse({'status':'ok'})
def view_USERS_post(request):
    lid=request.POST['lid']
    res = Users.objects.exclude(LOGIN_id=lid)
    l = []
    for i in res:
        l.append(
            {'id': i.id, 'uname':i.uname,'photo':i.photo,'email':i.email,
             'place':i.place,'district':i.district,
             })

    return JsonResponse({'status':'ok','data':l})
def view_usersPOst_post(request):
    uid=request.POST['uid']
    res = Post.objects.filter(USER=uid)
    l = []
    for i in res:
        l.append({'id': i.id, 'post': i.post,
                  'photo': i.image, 'date': i.date,
                  'user': i.USER.uname,
                  })
    return JsonResponse({'status':'ok','data':l})

def view_comments_user_post(request):
    pid=request.POST['pid']
    res = Comments.objects.filter(POST_id=pid)
    l = []
    for i in res:
        l.append({'id': i.id, 'comments': i.comments,'pid':i.POST.id,
                   'date': i.date,
                  'user': i.USER.uname,
                  })
    return JsonResponse({'status':'ok','data':l})
def view_other_user_post(request):
    lid=request.POST['lid']
    res = Post.objects.exclude(USER__LOGIN_id=lid)
    l = []
    for i in res:
        l.append({'id': i.id, 'post': i.post,
                  'image': i.image, 'date': i.date,
                  'user': i.USER.uname,
                  })
    return JsonResponse({'status':'ok','data':l})
def add_comments_others_post(request):
    lid=request.POST['lid']
    pid=request.POST['pid']
    comments=request.POST['comments']
    from datetime import datetime
    date = datetime.now().date().today()
    obj=Comments()
    obj.USER=Users.objects.get(LOGIN_id=lid)
    obj.POST=Post.objects.get(id=pid)
    obj.comments=comments
    obj.date=date
    obj.save()
    return JsonResponse({'status':'ok'})

def view_ev_station_user_post(request):
    res=Evstation.objects.filter(status='Approved')
    l=[]
    for i in res:
        l.append({'id':i.id,'stname':i.stationname,
                  'licno':i.licenseno,'email':i.email,
                  'phone':i.phone,'place':i.place,
                  'district':i.district,'state':i.state,
                  'pin':i.pincode})
    return JsonResponse({'status':'ok','data':l})
def view_slots_of_ev_stations(request):
    evid=request.POST['evid']
    res=Slots.objects.filter(EVSTATIONS_id=evid)
    l=[]
    for i in res:
        l.append({'id':i.id,'evid':i.EVSTATIONS.id,'date':i.date})
        return JsonResponse({'status':'ok','data':l})
def bookslot_evstation_user_post(request):
    lid = request.POST['lid']
    sid = request.POST['sid']
    obj = Slotbooking()
    obj.amount= 300
    obj.status = 'pending'
    obj.SLOTS =Slots.objects.get(id=sid)
    obj.USER =Users.objects.get(LOGIN_id=lid)
    obj.save()
    return JsonResponse({'status':'ok'})

def view_booking_status_user_post(request):
    lid = request.POST['lid']
    res = Slotbooking.objects.filter(USER__LOGIN_id=lid)
    l = []
    for i in res:
        l.append({'id': i.id, 'amount': i.amount,'LOGIN_id':i.USER.LOGIN.id,
                  'evid':i.SLOTS.EVSTATIONS.LOGIN.id,
                  'evs': i.SLOTS.EVSTATIONS.stationname,
                  'place': i.SLOTS.EVSTATIONS.place,
                  'date': i.SLOTS.date,
                  'sid': i.SLOTS.id,
                  'status': i.status})
    return JsonResponse({'status': 'ok', 'data': l})
def send_complaints_user_post(request):
    lid = request.POST["lid"]
    from datetime import datetime
    date = datetime.now().date().today()
    complaint = request.POST["complaint"]
    status = "pending"
    reply = 'pending'
    cobj = Complaints()
    cobj.date = date
    cobj.complaint= complaint
    cobj.status = status
    cobj.reply = reply
    cobj.type='User'
    cobj.LOGIN=Login.objects.get(id=lid)
    cobj.save()
    return JsonResponse({'status':'ok'})
def view_reply_user_post(request):
    lid = request.POST['lid']
    sf = Complaints.objects.filter(LOGIN_id=lid)
    l = []
    for i in sf:
        l.append({'id': i.id, 'date': i.date, 'complaint': i.complaint, 'status': i.status, 'reply': i.reply,})
    return JsonResponse({'status': 'ok', 'data': l})
def send_feedback_about_evstation_user_post(request):
    ev=request.POST['evid']
    lid = request.POST["lid"]
    from datetime import datetime
    date = datetime.now().date().today()
    feedback = request.POST["feedback"]
    cobj = Feedback()
    cobj.date = date
    cobj.feedback = feedback
    cobj.type = 'User'
    cobj.LOGIN = Login.objects.get(id=lid)
    cobj.EVSTATIONS_id=ev
    cobj.save()
    return JsonResponse({'status':'ok'})



def user_sendchat(request):
    FROM_id=request.POST['from_id']
    TOID_id=request.POST['to_id']



    # print(FROM_id, TOID_id,"Lk")



    msg=request.POST['message']

    from  datetime import datetime
    c=Chat()
    c.FROMID_id=FROM_id
    c.TOID_id=TOID_id
    c.message=msg
    c.date=datetime.now()
    c.save()
    return JsonResponse({'status':"ok"})

def user_viewchat(request):
    from_id=request.POST['from_id']
    to_id=request.POST['to_id']
    # print(to_id)

    l=[]
    data1=Chat.objects.filter(FROMID_id=from_id,TOID_id=to_id).order_by('id')
    data2=Chat.objects.filter(FROMID_id=to_id,TOID_id=from_id).order_by('id')

    data= data1 | data2
    print(data)


    # data= Chat.objects.all()




    for res in data:
        l.append({'id':res.id,'from':res.FROMID.id,'to':res.TOID.id,'msg':res.message,'date':res.date})



    return JsonResponse({'status':"ok",'data':l})
