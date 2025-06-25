## Vim / Neovim – Checklist pratique

- [ ] **Navigation rapide sans plugin**
    - HJKL (déplacement)
    - w/W, b/B, e/E (mot, début/fin mot)
    - 0, ^, $ (début/fin ligne)
    - gg, G (début/fin fichier)
    - `:42<CR>` (aller ligne N)
    - /motif, n/N, *, # (recherche)
- [ ] **Text-objects avancés**
    - ciw (change inner word)
    - da" (delete around ")
    - di( (delete inside parenthèses)
    - vi{, va', vip (sélection bloc/mot)
- [ ] **Opérateurs composés**
    - d$, cw, caw, gUw (effacer/changer)
    - . (répéter)
    - guu/GUU (basculer maj/min)
- [ ] **Visual mode**
    - v (sélection)
    - V (sélection ligne)
    - Ctrl+V (sélection colonne)
    - vaw/vip (sélection objet)
- [ ] **Recherche/remplacement natif**
    - `:%s/foo/bar/g` (remplacer global)
    - Visual+`:s/ancien/nouveau/g`
- [ ] **Macros**
    - qa … q (enregistrer macro dans a)
    - @a, 10@a (jouer macro)
    - `:reg` (voir registres)
- [ ] **Registers et historique**
    - "0p, "ap (coller registres)
    - `:reg` (liste des registres)
    - `<C-r>` en insert (coller registre)
- [ ] **Navigation buffers / splits / tabs**
    - `:ls`, `:bnext`, `:bprev`
    - `:split`, `:vsplit`
    - `:tabnew`, `:tabnext`
- [ ] **Commande shell et batch**
    - `:!ls`, `:r !date`
    - `vim -u NONE` (fallback sans config)
    - `:normal` (batch sur sélection)
- [ ] **Pause/reprise**
    - Ctrl+Z (suspendre)
    - fg (reprendre)
- [ ] **Remap ergonomie**
    - Exemple :
      ```vim
      inoremap jj <Esc>
      nnoremap <Space> :
      ```
- [ ] **Fonctions cachées et marks**
    - `:center`, `:reverse`, `:intro`
    - ma, `` `a``, `:marks` (marques)
