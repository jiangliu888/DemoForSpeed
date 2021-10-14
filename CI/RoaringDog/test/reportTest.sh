ctime=$1
site=$2
sn=$3
union=$4
lastmonth=$(date "+%Y-%m-%dT%H:%M:%SZ" -d '1 month ago')
lastweek=$(date "+%Y-%m-%dT%H:%M:%SZ" -d '1 week ago')

if [ $union ];then
    if [ $ctime = "lastmonth" ];then
        mongo --host mongo insight --eval "db.assets.update({ 'sn' : '$sn'},{\$set:{'createdAt': ISODate('$lastmonth')}})"
        mongo --host mongo insight --eval "db.sites.update({ 'name' : '$site'},{\$set:{'createdAt': ISODate('$lastmonth')}})"
        mongo --host mongo insight --eval "db.unions.update({ 'name' : '$union'},{\$set:{'createdAt': ISODate('$lastmonth')}})"
    elif [ $ctime = "lastweek" ];then
        mongo --host mongo insight --eval "db.assets.update({ 'sn' : '$sn'},{\$set:{'createdAt': ISODate('$lastweek')}})"
        mongo --host mongo insight --eval "db.sites.update({ 'name' : '$site'},{\$set:{'createdAt': ISODate('$lastweek')}})"
        mongo --host mongo insight --eval "db.unions.update({ 'name' : '$union'},{\$set:{'createdAt': ISODate('$lastweek')}})"
    fi
else
    if [ $ctime = "lastmonth" ];then
        mongo --host mongo insight --eval "db.assets.update({ 'sn' : '$sn'},{\$set:{'createdAt': ISODate('$lastmonth')}})"
        mongo --host mongo insight --eval "db.sites.update({ 'name' : '$site'},{\$set:{'createdAt': ISODate('$lastmonth')}})"
    elif [ $ctime = "lastweek" ];then
        mongo --host mongo insight --eval "db.assets.update({ 'sn' : '$sn'},{\$set:{'createdAt': ISODate('$lastweek')}})"
        mongo --host mongo insight --eval "db.sites.update({ 'name' : '$site'},{\$set:{'createdAt': ISODate('$lastweek')}})"
    fi
fi
