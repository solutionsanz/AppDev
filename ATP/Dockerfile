# LICENSE UPL 1.0
#
# Copyright (c) 2014-2018 Oracle and/or its affiliates. All rights reserved.
#
# ORACLE DOCKERFILES PROJECT
# --------------------------
#
# Dockerfile template for Oracle Instant Client
#
# Note: this dockerfile is designed to work with the vagrant project
# As such all required files should already be in the correct locations
# and all required sub-directories etc would already have been created as a 
# result of git clone.
# The following additional instructions are only to cover the Use Case where 
# you are trying to pick up this Dockerfile and run it outside of the vagrant 
# project.
#
# REQUIRED FILES TO BUILD THIS IMAGE
# ==================================
# 
# From http://www.oracle.com/technetwork/topics/linuxx86-64soft-092277.html
#  Download the following required and optional RPMs:
#
#    - REQUIRED
#    - oracle-instantclient18.3-basic-18.3.0.0.0-1.x86_64.rpm
#
#    - OPTIONAL
#    - oracle-instantclient18.3-devel-18.3.0.0.0-1.x86_64.rpm
#    - oracle-instantclient18.3-sqlplus-18.3.0.0.0-1.x86_64.rpm 
#
# HOW TO BUILD THIS IMAGE
# -----------------------
#
# Create the following directory tree structure under the directory containing this Dockerfile
#
# ---- directory containing Dockerfile
# ------ requiredFiles
# ------ requiredFiles/wallet
# ------ pythonFiles
#
# Put all the downloaded rpm files into the requiredFiles directory
#
# Run: 
#      $ docker build -t solutionsanz/instantclient-adw-py:18.3.0 . 
#
#      $ docker run -it --rm solutionsanz/instantclient-adw-py:18.3.0 bash
#
# Download the client credentials wallet.zip file for your Autonomous Transaction Processing and / or Autonmous Data Warehouse instance and drop into the requiredFiles/wallet directory
#
# Drop any of your python code into the pythonFiles directory
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
    mkdir -p /home/vagrant/pythonscripts && \
    mkdir -p /home/vagrant/cc_wallet

# Now stream edit the sqlnet.ora file to point to the location of the credential wallet 
ADD ./requiredFiles/wallet/* /home/vagrant/cc_wallet/
ENV TNS_ADMIN=/home/vagrant/cc_wallet
WORKDIR /home/vagrant/cc_wallet
RUN sed -i 's#?/network/admin#/home/vagrant/cc_wallet#g' ./sqlnet.ora && \
    sed -i 's/SSL_SERVER/#SSL_SERVER/g' ./sqlnet.ora

ADD ./pythonFiles/*.py /home/vagrant/pythonscripts/ 

CMD ["sqlplus", "-v"]

