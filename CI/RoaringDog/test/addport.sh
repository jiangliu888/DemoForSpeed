cd /opt/cmdb/tuhao;
sudo sqlite3 db.sqlite3 'insert or replace into configure_ip(id, is_nat,gateway,iface_name,netmask,isp_id,server_id,public_ip) values(13,0,"","enp1s0f3",24,2,47,"13.1.1.3");'
