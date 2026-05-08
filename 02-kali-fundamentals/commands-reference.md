# Linux command reference

A quick reference of commands practiced in this lab section. Each is grouped by purpose.

## Navigation

| Command | Purpose |
|---------|---------|
| `pwd` | Print current working directory |
| `cd ~` | Change to home directory |
| `cd $HOME` | Same as `cd ~` |
| `cd ..` | Move up one directory |
| `cd -` | Switch to previous directory |

## Listing

| Command | Purpose |
|---------|---------|
| `ls` | List visible files |
| `ls -l` | Long format with permissions, owner, size |
| `ls -al` | Include hidden files |
| `ls -lh` | Human-readable file sizes |

## File operations

| Command | Purpose |
|---------|---------|
| `echo "text" > file` | Create/overwrite file |
| `echo "text" >> file` | Append to file |
| `cat file` | Display file contents |
| `head file` | First 10 lines |
| `tail file` | Last 10 lines |
| `tail -f file` | Follow live (great for logs) |

## Process management

| Command | Purpose |
|---------|---------|
| `ps -aux` | All processes, all users |
| `ps -u` | Current user's processes |
| `top` | Live process monitor |
| `kill PID` | Terminate process |
| `kill -9 PID` | Force kill |

## Networking

| Command | Purpose |
|---------|---------|
| `ifconfig` | Network interface info (legacy) |
| `ip a` | Modern equivalent |
| `ping host` | ICMP echo test |
| `netstat -tuln` | Listening ports |
| `ss -tuln` | Modern netstat |

## System and services

| Command | Purpose |
|---------|---------|
| `sudo service --status-all` | List all services |
| `systemctl status NAME` | Check a specific service |
| `journalctl -u NAME` | Service logs (systemd) |

## Help

| Command | Purpose |
|---------|---------|
| `man COMMAND` | Manual page |
| `COMMAND --help` | Quick help |
| `which COMMAND` | Where the binary lives |
