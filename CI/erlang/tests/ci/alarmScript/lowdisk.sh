num=`df -h |grep sda2 |awk -F" " '{print $4}' |tr -cd "[0-9]"`
count=`echo "$(($num - 2))"`
ddNum=`expr $count \* 1024`
dd if=/dev/zero of=testdf bs=1M count=$ddNum& > disk.log