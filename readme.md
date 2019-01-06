# 中国桥梁网项目
> 网址参考 http://m.cnbridge.cn

## 使用方法

### 1. 安装

``` bash
# 将该仓库克隆到本地
git clone https://github.com/panghupy/bridge_engine.git
# 打开项目根目录
cd bridge_engine
# $project_root是git仓库的根目录
$project_root = pwd
# 安装依赖(可能需要sudo权限，必须是python3环境)
pip install -r requirements.txt
```

### 2. 配置

#### 2.1 mysql数据库配置

``` bash
# 进入mysql环境，并创建叫做bridge的数据库
mysql -u root -p
# 输入mysql密码，初始密码一般为123456，或者为空
> CREATE DATABASE bridge DEFAULT CHARACTER SET utf8 COLLATE utf8_general_ci;
> use bridge;
# 按CTRL + D退出
```

#### 2.2 项目配置

``` bash
cd $project_root/django_bridge/django_bridge
cp settings.example.py settings.py
# 修改settings.py中的数据库配置
# MYSQL_USER和MYSQL_PWD
vim settings.py
cd $project_root/spider_bridge/bridge
cp settings.example.py settings.py
# 修改settings.py中的数据库配置
# MYSQL_USER和MYSQL_PWD
vim settings.py
vim pipelines.py
# 找到第66行：self.conn = pymysql.Connect('localhost', 'root', '123456', 'bridge', charset="utf8", use_unicode=True)
# 这里的root，123456也需要修改成自己的实际mysql账号及密码

cd $project_root/django_bridge
python3 manage.py migrate
```

#### 3 项目运行

``` bash
# 运行爬虫
cd $project_root/spider_bridge/bridge/spiders
python3 main.py
# 运行django网站
cd $project_root/django_bridge
python3 manage.py runserver
```

## 使用须知

- 本项目的依赖基于python3，请确保python3环境安装正常
- 目前关键词是在`$project_root/spider_bridge/bridge/spiders/newsCreawl.py` 中，之后会改进其可扩展性