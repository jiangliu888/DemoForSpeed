import {exec_cmd_on_local} from '../utils/consulCheck-utils'


export function customerNameCheck(companyName){    
    let cmd = "export PYTHONPATH=../erlang;python cypress/integration/utils/python-util/CheckReport.py \"['customer_name_check']\" " + companyName
    exec_cmd_on_local(cmd)    
  }

export function emptyDownloadsDir(){    
    let cmd = "export PYTHONPATH=../erlang;python cypress/integration/utils/python-util/CheckReport.py \"['empty_downloads_dir']\" "
    exec_cmd_on_local(cmd)    
  }

export function serviceItemCheck(item,expect){    
    let cmd = "export PYTHONPATH=../erlang;python cypress/integration/utils/python-util/CheckReport.py \"['service_item_check']\" " + item + " " + expect
    exec_cmd_on_local(cmd)    
  }

export function exportSuccessCheck(){    
    let cmd = "export PYTHONPATH=../erlang;python cypress/integration/utils/python-util/CheckReport.py \"['export_success_check']\" "
    exec_cmd_on_local(cmd)    
  }

export function serviceOverviewCheck(data){    
    let cmd = "export PYTHONPATH=../erlang;python cypress/integration/utils/python-util/CheckReport.py \"['service_overview_check']\" " + data
    exec_cmd_on_local(cmd)    
  }

export function deviceStatusCheck(data){    
    let cmd = "export PYTHONPATH=../erlang;python cypress/integration/utils/python-util/CheckReport.py \"['device_status_check']\" " + data
    exec_cmd_on_local(cmd)    
  }

  export function serviceQualityCheck(data){    
    let cmd = "export PYTHONPATH=../erlang;python cypress/integration/utils/python-util/CheckReport.py \"['service_quality_check']\" " + data
    exec_cmd_on_local(cmd)    
  }

  export function ticketDetailCheck(data){    
    let cmd = "export PYTHONPATH=../erlang;python cypress/integration/utils/python-util/CheckReport.py \"['ticket_detail_check']\" " + data
    exec_cmd_on_local(cmd)    
  }