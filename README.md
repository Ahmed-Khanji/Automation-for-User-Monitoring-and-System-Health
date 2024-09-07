# Daily Machine Usage Report Script

This script generates a daily report tracking which users are currently logged into which machines in a company. It processes a list of system events, specifically user logins and logouts, to determine the current state of each machine. The script outputs a report listing each machine and the users connected to it, formatted with machine names followed by users separated by commas. This tool helps IT specialists monitor machine usage efficiently.
It also check machine health like CPU and Memory storage and report health condition.

To use: Pass a list of event objects to the script, which then processes the data and generates the report.

