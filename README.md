## uwsgi + nginx + Django1.8.4的开发框架

#### python版本 及 其他依赖包版本号

python3.5 
django==1.8.4
djangorestframework==3.2.0
django-rest-swagger==0.3.10
pymysql==0.7.10 

## Ubuntu服务器环境搭建：

sudo apt-get update
# 安装python3.5
sudo apt-get install -y python3.5

### 若原系统里有python2,先备份系统原来的python
sudo cp /usr/bin/python /usr/bin/python_bak
### 删除系统原来的Python
sudo rm /usr/bin/python
### 默认设置成python3.5，重建软链接这样在终端中输入python默认就是 3.5版本了
sudo ln -s /usr/bin/python3.5 /usr/bin/python

# 安装pip3
sudo apt-get install -y python3-pip 

### 安装nginx
sudo apt-get install nginx

### Install uwsgi
export LDFLAGS="-Xlinker --no-as-needed"
sudo pip3 install uwsgi -i https://pypi.tuna.tsinghua.edu.cn/simple

### 切换到/var/www路径下，从github上clone代码到www文件夹下
cd /var/www 
sudo git clone https://github.com/willschang/tencomb.git

sudo chmod +x tencomb

cd tencomb
# 安装相应的依赖包
pip3 install -r requirements.txt
# 初始化系统及同步数据库
## 在tencomb下运行以下语句，同步数据
python manage.py migrate
# python manage.py makemigrations


# 修改nginx的一些配置，参考tencomb下的nginx.conf 

# 配置好nginx后，在tencomb下启动uwsgi服务
uwsgi --ini uwsgi.ini 

# 重启nginx，即可访问




