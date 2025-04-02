# learning_log
learning_log


## 框架：DJANGO
### 📂目录
#### ll_project
├── 📂learning_logs



## 修改管理的数据时都采取如下三个步骤：
### 1、修改models.py
### 2、对leaning_logs调用makemigrations
    python manage.py makemigrations learning_logs
### 3、以及让 Django迁移项⽬。
    python manage.py migrate