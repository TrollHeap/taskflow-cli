## 4. **Monitoring et diagnostic live**


* [ ] Disque : `df`, `du`, `ncdu`, `ls -lhS`, `find . -size`, usage `inodes`
* [ ] RAM/CPU/process : `ps aux`, `top`, `htop`, `free`, `vmstat`, `iotop`, `glances`
* [ ] Process ouverts : `lsof`, `fuser`, `ss`, `netstat`, `ip`, `nmap`
* [ ] Diagnostic réseau : `ping`, `traceroute`, `nc`, `curl`, `wget`, `tcpdump`, `mtr`, `dig`, `bmon`
* [ ] SSH et accès distants : clés SSH, tunnel, multiplex, autossh, restrictions, logs, `scp`, `rsync`, `sftp`
* [ ] Lecture de logs : `cat`, `less`, `zcat`, `grep`, navigation dans gros fichiers
* [ ] Journalctl avancé : `journalctl -u`, `-f`, `--since`, `-p`, `--disk-usage`, logrotate
* [ ] Profiler le boot et les services systemd (`systemd-analyze`, `systemctl status`, timers, unit files, troubleshooting, override, templates, rescue/emergency mode)
* [ ] Export/triage d'incidents : compression, logs, diagnostics en masse
