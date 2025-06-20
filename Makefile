.PHONY: taskflow taskfocus taskswitch taskboard

taskflow:
	@python3 cli.py

taskfocus:
	@python3 cli.py --switch

taskswitch:
	@python3 cli.py --switch

taskboard:
	@python3 dashboard.py

