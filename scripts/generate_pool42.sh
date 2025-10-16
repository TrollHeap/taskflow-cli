#!/usr/bin/env bash
# =============================================================================
# Génère les fichiers Markdown de la Piscine C (C00→C13)
# Format compact Taskflow CLI, avec fonctions visibles (`ft_xxx`)
# Auteur : TrollHeap
# =============================================================================

set -euo pipefail

TARGET_DIR="${1:-$HOME/dotfiles/env-files/.config/scripts/tools/taskflow-cli/checklists/piscine-c}"
mkdir -p "$TARGET_DIR"

echo "📁 Dossier cible : $TARGET_DIR"
echo "⚙️  Génération des fichiers .md (avec fonctions formatées)..."

# -----------------------------------------------------------------------------
# 🧱 SEMAINE 1 — C00 → C02
# -----------------------------------------------------------------------------
cat >"$TARGET_DIR/semaine01_c00-c02.md" <<'EOF'
## 1. **Bases du C — affichage, fonctions, chaînes**

* [ ] Jour 1 – C00 ex00→ex04 : `ft_putchar`, `ft_print_alphabet`, `ft_print_reverse_alphabet`, `ft_print_numbers`, `ft_is_negative`
* [ ] Jour 2 – C00 ex05→ex07 : `ft_print_comb`, `ft_print_comb2`, `ft_putnbr`
* [ ] Jour 3 – C01 ex00→ex05 : `ft_ft`, `ft_ultimate_ft`, `ft_swap`, `ft_div_mod`, `ft_ultimate_div_mod`, `ft_putstr`
* [ ] Jour 4 – C01 ex06→ex08 : `ft_strlen`, `ft_rev_int_tab`, `ft_sort_int_tab`
* [ ] Jour 5 – C02 ex00→ex06 : `ft_strcpy`, `ft_strncpy`, `ft_str_is_alpha`, `ft_str_is_numeric`, `ft_str_is_lowercase`, `ft_str_is_uppercase`, `ft_str_is_printable`
EOF

# -----------------------------------------------------------------------------
# 🧱 SEMAINE 2 — C03 → C05
# -----------------------------------------------------------------------------
cat >"$TARGET_DIR/semaine02_c03-c05.md" <<'EOF'
## 2. **Comparaison, conversion et récursivité**

* [ ] Jour 6 – C02 ex07→ex09 + C03 ex00 : `ft_strupcase`, `ft_strlowcase`, `ft_strcapitalize`, `ft_strcmp`
* [ ] Jour 7 – C03 ex01→ex04 : `ft_strncmp`, `ft_strcat`, `ft_strncat`, `ft_strstr`
* [ ] Jour 8 – C04 ex00→ex03 : `ft_strlen`, `ft_putstr`, `ft_putnbr`, `ft_atoi`
* [ ] Jour 9 – C04 ex04→ex05 : `ft_putnbr_base`, `ft_atoi_base`
* [ ] Jour 10 – C05 ex00→ex07 : `ft_iterative_factorial`, `ft_recursive_factorial`, `ft_iterative_power`, `ft_recursive_power`, `ft_fibonacci`, `ft_sqrt`, `ft_is_prime`, `ft_find_next_prime`
EOF

# -----------------------------------------------------------------------------
# 🧱 SEMAINE 3 — C06 → C08
# -----------------------------------------------------------------------------
cat >"$TARGET_DIR/semaine03_c06-c08.md" <<'EOF'
## 3. **Arguments, mémoire dynamique et structures**

* [ ] Jour 11 – C06 ex00→ex03 : `ft_print_program_name`, `ft_print_params`, `ft_rev_params`, `ft_sort_params`
* [ ] Jour 12 – C07 ex00→ex02 : `ft_strdup`, `ft_range`, `ft_ultimate_range`
* [ ] Jour 13 – C07 ex03→ex05 : `ft_str_join`, `ft_split`
* [ ] Jour 14 – C08 ex00→ex02 : création de header `ft.h`, `ft_create_struct`, `ft_show_struct`
* [ ] Jour 15 – C08 ex03→ex05 : `ft_strdup_struct`, `ft_show_tab`, `ft_strs_to_tab`
EOF

# -----------------------------------------------------------------------------
# 🧱 SEMAINE 4 — C09 → C11
# -----------------------------------------------------------------------------
cat >"$TARGET_DIR/semaine04_c09-c11.md" <<'EOF'
## 4. **Mini-libft et logique fonctionnelle**

* [ ] Jour 16 – C09 ex00→ex03 : `ft_putchar`, `ft_swap`, `ft_putstr`, `ft_strlen`
* [ ] Jour 17 – C09 ex04→ex05 : `ft_strcmp`, `ft_sort_params`
* [ ] Jour 18 – C10 ex00→ex03 : open, read, write, `display_file`
* [ ] Jour 19 – C11 ex00→ex03 : `ft_foreach`, `ft_map`, `ft_any`, `ft_count_if`
* [ ] Jour 20 – C11 ex04→ex06 : `ft_is_sort`, `do_op`, exercices avancés
EOF

# -----------------------------------------------------------------------------
# 🧱 SEMAINE 5 — C12 → C13
# -----------------------------------------------------------------------------
cat >"$TARGET_DIR/semaine05_c12-c13.md" <<'EOF'
## 5. **Listes chaînées et projet final**

* [ ] Jour 21 – C12 ex00→ex03 : `ft_list_push_front`, `ft_list_size`, `ft_list_last`, `ft_list_clear`
* [ ] Jour 22 – C12 ex04→ex06 : `ft_list_at`, `ft_list_reverse`, `ft_list_foreach`
* [ ] Jour 23 – C13 ex00→ex02 : `ft_list_merge`, `ft_list_sort`, `ft_list_remove_if`
* [ ] Jour 24 – Projet final piscine : Compilation complète, `Makefile`, `README` structuré
* [ ] Jour 25 – Auto-évaluation & passage NSY103 : Tests finaux (`strace ./a.out`, `valgrind`), auto-notes
EOF

# -----------------------------------------------------------------------------
echo
echo "✅ Fichiers générés :"
ls -1 "$TARGET_DIR"/semaine*.md | sed 's/^/   ├── /'
echo "🎯 Piscine C prête pour Taskflow CLI."
