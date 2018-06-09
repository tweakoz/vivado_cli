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
  default_clk_mhz = .01
  default_clk_period = 10000 # 100khz
  def __init__(self):
    self.clock_period = Sim1mhz.default_clk_period
    self.clock_rate = 0.01e6
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
        genio("pmodA0","G17","LVCMOS33"),
        genio("pmodA1","G19","LVCMOS33"),
        genio("pmodA2","N18","LVCMOS33"),
        genio("pmodA3","L18","LVCMOS33"),
        genio("pmodA4","H17","LVCMOS33"),
        genio("pmodA5","H19","LVCMOS33"),
        genio("pmodA6","J19","LVCMOS33"),
        genio("pmodA7","K18","LVCMOS33"),
        genio("gpio0","M3","LVCMOS33"),   # PIO1
        genio("gpio1","L3","LVCMOS33"),   # PIO2
        genio("gpio2","A16","LVCMOS33"),  # PIO3
        genio("gpio3","K3","LVCMOS33"),   # PIO4
        genio("gpio4","C15","LVCMOS33"),  # PIO5
        genio("gpio5","L3","LVCMOS33"),   # PIO6
        genio("gpio6","H1","LVCMOS33"),   # PIO7
        genio("gpio7","B15","LVCMOS33"),  # PIO8
      ],
      toolchain="vivado" )

#################################################

class CmodA735t(XilinxPlatform):
  default_clk_name = "sysclock"
  default_clk_period = 83.333333 # 12mhz
  def __init__(self):
    self.clock_period = CmodA735t.default_clk_period
    self.clock_rate = 12e6
    self.prog_cmd = "djtgcfg prog --verbose -d CmodA7 -i 0 -f ./.migen/p2.bit"
    XilinxPlatform.__init__(
      self,
      "xc7a35tcpg236-1", 
      [ genio("sysclock","L17","LVCMOS33"), # 100mhz xtal
        genio("sw0","V8","LVCMOS33"),     # PIO48
        genio("led0","A17","LVCMOS33"),
        genio("led1","C16","LVCMOS33"),
        genio("ledR","B17","LVCMOS33"),
        genio("ledG","B16","LVCMOS33"),
        genio("ledB","C17","LVCMOS33"),
        genio("pc_tx","J17","LVCMOS33"),  # uart <- usb
        genio("pc_rx","J18","LVCMOS33"),  # uart -> usb
        genio("pmodA0","G17","LVCMOS33"), # pmod pin1
        genio("pmodA1","G19","LVCMOS33"), # pmod pin2
        genio("pmodA2","N18","LVCMOS33"), # pmod pin3
        genio("pmodA3","L18","LVCMOS33"), # pmod pin4
        genio("pmodA4","H17","LVCMOS33"), # pmod pin7
        genio("pmodA5","H19","LVCMOS33"), # pmod pin8
        genio("pmodA6","J19","LVCMOS33"), # pmod pin9
        genio("pmodA7","K18","LVCMOS33"), # pmod pin10
        genio("gpio0","M3","LVCMOS33"),   # PIO1
        genio("gpio1","L3","LVCMOS33"),   # PIO2
        genio("gpio2","A16","LVCMOS33"),  # PIO3
        genio("gpio3","K3","LVCMOS33"),   # PIO4
        genio("gpio4","C15","LVCMOS33"),  # PIO5
        genio("gpio5","L3","LVCMOS33"),   # PIO6
        genio("gpio6","H1","LVCMOS33"),   # PIO7
        genio("gpio7","B15","LVCMOS33"),  # PIO8
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
        genio("gpioX","XX","LVCMOS33"), # PIO1
        genio("gpioY","XX","LVCMOS33"), # PIO2
      ],
      toolchain="vivado" )

#################################################

class Nexys4(XilinxPlatform):
  default_clk_name = "sysclock"
  default_clk_period = 10 # 100mhz
  def __init__(self):
    self.clock_period = Nexys4.default_clk_period
    self.clock_rate = 100e6
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
        genio("pmodA0","B13","LVCMOS33"), # PMOD JA1
        genio("pmodA1","F14","LVCMOS33"), # PMOD JA2
        genio("pmodA2","D17","LVCMOS33"), # PMOD JA3
        genio("pmodA3","E17","LVCMOS33"), # PMOD JA4
        genio("pmodA4","G13","LVCMOS33"), # PMOD JA7
        genio("pmodA5","C17","LVCMOS33"), # PMOD JA8
        genio("pmodA6","D18","LVCMOS33"), # PMOD JA9
        genio("pmodA7","E18","LVCMOS33"), # PMOD JA10
        genio("gpio0","G14","LVCMOS33"),  # PMOD JB1
        genio("gpio1","P15","LVCMOS33"),  # PMOD JB2
        genio("gpio2","V11","LVCMOS33"),  # PMOD JB3
        genio("gpio3","V15","LVCMOS33"),  # PMOD JB4
        genio("gpio4","K16","LVCMOS33"),  # PMOD JB7
        genio("gpio5","R16","LVCMOS33"),  # PMOD JB8
        genio("gpio6","T9","LVCMOS33"),   # PMOD JB9
        genio("gpio7","U11","LVCMOS33"),  # PMOD JB10
      ],
      toolchain="vivado" )
