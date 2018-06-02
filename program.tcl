open_hw
connect_hw_server -url localhost:3121
current_hw_target [get_hw_targets */xilinx_tcf/Digilent/*]
open_hw_target
set theDevice [lindex [get_hw_devices] 0]
current_hw_device $theDevice
set_property PROGRAM.FILE {./.gen/p2.bit} $theDevice
#set_property PROBES.FILE {} $theDevice
program_hw_devices $theDevice
refresh_hw_device $theDevice

