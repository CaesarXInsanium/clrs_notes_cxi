PART1 = notes/Foundations/00intro.md \
		notes/Foundations/01algorithms_role.md \
		notes/Foundations/02getting_started.md \
		notes/Foundations/03function_growth.md \
		notes/Foundations/04divide_conquer.md \
		notes/Foundations/05probabilistic_analysis.md

SRC = $(PART1)
TARGET = clrs_notes.pdf

.PHONY: all
	
all:
	pandoc $(SRC) -o $(TARGET)

lint:
	markdownlint-cli2 $(SRC) -o .lint

clean:
	rm $(TARGET)