# **Shell & Coreutils**

Checklist :

* [ ] Suspension/reprise de process interactif (`Ctrl-Z`/`fg`, gestion des jobs en shell natif)
* [~] Pipe, redirection et duplication de flux (`|`, `>`, `>>`, `<`, `2>`, `tee`, rediriger stdout/stderr)
* [ ] Coreutils avancés (`date -d`, `touch -d`, `sleep 0.2`, `env -i`, `nproc`, `tty`, `numfmt`…)
* [ ] Exécution/test de scripts dans environnement minimal (`env -i`, `unset VAR`, process clean)
* [ ] Recherche CLI : `grep`, `find`, `awk`, `sed`, natif + fallback modernes (`rg`, `fd`)
* [~] Navigation shell rapide : `cd`, `pushd`/`popd`, navigation efficace dans l’historique, outils genre `z`, `zoxide`
* [x] Compréhension fine du rôle du shell (`sh`, `bash`, `zsh`, différence avec scripts POSIX)
* [ ] Utilisation judicieuse des substitutions de commandes (`$(cmd)`, `` `cmd` ``), arithmétiques, expansions avancées
* [x] Gestion et modification de l’environnement (`export`, `set`, `unset`, variables temporaires pour une commande)
* [ ] Savoir quand recourir à des outils externes (ex : utiliser bash natif plutôt que `sed`/`awk` pour des traitements simples)
* [ ] Usage de `Pure Bash Bible`/`Pure SH Bible` ou équivalent pour optimiser scripts natifs
* [ ] Récupération d’infos système bas niveau sans outils non-standards
