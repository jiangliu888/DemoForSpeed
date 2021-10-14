#!/bin/bash
export  WORKSPACE=/home/jenkins
cd ${WORKSPACE}/ipk
pkg=`ls aiwan-cpe*.ipk`
opkg install  --force-reinstall $pkg
if [ $? -ne 0 ];then
   echo "install aiwan-cpe failed."
   exit 1
fi