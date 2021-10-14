# befor run the script,you should connet to azure by the follow command
# Connect-AzAccount -Environment AzureChinaCloud
# then run the script like this: 
#.\azure.ps1 "C:\Users\aohan\Desktop\outTest\2006\netskyper-cpe_azure.vhd"

$vhdFilePath = $args[0]
$vhdSizeBytes = (Get-Item $vhdFilePath).length

$diskconfig = New-AzDiskConfig -SkuName 'StandardSSD_LRS' -OsType 'linux' -UploadSizeInBytes $vhdSizeBytes -Location 'chinanorth2' -CreateOption 'Upload'

New-AzDisk -ResourceGroupName 'netskyperRes' -DiskName 'netskyperDisk' -Disk $diskconfig

$diskSas = Grant-AzDiskAccess -ResourceGroupName 'netskyperRes' -DiskName 'netskyperDisk' -DurationInSecond 86400 -Access 'Write'

$disk = Get-AzDisk -ResourceGroupName 'netskyperRes' -DiskName 'netskyperDisk' 

AzCopy.exe copy $vhdFilePath $diskSas.AccessSAS --blob-type PageBlob

Revoke-AzDiskAccess -ResourceGroupName 'netskyperRes' -DiskName 'netskyperDisk' 