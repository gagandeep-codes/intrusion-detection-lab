# 02 — Kali fundamentals

Linux command line essentials — practiced inside Kali Linux. These are the daily-driver skills behind almost every security role.

---

## Why this matters

Almost every security tool, log file, and forensic artifact lives in a Linux environment. SOC analysts read system logs. Pentesters chain Linux utilities together. Incident responders pivot through compromised hosts using shell commands.

Comfort with the command line isn't optional — it's the foundation for everything that follows.

---

## Topics covered

### File system navigation
- `pwd` — show current working directory
- `cd ~` — return to home directory
- `cd ..` — move up one directory
- `ls -l` — list files with details
- `ls -al` — include hidden files (dotfiles)

### File operations
- `echo "text" > file.txt` — create or overwrite a file
- `cat file.txt` — display file contents
- `man <command>` — read manual page for any command

### Permissions
Reading the permission string from `ls -l`:

```
-rw-r--r--  1 kali kali  220 Dec  2 21:36 .profile
```

Breakdown:
| Position | Meaning |
|----------|---------|
| `-` | File (would be `d` for directory) |
| `rw-` | Owner: read + write |
| `r--` | Group: read only |
| `r--` | Others: read only |

### Process management
- `ps -aux` — list all running processes
- `ps -u` — list current user's processes
- `kill <PID>` — terminate a process by ID
- `ping <host>` — send ICMP echo requests (used as a long-running process for practice)

### Networking
- `ifconfig` — show network interface configuration (legacy but still common)
- `ip a` — modern equivalent

### Services and logs
- `sudo service --status-all` — list all services and their state (`+` running, `-` stopped)
- `/var/log/` — system log directory
- `sudo head /var/log/boot.log` — view start of boot log

---

## Practical exercise: kill a runaway process

A common real-world situation: a process is consuming resources and you need to stop it.

```bash
# Terminal 1 — start a long-running process
ping 127.0.0.1

# Terminal 2 — find its PID
ps -u

# Terminal 2 — kill it
kill <PID-of-ping>
```

Verify in Terminal 1 that the ping has stopped. This same pattern applies to investigating suspicious processes, killing stuck services, and responding to malware.

---

## Lessons learned

1. **`man` pages are your first line of defense.** Before searching online, read the manual — it's authoritative and offline-friendly.
2. **Permissions tell a story.** A world-writable file (`rw-rw-rw-`) on a system file is often the first sign of misconfiguration or compromise.
3. **Logs in `/var/log` are forensic gold.** `auth.log`, `syslog`, and `boot.log` reveal what the system has been doing — and who's been doing it.

---

## Screenshots

Real terminal output from the lab is in [screenshots/](screenshots/).

---

## Back to [main README](../README.md)
