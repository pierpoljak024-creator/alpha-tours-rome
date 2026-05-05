' Create Desktop shortcuts for Alpha Tours Rome Bot
Set WshShell = CreateObject("WScript.Shell")
strDesktop = WshShell.SpecialFolders("Desktop")
strStartup = WshShell.SpecialFolders("Startup")

' 1. Desktop shortcut - Open Bot Chat
Set Shortcut = WshShell.CreateShortcut(strDesktop & "\Alpha Tours Bot - Chat.lnk")
Shortcut.TargetPath = "C:\Users\pierf\Desktop\Start Alpha Tours Bot.bat"
Shortcut.WorkingDirectory = "C:\Users\pierf\AlphaTours-Project"
Shortcut.Description = "Start Alpha Tours Rome Telegram bot"
Shortcut.Save

' 2. Desktop shortcut - Deploy to Cloud
Set Shortcut2 = WshShell.CreateShortcut(strDesktop & "\Alpha Tours Bot - Deploy to Cloud.lnk")
Shortcut2.TargetPath = "cmd.exe"
Shortcut2.Arguments = "/k cd /d C:\Users\pierf\AlphaTours-Project && echo Ready to deploy! Type: modal deploy modal_deploy.py"
Shortcut2.WorkingDirectory = "C:\Users\pierf\AlphaTours-Project"
Shortcut2.Description = "Deploy Alpha Tours bot to Modal cloud"
Shortcut2.Save

' 3. Startup folder - Auto-start bot on login
Set Shortcut3 = WshShell.CreateShortcut(strStartup & "\Alpha Tours Bot.lnk")
Shortcut3.TargetPath = "C:\Users\pierf\Desktop\Start Alpha Tours Bot.bat"
Shortcut3.WorkingDirectory = "C:\Users\pierf\AlphaTours-Project"
Shortcut3.Description = "Auto-start Alpha Tours bot on login"
Shortcut3.Save

WScript.Echo "All shortcuts created!"
