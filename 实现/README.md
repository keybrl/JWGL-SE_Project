# 基于Web的教务管理系统

该目录下为该项目的源代码

其中`server/`是后端源代码，`user_interface/`是前端源代码。

## 如何运行

后端是基于Python Flask框架的，依赖MySQL数据库。

启动后端，首先需要配置好MySQL服务，这不是本项目的一部分。然后将数据库连接所需的参数写入`server/config.py`中

然后确保你的Python版本大于3.5，使用以下命令安装依赖

```bash
pip install -r requirements.txt
```

初始化和创建migration文件

```bash
python manage.py db init
python manage.py db migrate
```

建表

```bash
python manage.py db upgrade
```

插入测试数据（可选）：

首先进入Flask Shell

```base
python manage.py shell
```

然后在Shell中输入：

```python
InsertData.main()
```

如果没有报错，那么数据就插入完成了。

然后启动服务器

```bash
python manage.py runserver
```

默认会在 `127.0.0.1:5000` 启动测试服务器



前端，你只需要将后端的ip地址填进`user_interface/js/leader.js`和`user_interface/js/leader.min.js`，然后双击打开`user_interface/index.html`就可以了（如果后端是默认的 `127.0.0.1:5000` ，那么前端可以不用修改），或者用一个静态服务器部署它

