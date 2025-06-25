# **Automatisation & sécurité shell**

Checklist :

* [x] Versionnement systématique de tes configs (dotfiles, `.vimrc`, `.bashrc`, scripts shell) via Git ou équivalent
* [x] Documentation de tes principaux alias, scripts, raccourcis personnalisés, *sans* te reposer uniquement sur ta mémoire
* [~] Anticipation et gestion des commandes à risque (`rm -rf`, test de sécurité, dry-run, protections natives, alias safe…)
* [~] Capacité à restaurer rapidement un shell minimal sur machine vierge (config d’urgence, coreutils only, pas de plugin)
* [~] Automatisation des sauvegardes critiques (script shell, cron, rsync, snapshot)
* [ ] Analyse et gestion des logs systèmes en natif (rotation, archivage, suppression planifiée)
* [ ] Sécurisation de base d’un shell distant (SSH keys, configuration stricte, limitation des accès, logs de connexion)
* [~] Inspection, modification, restauration de permissions/ownership (`chmod`, `chown`, `chgrp`, scénarios d’usage “tendus”)
* [ ] Audit de sessions/actions (`script`, `history`, centralisation des logs, transmission à un tiers)
* [ ] Maîtrise des techniques de fallback/survie en environnement restreint (perte de SSH, shell limité, tty de secours)
* [ ] Préparation de “kits de secours” : liste de commandes/actions pour prise en main d’un système inconnu


 **Diagnostic système & monitoring**

Checklist :

* [~] Diagnostic de l’espace disque sans GUI (`df`, `du`, outils alternatifs modernes type `ncdu`, `duf`, `disk` rust)
* [~] Analyse et surveillance des processus (`ps aux`, `top`, `htop`, `glances`, `procs`)
* [ ] Identification et gestion des ressources (CPU, RAM, swap, load average…) via outils natifs et alternatifs
* [ ] Usage de `jq`, `numfmt` pour manipuler/transformer des sorties JSON/numériques en shell
* [ ] Utilisation de `watch`, `while`/`for` shell, boucles de monitoring “pauvres” mais natives
* [ ] Automatisation de tâches répétitives : scripts shell, alias, fonctions shell, usage de `cron` natif (cron user, systemd timers)
* [ ] Détection automatique de la présence/disponibilité d’un outil (ex : test `command -v`, fallback)
* [ ] Intégration d’outils modernes (rust/binaire) sans casser la portabilité de workflow (ne pas rendre son shell dépendant)
* [~] Recherche et inspection rapide de logs via shell pur (`cat`, `less`, `zcat`, `grep`, navigation/filtres/visualisation dans gros fichiers)
* [x] Manipulation efficace de fichiers volumineux, paginés, compressés (`less`, `zless`, `head`, `tail`, options avancées)
* [ ] Accès rapide aux tâches planifiées système (`crontab -l`, `/etc/cron.*`, `systemctl list-timers`, inspection/édition)
* [ ] Vérification des connexions réseau actives/ports ouverts (`ss`, `netstat`, `lsof`, compréhension des arguments clés)
* [ ] Utilisation d’outils de test réseau natifs (`ping`, `traceroute`, `curl`, `wget`, diagnostic connectivité)
* [ ] Prise en main et usage des formats d’export : CSV, JSON (sortie outils/parse), traitements ad hoc (`cut`, `awk`, `sed`, `csvkit`…)
* [~] Sauvegarde, archivage, transfert de données sans GUI (`cp`, `mv`, `tar`, `gzip`, `rsync`…)
* [ ] Gestion de l’historique et de la reproductibilité des commandes (`history`, `script`, `tee`, export historique, session replay)

#  **Exploration un système inconnu (Unix/Linux)**

Checklist :

* [ ] Identification immédiate du contexte système (distro, version, kernel, arch, `uname`, `lsb_release`, `/etc/os-release`)
* [ ] Découverte et analyse des utilisateurs, sessions actives, connexions (`who`, `w`, `last`, `env`, `id`)
* [~] Inspection de l’environnement utilisateur (variables, shell, `echo $SHELL`, `printenv`, `set`)
* [ ] Observation et analyse des processus en cours (`ps aux`, `top`, statuts, priorités, `nice`, `renice`, kill signal)
* [ ] Navigation arborescente, découverte rapide des dossiers/fichiers critiques (`pwd`, `ls -lah`, `tree`, repérage des dotfiles)
* [ ] Recherche efficace de fichiers/chaînes (`find`, `grep`, options avancées, extraction de contexte, navigation rapide)
* [x] Lecture et exploration fine des fichiers volumineux/logs (`cat`, `head`, `tail`, `less`, recherche dans less, `zcat` sur logs compressés)
* [ ] Investigation du réseau (ports ouverts, connexions actives, `ss -tuln`, `netstat`, `lsof -i`, diagnostic connectivité, `ping`, `curl`, `traceroute`)
* [ ] Audit rapide de la planification des tâches système (`crontab -l`, `/etc/cron*`, `systemctl list-timers`, analyse des scripts automatisés)
* [x] Vérification de la sécurité, permissions et accès critiques (`ls -l`, `chmod`, `chown`, analyse des droits sur les dossiers stratégiques)
* [ ] Lecture, analyse et gestion des logs système (`/var/log/*`, rotation, recherche ciblée, identification d’anomalies)
* [ ] Traces et audit d’activité utilisateur (`history`, `script`, sauvegarde de session, export d’historique pour reporting)
* [ ] Sauvegarde de découvertes, extraction de preuves, partage reproductible (logs, exports, fichiers clés)
* [ ] Capacité à tout réaliser sans aucun outil tiers (coreutils, POSIX) et à identifier rapidement la présence/absence d’outils modernes
#  **Sauvegarde & permissions**

