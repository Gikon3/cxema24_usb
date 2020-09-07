from com_port import ComPort
from parser_data import *

MODE = "GPS"
COM_PORT = "COM17"

param_gps = {
    "mode": "GPS",
    "min_freq": 4070000,
    "max_freq": 4090000,
    "step_freq": 50
}

param_glo = {
    "mode": "GLO",
    "min_freq": 717941,
    "max_freq": 737941,
    "step_freq": 50
}

ser_port = ComPort(COM_PORT)
ser_port.flush_input_buffer()

param_dict = param_gps if MODE == 'GPS' else param_glo
for value in param_dict.values():
    ser_port.write(str(value) + "\n")

data_frame = ser_port.read()
prs_data = ParserData()
msg = []
while data_frame != "":
    try:
        print(data_frame)
        msg.append(data_frame)
        data_frame = ser_port.read()
    except KeyboardInterrupt:
        break

prs_data.parse_msg(msg, param_dict['mode'])
prs_data.paint_window(param_dict['mode'])

# import random
#
#
# def rand_str(g2, numb_pare):
#     str_msg = []
#     for j in range(9):
#         str_msg_frame = f"g:{g2}."
#         for i in range(numb_pare):
#             x0 = random.randint(4000000, 5000000)
#             x1 = random.randint(10, 900)
#             str_msg_frame += f"{x0}:{x1}."
#         str_msg.append(str_msg_frame[:-1])
#     return str_msg
#
#
# if MODE == 'GPS':
#     msg_stack_gps = [rand_str(g2, 1) for g2 in range(37)]
#     prs_data = ParserData()
#     for msg in msg_stack_gps:
#         prs_data.parse_msg(msg, MODE)
#     prs_data.paint_window(MODE)
# elif MODE == 'GLO':
#     msg_stack_glo = [rand_str(g2, 2) for g2 in range(-7, 7, 1)]
#     prs_data = ParserData()
#     for msg in msg_stack_glo:
#         prs_data.parse_msg(msg, MODE)
#     prs_data.paint_window(MODE)
