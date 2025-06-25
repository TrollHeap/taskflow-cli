## 5. **Shell avancé, patterns modernes, “CLI Power User”**

* [ ] Gestion avancée des jobs : `jobs`, `sleep 100 &`, `fg %1`, `bg %1`, `kill %1`, `kill 1234`
* [ ] Subshells et isolation de contexte : `(cd /tmp && ls)`
* [ ] Substitution de process : `diff <(ls dir1) <(ls dir2)`
* [ ] Traitement par `xargs`, `parallel`, fork massif (`find . -name '*.log' | xargs`, `parallel gzip`, `for i in … &`)
* [ ] Utilisation de `trap` pour capture d’événements (`trap '...' EXIT`, `trap '' INT`, `trap '...' SIGUSR1`)
* [ ] Nettoyage sécurisé de ressources temporaires avec `trap`
* [ ] Redirections avancées : `exec > >(tee log.txt)`, `2> err.log 1> out.log`, `: > vide.txt`
* [ ] Manipulations de flux via `tee` + substitution (`ls | tee >(wc -l)`)
* [ ] Pure Bash : suppression suffixe `${f%.txt}`, tableaux `${a[1]}`, `[[ "$str" == *foo* ]]`, `declare` + `${!var}`
* [ ] Pattern matching natif avec `[[ ... ]]`
* [ ] Accès indexé des arrays Bash avec `${!a[@]}` et boucles
* [ ] Indirection Bash : `${!eval_var}`
* [ ] Détection d’outils avec `command -v`
* [ ] Fallback natif : `if command -v bat; then bat; else cat; fi`
* [ ] Fallback moderne/natif : `rg || grep`, `fd || find`
* [ ] Containers Docker : `ps`, `exec`, `logs`, `run`, `prune`, `network`
* [ ] Podman : usage rootless équivalent à Docker
* [ ] SSH distant : `ssh user@host 'commande'`
