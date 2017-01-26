#!powershell
# <license>

# WANT_JSON
# POWERSHELL_COMMON

$module = New-Object psobject @{
    changed = $false
};

$params = Parse-Args $args

$usr= Get-Attr $params "usr" $FALSE
$pwd= Get-Attr $params "pwd" $FALSE

If ($usr -eq $FALSE) { Fail-Json (New-Object psobject) "Missing required argument: usr" }
If ($pwd -eq $FALSE) { Fail-Json (New-Object psobject) "Missing required argument: pwd" }

Set-ADAccountPassword $usr -Reset -NewPassword (ConvertTo-SecureString -AsPlainText $pwd -Force);

Exit-Json $module
