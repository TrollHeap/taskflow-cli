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
