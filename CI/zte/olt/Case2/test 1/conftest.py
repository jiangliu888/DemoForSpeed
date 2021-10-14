#!/usr/bin/python
# -*- coding: utf-8 -*-
# conftest.py

# 1.conftest.py文件名字是固定的，不可以做任何修改
# 2.文件和用例文件在同一个目录下，那么conftest.py作用于整个目录
# 3.conftest.py文件所在目录必须存在__init__.py文件
# 4.conftest.py文件不能被其他文件导入
# 5.所有同目录测试文件运行前都会执行conftest.py文件

import pytest
import paramiko
from paramiko.py3compat import u

@pytest.fixture()
def login(username='zte', password='DRLzte123..', ip='10.230.183.167', v_port=22):
    ssh = paramiko.SSHClient()
    ssh.set_missing_host_key_policy(paramiko.AutoAddPolicy())
    ssh.connect(ip, v_port, username, password)

    return ssh