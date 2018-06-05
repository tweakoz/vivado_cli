#!/usr/bin/env python3

import sys, argparse
from os import path
par_dir = path.dirname( path.dirname( path.abspath(__file__) ) )
sys.path.append( par_dir )

from migen import *

from migen.build.generic_platform import *
from migen.build.xilinx import vivado

import platforms

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
      platform = platforms.Nexys4()
  elif args.platform == "artya7":
      platform = platforms.ArtyA735t()
  elif args.platform == "cmoda7":
      platform = platforms.CmodA735t()

  assert( platform!=None )

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
