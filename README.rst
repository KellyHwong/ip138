=====
ip138
=====
ip138 IP 地理位置信息查询API
http://www.ip138.com/


========================
Installation 安装 (pip3)
========================
.. code-block:: bash

    pip3 install ip138

=============================
Installation 安装 (git clone)
=============================
.. code-block:: bash

    git clone https://github.com/KellyHwong/ip138
    cd ip138
    python3 setup.py install

==========
Usage 用法
==========
.. code-block:: bash

    ip138 --ip={Your Query IP Address}

============
Example 例子
============
.. code-block:: bash

    ip138 --ip=172.217.161.164


======================
import use import 使用
======================
.. code-block:: python

    from ip138.ip138 import ip138
    ip138("111.111.111.111")
