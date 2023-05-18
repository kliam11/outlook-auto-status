$objShell = New-Object -ComObject ("WScript.Shell")
$objShortcut = $objShell.CreateShortcut($env:USERPROFILE+"AppData\Roaming\Microsoft\Windows\Start Menu\Programs\Startup"+"\OutlookAuto.lnk")
$objShortcut.TargetPath("C:\src\OutlookAuto\dist\dist\main.exe")
$objShortcut.Save() 