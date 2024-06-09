from django.shortcuts import render,HttpResponse,reverse,redirect
from exam.models import Student,TestPaper,Record,Course,Academy,Teacher,AdminManager,CourseManager,Major,QuestionBank
from datetime import datetime
from django.core.exceptions import ObjectDoesNotExist
from .forms import QuestionBankForm
from django.http import JsonResponse
# Create your views here.

def Login(request):
    return render(request, 'login.html')
def studentLogin(request):
    if request.method == 'POST':
        #获取表单信息
        sid = request.POST.get('sid')
        password = request.POST.get('password')
        try:
            #通过学号获取该学生实体
            student = Student.objects.get(sid=sid)
            if password == student.pwd:
                request.session['username']=sid
                request.session['is_Login_1']=True
                paper = TestPaper.objects.filter(major=student.major)
                grade = Record.objects.filter(sid=student.sid)

                return render(request,'student/index.html',{'student':student,'paper':paper,'grade':grade})
            else:
                return render(request,'student/login1.html',{'message':'密码不正确'})
        except ObjectDoesNotExist:
            return render(request,'student/login1.html',{'message':'学号不存在'})
    elif request.method == 'GET':
        return render(request,'student/login1.html')
    else:
        return redirect('login')

#教师登录
def teacherLogin(request):
    if request.method == 'POST':
        #获取表单信息
        sid = request.POST.get('sid')
        password = request.POST.get('password')
        try:
            #通过学号获取该学生实体
            teacher = Teacher.objects.get(sid=sid)
            if password == teacher.pwd:
                request.session['username']=sid
                request.session['is_Login_2']=True

                return render(request,'teacher/index.html',{'teacher':teacher})
            else:
                return render(request,'teacher/login2.html',{'message':'密码不正确'})
        except ObjectDoesNotExist:
            return render(request,'teacher/login2.html',{'message':'编号不存在'})
    elif request.method == 'GET':
        return render(request,'teacher/login2.html')
    else:
        return redirect('login')

def adminManagerLogin(request):
    if request.method == 'POST':
        #获取表单信息
        sid = request.POST.get('sid')
        password = request.POST.get('password')
        try:
            #通过学号获取该学生实体
            adminManager = AdminManager.objects.get(sid=sid)
            if password == adminManager.pwd:
                request.session['username']=sid
                request.session['is_Login_3']=True

                return render(request, 'adminManager/index.html', {'adminManager':adminManager})
            else:
                return render(request,'adminManager/login3.html',{'message':'密码不正确'})
        except ObjectDoesNotExist:
            return render(request,'adminManager/login3.html',{'message':'编号不存在'})
    elif request.method == 'GET':
        return render(request,'adminManager/login3.html')
    else:
        return redirect('login')

def courseManagerLogin(request):
    if request.method == 'POST':
        #获取表单信息
        sid = request.POST.get('sid')
        password = request.POST.get('password')
        try:
            #通过学号获取该学生实体
            courseManager = CourseManager.objects.get(sid=sid)
            if password == courseManager.pwd:
                request.session['username']=sid
                request.session['is_Login_4']=True

                return render(request, 'courseManager/index.html', {'courseManager':courseManager})
            else:
                return render(request,'courseManager/login4.html',{'message':'密码不正确'})
        except ObjectDoesNotExist:
            return render(request,'courseManager/login4.html',{'message':'编号不存在'})
    elif request.method == 'GET':
        return render(request,'courseManager/login4.html')
    else:
        return redirect('login')
#首页
def index(request):
    # 检查学生是否已登录
    if request.session.get('is_Login_1', None):
        # 如果是学生已登录，执行学生相关逻辑
        username = request.session.get('username', None)
        student = Student.objects.get(sid=username)
        paper = TestPaper.objects.filter(major=student.major)
        return render(request, 'student/index.html', {'student': student, 'paper': paper})

    # 检查教师是否已登录
    elif request.session.get('is_Login_2', None):
        # 如果是教师已登录，执行教师相关逻辑
        username = request.session.get('username', None)
        teacher = Teacher.objects.get(sid=username)
        return render(request, 'teacher/index.html', {'user': teacher})

    elif request.session.get('is_Login_3', None):
        # 如果是教师已登录，执行教师相关逻辑
        username = request.session.get('username', None)
        adminManager = AdminManager.objects.get(sid=username)
        return render(request, 'adminManager/index.html', {'user': adminManager})

    elif request.session.get('is_Login_4', None):
        # 如果是教师已登录，执行教师相关逻辑
        username = request.session.get('username', None)
        print(f'年后{username}')
        courseManager = CourseManager.objects.get(sid=username)
        print(f'年后{courseManager}')
        return render(request, 'courseManager/index.html', {'user': courseManager})

    # 如果未登录，跳转到登录页面
    else:
        return render(request, 'index.html')


