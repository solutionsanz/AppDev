# LICENSE UPL 1.0
#
# Copyright (c) 2014-2018 Oracle and/or its affiliates. All rights reserved.
#
# ORACLE DOCKERFILES PROJECT
# --------------------------
#
# Dockerfile template for Oracle Instant Client
#
# REQUIRED FILES TO BUILD THIS IMAGE
# ==================================
# 
# From http://www.oracle.com/technetwork/topics/linuxx86-64soft-092277.html
#  Download the following three RPMs:
#    - oracle-instantclient18.3-basic-18.3.0.0.0-1.x86_64.rpm
#    - oracle-instantclient18.3-devel-18.3.0.0.0-1.x86_64.rpm
#    - oracle-instantclient18.3-sqlplus-18.3.0.0.0-1.x86_64.rpm 
#
# HOW TO BUILD THIS IMAGE
# -----------------------
# Put all downloaded files in the same directory as this Dockerfile
# Run: 
#      $ docker build -t oracle/instantclient-adw-py:18.3.0 . 
#
#      $ docker run -it --rm oracle/instantclient-adw-py:18.3.0 bash
#
#
FROM oraclelinux:7-slim

ADD ./requiredFiles/oracle-instantclient*.rpm /tmp/

RUN  yum -y install /tmp/oracle-instantclient*.rpm && \
     rm -rf /var/cache/yum && \
     rm -f /tmp/oracle-instantclient*.rpm && \
     echo /usr/lib/oracle/18.3/client64/lib > /etc/ld.so.conf.d/oracle-instantclient18.3.conf && \
     ldconfig

ENV PATH=$PATH:/usr/lib/oracle/18.3/client64/bin
ENV LD_LIBRARY_PATH=$LD_LIBRARY_PATH:/usr/lib/oracle/18.3/client64/lib

RUN yum -y install yum-utils && \
    yum-config-manager --enable ol7_developer_EPEL && \
    yum-config-manager --enable ol7_developer && \
    yum install -y gcc python-devel && \ 
    yum install -y python-pip && \
    pip install --upgrade pip && \
    python -m pip install cx_Oracle --upgrade &&\
    pip install cx_Oracle && \
    mkdir -p /home/pythonscripts && \
    mkdir -p /home/cc_wallet

# Now stream edit the sqlnet.ora file to point to the location of the credential wallet 
ADD ./requiredFiles/wallet/* /home/cc_wallet/
ENV TNS_ADMIN=/home/cc_wallet
WORKDIR /home/cc_wallet
RUN sed -i 's#?/network/admin#/home/cc_wallet#g' ./sqlnet.ora && \
    sed -i 's/SSL_SERVER/#SSL_SERVER/g' ./sqlnet.ora

ADD *.py /home/pythonscripts/ 

CMD ["sqlplus", "-v"]

