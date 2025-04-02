"""定义 learning_logs 的 URL 模块"""

from django.urls import path
from . import views

app_name = 'learning_logs'
urlpatterns = [
    # 主页
    path('', views.index, name='index'),
    # # 显示所有的主题
    # path('topics/', views.topics, name='topics'),
    # # 显示单个主题及其所有的条目
    # path('topics/<int:topic_id>/', views.topic, name='topic'),
    # # 用于添加新主题的网页
    # path('new_topic/', views.new_topic, name='new_topic'),
    # # 用于添加新条目的网页
    # path()
]