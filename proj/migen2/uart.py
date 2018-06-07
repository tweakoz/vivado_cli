from migen import *
from migen.genlib.fsm import *

#################################################

class TX(Module):
  def __init__(self,top,baudrate=300):

    self.inp_data = Signal(8)
    self.inp_wr = Signal()

    self.clock_domains.clk_uart = ClockDomain("clk_uart")
    self.clock_domains.clk_char = ClockDomain("clk_char")

    self.baud = baudrate
    self.baudticks = int(0.5*top.platform.clock_rate/self.baud)
    print( "Baud<%d>"%self.baud)
    print( "BaudTicks<%d>"%self.baudticks)

    rx = top.platform.request("pc_tx")
    tx = top.platform.request("pc_rx")

    inp_sw0 = top.platform.request("sw0")
    out_led0 = top.platform.request("led0")
    out_led1 = top.platform.request("led1")
    out_pmod0 = top.platform.request("pmodA0")
    out_pmod1 = top.platform.request("pmodA1")
    out_gpio0 = top.platform.request("gpio0")
    out_gpio1 = top.platform.request("gpio1")
    out_gpio2 = top.platform.request("gpio2")
    inp_gpio3 = top.platform.request("gpio3")
    out_gpio4 = top.platform.request("gpio4")

    ###############################
    # MAIN
    ###############################

    clk_uart = self.clk_uart
    clk_char = self.clk_char

    reg_uart_counter = Signal(32)
    reg_uart_data = Signal(8)
    reg_uart_bit = Signal(4)
    reg_uart_databit = Signal(4)
    reg_uart_out = Signal()
    sig_uart_counter_zero = Signal()

    self.comb += [
      out_led0.eq(clk_uart.clk),
      out_led1.eq(reg_uart_bit[0]),
    ]

    self.sync.clk_uart += [
      out_gpio2.eq(inp_gpio3),
    ]

    ###############################
    # UART 
    ###############################

    self.comb += [
      sig_uart_counter_zero.eq(reg_uart_counter==0),
      reg_uart_databit.eq(reg_uart_bit),
      tx.eq(reg_uart_out),
      out_pmod0.eq(clk_uart.clk),
      out_pmod1.eq(reg_uart_out),
      out_gpio0.eq(clk_uart.clk),
      out_gpio1.eq(reg_uart_out),
      out_gpio4.eq(clk_char.clk)
    ]

    top.sync.clk_sys += [

      clk_char.clk.eq(reg_uart_bit<5),

      If( sig_uart_counter_zero,[

          clk_uart.clk.eq(~clk_uart.clk),
          reg_uart_counter.eq(self.baudticks), # baudrate counter

          If(clk_uart.clk,[

              If(reg_uart_bit==9,[

                  reg_uart_bit.eq(0),
                  reg_uart_out.eq(0), # start bit
                  reg_uart_data.eq(self.inp_data), # latch character data
              ])
              .Else([
              
                  If(reg_uart_bit==8,
                      reg_uart_out.eq(1), # stop bit
	                  self.inp_wr.eq(0),
                  ) 
                  .Else([
                      reg_uart_out.eq(reg_uart_data[0]), # data bit
                      reg_uart_data.eq(Cat(reg_uart_data[1:8],0))
                  ]),

                  reg_uart_bit.eq(reg_uart_bit+1),

              ])
          ])

      ])
      .Else(
          reg_uart_counter.eq(reg_uart_counter-1)
      ),

    ]


    ###############################
#
