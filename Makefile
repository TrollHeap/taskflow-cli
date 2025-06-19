.PHONY: taskflow taskswitch

taskflow:
	@python3 cli.py

taskswitch:
	@python3 cli.py --switch
