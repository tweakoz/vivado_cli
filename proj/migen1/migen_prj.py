#!/usr/bin/env python3

import sys, argparse
from migen import *

from migen.build.generic_platform import *
from migen.build.xilinx import XilinxPlatform
from migen.build.generic_platform import GenericPlatform
from migen.build.xilinx import vivado

#################################################

def genio(name,pin,iostd):
 return ( name, 0, Pins(pin), IOStandard(iostd) )

#################################################

class CmodA735t(XilinxPlatform):
  default_clk_name = "sysclock"
  default_clk_period = 83.333333 # 12mhz
  def __init__(self):
    self.prog_cmd = "djtgcfg prog --verbose -d CmodA7 -i 0 -f ./.migen/p2.bit"
    XilinxPlatform.__init__(
      self,
      "xc7a35tcpg236-1", 
      [ genio("sysclock","L17","LVCMOS33"), # 100mhz xtal
        genio("sw0","M3","LVCMOS33"), # PIO0
        genio("led0","A17","LVCMOS33"),
        genio("ledR","B17","LVCMOS33"),
        genio("ledG","B16","LVCMOS33"),
        genio("ledB","C17","LVCMOS33"),
      ],
      toolchain="vivado" )

#################################################

class ArtyA735t(XilinxPlatform):
  default_clk_name = "sysclock"
  default_clk_period = 10 # 8mhz
  def __init__(self):
    self.prog_cmd = "djtgcfg prog --verbose -d Arty -i 0 -f ./.migen/p2.bit"
    XilinxPlatform.__init__(
      self,
      "xc7a35ticsg324-1L", 
      [ genio("sysclock","E3","LVCMOS33"), # 100mhz xtal
        genio("sw0","A8","LVCMOS33"), # SW0
        genio("led0","H5","LVCMOS33"), # LD4
        genio("ledR","G6","LVCMOS33"), # LD0r
        genio("ledG","F6","LVCMOS33"), # LD0g
        genio("ledB","E1","LVCMOS33"), # LD0b
      ],
      toolchain="vivado" )

#################################################

class Nexys4(XilinxPlatform):
  default_clk_name = "sysclock"
  default_clk_period = 10 # 100mhz
  def __init__(self):
    self.prog_cmd = "djtgcfg prog --verbose -d Nexys4 -i 0 -f ./.migen/p2.bit"
    XilinxPlatform.__init__(
      self,
      "xc7a100t-CSG324-1", 
      [ genio("sysclock","E3","LVCMOS33"), # 100mhz xtal
        genio("sw0","U9","LVCMOS33"), # SW0
        genio("led0","T8","LVCMOS33"),
        genio("ledR","K6","LVCMOS33"),
        genio("ledG","H6","LVCMOS33"),
        genio("ledB","L16","LVCMOS33"),
      ],
      toolchain="vivado" )

#################################################

class P2(Module):
  def __init__(self,platform):
    self.inp_sw0 = platform.request("sw0")
    self.out_led0 = platform.request("led0")
    self.out_ledR = platform.request("ledR")
    self.out_ledG = platform.request("ledG")
    self.out_ledB = platform.request("ledB")

    self.reg_sw0 = Signal()
    self.reg_counter = Signal(32)

    self.sync += [
      self.reg_sw0.eq(self.inp_sw0),
      self.reg_counter.eq(self.reg_counter+1)
    ]

    self.comb += [
      self.out_led0.eq(self.reg_sw0),
      self.out_ledR.eq(self.reg_counter[24]),
      self.out_ledG.eq(self.reg_counter[25]),
      self.out_ledB.eq(self.reg_counter[26])
    ]

#################################################

if __name__ == "__main__":
  from migen.fhdl.verilog import convert

  parser = argparse.ArgumentParser()
  parser.add_argument("--build", help="generate .bit file", action="store_true")
  parser.add_argument("--progj", help="program device (jtag)", action="store_true")
  parser.add_argument("--platform", help="platform [nexys4,cmoda7,artya7]", action="store", default="nexys4")

  args = parser.parse_args()

  ############################
  # determine platform
  ############################

  if args.platform == "nexys4":
      platform = Nexys4()
  elif args.platform == "artya7":
      platform = ArtyA735t()
  elif args.platform == "cmoda7":
      platform = CmodA735t()

  ############################
  if args.build: # build ?
  ############################

    instance = P2(platform=platform)
    platform.build( instance,
                    build_dir=".migen",
                    build_name="p2" )

  ############################
  elif args.progj: # program ?
  ############################

    os.system(platform.prog_cmd)

  ############################
  else: # help ?
  ############################

    parser.print_help()

  #convert(instance).write("p2.v")
