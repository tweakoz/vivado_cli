puts "what up yo"
set outputDir ./.gen/p2_project
file mkdir $outputDir
read_verilog [ glob ./src/*.v ]
read_xdc ./src/p2.xdc
synth_design -top trackertest -part xc7a35tcpg236-1
write_checkpoint -force $outputDir/post_synth.dcp