Checklist :

* [~] Sauvegarde manuelle et automatisée de fichiers et dossiers critiques (`cp`, `tar`, `gzip`, `rsync`, scripts, cron/systemd timer)
* [~] Utilisation d’`rsync` : compréhension des concepts (delta transfer, partial, archive, preserve, exclude, delete, update…), flags essentiels, scénarios de backup/restauration
* [ ] Détection et gestion des pièges/finesses d’`rsync` (slash terminal, permissions, synchronisation bidirectionnelle, edge-cases)
* [ ] Gestion et rotation des sauvegardes (logrotate, scripts, archivage périodique, purge automatisée)
* [ ] Restauration rapide depuis des archives ou backups (décompression, restauration sélective, vérification d’intégrité)
* [x] Manipulation des permissions fichiers/dossiers (`ls -l`, `chmod`, `chown`, `chgrp`), octal/symbolique, scénarios classiques/complexes
* [~] Analyse et modification récursive des droits (`chmod -R`, `chown -R`)
* [~] Compréhension des liens symboliques/hardlinks, usages et limitations
* [x] Identification et résolution de problèmes de droits (“Permission denied”, ownership incorrect, gestion d’accès multi-utilisateurs)
* [x] Mise en œuvre de sauvegardes reproductibles/portables (backup cross-OS, script shell natif)
* [~] Automatisation de sauvegardes et restaurations (cron/systemd, alertes, reporting)

# **Shell & Coreutils**

Checklist :

* [ ] Suspension/reprise de process interactif (`Ctrl-Z`/`fg`, gestion des jobs en shell natif)
* [~] Pipe, redirection et duplication de flux (`|`, `>`, `>>`, `<`, `2>`, `tee`, rediriger stdout/stderr)
* [ ] Coreutils avancés (`date -d`, `touch -d`, `sleep 0.2`, `env -i`, `nproc`, `tty`, `numfmt`…)
* [ ] Exécution/test de scripts dans environnement minimal (`env -i`, `unset VAR`, process clean)
* [~] Recherche CLI : `grep`, `find`, `awk`, `sed`, natif + fallback modernes (`rg`, `fd`)
* [~] Navigation shell rapide : `cd`, `pushd`/`popd`, navigation efficace dans l’historique, outils genre `z`, `zoxide`
* [x] Compréhension fine du rôle du shell (`sh`, `bash`, `zsh`, différence avec scripts POSIX)
* [ ] Utilisation judicieuse des substitutions de commandes (`$(cmd)`, `` `cmd` ``), arithmétiques, expansions avancées
* [x] Gestion et modification de l’environnement (`export`, `set`, `unset`, variables temporaires pour une commande)
* [ ] Savoir quand recourir à des outils externes (ex : utiliser bash natif plutôt que `sed`/`awk` pour des traitements simples)
* [ ] Usage de `Pure Bash Bible`/`Pure SH Bible` ou équivalent pour optimiser scripts natifs
* [ ] Récupération d’infos système bas niveau sans outils non-standards

# **Vim / Neovim : édition & navigation**

Checklist :

* [~] Navigation rapide sans plugin (HJKL, w/W, b/B, e/E, 0, ^, $, gg, G, f/F/t/T, ;, ,, chiffres en préfixe)
* [ ] Usage avancé des text-objects (`ciw`, `da"`, `di(`, `cip`, etc.)
* [~] Opérateurs composés (`d`, `c`, `y`, `.`) et leur combinaison avec motions/text-objects
* [x] Visual mode (v, V, Ctrl+V) : sélection ligne/bloc, édition par colonne
* [ ] Rechercher/remplacer natif (`:s`, `:g`, `:v`, regex, visual+`:s`)
* [ ] Commande `:normal` pour batch processing sur sélection
* [ ] Macros : enregistrement, exécution, adaptation par ligne ou répétition
* [ ] Registers : usage natif (`"`, `@`, `<C-r>`, registres spéciaux `-`, `"0`), visualisation (`:reg`)
* [ ] Navigation via marks (`ma`, `` `a``, `:marks`, marks auto `'<'`, `'>'`, jump historique)
* [ ] Buffers, splits, tabs sans plugins (`:bnext`, `:ls`, `:split`, `:tabnew`)
* [ ] Pause/reprise process Vim (`Ctrl-Z`/`fg`) et workflow shell+Vim natif
* [ ] Exécution commandes shell / lecture fichier externe (`:!cmd`, `:r !cmd`)
* [x] Utilisation sans plugin/config (`vim -u NONE`)
* [ ] Config natif : `.vimrc`, mappings, autocmds de base
* [ ] Replace mode (`R`), dot operator, édition massive multi-ligne/bloc
* [ ] Manipulation intelligente des blocs (`%`, parenthèses, quotes…)
* [x] Remap ergonomie (ex : jj/jk pour Escape)
* [ ] Fonctions cachées/peu connues (`:center`, `:right`, `:reverse`, `:sf`, `:intro`)
* [ ] Navigation inter-buffer, historique (jumplist, changelist)
* [x] Connaissance plugins structurels/ergonomiques (sans dépendance)




Je dois pratiquer cela, en lien avec les différents PDF. Est-ce qu'il y a des choses que tu changerais ou supprimerais ou ajouterais dans cette liste ?
