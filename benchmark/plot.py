#!/usr/bin/python3

import matplotlib.pyplot as plt
import numpy

INPUT_DATA_CSV = 'benchmark.2017.05.12.11.46'

in_data = numpy.genfromtxt(
    INPUT_DATA_CSV, delimiter=',', names=[
        'playbooks', 'dockerreal', 'dockeruser', 'dockersys',
        'nodockerreal', 'nodockeruser', 'nodockersys'])


def create_plot(x_data, line1_label, line2_label, filename):
    x_minor_ticks = [int(x) for x in x_data[1:]]
    x_major_ticks = [int(x) for x in x_data[1::5]]
    plt.xticks(x_major_ticks)
    plt.ylabel(line1_label)
    plt.xlabel(line2_label)
    plt.legend(framealpha=0.1)
    plt.box(on=False)
    plt.grid(which='minor', alpha=0.1)
    plt.grid(which='major', alpha=0.2)
    plt.minorticks_on()
    plt.savefig(filename)
    plt.close()


plt.plot(in_data['playbooks'], in_data['dockerreal'],
         label='Real Time with Docker', linewidth=3.0)
plt.plot(in_data['playbooks'], in_data['nodockerreal'],
         label='Real Time without Docker', linewidth=3.0)

create_plot(in_data['playbooks'],
            'Real-Time in seconds',
            'Number of checked playbooks', "real-time-comp.png")

####################################################################

plt.plot(in_data['playbooks'], in_data['dockeruser'],
         label='User Time with Docker', linewidth=3.0)
plt.plot(in_data['playbooks'], in_data['nodockeruser'],
         label='User Time without Docker', linewidth=3.0)

create_plot(in_data['playbooks'],
            'User-Time in seconds',
            'Number of checked playbooks', "user-time-comp.png")

####################################################################

plt.plot(in_data['playbooks'], in_data['dockersys'],
         label='Sys Time with Docker', linewidth=3.0)
plt.plot(in_data['playbooks'], in_data['nodockersys'],
         label='Sys Time without Docker', linewidth=3.0)

create_plot(in_data['playbooks'],
            'Sys-Time in seconds',
            'Number of checked playbooks', "sys-time-comp.png")
