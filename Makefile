# ===========================================================
# Taskflow CLI - Makefile (avec UV)
# ===========================================================

UV := uv
VENV := .venv
PYFILES := cli.py dashboard.py
REQUIREMENTS := rich toml

# =============================================
# 🧱 Cibles principales
# =============================================

.PHONY: all setup install run clean reset taskflow taskfocus taskswitch taskboard

# 🔹 Installation complète
all: setup install

# 🔹 Crée un environnement virtuel avec uv s’il n’existe pas
setup:
	@if [ ! -d "$(VENV)" ]; then \
		echo "📦 Création du venv avec uv..."; \
		$(UV) venv $(VENV); \
	else \
		echo "✅ Venv déjà présent."; \
	fi

# 🔹 Installe les dépendances dans le venv
install:
	@echo "📚 Installation des dépendances Python..."
	@$(UV) pip install $(REQUIREMENTS)

# 🔹 Nettoie le venv
clean:
	@echo "🧹 Suppression du venv..."
	@rm -rf $(VENV)

# 🔹 Réinitialise tout
reset: clean all

# =============================================
# 🚀 Commandes Taskflow (via UV)
# =============================================

# UV active automatiquement le venv et exécute la commande dans ce contexte

taskflow:
	@$(UV) run python cli.py

taskfocus:
	@$(UV) run python cli.py --focus

taskswitch:
	@$(UV) run python cli.py --switch

taskboard:
	@$(UV) run python dashboard.py
