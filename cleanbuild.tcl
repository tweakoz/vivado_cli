puts "what up yo"
set outputDir ./.gen
file mkdir $outputDir
read_verilog [ glob ./src/*.v ]
read_xdc ./src/p2.xdc
synth_design -top trackertest -part xc7a35tcpg236-1
write_checkpoint -force $outputDir/post_synth.dcp
report_timing_summary -file $outputDir/post_syn_timing_summary.txt
report_utilization -file $outputDir/post_syn_utilization_summary.txt
#opt_design
place_design
route_design
write_verilog -force $outputDir/impl_netlist.v
write_bitstream -force $outputDir/p2.bit

