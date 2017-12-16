# FILE
TARGET = life
EXT = .c
COMPILER = gcc

# Test parameters
GENERATIONS=20
GRID_SIZE=300

compile:
	@$(COMPILER) $(TARGET)$(EXT) -o $(TARGET) -D Generations=10 -D N=20

run: clean compile
	./$(TARGET)

compile_test:
	@$(COMPILER) $(TARGET)$(EXT) -o $(TARGET) -D Generations=$(GENERATIONS) -D N=$(GRID_SIZE)

run_test: clean compile_test
	@clear
	@date | tee Time.txt
	@echo "\nRowDim \t\t ColDim \t Status \t T.Real(sg) \t T.Usuario(sg) \t T.Kernel(sg) \t CPU \t Memoria(KB)" | tee -a Time.txt
	@/usr/bin/time -f "%e \t\t %U \t\t %S \t\t %P \t %M" ./$(TARGET)  2>&1 | tee -a Time.txt

clean:
	rm -f $(TARGET) *.txt *.dat