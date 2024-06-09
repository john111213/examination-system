

from django.urls import path
from . import views

app_name = 'exam'  # 指定应用的命名空间

urlpatterns = [
    path('', views.index, name='index'),  # 默认访问首页
    path('index/', views.index, name='index'),
    path('Login/', views.Login, name='Login'),
    path('studentLogin/', views.studentLogin, name='studentLogin'),  # 学生登录
    path('teacherLogin/', views.teacherLogin, name='teacherLogin'),  # 老师登录
    path('adminManagerLogin/', views.adminManagerLogin, name='adminManagerLogin'),  # 管理员登录
    path('courseManagerLogin/', views.courseManagerLogin, name='courseManagerLogin'),  # 教务人员登录
    path('startExam/', views.startExam, name='startExam'),  # 开始考试
    path('calculateGrade/', views.calculateGrade, name='calculateGrade'),  # 考试评分
    path('stulogout/', views.stulogout, name='stulogout'),  # 学生退出登录
    path('userfile/', views.userfile, name='userfile'),  # 学生个人信息
    path('adminuserfile/', views.adminuserfile, name='adminuserfile'),  # 管理员个人信息
    path('courseuserfile/', views.courseuserfile, name='courseuserfile'),  # 教务人员个人信息
    path('teacheruserfile/', views.teacheruserfile, name='teacheruserfile'),  # 教师个人信息
    path('adminpi/<int:sid>', views.adminpi, name='adminpi'),  # 管理员个人信息修改
    path('coursepi/<int:sid>', views.coursepi, name='coursepi'),  # 教务人员个人信息修改
    path('teacherpi/<int:sid>', views.teacherpi, name='teacherpi'),  # 教务人员个人信息修改
    path('examinfo/', views.examinfo, name='examinfo'),  # 考试信息
    path('teacherindex/', views.teacherindex, name='teacherindex'),  # 教师信息
    path('teachercreate/', views.teachercreate, name='teachercreate'),  # 教师添加
    path('teacherupdate/<int:sid>',views.teacherupdate,name='teacherupdate'),#教师修改
    path('teacherdrop/<int:sid>',views.teacherdrop,name='teacherdrop'),#教师删除
    path('cindex/', views.cindex, name='cindex'),  # 教务人员信息
    path('ccreate/', views.ccreate, name='ccreate'),  # 教务人员添加
    path('cupdate/<int:sid>',views.cupdate,name='cupdate'),#教务人员修改
    path('cdrop/<int:sid>',views.cdrop,name='cdrop'),#教务人员删除
    path('collindex/', views.collindex, name='collindex'),  # 学院信息
    path('collcreate/', views.collcreate, name='collcreate'),  # 学院添加
    path('colldrop/<str:name>',views.colldrop,name='colldrop'),#学院删除
    path('view_major/<str:academy_name>/', views.view_major, name='view_major'),
    path('view_stu/<str:major_name>/', views.view_stu, name='view_stu'),
    path('majordrop/<str:name>',views.majordrop,name='majordrop'),
    path('majorcreate/',views.majorcreate,name='majorcreate'),
    path('studrop/<str:name>',views.studrop,name='studrop'),
    path('stucreate/',views.stucreate,name='stucreate'),
    path('subindex/', views.subindex, name='subindex'),  # 科目信息
    path('subcreate/', views.subcreate, name='subcreate'),  # 科目添加信息
    path('subdrop/<str:name>',views.subdrop,name='subdrop'),#科目删除
    path('view_TestPaper/<str:course_name>/', views.view_TestPaper, name='view_TestPaper'),
    path('Testcreate/',views.Testcreate,name='Testcreate'),
    path('Testdrop/<str:name>',views.Testdrop,name='Testdrop'),#科目删除
    path('checkExam/', views.checkExam, name='checkExam'),  # 试卷查看
    path('add_question_bank/', views.add_question_bank, name='add_question_bank'),  # 试卷修改
]
