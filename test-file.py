print("%+10s %+10s %+10s" % ('papam1', 'papam2', 'papam3'))
print('{}'.format(['el_1', 'el_2', 'el_3', 'el_4']))
print("{:<20} {:<20} {:<20}". format('my_param_1', 'my_param_2', 'my_param_3'))
print("{:.3f}".format(5.0/3))
print('The third element: {2}; The second element: {1}; The first element: {0}'.format('el_1', 'el_2', 'el_3'))

ip = '192.168.1.4'
mask = 10

print(f'ip-params: {ip}, mask: {mask}')

octets = ['10', '1', '1', '1']
print(f"ip-params: {'.'.join(octets)}, mask:(mask)")

oct1, oct2, oct3, oct4 = [10, 1, 1, 1]
print(f'''IP-adress: {oct1:<8} {oct2:<8} {oct3:<8} {oct4:<8}''')


