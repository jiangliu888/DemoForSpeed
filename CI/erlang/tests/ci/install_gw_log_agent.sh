#!/bin/bash
export  WORKSPACE=/home/jenkins
cd ${WORKSPACE}/ipk
pkg=`ls aiwan-log-agent*.ipk`
opkg install   --force-reinstall $pkg --nodeps
if [ $? -ne 0 ];then
       echo "install aiwan-log-agent failed."
       exit 1
fi