def userfile(request):
    if request.session.get('is_Login_1', None): #若session认证为真
        username = request.session.get('username', None)
        print(username)
        student = Student.objects.get(sid=username)
        # 查询考试信息
        paper = TestPaper.objects.filter(major=student.major)
        print(f'考试信息：{paper}')
        context = {'student': student, 'paper': paper}
    else:
        context = {}
    return render(request, 'student/userfile.html', context)
#admin
def adminuserfile(request):
    if request.session.get('is_Login_3', None):
        username = request.session.get('username', None)
        print(username)
        adminManager = AdminManager.objects.get(sid=username)
        context = {'adminManager': adminManager}
    else:
        context = {}
    return render(request, 'adminManager/userfile.html', context)
#course
def courseuserfile(request):
    if request.session.get('is_Login_4', None):
        username = request.session.get('username', None)
        print(username)
        courseManager = CourseManager.objects.get(sid=username)
        context = {'courseManager': courseManager}
    else:
        context = {}
    return render(request, 'courseManager/userfile.html', context)
#teacher
def teacheruserfile(request):
    if request.session.get('is_Login_2', None):
        username = request.session.get('username', None)
        print(username)
        teacher = Teacher.objects.get(sid=username)
        context = {'teacher': teacher}
    else:
        context = {}
    return render(request, 'teacher/userfile.html', context)
#管理员修改个人信息
def adminpi(request, sid):
    if request.method == 'POST':
        name = request.POST.get('editName', "")
        age = request.POST.get('editAge', "")
        sex = request.POST.get('editSex', '')  # 默认为 'M'，可以根据需要修改
        print(f'性别为{sex}')
        # 更新数据库中的数据
        AdminManager.objects.filter(sid=sid).update(
            name=name,
            age=age,
            sex=sex,
        )
        return redirect(reverse("exam:adminuserfile"))
    return render(request, 'adminManager/userfile.html')

#教务人员修改个人信息
def coursepi(request, sid):
    if request.method == 'POST':
        name = request.POST.get('editName', "")
        age = request.POST.get('editAge', "")
        sex = request.POST.get('editSex', '')  # 默认为 'M'，可以根据需要修改
        print(f'性别为{sex}')
        # 更新数据库中的数据
        CourseManager.objects.filter(sid=sid).update(
            name=name,
            age=age,
            sex=sex,
        )
        return redirect(reverse("exam:courseuserfile"))
    return render(request, 'courseManager/userfile.html')
#教师人员修改个人信息
def teacherpi(request, sid):
    if request.method == 'POST':
        name = request.POST.get('editName', "")
        age = request.POST.get('editAge', "")
        sex = request.POST.get('editSex', '')  # 默认为 'M'，可以根据需要修改
        print(f'性别为{sex}')
        # 更新数据库中的数据
        Teacher.objects.filter(sid=sid).update(
            name=name,
            age=age,
            sex=sex,
        )
        return redirect(reverse("exam:teacheruserfile"))
    return render(request, 'teacher/userfile.html')
#退出登录
def stulogout(request):
    request.session.clear()
    url = reverse('exam:index')
    return redirect(url)

#考试信息
# 处理考试开始请求的视图函数
# 考试信息
def startExam(request):
    sid = request.GET.get('sid')
    title = request.GET.get('title')  # 试卷名字 唯一
    subject1 = request.GET.get('subject')  # 考试科目

    # 获取学生信息
    student = Student.objects.get(sid=sid)

    # 试卷信息
    paper = TestPaper.objects.filter(title=title, course__course_name=subject1)

    context = {
        'student': student,
        'paper': paper,
        'title': title,
        'subject': subject1,
        'count': paper.count()  # 数据表中数据的条数
    }

    return render(request, 'student/exam.html', context=context)



