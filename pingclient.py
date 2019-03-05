from socket import *
import time

with socket(AF_INET, SOCK_DGRAM) as client_socket:

    for i in range(1, 11):
        data = 'ping ' + str(i) + ' ' + time.asctime()

        try:
            print('send:\n{0}'.format(data))
            RTT_send = time.time()
            client_socket.sendto(data.encode(), ('10.0.0.2', 1234))
            client_socket.settimeout(1)

            print('receive:')
            return_msg = client_socket.recv(1024)
            RTT_receive = time.time()

            time_difference = RTT_receive - RTT_send

            if i is 10:
                print(return_msg.decode())
                print('RTT: {0} {1}'.format(format(time_difference, '.5f'), 'seconds'))
            else:
                print(return_msg.decode())
                print('RTT: {0} {1}\n'.format(format(time_difference, '.5f'), 'seconds'))

        except timeout:
            if i is 10:
                print('Request timed out')
            else:
                print('Request timed out\n')