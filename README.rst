=====
ip138
=====
ip138 IP 地理位置信息查询API
http://www.ip138.com/

|travis|
|pypi|
|license|

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
import usage import 使用
======================
.. code-block:: python

    from ip138.ip138 import ip138
    ip138("111.111.111.111")


.. |travis| image:: https://travis-ci.org/RicterZ/nhentai.svg?branch=master
   :target: https://travis-ci.org/RicterZ/nhentai

.. |pypi| image:: https://img.shields.io/pypi/dm/ip138.svg
   :target: https://pypi.org/project/ip138/

.. |license| image:: https://img.shields.io/github/license/kellyhwong/ip138.svg
   :target: https://github.com/KellyHwong/ip138/blob/master/LICENSE