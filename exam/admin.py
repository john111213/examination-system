from django.contrib import admin
from exam.models import Academy, Major, Course, Student, QuestionBank, TestPaper, Record,Teacher,CourseManager,AdminManager

# Register your models here.

# 修改名称
admin.site.site_header = '在线考试系统后台'
admin.site.site_title = '在线考试系统'

admin.site.register([Academy, Major, Course, Student, QuestionBank, TestPaper, Record,Teacher,CourseManager,AdminManager])