def examinfo(request):
    if request.session.get('is_Login_1',None):
        username = request.session.get('username',None)
        student = Student.objects.get(sid=username)
        #查询成绩信息
        grade = Record.objects.filter(sid=student.sid)
        return render(request,'student/examinfo.html',{'student':student,'grade':grade})
    else:
        return render(request,'student/examinfo.html')

#计算考试成绩
# 处理计算考试成绩的请求的视图函数
def calculateGrade(request):
    # 检查请求的方法是否为POST
    if request.method == 'POST':
        # 从POST参数中获取学生学号和考试科目
        sid = request.POST.get('sid')
        subject1 = request.POST.get('subject')
        # 通过学号从数据库中获取学生对象
        student = Student.objects.get(sid=sid)
        # 从数据库中获取该学生所属专业的试卷对象
        paper = TestPaper.objects.filter(major=student.major)
        # 从数据库中获取学生的考试记录
        grade = Record.objects.filter(sid=student.sid)
        # 从数据库中获取考试科目对应的课程对象
        course = Course.objects.filter(course_name=subject1).first()
        # 获取当前时间
        now = datetime.now()
        # 计算考试成绩
        # 从数据库中获取考试科目的所有题目及其答案和分数
        questions = TestPaper.objects.filter(course__course_name=subject1).\
            values('pid').values('pid__id', 'pid__answer', 'pid__score')
        # 初始化学生的总成绩
        stu_grade = 0
        # 遍历所有题目，比对学生的答案和正确答案，累加得分
        for p in questions:
            qid = str(p['pid__id'])
            stu_ans = request.POST.get(qid)
            cor_ans = p['pid__answer']
            if stu_ans == cor_ans:
                stu_grade += p['pid__score']

        # 在数据库中创建一条新的考试记录
        Record.objects.create(sid_id=sid, course_id=course.id, grade=stu_grade, rtime=now)

        # 构建传递给模板的上下文数据
        context = {
            'student': student,
            'paper': paper,
            'grade': grade,
        }

        # 使用Django的render函数将数据传递给模板'index.html'，并返回渲染后的HTML作为HTTP响应
        return render(request, 'student/index.html', context=context)


#1.	管理员：负责人员的管理（增删改查），人员包括教师、教务人员。可以修改个人信息
def teacherindex(request):
    Teachers = Teacher.objects.all()
    return render(request,'adminManager/teacher management/teachers.html',{'Teachers':Teachers})


def teachercreate(request):
    if request.method == 'POST':
        sid = request.POST.get('sid', "")
        name = request.POST.get('name', "")
        age = request.POST.get('age', "")
        pwd = request.POST.get('pwd', "")
        academy_name = request.POST.get('Academy', "")
        # 检查教师是否已存在
        tea_check = Teacher.objects.filter(name=name)
        if tea_check:
            return render(request, 'adminManager/teacher management/add.html', {"message": "该用户已存在"})
        # 创建教师对象，跳过外键字段
        teacher = Teacher.objects.create(
            sid=sid,
            name=name,
            age=age,
            pwd=pwd
        )
        # 获取学院实例并将其分配给教师对象
        if academy_name:
            try:
                academy_instance = Academy.objects.get(name=academy_name)
                teacher.academy = academy_instance
                teacher.save()
            except Academy.DoesNotExist:
                pass
        return redirect(reverse("exam:teacherindex"))

    return render(request, 'adminManager/teacher management/add.html', {"message": ""})

def teacherupdate(request,sid):
    if request.method == 'POST':
        name = request.POST.get('name', "")
        age = request.POST.get('age', "")
        pwd = request.POST.get('pwd', "")
        Teacher.objects.filter(sid=sid).update(
            name=name,
            age=age,
            pwd=pwd,
        )
        return redirect(reverse("exam:teacherindex"))
    return render(request,'adminManager/teacher management/update.html')

def teacherdrop(request,sid):
    Teacher.objects.filter(sid=sid).delete()
    return redirect(reverse("exam:teacherindex"))
#教务人员
def cindex(request):
    CourseManagers = CourseManager.objects.all()
    return render(request,'adminManager/cmanager managemant/teachers.html',{'CourseManagers':CourseManagers})
