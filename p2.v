module trackertest (
    input sys_clock,
    input phin,
    output led0,
    output rgb_led_tri_o_0,
    output rgb_led_tri_o_1,
    output rgb_led_tri_o_2
);

    reg phinr;
    reg [32:0] counter;
    
    assign rgb_led_tri_o_0 = counter[24];
    assign rgb_led_tri_o_1 = counter[25];
    assign rgb_led_tri_o_2 = counter[26];
    assign led0 = phinr;
        
    always @ (posedge sys_clock) begin
        phinr <= phin;
        counter <= counter + 1;
        
    end

endmodule