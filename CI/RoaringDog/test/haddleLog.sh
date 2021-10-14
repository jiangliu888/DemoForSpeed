logType=$2
company=$3
action=$1

if [ $action = 'emptyLog' ];then
    if [ $logType = "登录日志" ];then
        if [ $company = "ALL" ];then
            mongo --host  mongo insight --eval "db.operations.remove({})"
        else
            mongo --host  mongo insight --eval "db.operations.remove({'companyName':'$company'})"
        fi
    elif [ $logType = "操作日志" ];then
        if [ $company = "ALL" ];then
            mongo --host  mongo insight --eval "db.logs.remove({})"
        else
            mongo --host  mongo insight --eval "db.logs.remove({'companyName':'$company'})"
        fi       
    fi
elif [ $action = 'modifyLogTime' ];then
    if [ $logType = "登录日志" ];then
        mongo --host  mongo insight --eval "db.operations.update({ 'company':'$company'},{\$set:{'date' : ISODate('2021-08-01T07:00:37.995Z')}},{multi:true})"
        
    elif [ $logType = "操作日志" ];then
        mongo --host  mongo insight --eval "db.logs.update({ 'companyName':'$company'},{\$set:{'date' : ISODate('2021-08-01T07:00:37.995Z')}},{multi:true})"      
    fi
fi