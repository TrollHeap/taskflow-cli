## 5. **Shell avancé, patterns modernes, “CLI Power User”**

- [ ] **Gestion avancée des jobs, subshells, background/foreground**
    - `jobs`                  # Lister jobs en arrière-plan
    - `sleep 100 &`           # Lancer tâche en arrière-plan
    - `fg %1`                 # Ramener job au foreground
    - `bg %1`                 # Remettre job en arrière-plan
    - `kill %1` / `kill 1234` # Tuer un job/processus
    - `(cd /tmp && ls)`       # Subshell pour isoler contexte

- [ ] **Process substitution, fork, xargs, parallel**
    - `diff <(ls dir1) <(ls dir2)`            # Substitution de process
    - `find . -name '*.log' | xargs grep "foo"` # Appliquer grep sur chaque fichier
    - `ls *.txt | parallel gzip`              # Compression multi-thread (si `parallel` installé)
    - `for i in {1..5}; do sleep 1 & done`    # Fork massif, jobs multiples

- [ ] **Traps, gestion d’événements, nettoyage sécurisé**
    - `trap 'echo "bye"' EXIT`                # Action à la sortie du shell/script
    - `trap 'rm -f /tmp/tmp*' EXIT`           # Nettoyage fichiers temporaires à la fin
    - `trap '' INT`                           # Ignorer Ctrl-C
    - `trap 'echo SIGUSR1' SIGUSR1`           # Handler signal personnalisé

- [ ] **Manipulation des flux & redirections avancées**
    - `exec > >(tee log.txt)`                 # Dupliquer stdout dans un fichier
    - `command 2> err.log 1> out.log`         # Rediriger stdout/stderr séparément
    - `ls | tee >(wc -l) | sort`              # Split/brancher un flux avec process substitution
    - `: > vide.txt`                          # Créer/vider un fichier sans fork

- [ ] **“Pure Bash” : expansions, arrays, pattern matching, indirection**
    - `f="foo-bar.txt"; echo ${f%.txt}`       # Supprimer suffixe
    - `a=(un deux trois); echo ${a[1]}`       # Tableaux Bash
    - `[[ "$str" == *foo* ]] && echo "ok"`    # Pattern matching natif
    - `for i in "${!a[@]}"; do echo $i:${a[$i]}; done` # Boucle avec index
    - `declare var="world"; eval_var="var"; echo ${!eval_var}` # Indirection

- [ ] **Detection automatique d’outils / fallback**
    - `command -v jq`                         # Vérifier la présence d’un binaire
    - `if command -v bat >/dev/null; then bat file; else cat file; fi` # Fallback natif

- [ ] **Outils modernes vs natif**
    - `rg pattern . || grep -r pattern .`     # Recherche rust (ripgrep) puis natif en fallback
    - `fd . || find .`                        # Find moderne ou fallback POSIX
    - **Principe** : *Ne jamais casser le workflow natif si l’outil rust/binaire n’est pas dispo.*

- [ ] **Containers, réseau, shell distant**
    - `docker ps -a`                          # Lister containers
    - `docker exec -it <id> bash`             # Shell dans un container
    - `docker logs <id>`                      # Logs container
    - `docker run -it --rm alpine sh`         # Shell temporaire dans conteneur jetable
    - `docker system prune -a`                # Cleanup massif
    - `docker network ls`                     # Voir réseaux containers
    - `podman ...`                            # Idem docker, mais rootless
    - `ssh user@host 'uptime'`                # Exécution distante
