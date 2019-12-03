from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from django.http import Http404

from formsapi.serializer import UsersSerializer,FormsSerializer,QuestionSerializer,AnswerSerializer,ResponseSerializer
from formsapi.models import User,Form,Question,Answer
from formsapi.models import Response as Resp

# Create your views here.

#class to get all the users
class AllUsersViewSet(APIView):
    #to get all the users
    def get(self,request):
        users = User.objects.all().order_by("id")
        serializer = UsersSerializer(users, many=True)
        return Response(serializer.data)
    
    #to add new user
    def post(self,request):
        data = request.data
        serializer = UsersSerializer(data=data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=400)

#class to get the user with specific email ID
class GetUserViewSet(APIView):
    #to get the user with passed email ID
    def get(self,request,email,format=None):
        try:
            user = User.objects.get(email=email)
        except User.DoesNotExist:
            raise Http404
        serializer = UsersSerializer(user)
        return Response(serializer.data)

#class to get all forms
class AllFormsViewSet(APIView):
    #to get all the forms
    def get(self,request):
        forms = Form.objects.all().order_by("id")
        serializer = FormsSerializer(forms, many=True)
        return Response(serializer.data)

    #to add new form
    def post(self,request):
        data = request.data
        serializer = FormsSerializer(data=data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors,status=400)

#class to delete a form
class DeleteFormViewSet(APIView):
    #to get the form id to delete it
    def delete(self,request,id,format=None):
        form = Form.objects.get(id=id)
        form.delete()
        return Response({'delete':'successfull'},status=204)


#class to get the form with specific link
class GetFormViewSet(APIView):
    #to get the from with passed link
    def get(self,request,link,format=None):
        try:
            form = Form.objects.get(link=link)
        except Form.DoesNotExist:
            raise Http404
        serializer = FormsSerializer(form)
        return Response(serializer.data)

#class to update attributes of form
class UpdateFormViewSet(APIView):
    #to update the profile pic,..  of passed in form id
    def put(self,request,id,format=None):
        form = Form.objects.get(id=id)
        serializer = FormsSerializer(form,data=request.data,partial=True)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors,status=404)

    #to delete profile pic
    def delete(self,request,id,format=None):
        form = Form.objects.get(id=id).profile.delete(save=True)
        return Response({'delete':'successfull'},status=204)

#class to get all questions
class AllQuestionsViewSet(APIView):
    #to get all the questions
    def get(self,request):
        questions = Question.objects.all().order_by("id")
        serializer = QuestionSerializer(questions,many=True)
        return Response(serializer.data)

    #to add new question
    def post(self,request):
        data = request.data
        serializer = QuestionSerializer(data=data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors,status=404)

#class to delete a question
class DeleteQuestionViewSet(APIView):
    #to get the id of the question to delete it
    def delete(self,request,id,format=None):
        question = Question.objects.get(id=id)
        question.delete()
        return Response({'delete':'successfull'},status=204)

#class to get the questions of a specific form
class GetQuestionsViewSet(APIView):
    #to get the questions of passed in form id
    def get(self,request,form,format=None):
        try:
            questions = Question.objects.filter(form=form)
            if len(questions) == 0:
                return Response({'error':'no questions for form found'},status=404)
        except Question.DoesNotExist:
            raise Http404
        serializer = QuestionSerializer(questions,many=True)
        return Response(serializer.data)

#class to get all answers
class AllAnswersViewSet(APIView):
    #to get all the answers
    def get(self,request):
        answers = Answer.objects.all().order_by("id")
        serializer = AnswerSerializer(answers,many=True)
        return Response(serializer.data)

    #to add new answer
    def post(self,request):
        data = request.data
        serializer = AnswerSerializer(data=data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors,status=404)

#class to update an answer
class UpdateAnswerViewSet(APIView):
    #to update an answer
    def put(self,request,answer_id,format=None):
        answer = Answer.objects.get(id=answer_id)
        serializer = AnswerSerializer(answer,data=request.data,partial=True)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors,status=404)

#class to get the answers of a specific form by a specific user
class GetAnswersViewSet(APIView):
    #to get the answers of passed in form id and user id
    def get(self,request,form,user,format=None):
        try:
            answers = Answer.objects.filter(user=user).filter(form=form)
        except Answer.DoesNotExist:
            raise Http404
        serializer = AnswerSerializer(answers,many=True)
        return Response(serializer.data)

#class to get all responses
class AllResponsesViewSet(APIView):
    #to get all the responses
    def get(self,request):
        responses = Resp.objects.all().order_by("id")
        serializer = ResponseSerializer(responses,many=True)
        return Response(serializer.data)

    #to add new response
    def post(self,request):
        data = request.data
        serializer = ResponseSerializer(data=data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors,status=404)

#class to get the responses of a form which are completed (and to create a csv file and return it)
class GetResponsesViewSet(APIView):
    #to get the completed responses of passed in form
    def get(self,request,form,format=None):
        try:
            resp = Resp.objects.filter(form=form).filter(completed=True)
        except Resp.DoesNotExist:
            raise Http404
        serializer = ResponseSerializer(resp,many=True)
        return Response(serializer.data) 

#class to get the response of a form for a user and to update also
class GetUserResponseViewSet(APIView):
    #to get the response of the form for the passed in user and form
    def get(self,request,user,form,format=None):
        try:
            resp = Resp.objects.filter(user=user).filter(form=form)
            if len(resp) == 0 :
                return Response({'error':'no response found'},status=404)
        except Resp.DoesNotExist:
            raise Http404
        serializer = ResponseSerializer(resp,many=True)
        return Response(serializer.data)
    
    #to update a response of form for the passed in user and form
    def put(self,request,user,form,format=None):
        resp = Resp.objects.filter(user=user).filter(form=form).first()
        serializer = ResponseSerializer(resp,data=request.data,partial=True)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors,status=404)


