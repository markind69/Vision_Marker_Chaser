pid_Yaw = rm_ctrl.PIDCtrl()
pid_Pitch = rm_ctrl.PIDCtrl()
list_Marker = RmList()
variable_X = 0
variable_Y = 0
def start():
    global variable_X
    global variable_Y
    global list_Marker
    global pid_Yaw
    global pid_Pitch
    gimbal_ctrl.set_rotate_speed(500)
    vision_ctrl.enable_detection(rm_define.vision_detection_marker)
    robot_ctrl.set_mode(rm_define.robot_mode_chassis_follow)
    pid_Yaw.set_ctrl_params(115,0,5)
    pid_Pitch.set_ctrl_params(85,0,3)
    while True:
        list_Marker=RmList(vision_ctrl.get_marker_detection_info())
        if list_Marker[1] == 1:
            variable_X = list_Marker[3]
            variable_Y = list_Marker[4]
            pid_Yaw.set_error(variable_X - 0.5)
            pid_Pitch.set_error(0.5 - variable_Y)
            gimbal_ctrl.rotate_with_speed(pid_Yaw.get_output(),pid_Pitch.get_output())
            chassis_ctrl.set_trans_speed(0.2)
            chassis_ctrl.set_follow_gimbal_offset(0)
            chassis_ctrl.move(0)
            time.sleep(0.05)
        else:
            chassis_ctrl.stop()
