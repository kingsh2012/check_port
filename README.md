check_port

一个用于解析nginx配置文件并检测所有upstreams端口是否通的web系统

功能如下:

```
1.自动检测和解析线上nginx配置文件中的所有upstream和server,对所有upstream做端口跟踪
2.自动检测和解析测试nginx配置文件中的所有upstream以及proxy_pass和server,对所有proxy_pass和upstream做端口跟踪
3.自动配置nginx数据库仓库与远程仓库同步,更新服务器端口追踪列表
4.增加自定义追踪模式(非nginx配置文件解析)
```
添加自定义探测:
![image](https://note.youdao.com/favicon.ico)

后台管理:
![image](https://note.youdao.com/favicon.ico)

```
#大致部署过程
pip install -r pip.text
#创建checkport数据库
#修改settings.py中的数据库配置
python manage.py makemigrations
python manage.py migrate
#安装redis,修改settings.py中的redis配置
#修改readnginx的handle.py和handle_test.py中的CONFIG_PATH以及GIT_PATH(用于自动解析和更新nginx配置)
#用supervisor启动系统
supervisord -c checkport/supervisord.conf
#此外,flower需要用nginx做转发,参考配置文件如下
    location ~ ^/flower/? {
        rewrite ^/flower/?(.*)$ /$1 break;
    
        sub_filter '="/' '="/flower/';
        sub_filter_last_modified on;
        sub_filter_once off;
    
        # proxy_pass http://unix:/tmp/flower.sock:/;
        proxy_pass http://xxxxxxxxxxxxxxxx;
        proxy_redirect off;
        proxy_set_header Host $host;
        proxy_set_header Upgrade $http_upgrade;
        proxy_set_header Connection "upgrade";
        proxy_http_version 1.1;
    }
```

```
其中三种常见操作为:
1.将nginx配置文件列表pull到最新
2.自动读取和解析nginx配置文件,并将获取的upstream以及proxy_pass列表写进数据库
3.探测数据库中所有需要探测的IP:PORT对象实例

可在后台管理->数据更新中手动按键更新
也可在admin后台配置Periodic tasks的celery beat定时任务
其中:
1.readnginx.tasks.git_pull_config 任务更新nginx配置文件仓库
2.pubstatus.tasks.get_status 任务获取所有IP:PORT对象状态
3.readnginx.tasks.read_nginx 任务度读取nginx配置文件并解析,更新数据库IP:PORT对象列表
可根据需求设置定时任务周期
通过flower后台可以查看任务执行情况
```

```
自定义追踪checkport的IP:PORT列表通过admin后台添加instance即可实现
```



