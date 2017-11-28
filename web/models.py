from django.db import models
#from django_summernote import models as summer_model
#from django_summernote import fields as summer_fields

# Create your models here.

# - Home
# - About
#     - Greeting(page)
#     - Member(list)
#     - Lab(list)
#     - Project(page)
# - Research
#     - Github(link)
#     - LectureNote(imagelist,video)
#     - LectureVideo(imagelist)
#     - DemoResource(imagelist)
#     - Publication(textlist)
#     - Patent(textlist)
#     - Report(textlist)
# - News&Info
#     - Notice(textlist)
#     - News(imagelist)
#     - Gallery(imagelist)
#     - Community(board)
# - Contact(page)

class TopMenu(models.Model):
    titleko = models.CharField(max_length=100)
    titleen = models.CharField(max_length=100)

    def __str__(self):
        return self.titleen

class SubMenu(models.Model):
    titleko = models.CharField(max_length=100)
    titleen = models.CharField(max_length=100)
    topmenu_id = models.ForeignKey(TopMenu)

    def __str__(self):
        return self.titleen

# About
class Greeting(models.Model):
    titleko = models.CharField(max_length=100)
    titleen = models.CharField(max_length=100)
    writer = models.CharField(max_length=45)
    date = models.DateField()
    contentko = models.TextField()
    contenten = models.TextField()
    image = models.CharField(max_length=100)
    submenu_id = models.ForeignKey(SubMenu)

    def __str__(self):
        return self.titleen

class Member(models.Model):
    nameko = models.CharField(max_length=100)
    nameen = models.CharField(max_length=100)
    positionko = models.CharField(max_length=100)
    positionen = models.CharField(max_length=100)
    departmentko = models.TextField()
    departmenten = models.TextField()
    educationko = models.TextField()
    educationen = models.TextField()
    careerko = models.TextField()
    careeren = models.TextField()
    image = models.CharField(max_length=100)
    submenu_id = models.ForeignKey(SubMenu)
    # IMAGE UPLOAD
    testImage = models.ImageField(upload_to="member", default='noImage')

    def __str__(self):
        return self.nameen

class Lab(models.Model):
    titleko = models.CharField(max_length=100)
    titleen = models.CharField(max_length=100)
    writer = models.CharField(max_length=45)
    date = models.DateField()
    careerko = models.TextField()
    careeren = models.TextField()
    image = models.CharField(max_length=100)
    submenu_id = models.ForeignKey(SubMenu)

    def __str__(self):
        return self.titleen

class Project(models.Model):
    titleko = models.CharField(max_length=100)
    titleen = models.CharField(max_length=100)
    writer = models.CharField(max_length=45)
    date = models.DateField()
    contentko = models.TextField()
    contenten = models.TextField()
    image = models.CharField(max_length=100)
    submenu_id = models.ForeignKey(SubMenu)

    def __str__(self):
        return self.titleen

# Research
class LectureNote(models.Model):
    titleko = models.CharField(max_length=100)
    titleen = models.CharField(max_length=100)
    writer = models.CharField(max_length=45)
    date = models.DateField()
    contentko = models.TextField()
    contenten = models.TextField()
    image = models.CharField(max_length=100)
    submenu_id = models.ForeignKey(SubMenu)

    def __str__(self):
        return self.titleen

class LectureVideo(models.Model):
    titleko = models.CharField(max_length=100)
    titleen = models.CharField(max_length=100)
    writer = models.CharField(max_length=45)
    date = models.DateField()
    contentko = models.TextField()
    contenten = models.TextField()
    link = models.CharField(max_length=100)
    submenu_id = models.ForeignKey(SubMenu)

    def __str__(self):
        return self.titleen

class DemoResource(models.Model):
    titleko = models.CharField(max_length=100)
    titleen = models.CharField(max_length=100)
    writer = models.CharField(max_length=45)
    date = models.DateField()
    contentko = models.TextField()
    contenten = models.TextField()
    image = models.CharField(max_length=100)
    submenu_id = models.ForeignKey(SubMenu)

    def __str__(self):
        return self.titleen

class Publication(models.Model):
    titleko = models.CharField(max_length=100)
    titleen = models.CharField(max_length=100)
    writer = models.CharField(max_length=45)
    date = models.DateField()
    contentko = models.TextField()
    contenten = models.TextField()
    image = models.CharField(max_length=100)
    submenu_id = models.ForeignKey(SubMenu)

    def __str__(self):
        return self.titleen

class Patent(models.Model):
    titleko = models.CharField(max_length=100)
    titleen = models.CharField(max_length=100)
    writer = models.CharField(max_length=45)
    date = models.DateField()
    contentko = models.TextField()
    contenten = models.TextField()
    image = models.CharField(max_length=100)
    submenu_id = models.ForeignKey(SubMenu)

    def __str__(self):
        return self.titleen

class Report(models.Model):
    titleko = models.CharField(max_length=100)
    titleen = models.CharField(max_length=100)
    writer = models.CharField(max_length=45)
    date = models.DateField()
    contentko = models.TextField()
    contenten = models.TextField()
    image = models.CharField(max_length=100)
    submenu_id = models.ForeignKey(SubMenu)

    def __str__(self):
        return self.titleen

# News&Info
class Notice(models.Model):
    titleko = models.CharField(max_length=100)
    titleen = models.CharField(max_length=100)
    writer = models.CharField(max_length=45)
    date = models.DateField()
    contentko = models.TextField()
    contenten = models.TextField()
    image = models.CharField(max_length=100)
    submenu_id = models.ForeignKey(SubMenu)

    def __str__(self):
        return self.titleen

class News(models.Model):
    titleko = models.CharField(max_length=100)
    titleen = models.CharField(max_length=100)
    writer = models.CharField(max_length=45)
    date = models.DateField()
    contentko = models.TextField()
    contenten = models.TextField()
    image = models.CharField(max_length=100)
    submenu_id = models.ForeignKey(SubMenu)

    def __str__(self):
        return self.titleen

class Gallery(models.Model):
    titleko = models.CharField(max_length=100)
    titleen = models.CharField(max_length=100)
    writer = models.CharField(max_length=45)
    date = models.DateField()
    contentko = models.TextField()
    contenten = models.TextField()
    image = models.CharField(max_length=100)
    submenu_id = models.ForeignKey(SubMenu)

    def __str__(self):
        return self.titleen

class Community(models.Model):
    titleko = models.CharField(max_length=100)
    titleen = models.CharField(max_length=100)
    writer = models.CharField(max_length=45)
    date = models.DateField()
    contentko = models.TextField()
    contenten = models.TextField()
    image = models.CharField(max_length=100)
    submenu_id = models.ForeignKey(SubMenu)

    def __str__(self):
        return self.titleen