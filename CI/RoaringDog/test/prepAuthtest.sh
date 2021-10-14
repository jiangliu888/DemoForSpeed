export PYTHONPATH=../erlang
export PYTHONHTTPSVERIFY=0
python cypress/integration/utils/python-util/CheckAudit.py "['delete_corps']" 'CompanyAudit' '公司审计'