sn=$1
model=$2
cd /opt/cmdb/tuhao;
echo "update asset_cpes set model_id=(select id from asset_cpe_model where name=$model) where sn=2002;"
sudo sqlite3 db.sqlite3 "update asset_cpes set model_id=(select id from asset_cpe_model where name='$model') where sn=$sn;"
