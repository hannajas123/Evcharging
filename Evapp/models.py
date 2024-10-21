from django.db import models

# Create your models here.
class Login(models.Model):
    username=models.CharField(max_length=50)
    password=models.CharField(max_length=50)
    type=models.CharField(max_length=30)
class Evstation(models.Model):
    stationname=models.CharField(max_length=300)
    place=models.CharField(max_length=300)
    licenseno=models.CharField(max_length=500)
    phone=models.CharField(max_length=10)
    email=models.CharField(max_length=50)
    pincode=models.CharField(max_length=50)
    district=models.CharField(max_length=50)
    state=models.CharField(max_length=50)
    status=models.CharField(max_length=50)
    LOGIN=models.ForeignKey(Login,on_delete=models.CASCADE)
class Workers(models.Model):
    wname=models.CharField(max_length=300)
    place=models.CharField(max_length=300)
    gender=models.CharField(max_length=50)
    dob=models.CharField(max_length=50)
    phone=models.CharField(max_length=10)
    email=models.CharField(max_length=50)
    experience=models.CharField(max_length=50)
    qualification=models.CharField(max_length=50)
    certificate=models.CharField(max_length=50)
    photo=models.CharField(max_length=500)
    district=models.CharField(max_length=50)
    state=models.CharField(max_length=50)
    status=models.CharField(max_length=50)
    LOGIN=models.ForeignKey(Login,on_delete=models.CASCADE)
class Users(models.Model):
    uname=models.CharField(max_length=30)
    place=models.CharField(max_length=300)
    pincode=models.CharField(max_length=50)
    phone=models.CharField(max_length=10)
    email=models.CharField(max_length=50)
    photo=models.CharField(max_length=500)
    district=models.CharField(max_length=50)
    state=models.CharField(max_length=50)
    LOGIN=models.ForeignKey(Login,on_delete=models.CASCADE)
class Category(models.Model):
    categoryname=models.CharField(max_length=50)
class Complaints(models.Model):
    complaint=models.CharField(max_length=50)
    status=models.CharField(max_length=50)
    reply=models.CharField(max_length=50)
    date=models.CharField(max_length=50)
    type=models.CharField(max_length=50)
    LOGIN=models.ForeignKey(Login,on_delete=models.CASCADE)
class Feedback(models.Model):
    LOGIN=models.ForeignKey(Login,on_delete=models.CASCADE,default=1)
    feedback=models.CharField(max_length=50,default="")
    date=models.CharField(max_length=50,default="")
    type=models.CharField(max_length=30,default="")
    EVSTATIONS=models.ForeignKey(Evstation,on_delete=models.CASCADE,default=1)
class Slots(models.Model):
    EVSTATIONS=models.ForeignKey(Evstation,on_delete=models.CASCADE)
    date=models.CharField(max_length=50,default="")
    time=models.CharField(max_length=50,default="")
class Slotbooking(models.Model):
    SLOTS=models.ForeignKey(Slots,on_delete=models.CASCADE,default="")
    USER=models.ForeignKey(Users,on_delete=models.CASCADE,default="")
    status=models.CharField(max_length=30,default="")
    amount=models.CharField(max_length=50)
class Payment(models.Model):
    SLOTS=models.ForeignKey(Slots,on_delete=models.CASCADE)
    date=models.CharField(max_length=50)
    account_no=models.CharField(max_length=50)
class Post(models.Model):
    USER=models.ForeignKey(Users,on_delete=models.CASCADE)
    post=models.CharField(max_length=200)
    image=models.CharField(max_length=500)
    date=models.CharField(max_length=10)
class Chat(models.Model):
    FROMID=models.ForeignKey(Login,on_delete=models.CASCADE,default="",related_name="fuser")
    TOID=models.ForeignKey(Login,on_delete=models.CASCADE,default="",related_name="tuser")
    date=models.CharField(max_length=10)
    message=models.CharField(max_length=1000,default="")
class Comments(models.Model):
    USER=models.ForeignKey(Users,on_delete=models.CASCADE)
    POST=models.ForeignKey(Post,on_delete=models.CASCADE)
    comments=models.CharField(max_length=1000)
    date=models.CharField(max_length=10)
class Doubt(models.Model):
    USER=models.ForeignKey(Users,on_delete=models.CASCADE)
    WORKER=models.ForeignKey(Workers,on_delete=models.CASCADE)
    doubt=models.CharField(max_length=1000)
    reply=models.CharField(max_length=1000)
class Services(models.Model):
    WORKER=models.ForeignKey(Workers,on_delete=models.CASCADE)
    service=models.CharField(max_length=1000)
    servicecharge=models.CharField(max_length=100)
    date=models.CharField(max_length=100)
    location=models.CharField(max_length=100)
class Service_booking(models.Model):
    WORKER=models.ForeignKey(Workers,on_delete=models.CASCADE)
    USER=models.ForeignKey(Users,on_delete=models.CASCADE)
    SERVICE=models.ForeignKey(Services,on_delete=models.CASCADE)
    # type_of_service=models.CharField(max_length=100,default="")
    status=models.CharField(max_length=100,default="")




