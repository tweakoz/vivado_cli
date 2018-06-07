#!/usr/bin/env python3

import sys, argparse
from os import path
par_dir = path.dirname( path.dirname( path.abspath(__file__) ) )
sys.path.append( par_dir )

from migen import *
from migen.genlib.fsm import *
#from migen.fhdl.std import *
#from migen.sim.generic import run_simulation, Simulator, TopLevel
#from migen.sim.icarus import Runner

from migen.build.generic_platform import *
from migen.build.xilinx import vivado

import platforms
import uart

#################################################

class LEDS(Module):
  def __init__(self,top):

    out_ledR = top.platform.request("ledR")
    out_ledG = top.platform.request("ledG")
    out_ledB = top.platform.request("ledB")

    reg_counter = Signal(32)

    ###############################
    # MAIN
    ###############################

    self.comb += [
      out_ledR.eq(reg_counter[24]),
      out_ledG.eq(reg_counter[25]),
      out_ledB.eq(reg_counter[26]),
    ]

    top.sync.clk_sys += [
      reg_counter.eq(reg_counter+1)
    ]

    ###############################

#################################################

class TOP(Module):
  def __init__(self,platform,sysclock):
    self.sysclock = sysclock
    self.platform = platform
    self.clock_domains.clk_sys = ClockDomain("clk_sys")

    tx = self.submodules.tx = uart.TX(self,baudrate=300)
    leds = self.submodules.leds = LEDS(self)

    character = Signal(5)

    ###############################
    # character stream
    ###############################

    mystr = "WhatUpYo... "

    self.specials.mrom = Memory(8, len(mystr), init=[ord(s) for s in list(mystr)])

    rom_port1 = self.mrom.get_port(has_re=False,
                                   async_read=True,
                                   clock_domain="clk_sys")

    self.specials += [rom_port1]

    self.comb += [
      self.clk_sys.clk.eq(self.sysclock),
      rom_port1.adr.eq(character),
      tx.inp_data.eq(rom_port1.dat_r),
    ]

    self.sync.clk_sys += [

        If(tx.inp_wr==0,[
          If( character==len(mystr)-1, [
            character.eq(0)
          ])
          .Else([
            character.eq(character+1)
          ]),
          tx.inp_wr.eq(1)
        ])
    ]

#################################################
# driver
#################################################

if __name__ == "__main__":
  from migen.fhdl.verilog import convert

  parser = argparse.ArgumentParser()
  parser.add_argument("--sim", help="simulate", action="store_true")
  parser.add_argument("--build", help="generate .bit file", action="store_true")
  parser.add_argument("--progj", help="program device (jtag)", action="store_true")
  parser.add_argument("--platform", help="platform [nexys4 or cmoda7]", action="store", default="nexys4")

  args = parser.parse_args()

  ############################
  if args.sim: # Simulation ?
  ############################

    convert(TOP(platforms.Sim1mhz(),Signal())).write(".migen/p2.v")
    dut = TOP(platforms.Sim1mhz(),Signal())

    def testbench():
        print("wtf...")
        yield 

    #dut.clock_domains.cd_sys = ClockDomain("clk_sys")

    mysim = Simulator(dut,
                      testbench(),
                      clocks={
                        "clk_sys": 100000,
                        "sys":10
                      },
                      vcd_name="p2.vcd",
                      special_overrides={})

    mysim.run()

    os.system("gtkwave -a p2.gtkw p2.vcd")
    pass

  ############################
  else: # Build, Program or Help ?
  ############################

    # determine platform

    if args.platform == "nexys4":
        platform = platforms.Nexys4()
    elif args.platform == "artya7":
        platform = platforms.ArtyA735t()
    elif args.platform == "cmoda7":
        platform = platforms.CmodA735t()

    assert( platform!=None )
    
    ###########

    if args.build:
      sysclock = platform.request("sysclock")
      instance = TOP(platform,sysclock)
      platform.build( instance,
                      build_dir=".migen",
                      build_name="p2" )
    elif args.progj:
      os.system(platform.prog_cmd)
    else:
      parser.print_help()
