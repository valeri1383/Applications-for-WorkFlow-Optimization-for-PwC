import subprocess



# PowerShell command

#powershell_command = "$Env:ComputerName"



# Execute PowerShell command
result = subprocess.run(["powershell", "-Command", powershell_command], capture_output=True, text=True)

# Check if the command was successful
if result.returncode == 0:
    # Print the command output
    print(result.stdout)
else:
    # Print the error message
    print(result.stderr)


