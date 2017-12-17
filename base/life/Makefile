
SHELL=/bin/sh

# FILE
TARGET = life
EXT = .c
COMPILER = gcc

# Test parameters
GENERATIONS=20
# GRID_SIZES = 250 500 750 1000 1250 1500
GRID_SIZES = 20 40
ITERATIONS = 1 2 3


compile:
	@$(COMPILER) $(TARGET)$(EXT) -o $(TARGET) -D Generations=10 -D N=20

run: clean compile
	./$(TARGET)

run_test: clean
	@date | tee Time.txt
	@echo "\nRowDim \t\t ColDim \t Status \t T.Real(sg) \t T.Usuario(sg) \t T.Kernel(sg) \t CPU \t Memoria(KB)" | tee -a Time.txt; \

	@for size in $(GRID_SIZES); do \
		$(COMPILER) $(TARGET)$(EXT) -o $(TARGET) -D Generations=$(GENERATIONS) -D N=$$size; \
		/usr/bin/time -f "%e \t\t %U \t\t %S \t\t %P \t %M" ./$(TARGET)  2>&1 | tee -a Time.txt; \
	done 



clean:
	@clear
	rm -f $(TARGET) *.txt *.dat