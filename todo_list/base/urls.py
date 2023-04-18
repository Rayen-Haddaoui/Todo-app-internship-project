from django.urls import path
from  .views import TaskList, TaskDetail, TaskCreate, TaskUpdate, DeleteView, CustomLoginView, SignupPage
from django.contrib.auth.views import  LogoutView,PasswordResetView,PasswordResetDoneView,PasswordResetConfirmView,PasswordResetCompleteView


urlpatterns=[
   
    path('login/', CustomLoginView.as_view(), name='login'),
    path('signup/', SignupPage.as_view(), name='signup'),
    path('logout/', LogoutView.as_view(next_page='login'), name='logout'),
    path('reset-password', PasswordResetView.as_view(template_name ="base/password_reset.html"),name='reset_password'),
    path('reset-password-sent', PasswordResetDoneView.as_view(template_name ="base/password_reset_sent.html"),name='password_reset_done'),
    path('reset/<uidb64>/<token>/', PasswordResetConfirmView.as_view(template_name ="base/password_reset_form.html"), name='password_reset_confirm'),
    path('reset-password-complete', PasswordResetCompleteView.as_view(template_name ="base/password_reset_complete.html"), name='password_reset_complete'),


    path('',TaskList.as_view(),name='tasks'),
    path('task/<int:pk>/',TaskDetail.as_view(),name='task'),
    path('task-create/',TaskCreate.as_view(),name='task-create'),
    path('task-update/<int:pk>',TaskUpdate.as_view(),name='task-update'),
    path('task-delete/<int:pk>',DeleteView.as_view(),name='task-delete'),


]