> 转载请标明出处：
> [http://www.cnblogs.com/why168888/p/6445044.html](http://www.cnblogs.com/why168888/p/6445044.html)
>
>
> 本文出自:[【Edwin博客园】](http://www.cnblogs.com/why168888/)

<br/>



study python server django

# Python开发记录

###Mac OS中创建虚拟环境virtualenv

```
sudo pip install virtualenv


virtualenv testvir

cd testvir
source bin/activate

pip install pyramid
pip install flask
pip install django

deactivate
```


###Mac OS中创建虚拟环境virtualenvwrapper

```
.bash_profile文件添加
	sudo easy_install virtualenvwrapper
	source /usr/local/bin/virtualenvwrapper.sh

mkvirtualenv env1 创建虚拟环境env1
worken  查看虚拟环境
lsvirtualenv -b  查看虚拟环境
worken xxx 进入xxx虚拟环境
rmvirtualenv xxx 删除xxx虚拟环境
lssitepackages 查看环境里安装了哪些包

pip list 查看安装的库
pip install requests 安装requests
pip uninstall requests 卸载requests

pip install django==1.9.8 安装django1.9.8
```

###MySql数据操作

```
https://dev.mysql.com/downloads/mysql/

http://www.jianshu.com/p/fd3aae701db9

vim ~/.bash_profile
export PATH=$PATH:/usr/local/mysql/bin
mysql -uroot -p 登录mysql
SET PASSWORD FOR 'root'@'localhost' = PASSWORD('newpass');

Navicat操作

pip install mysql-python  驱动安装
```


###django 运行

```
startapps message 创建app

--static 存放css
--log 存放日子
--media 存放用户上传的目录

settings.py:
	TIME_ZONE = 'Asia/Shanghai' #中国时间
	STATIC_ROOT = 'static'  # 静态文件的物理路径

STATICFILES_DIRS = [
    os.path.join(BASE_DIR, 'static')
] #手动添加到末尾，不然找到static下存放的css文件



Mysql创建数据库
编码格式与排序格式：utf-8----utf8-general-ci

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.mysql',
        'NAME': "testdjango",
        'USER': "root",
        'PASSWORD': "root",
        'HOST': "127.0.0.1"
    }
}



Run manage.py Task 允许Task

初始化先执行：makemigrations 再执行 migrate


makemigrations xx 创建建议数据库
migrate xx 迁移数据

```
