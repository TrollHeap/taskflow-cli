.PHONY: checklist log stats reset

checklist:
	@python3 cli.py

log:
	@python3 cli.py --log

stats:
	@python3 cli.py --stats

reset:
	@python3 cli.py --reset
