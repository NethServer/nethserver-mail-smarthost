nethserver-mail-smarthost
=========================

Send mail using smart host, also provide basic web interface implementation for web server.

Features
--------

* Smarthost

Configuration database
----------------------

Postfix example: ::

 postfix=service
    ...
    SmartHostAuth=disabled
    SmartHostAuthStatus=disabled
    SmartHostName=192.168.5.252
    SmartHostPassword=password
    SmartHostPort=25
    SmartHostStatus=disabled
    SmartHostTlsStatus=enabled
    SmartHostUsername=ns1

