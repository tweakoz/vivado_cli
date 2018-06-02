
create_clock -period 50.000 -name sys_clock [get_ports sys_clock]
set_output_delay -clock [get_clocks sys_clock] -min -add_delay 0.000 [get_ports rgb_led_tri_o_0]
set_output_delay -clock [get_clocks sys_clock] -max -add_delay 20.000 [get_ports rgb_led_tri_o_0]
set_output_delay -clock [get_clocks sys_clock] -min -add_delay 0.000 [get_ports rgb_led_tri_o_1]
set_output_delay -clock [get_clocks sys_clock] -max -add_delay 20.000 [get_ports rgb_led_tri_o_1]
set_output_delay -clock [get_clocks sys_clock] -min -add_delay 0.000 [get_ports rgb_led_tri_o_2]
set_output_delay -clock [get_clocks sys_clock] -max -add_delay 20.000 [get_ports rgb_led_tri_o_2]

set_property IOSTANDARD LVCMOS33 [get_ports sys_clock]
set_property IOSTANDARD LVCMOS33 [get_ports phin]
set_property IOSTANDARD LVCMOS33 [get_ports led0]
set_property IOSTANDARD LVCMOS33 [get_ports rgb_led_tri_o_0]
set_property IOSTANDARD LVCMOS33 [get_ports rgb_led_tri_o_1]
set_property IOSTANDARD LVCMOS33 [get_ports rgb_led_tri_o_2]

set_property PACKAGE_PIN L17 [get_ports sys_clock]
set_property PACKAGE_PIN M3 [get_ports phin]
set_property PACKAGE_PIN A17 [get_ports led0]
set_property PACKAGE_PIN B17 [get_ports rgb_led_tri_o_0]
set_property PACKAGE_PIN B16 [get_ports rgb_led_tri_o_1]
set_property PACKAGE_PIN C17 [get_ports rgb_led_tri_o_2]

set_property SLEW FAST [get_ports led0]
set_property SLEW FAST [get_ports rgb_led_tri_o_2]
set_property SLEW FAST [get_ports rgb_led_tri_o_1]
set_property SLEW FAST [get_ports rgb_led_tri_o_0]

