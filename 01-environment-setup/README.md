# 01 — Environment setup

Building the foundation: a safe, isolated cybersecurity lab using virtualization.

---

## Goal

Create a self-contained lab where offensive security tools and intentionally vulnerable systems can interact safely, without risk to the host machine or external networks.

## Components

| Component | Purpose | Version used |
|-----------|---------|--------------|
| Oracle VirtualBox | Hypervisor | 7.x |
| Kali Linux | Attacker VM | Kali Rolling 2025.4 |
| Metasploitable 2 | Target VM | 2.0.0 |
| NAT Network | Isolated VM-to-VM network | VirtualBox NAT Network |
| Wireshark | Packet capture and analysis | Latest |
| Cisco Packet Tracer | Network topology design | 8.2 |

---

## Setup steps

### 1. Install Oracle VirtualBox

Download from [virtualbox.org](https://www.virtualbox.org/) and install with default settings. VirtualBox is the hypervisor that runs the VMs.

### 2. Create an isolated NAT network

In VirtualBox: **File → Tools → Network Manager → NAT Networks → Create**

This creates a private network where VMs can communicate with each other and reach the internet, but cannot be reached from the host or external networks. This isolation is critical when running deliberately vulnerable systems like Metasploitable.

### 3. Deploy Kali Linux

Download the pre-built VirtualBox image from [kali.org](https://www.kali.org/get-kali/#kali-virtual-machines) and import it into VirtualBox. Default credentials: `kali / kali`.

In **VM Settings → Network**, attach the adapter to the NAT network created in step 2.

### 4. Deploy Metasploitable 2

Download from [SourceForge](https://sourceforge.net/projects/metasploitable/) and import. Default credentials: `msfadmin / msfadmin`.

Attach its network adapter to the same NAT network as Kali.

### 5. Verify connectivity

Boot both VMs and check IP assignment with `ifconfig` (or `ip a`). Then from Kali, ping the Metasploitable IP to confirm they can communicate:

```bash
ping <metasploitable-ip>
```

A successful ping confirms the lab is ready.

---

## Network design reference

Beyond the virtualized lab, network topology was practiced in Cisco Packet Tracer — building multi-router, multi-switch networks to reinforce how packets flow across segmented infrastructure. This understanding feeds directly into firewall placement, IDS positioning, and traffic flow analysis.

---

## Lessons learned

1. **Network isolation comes first.** Bridged networking exposes a vulnerable VM to your home network — always use NAT or host-only for lab work.
2. **Snapshot before experimenting.** VirtualBox snapshots let you roll back instantly when (not if) something breaks.
3. **Document IPs and credentials.** A simple lab notebook saves a lot of time when machines change addresses on reboot.

---

## Screenshots

Screenshots from the actual setup are in [screenshots/](screenshots/).

---

## Next: [02 — Kali fundamentals →](../02-kali-fundamentals/)
