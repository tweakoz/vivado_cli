#!/usr/bin/env python3
import os, fileinput

os.environ["PATH"]+=":/opt/Xilinx/Vivado/2018.1/bin"

for line in fileinput.input(["cleanbuild.tcl"]):
	print(line)

os.system("vivado -mode batch -source cleanbuild.tcl -nojournal -nolog -tclargs cmoda7")
