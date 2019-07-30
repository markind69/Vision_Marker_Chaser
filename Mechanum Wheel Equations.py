from math import sin, cos, radians

'''
VX is the Speed Multiplier for Wheel X
Vd is mostly a constant - the max speed you want for this run
T0 is Theta Zero the desired direction of travel, hopefully to be variable
Vo is an offset to help change direction, I think?
0.7854 is Pi/4
'''
V1 = 0
V2 = 0
V3 = 0
V4 = 0
Vd = 5
T0 = 90
Vo = 0
RADS = radians(T0)
# robot_ctrl.set_mode(rm_define.robot_mode_chassis_follow)
# chassis_ctrl.set_trans_speed(0)
V1 = Vd * (sin(RADS + 0.7854) + Vo)
V1a = Vd * sin(T0 + 0.7854) + Vo
V2 = Vd * (cos(RADS + 0.7854) - Vo)
V2a = Vd * cos(T0 + 0.7854) - Vo
V3 = Vd * (cos(RADS + 0.7854) + Vo)
V3a = Vd * cos(T0 + 0.7854) + Vo
V4 = Vd * (sin(RADS + 0.7854) - Vo)
V4a = Vd * sin(T0 + 0.7854) - Vo
# V2 = Vd * cos(T0 + 0.7854) - Vo
# V3 = Vd * cos(T0 + 0.7854) + Vo
# V4 = Vd * sin(T0 + 0.7854) - Vo

# print(V1, V1a, V2, V2a, V3, V3a, V4, V4a)
print(V1, V2, V3, V4)


'''
    circle_1 = 50 * (1 + sin(radians(n * 10)))
    circle_2 = 50 * (1 + cos(radians(n * 10)))


chassis_ctrl.set_wheel_speed(V1, V2, V3, V4)
time.sleep(2)
chassis_ctrl.set_trans_speed(0)
'''