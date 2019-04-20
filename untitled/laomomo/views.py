from django.shortcuts import render

# Create your views here.


from django.shortcuts import render  # 导入render模块

# 先定义一个数据列表，当然后面熟了可以从数据库里取出来

list = [{"name": 'good', 'password': 'python'}, {'name': 'learning', 'password': 'django'}]
#列表中的每一个元素都是字典类型

def index(request):
    # 获取前端post过来的用户名和密码

    name = request.POST.get('name', None)

    password = request.POST.get('password', None)

    # 把用户和密码组装成字典

    data = {'name': name, 'password': password}

    list.append(data)

    return render(request, 'index.html', {'form': list})
    # 通过render模块把index.html这个文件返回到前端，并且返回给了前端一个变量form，在写html时可以调用这个form来展示list里的内容




