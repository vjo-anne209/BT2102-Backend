# This is an auto-generated Django model module.
# You'll have to do the following manually to clean this up:
#   * Rearrange models' order
#   * Make sure each model has one field with primary_key=True
#   * Make sure each ForeignKey and OneToOneField has `on_delete` set to the desired behavior
#   * Remove `managed = False` lines if you wish to allow Django to create, modify, and delete the table
# Feel free to rename the models, but don't rename db_table values or field names.
from django.db import models


class Adminuser(models.Model):
    adminid = models.IntegerField(db_column='adminID', primary_key=True)  # Field name made lowercase.
    adminpassword = models.CharField(db_column='adminPassword', max_length=30)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'adminuser'


class Book(models.Model):
    bookid = models.IntegerField(db_column='BookID', primary_key=True)  # Field name made lowercase.
    title = models.CharField(db_column='Title', max_length=100)  # Field name made lowercase.
    borrowerid = models.ForeignKey('Memberuser', models.DO_NOTHING, db_column='BorrowerID', blank=True, null=True)  # Field name made lowercase.
    availabilitystatus = models.IntegerField(db_column='availabilityStatus')  # Field name made lowercase.
    expectedduedate = models.DateField(db_column='expectedDueDate', blank=True, null=True)  # Field name made lowercase.
    reservationstatus = models.IntegerField(db_column='reservationStatus')  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'book'


class Fine(models.Model):
    memberid = models.ForeignKey('Memberuser', models.DO_NOTHING, db_column='memberID')  # Field name made lowercase.
    paymentno = models.IntegerField(db_column='paymentNo')  # Field name made lowercase.
    amount = models.DecimalField(max_digits=10, decimal_places=0)
    paymentmethod = models.CharField(db_column='paymentMethod', max_length=22, blank=True, null=True)  # Field name made lowercase.
    paymentstatus = models.CharField(db_column='paymentStatus', max_length=12, blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'fine'


class Memberuser(models.Model):
    memberid = models.IntegerField(db_column='memberID', primary_key=True)  # Field name made lowercase.
    memberpassword = models.CharField(db_column='memberPassword', max_length=30)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'memberuser'


class Reservation(models.Model):
    reserverid = models.ForeignKey(Memberuser, models.DO_NOTHING, db_column='reserverID')  # Field name made lowercase.
    bookid = models.ForeignKey(Book, models.DO_NOTHING, db_column='BookID')  # Field name made lowercase.
    reservationno = models.IntegerField(db_column='ReservationNo')  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'reservation'
