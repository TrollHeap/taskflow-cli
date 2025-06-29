.PHONY: taskflow taskfocus taskswitch taskboard
#t
taskflow:
	@python3 cli.py

taskfocus:
	@python3 cli.py --focus

taskswitch:
	@python3 cli.py --switch

taskboard:
	@python3 dashboard.py

