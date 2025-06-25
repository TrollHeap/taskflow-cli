## Vim / Neovim – Checklist pratique

* [ ] Navigation sans plugin : HJKL (déplacement)
* [ ] Navigation mots : w/W, b/B, e/E
* [ ] Navigation ligne : 0, ^, $
* [ ] Navigation fichier : gg, G
* [ ] Aller à une ligne : `:42<CR>`
* [ ] Recherche : /motif, n/N, *, #
* [ ] Text-objects : ciw (change inner word)
* [ ] Text-objects : da" (delete around quote)
* [ ] Text-objects : di( (delete inside parentheses)
* [ ] Text-objects : vi{, va', vip (sélections)
* [ ] Opérateurs : d$, cw, caw, gUw
* [ ] Répétition : `.`
* [ ] Majuscules/minuscules : guu / GUU
* [ ] Visual mode : v (caractère)
* [ ] Visual mode : V (ligne)
* [ ] Visual mode : Ctrl+V (colonne)
* [ ] Visual + text-object : vaw, vip
* [ ] Remplacement global : `:%s/foo/bar/g`
* [ ] Remplacement en visual : `:s/ancien/nouveau/g`
* [ ] Macros : qa…q (enregistrement), @a, 10@a (exécution)
* [ ] Voir les registres : `:reg`
* [ ] Coller depuis registre : "0p, "ap
* [ ] Coller en insert : <C-r>
* [ ] Navigation buffers : `:ls`, `:bnext`, `:bprev`
* [ ] Splits horizontaux / verticaux : `:split`, `:vsplit`
* [ ] Tabs : `:tabnew`, `:tabnext`
* [ ] Commandes shell : `:!ls`, `:r !date`
* [ ] Mode sans config : `vim -u NONE`
* [ ] Exécution normal-mode en batch : `:normal`
* [ ] Suspendre Vim : Ctrl+Z
* [ ] Reprendre Vim : `fg`
* [ ] Remapping : `inoremap jj <Esc>`, `nnoremap <Space> :`
* [ ] Commandes méconnues : `:center`, `:reverse`, `:intro`
* [ ] Marques : `ma`, `` `a` ``, `:marks`
