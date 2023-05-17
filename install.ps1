$objShell = New-Object -ComObject ("WScript.Shell")
$objShortcut = $objShell.CreateShortcut($env:USERPROFILE+"AppData\Roaming\Microsoft\Windows\Start Menu\Programs\Startup"+"\program.lnk")
$objShortcut.TargetPath("C:\src\OutlookAuto\dist\main\main.exe")
$objShortcut.Save() 