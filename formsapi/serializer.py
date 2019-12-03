from rest_framework import serializers
from formsapi.models import User, Form, Question, Answer, Response

#Serializer for the User to get the details of users
class UsersSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = "__all__"

#Serializer for the Form to get the details of form
class FormsSerializer(serializers.ModelSerializer):
    class Meta:
        model = Form
        fields = ("id","user","profile","name","domain","link")
    #for foreign key user
    def to_representation(self, instance):
        self.fields["user"] = UsersSerializer(read_only=True)
        return super(FormsSerializer,self).to_representation(instance)

#Serializer for the Question to get the details of the question
class QuestionSerializer(serializers.ModelSerializer):
    class Meta:
        model = Question
        fields = ("id","form","question","suggestions","hint","answer_type")
    #for foreign key form
    def to_representation(self, instance):
        self.fields["form"] = FormsSerializer(read_only=True) 
        return super(QuestionSerializer,self).to_representation(instance)

#Serializer for the Answer to get the detail of the answer
class AnswerSerializer(serializers.ModelSerializer):
    class Meta:
        model = Answer
        fields = ("id","question","answer","timestamp","user","form")
    #for foreign key user,form,question
    def to_representation(self, instance):
        self.fields["question"] = QuestionSerializer(read_only=True)
        self.fields["user"] = UsersSerializer(read_only=True)
        return super(AnswerSerializer,self).to_representation(instance)

#Serializer for the Response to get the detail of the response of a form
class ResponseSerializer(serializers.ModelSerializer):
    class Meta:
        model = Response
        fields = ("id","user","form","timestamp","completed")
    #for foreign key user,form
    def to_representation(self, instance):
        self.fields["user"] = UsersSerializer(read_only=True)
        self.fields["form"] = FormsSerializer(read_only=True)
        return super(ResponseSerializer,self).to_representation(instance)