def ccreate(request):
    if request.method == 'POST':
        sid = request.POST.get('sid', "")
        name = request.POST.get('name', "")
        age = request.POST.get('age', "")
        pwd = request.POST.get('pwd', "")
        tea_check = Teacher.objects.filter(name=name)
        if tea_check:
            return render(request, 'adminManager/cmanager managemant/add.html', {"message": "该用户已存在"})
        CourseManager.objects.create(
            sid=sid,
            name=name,
            age=age,
            pwd=pwd
        )
        return redirect(reverse("exam:cindex"))
    return render(request, 'adminManager/cmanager managemant/add.html', {"message": ""})
def cupdate(request,sid):
    if request.method == 'POST':
        name = request.POST.get('name', "")
        age = request.POST.get('age', "")
        pwd = request.POST.get('pwd', "")
        CourseManager.objects.filter(sid=sid).update(
            name=name,
            age=age,
            pwd=pwd,
        )
        return redirect(reverse("exam:cindex"))
    return render(request,'adminManager/cmanager managemant/update.html')
def cdrop(request,sid):
    CourseManager.objects.filter(sid=sid).delete()
    return redirect(reverse("exam:cindex"))
#2.	教务人员：负责学院、专业、课程、学生等的管理。可以修改个人信息。
#学院
def collindex(request):
    academys = Academy.objects.all()
    return render(request,'courseManager/College Management/teachers.html',{'academys':academys})
def collcreate(request):
    if request.method == 'POST':
        name = request.POST.get('name', "")
        tea_check = Academy.objects.filter(name=name)
        if tea_check:
            return render(request, 'courseManager/College Management/add.html', {"message": "该用户已存在"})
        Academy.objects.create(
            name=name,
        )
        return redirect(reverse("exam:collindex"))
    return render(request, 'courseManager/College Management/add.html', {"message": ""})

def colldrop(request,name):
    Academy.objects.filter(name=name).delete()
    return redirect(reverse("exam:collindex"))
def view_major(request, academy_name):
    academy = Academy.objects.get(name=academy_name)
    # 查询该学院下的所有专业
    majors = Major.objects.filter(academy=academy)
    print(f'专业为{majors}')
    # 将学院和专业传递给模板
    context = {
        'academy': academy,
        'majors': majors,
    }
    # 设置session
    request.session['current_academy'] = academy_name
    # 渲染模板并返回响应
    return render(request, 'courseManager/College Management/majar.html', context)
#添加专业
def majorcreate(request):
    if request.method == 'POST':
        name = request.POST.get('name', "")
        current_academy = request.session.get('current_academy', None)
        # 获取学院对象
        academy_instance = Academy.objects.get(name=current_academy)
        # 检查专业是否已存在
        major_check = Major.objects.filter(major=name, academy=academy_instance)
        if major_check:
            return render(request, 'courseManager/College Management/majoradd.html', {"message": "该专业已存在"})
        # 创建专业对象
        Major.objects.create(
            major=name,
            academy=academy_instance
        )
        return redirect(reverse("exam:view_major", args=[current_academy]))
    return render(request, 'courseManager/College Management/majoradd.html', {"message": ""})

# 删除专业
def majordrop(request, name):
    # 获取当前学院名称
    current_academy = request.session.get('current_academy', None)
    if current_academy:
        # 删除专业
        Major.objects.filter(major=name).delete()
        # 重定向到view_major，并传递学院名称
        return redirect(reverse("exam:view_major", args=[current_academy]))
    else:
        # 处理没有学院名称的情况，可以根据实际需求进行适当的处理
        return HttpResponse("Error")
#学生
def view_stu(request, major_name):
    # 查询学生
    major = Major.objects.get(major=major_name)
    stu = Student.objects.filter(major=major)
    print(f'专业为{stu}')
    context = {
        'major': major,
        'stu': stu,
    }
    request.session['current_major'] = major_name
    return render(request, 'courseManager/College Management/stu.html', context)

