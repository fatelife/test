import traceback
from pickle import dump, load


class user:
    def __init__(self, username=None, password=None):
        """创建实例对象时初始化用户名和登录密码，默认值为None"""
        self.username = username
        self.password = password

    def update(self, username=None, password=None):
        """修改用户名和密码"""
        if username != None:
            self.username = username
        if password != None:
            self.password = password

    def __repr__(self):
        """定义对象打印方式"""
        return f'username={self.username}\tpassword={self.password}'


def showall():
    """显示当前所有已注册用户"""
    global userlist
    if len(userlist) == 0:
        print("\t当前无注册用户")
    else:
        print("\t当前已注册用户信息如下：")
        n = 0
        for x in userlist:
            n += 1
            print(f'\t{n} {x}')
    input('\n\t按Enter继续……\n')


def adduser():
    '''添加新用户'''
    global userlist
    username = input('\n\t请输入新的用户名：')
    if username == '':
        print('\t输入用户名为空！')
    else:
        if find(username) > -1:
            print("\t用户名已存在，请重新输入！")
        else:
            password = input('\t请输入新用户登录密码：')
            if password == '':
                print('\t输入密码为空！')
            else:
                userlist.append(user(username, password))
                print('\t添加用户成功！')
    input('\n\t按Enter继续……\n')

    
def check_updata():
    '''查询修改用户信息'''
    global userlist
    username = input('\t请输入要查找的用户名：')
    index = find(username)
    if index == -1:
        print(f'\t{username}不存在！')
    else:
        print(f'{username}已注册！')
        print('\t请选择操作：')
        print('\t  1.修改用户')
        print('\t  2.删除用户')
        op = input('\t 请输入序号选择对应操作：')
        if op == '2':
            del userlist[index]
            print('\n\t  已成功删除用户')
        elif op == '1':
            username = input('\t请输入新的用户名(不修改用户名请保持为空)：')
            if username == '':
                username = userlist[index].username
                password = input('\t请输入新用户登录密码：')
                if password == '':
                    print('\t输入密码为空！')
                else:
                    userlist[index].update(username, password)
                    print('\n\t修改用户信息成功')
            else:
                if find(username) > -1:
                    print("\t用户名已存在，请重新输入！")
                else:
                    password = input('\t请输入新用户登录密码：')
                    if password == '':
                        print('\t输入密码为空！')
                    else:
                        userlist[index].updata(username, password)
                        print('\n\t修改用户信息成功')
        else:
            print('\t输入序号有误，请核对后重新输入！')
            input('\n\t按Enter继续……\n')


def find(namekey):
    '''查找用户是否存在'''
    global userlist
    n = -1
    for x in userlist:
        n += 1
        if x.username == namekey:
            break
    else:
        n = -1
    return n


def save():
    '''将用户信息写入文件'''
    global userlist
    myfile = open(r'D:\Desktop\userdata.bin', 'wb')
    global userlist
    dump(userlist, myfile)
    myfile.close()
    print('\t成功保存用户信息')
    input('\n\t按Enter继续……\n')

try:
    myfile = open(r'C:\userdata.bin', 'rb')
    x = myfile.read(1)
    if x == b'':
        userlist = list()
    else:
        myfile.seek(0)
        userlist = load(myfile)
    myfile.close()
except Exception as e:
    print(e)
    myfile = open(r'C:\userdata.bin', 'xb')
    userlist = list()
    myfile.close()

while True:
    print('用户注册信息管理系统')
    print('\t1.显示全部已注册用户')
    print('\t2.查找/修改/删除用户信息')
    print('\t3.添加新用户')
    print('\t4.保存用户数据')
    print('\t5.退出系统')
    no = input('请输入对应序号选择对应操作：')
    if no == '1':
        showall()
    elif no == '2':
        check_updata()
    elif no == '3':
        adduser()
    elif no == '4':
        save()
    elif no == '5':
        print('谢谢使用')
        break
    else:
        print('\t输入序号有误，请核对后重新输入！')
        input('\n\t按Enter继续……\n')
