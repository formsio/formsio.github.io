from django.urls import path, include
from formsapi.views import (AllUsersViewSet,GetUserViewSet,AllFormsViewSet,GetFormViewSet,AllQuestionsViewSet,
GetQuestionsViewSet,AllAnswersViewSet,UpdateAnswerViewSet,UpdateFormViewSet,GetUserResponseViewSet,
DeleteFormViewSet,DeleteQuestionViewSet,GetAnswersViewSet,AllResponsesViewSet,GetResponsesViewSet)
from rest_framework.urlpatterns import format_suffix_patterns

urlpatterns = [
    #to get all users and create one
    #key - email,name for post in body
    #e.g http://127.0.0.1:8000/api/allusers/
    path("allusers/",AllUsersViewSet.as_view(),name="All_Users"),
    #to check if the user exists
    #e.g http://127.0.0.1:8000/api/getuser/vineet.patel@sakec.ac.in/
    path("getuser/<str:email>/",GetUserViewSet.as_view(),name="Get_User"),
    #to get all forms and create one
    #key - user(id),profile(file),name,domain,link,color for post in body
    #e.g http://127.0.0.1:8000/api/allforms/
    path("allforms/",AllFormsViewSet.as_view(),name="All_Forms"),
    #to update the form with passed in id
    #key are same as in 'allforms' and delete method to delete profile pic
    #e.g http://127.0.0.1:8000/api/updateform/1/
    path("updateform/<int:id>/",UpdateFormViewSet.as_view(),name="Update_Form"),
    #to delete a form with passed in id
    #e.g http://127.0.0.1:8000/api/deleteform/2/
    path("deleteform/<int:id>/",DeleteFormViewSet.as_view(),name="Delete_Form"),
    #to get the form with passed in link
    #e.g http://127.0.0.1:8000/api/getform/demo1/
    path("getform/<str:link>/",GetFormViewSet.as_view(),name="Get_Form"),
    #to get all questions and create one
    #key - form(id),question,suggestions,hint,answer_type for post in body
    #e.g http://127.0.0.1:8000/api/allquestions/
    path("allquestions/",AllQuestionsViewSet.as_view(),name="All_Questions"),
    #to delete a question with passed in id
    #e.g http://127.0.0.1:8000/api/deletequestion/8/
    path("deletequestion/<int:id>/",DeleteQuestionViewSet.as_view(),name="Delete_Question"),
    #to get the questions of passed in form id
    #e.g http://127.0.0.1:8000/api/getquestions/1/
    path("getquestions/<int:form>/",GetQuestionsViewSet.as_view(),name="Get_Question"),
    #to get all answers and create one
    #key - form(id),question(id),answer,timestamp(e.g 2019-12-02T04:20:20Z)optional,user(id) for post in body
    #e.g http://127.0.0.1:8000/api/allanswers/
    path("allanswers/",AllAnswersViewSet.as_view(),name="All_Answers"),
    #same key as above but pass the answer id to update the answer
    #e.g http://127.0.0.1:8000/api/updateanswer/8/
    path("updateanswer/<int:answer_id>/",UpdateAnswerViewSet.as_view(),name="Update_Answers"),
    #to get the answers of passed in form id and user id
    #e.g http://127.0.0.1:8000/api/getanswers/1/3/
    path("getanswers/<int:form>/<int:user>/",GetAnswersViewSet.as_view(),name="Get_Answer"),
    #to get all responses and create one
    #key - form(id),user(id),timestamp(e.g 2019-12-02T04:20:20Z)optional,completed(boolean) for post in body
    #e.g http://127.0.0.1:8000/api/allresponses/
    path("allresponses/",AllResponsesViewSet.as_view(),name="All_Responses"),
    #to get the completed responses of passed in form id
    #e.g http://127.0.0.1:8000/api/getresponses/1/
    path("getresponses/<int:form>/",GetResponsesViewSet.as_view(),name="Get_Responses"),
    #to get the response of a user for a form by passed in form id and user id
    #use put to update the same with the keys in all responses
    #first user id then form id
    #e.g http://127.0.0.1:8000/api/getuserresponse/2/1/
    path("getuserresponse/<int:user>/<int:form>/",GetUserResponseViewSet.as_view(),name="Get_Response"), 
]