from django.db import models
from django.utils import timezone

# Create your models here.
#model/table for a user
class User(models.Model):
    id = models.AutoField(primary_key=True)
    #email id's of the user 
    email = models.EmailField(unique=True)
    #name of the user
    name = models.CharField(max_length=50, blank=True, null=True)

    def __str__(self):
        return '%s %s' % (self.email,self.name)


#model/table for form
class Form(models.Model):
    id = models.AutoField(primary_key=True)
    #user is the owner of the form
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name="user_owner")
    #profile pic to display on the form chat
    profile = models.ImageField(upload_to="profile", max_length=255, blank=True, null=True)
    #name that will appear on the form chat title
    name = models.CharField(max_length=50, blank=False, null=False)
    #color of the form i.e chat window
    color = models.CharField(max_length=30,blank=True,null=True)
    #domain which are allowed to fill the form e.g '@sakec.ac.in' , default is all
    domain = models.CharField(max_length=20, blank=False, null=False, default='all')
    #link of the form to access it , it is editable by the user
    link = models.CharField(max_length=20, blank=True, null=True, unique=True, default='to call a function which returns unique link')

    def __str__(self):
        return '%s %s %s' % (self.name, self.domain, self.link)


#model/table for question
class Question(models.Model):
    id = models.AutoField(primary_key=True)
    #form to which the question belongs to
    form = models.ForeignKey(Form, on_delete=models.CASCADE, related_name='owner_form')
    #question (actual text)
    question = models.TextField(blank=False, null=False)
    #suggestions for a question which can be null, note there shoulb ';' between two suggestions to descriminate
    suggestions = models.TextField(blank=True, null=True)
    #hint associated with each question ,it will be displayed on the users textbox input in light textcolor
    hint = models.TextField(blank=True, null=True)
    #answer type i.e whether the answer accepted is of type emial, name or integer like age
    answer_type = models.CharField(max_length=30, blank=True, null=True)

    def __str__(self):
        return '%s %s %s %s' % (self.question, self.suggestions, self.hint, self.answer_type)


#model/table for answer
class Answer(models.Model):
    id = models.AutoField(primary_key=True)
    #question to which the answer belongs to
    question = models.ForeignKey(Question, on_delete=models.CASCADE, related_name='owner_question')
    #answer for a question
    answer = models.TextField(blank=False, null=False)
    #date and time to specify when the answer was submited on the chat window
    timestamp = models.DateTimeField(default=timezone.now, blank=False, null=False)
    #user to which the answer belongs to
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='answer_user')
    #form to which the question , answer and user response belongs to
    form = models.ForeignKey(Form, on_delete=models.CASCADE, related_name='answer_form')

    def __str__(self):
        return '%s' % (self.answer)


#model/table for responses to a form
class Response(models.Model):
    id = models.AutoField(primary_key=True)
    #user to which the form response belongs to
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='response_user')
    #form to which user's response is
    form = models.ForeignKey(Form, on_delete=models.CASCADE, related_name='response_form')
    #date and time at which user last interacted with the form
    timestamp = models.DateTimeField(auto_now=True, blank=False, null=False)
    #completed or not i.e form is completed by the user or not 
    completed = models.BooleanField(blank=False, null=False)

    def __str__(self):
        return '%s' % (str(self.completed))
