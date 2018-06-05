#!/usr/bin/env python3

import sys, argparse
from os import path
par_dir = path.dirname( path.dirname( path.abspath(__file__) ) )
sys.path.append( par_dir )

from migen import *
from migen.genlib.fsm import *

from migen.build.generic_platform import *
from migen.build.xilinx import vivado

import platforms

#################################################

class P2(Module):
  def __init__(self,platform):

    self.rx = platform.request("pc_tx")
    self.tx = platform.request("pc_rx")

    inp_sw0 = platform.request("sw0")
    out_led0 = platform.request("led0")
    out_led1 = platform.request("led1")
    out_led2 = platform.request("led2")
    out_led3 = platform.request("led3")
    out_led4 = platform.request("led4")
    out_ledR = platform.request("ledR")
    out_ledG = platform.request("ledG")
    out_ledB = platform.request("ledB")

    reg_counter = Signal(32)

    ###############################
    # MAIN
    ###############################

    reg_uart_counter = Signal(32)
    reg_uart_data = Signal(8)
    reg_uart_bit = Signal(4)
    reg_uart_databit = Signal(3)
    reg_uart_out = Signal()
    clk_uart = Signal()
    sig_uart_counter_zero = Signal()

    self.comb += [
      out_led0.eq(clk_uart),
      out_led1.eq(reg_uart_bit[0]),
      out_led2.eq(reg_uart_bit[1]),
      out_led3.eq(reg_uart_bit[2]),
      out_led4.eq(reg_uart_out),
      out_ledR.eq(reg_counter[24]),
      out_ledG.eq(reg_counter[25]),
      out_ledB.eq(reg_counter[26]),
    ]

    self.sync += [
      reg_counter.eq(reg_counter+1)
    ]

    ###############################
    # UART 
    ###############################

    self.comb += [
      sig_uart_counter_zero.eq(reg_uart_counter==0),
      reg_uart_databit.eq(reg_uart_bit-1),
      self.tx.eq(reg_uart_out)
    ]

    self.sync += [

      If( sig_uart_counter_zero,[
          
          clk_uart.eq(~clk_uart),
          
          reg_uart_counter.eq(333333), # 300 baud @ 100mhz
          If(reg_uart_bit==0,[
            reg_uart_bit.eq(9),
            reg_uart_data.eq(65),
            reg_uart_out.eq(0), # start bit
          ])
          .Else([
            reg_uart_bit.eq(reg_uart_bit-1),
            If(reg_uart_bit==9,
              reg_uart_out.eq(1) # stop bit
            ) 
            .Else([
              reg_uart_out.eq(reg_uart_data[0]), # data bit
              reg_uart_data.eq(Cat(reg_uart_data[1:8],0))
            ])
          ])
      ])
      .Else(
          reg_uart_counter.eq(reg_uart_counter-1)
      )
    ]

    ###############################

#################################################
# build-driver
#################################################

if __name__ == "__main__":
  from migen.fhdl.verilog import convert

  parser = argparse.ArgumentParser()
  parser.add_argument("--build", help="generate .bit file", action="store_true")
  parser.add_argument("--progj", help="program device (jtag)", action="store_true")
  parser.add_argument("--platform", help="platform [nexys4 or cmoda7]", action="store", default="nexys4")

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
  if args.build:
  ############################

    instance = P2(platform=platform)
    platform.build( instance,
                    build_dir=".migen",
                    build_name="p2" )
  ############################
  elif args.progj:
  ############################

    os.system(platform.prog_cmd)

  else:
    parser.print_help()