def stucreate(request):
    if request.method == 'POST':
        sid = request.POST.get('sid', "")
        name = request.POST.get('name', "")
        age = request.POST.get('age', "")
        sclass = request.POST.get('sclass', "")
        email = request.POST.get('email', "")
        current_academy = request.session.get('current_academy', None)
        current_major = request.session.get('current_major', None)
        academy_instance = Academy.objects.get(name=current_academy)
        major_instance = Major.objects.get(major=current_major)
        major_check = Student.objects.filter(name=name)
        if major_check:
            return render(request, 'courseManager/College Management/majoradd.html', {"message": "该专业已存在"})
        Student.objects.create(
            sid=sid,
            name=name,
            age=age,
            academy=academy_instance,
            major=major_instance,
            sclass=sclass,
            email=email
        )
        return redirect(reverse("exam:view_stu", args=[current_major]))
    return render(request, 'courseManager/College Management/stuadd.html', {"message": ""})

def studrop(request, name):
    current_major = request.session.get('current_major', None)
    if current_major:
        Student.objects.filter(name=name).delete()
        return redirect(reverse("exam:view_stu", args=[current_major]))
    else:
        return HttpResponse("Error")

# 3.教师：负责试卷题目的维护、试卷的维护。可以修改个人信息。
def subindex(request):
    courses = Course.objects.all()
    return render(request,'teacher/subject Management/teachers.html',{'courses':courses})
def subcreate(request):
    if request.method == 'POST':
        sid = request.POST.get('sid', "")
        name = request.POST.get('name', "")
        tea_check = Course.objects.filter(course_name=name)
        if tea_check:
            return render(request, 'teacher/subject Management/add.html', {"message": "该科目已存在"})
        Course.objects.create(
            course_id=sid,
            course_name=name,
        )
        return redirect(reverse("exam:subindex"))
    return render(request, 'teacher/subject Management/add.html', {"message": ""})
def subdrop(request,name):
    Course.objects.filter(course_name=name).delete()
    return redirect(reverse("exam:subindex"))

# 查看试卷
def view_TestPaper(request, course_name):
    course = Course.objects.get(course_name=course_name)
    testPapers = TestPaper.objects.filter(course=course)
    context = {
        'course': course,
        'testPapers': testPapers,
    }
    request.session['current_course'] = course_name
    # 渲染模板并返回响应
    return render(request, 'teacher/subject Management/Text.html', context)
def Testcreate(request):
    question_bank_list = QuestionBank.objects.all()
    if request.method == 'POST':
        title = request.POST.get('title', "")
        major = request.POST.get('major', "")
        time = request.POST.get('time', "")
        examtime = request.POST.get('examtime', "")
        selected_question_banks = request.POST.getlist('question_banks', [])
        current_course = request.session.get('current_course', None)
        course_instance = Course.objects.get(course_name=current_course)
        major_instance, created = Major.objects.get_or_create(major=major)
        major_check = TestPaper.objects.filter(title=title, course=course_instance)
        if major_check:
            return render(request, 'teacher/subject Management/Testadd.html', {"message": "该专业已存在"})
        test_paper = TestPaper.objects.create(
            title=title,
            course=course_instance,
            major=major_instance,
            time=time,
            examtime=examtime
        )
        # 关联选择的题库到 TestPaper 对象
        test_paper.pid.set(selected_question_banks)
        return redirect(reverse("exam:view_TestPaper", args=[current_course]))
    return render(request, 'teacher/subject Management/Testadd.html', {'question_bank_list': question_bank_list})


def Testdrop(request, name):
    current_course = request.session.get('current_course', None)
    if current_course:
        TestPaper.objects.filter(title=name).delete()
        return redirect(reverse("exam:view_TestPaper", args=[current_course]))
    else:
        return HttpResponse("Error")

def checkExam(request):
    title = request.GET.get('title')  # 试卷名字 唯一
    subject1 = request.GET.get('subject')  # 考试科目
    # 获取学生信息
    # 试卷信息
    paper = TestPaper.objects.filter(title=title, course__course_name=subject1)
    context = {
        'paper': paper,
        'title': title,
        'subject': subject1,
        'count': paper.count()  # 数据表中数据的条数
    }
    return render(request, 'teacher/subject Management/exam.html', context=context)

#试卷
def add_question_bank(request):
    if request.method == 'POST':
        form = QuestionBankForm(request.POST)
        if form.is_valid():
            # 处理表单数据，保存到数据库等
            form.save()
            return redirect(reverse("exam:Testcreate"))
    else:
        form = QuestionBankForm()
    return render(request, 'teacher/subject Management/sjadd.html', {'form': form})
