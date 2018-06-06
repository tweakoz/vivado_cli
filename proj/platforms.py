from migen import *
from migen.genlib.fsm import *
from migen.build.generic_platform import *
from migen.build.xilinx import vivado
from migen.build.xilinx import XilinxPlatform
from migen.build.generic_platform import GenericPlatform

#################################################

def genio(name,pin,iostd):
 return ( name, 0, Pins(pin), IOStandard(iostd) )

#################################################

class Sim1mhz(XilinxPlatform):
  default_clk_name = "sysclock"
  #default_clk_period = 83.333333 # 12mhz
  default_clk_period = 1000000 # 100khz
  def __init__(self):
    self.clock_period = Sim1mhz.default_clk_period
    self.clock_rate = 1e11/Sim1mhz.default_clk_period
    print("ClockPeriod<%f ns>"%self.clock_period)
    print("ClockRate<%f Mhz>"%(self.clock_rate/1e6))
    self.prog_cmd = "djtgcfg prog --verbose -d CmodA7 -i 0 -f ./.migen/p2.bit"
    XilinxPlatform.__init__(
      self,
      "xc7a35tcpg236-1", 
      [ genio("sysclock","L17","LVCMOS33"), # 100mhz xtal
        genio("sw0","M3","LVCMOS33"), # PIO0
        genio("led0","A17","LVCMOS33"),
        genio("led1","C16","LVCMOS33"),
        genio("ledR","B17","LVCMOS33"),
        genio("ledG","B16","LVCMOS33"),
        genio("ledB","C17","LVCMOS33"),
        genio("pc_tx","J17","LVCMOS33"),
        genio("pc_rx","J18","LVCMOS33"),
        genio("pmod1","G17","LVCMOS33"),
        genio("pmod2","G19","LVCMOS33"),
      ],
      toolchain="vivado" )

#################################################

class CmodA735t(XilinxPlatform):
  default_clk_name = "sysclock"
  #default_clk_period = 83.333333 # 12mhz
  default_clk_period = 8333.3333 # 12mhz
  def __init__(self):
    self.clock_period = CmodA735t.default_clk_period
    self.clock_rate = 1e11/CmodA735t.default_clk_period
    self.prog_cmd = "djtgcfg prog --verbose -d CmodA7 -i 0 -f ./.migen/p2.bit"
    XilinxPlatform.__init__(
      self,
      "xc7a35tcpg236-1", 
      [ genio("sysclock","L17","LVCMOS33"), # 100mhz xtal
        genio("sw0","M3","LVCMOS33"), # PIO0
        genio("led0","A17","LVCMOS33"),
        genio("led1","C16","LVCMOS33"),
        genio("ledR","B17","LVCMOS33"),
        genio("ledG","B16","LVCMOS33"),
        genio("ledB","C17","LVCMOS33"),
        genio("pc_tx","J17","LVCMOS33"),
        genio("pc_rx","J18","LVCMOS33"),
        genio("pmod1","G17","LVCMOS33"),
        genio("pmod2","G19","LVCMOS33"),
      ],
      toolchain="vivado" )

#################################################

class ArtyA735t(XilinxPlatform):
  default_clk_name = "sysclock"
  default_clk_period = 10 # 8mhz
  def __init__(self):
    self.clock_period = ArtyA735t.default_clk_period
    self.clock_rate = 1e11/ArtyA735t.default_clk_period
    self.prog_cmd = "djtgcfg prog --verbose -d Arty -i 0 -f ./.migen/p2.bit"
    XilinxPlatform.__init__(
      self,
      "xc7a35ticsg324-1L", 
      [ genio("sysclock","E3","LVCMOS33"), # 100mhz xtal
        genio("sw0","A8","LVCMOS33"), # SW0
        genio("led0","H5","LVCMOS33"), # LD4
        genio("led1","J5","LVCMOS33"), # LD5
        genio("led2","T9","LVCMOS33"), # LD6
        genio("led3","T10","LVCMOS33"), # LD7
        genio("led4","J4","LVCMOS33"), # LD1g
        genio("ledR","G6","LVCMOS33"), # LD0r
        genio("ledG","F6","LVCMOS33"), # LD0g
        genio("ledB","E1","LVCMOS33"), # LD0b
        genio("pc_tx","A9","LVCMOS33"),
        genio("pc_rx","D10","LVCMOS33"),
        genio("pmod1","G17","LVCMOS33"),
        genio("pmod2","G19","LVCMOS33"),
      ],
      toolchain="vivado" )

#################################################

class Nexys4(XilinxPlatform):
  default_clk_name = "sysclock"
  default_clk_period = 10 # 100mhz
  def __init__(self):
    self.clock_period = Nexys4.default_clk_period
    self.clock_rate = 1e11/Nexys4.default_clk_period
    self.prog_cmd = "djtgcfg prog --verbose -d Nexys4 -i 0 -f ./.migen/p2.bit"
    XilinxPlatform.__init__(
      self,
      "xc7a100t-CSG324-1", 
      [ genio("sysclock","E3","LVCMOS33"), # 100mhz xtal
        genio("sw0","U9","LVCMOS33"), # SW0
        genio("led0","T8","LVCMOS33"),
        genio("led1","V9","LVCMOS33"),
        genio("led2","R8","LVCMOS33"),
        genio("led3","T6","LVCMOS33"),
        genio("led4","T5","LVCMOS33"),
        genio("ledR","K6","LVCMOS33"),
        genio("ledG","H6","LVCMOS33"),
        genio("ledB","L16","LVCMOS33"),
        genio("pc_tx","C4","LVCMOS33"),
        genio("pc_rx","D4","LVCMOS33"),
        genio("pmod1","G17","LVCMOS33"),
        genio("pmod2","G19","LVCMOS33"),
      ],
      toolchain="vivado" )
