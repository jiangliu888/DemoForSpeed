#!/bin/bash
export  WORKSPACE=/home/jenkins
cd ${WORKSPACE}/ipk
pkg=`ls aiwan-agent-cpe*.ipk`
opkg install --force-reinstall $pkg
if [ $? -ne 0 ];then
   echo "install aiwan-agent-cpe failed."
   exit 1
fi
