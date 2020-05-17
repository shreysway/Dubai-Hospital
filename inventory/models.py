from django.db import models

# Create your models here.

class Device(models.Model):

    Status = models.CharField(max_length=200, blank=False)
    DoctorName = models.CharField(max_length=200)

    TokenNo = models.CharField(max_length=50)
    issues = models.CharField(max_length=50)

    class Meta:
        abstract = True
    
    def __str__(self):
        return 'Status: {0} TokenNo: {1}'.format(self.Status, self.TokenNo)

class Desktops(Device):
    pass

class Laptops(Device):
    pass

class Mobiles(Device):
    pass


# class Desktops(models.Model):
#     status = models.CharField(max_length=200, blank=False)
#     doctorname = models.IntegerField()
#
#     roomno = (
#         ('SOLD', 'Item already purchased'),
#         ('AVAILABLE', 'Item ready to be purchased'),
#         ('RESTOCKING', 'Item restocking in few days')
#     )
#
#     status = models.CharField(max_length=10, roomno=roomno, default='SOLD')
#     issues = models.CharField(max_length=50, default="No Issues")
#
#     def __str__(self):
#         return 'status: {0} doctorname: {1}'.format(self.status, self.doctorname)
#
#
# class Laptops(models.Model):
#     status = models.CharField(max_length=200, blank=False)
#     doctorname = models.IntegerField()
#
#     roomno = (
#         ('SOLD', 'Item already purchased'),
#         ('AVAILABLE', 'Item ready to be purchased'),
#         ('RESTOCKING', 'Item restocking in few days')
#     )
#
#     status = models.CharField(max_length=10, roomno=roomno, default='SOLD')
#     issues = models.CharField(max_length=50, default="No Issues")
#
#     def __str__(self):
#         return 'status: {0} doctorname: {1}'.format(self.status, self.doctorname)
#
#
# class Mobiles(models.Model):
#     status = models.CharField(max_length=200, blank=False)
#     doctorname = models.IntegerField()
#
#     roomno = (
#         ('SOLD', 'Item already purchased'),
#         ('AVAILABLE', 'Item ready to be purchased'),
#         ('RESTOCKING', 'Item restocking in few days')
#     )
#
#     status = models.CharField(max_length=10, roomno=roomno, default='SOLD')
#     issues = models.CharField(max_length=50, default="No Issues")
#
#     def __str__(self):
#         return 'status: {0} doctorname: {1}'.format(self.status, self.doctorname)
