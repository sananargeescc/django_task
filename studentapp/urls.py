from django.urls import path

from studentapp import views
urlpatterns = [
    path('', views.home, name='home'),
    path('log',views.log,name='log'),
    path('stud_reg',views.stud_reg,name='stud_reg'),
    path('admin12',views.admin12,name='admin12'),
    path('student1',views.student1,name='student1'),
    path('add_mark',views.add_mark,name='add_mark'),
    path('view_admin_mark',views.view_admin_mark,name='view_admin_mark'),
    path('view_student_mark',views.view_student_mark,name='view_student_mark'),
    path('mark_update/<int:id>/',views.mark_update,name='mark_update'),
    path('mark_delete/<int:id>/',views.mark_delete,name='mark_delete'),
    path('view_profile', views.view_profile, name='view_profile'),
    path('admin_reg', views.admin_reg, name='admin_reg'),
    path('log', views.log, name='log'),
    path('profile_update',views.profile_update,name='profile_update'),
    path('view_admin_student',views.view_admin_student,name='view_admin_student'),
    path('view_logout_student', views.view_logout_student, name='view_logout_student'),
    path('view_logout_admin', views.view_logout_admin, name='view_logout_admin'),








]