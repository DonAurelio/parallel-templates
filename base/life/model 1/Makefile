
SHELL=/bin/sh

# FILE
TARGET = life
EXT = .c

# GNU Compiler flags
# COMPILER = gcc
# CFLAGS = -O3
# CFLAGS = -O3 -fopenmp

# PGI Compiler flags
COMPILER = pgc++
# CFLAGS = -O3
CFLAGS = -O3 -mp
# CFLAGS = -O3 -acc -ta=tesla:cc30 -Minfo=accel

# Test parameters
GENERATIONS = 100
GRID_SIZES = 500 1000 1500 2000 2500 3000
ITERATIONS = 1 2 3


compile:
	@$(COMPILER) $(TARGET)$(EXT) -o $(TARGET) -D Generations=10 -D N=20

run: clean compile
	./$(TARGET)

run_test: clean
	@date | tee Time.txt
	@echo "\nRowDim \t ColDim \t Status \t T.Real(sg) \t T.Usuario(sg) \t T.Kernel(sg) \t CPU \t Memoria(KB)" | tee -a Time.txt; \

	@for size in $(GRID_SIZES); do \
		$(COMPILER) $(TARGET)$(EXT) -o $(TARGET) -D Generations=$(GENERATIONS) -D N=$$size $(CFLAGS);\
		for iteration in $(ITERATIONS); do \
			/usr/bin/time -f "%e \t %U \t %S \t %P \t %M" ./$(TARGET)  2>&1 | tee -a Time.txt; \
		done;\
	done 



clean:
	@clear
	rm -f $(TARGET) *.txt *.dat