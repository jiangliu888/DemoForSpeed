#!/bin/bash
set -x
key=$1
value=$2
envPath="/etc/aiwan_env.json"
tmpEnv="/tmp/aiwan_env.tmp"
if [ -e $envPath ]; then
  cat $envPath |jq > $tmpEnv
  grep $key $tmpEnv
  rc=`echo $?`
  if [ $rc -eq 0 ];then
    echo "env exist,update value"
    sed -ri "s/($key\")[^,]*/$key\": $value/" $tmpEnv
    mv $tmpEnv $envPath
  elif [ $rc -eq 1 ];then
    echo "need to add env"
    sed -i "2i\  \"$key\": $value," $tmpEnv
    mv $tmpEnv $envPath
  fi
else
  echo -e "{\n  \"$key\": $value\n}" > $envPath
fi
