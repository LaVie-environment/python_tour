#!/usr/bin/env python3

def sanitize(time_string):
    if '-' in time_string:
        splitter = '-'
    elif ':' in time_string:
        splitter = ':'
    else:
        return(time_string)
    (mins, secs) = time_string.split(splitter)
    return(mins + '.' + secs)

class AthleteList(list):
    def __init__(self, a_name, a_dob=None, a_times=[]):
            list.__init__([])
            self.name = a_name
            self.dob = a_dob
            self.extend(a_times)

    def top3(self):
            return(sorted(set([sanitize(t) for t in self]))[0:3])


def get_coach_data(filename):
    try:
        with open(filename, 'r') as f:
            data = f.readline()
        templ = data.strip().split(',')
        return(AthleteList(templ.pop(0),templ.pop(0), templ))
    except IOError as ioerr:
        print('File error: ' + str(ioerr))
        return(None)

"""
class Athlete:
    def __init__(self, a_name, a_dob=None, a_times=[]):
        self.name = a_name
        self.dob = a_dob
        self.times= a_times

    def top3(self):
        return(sorted(set([sanitize(t) for t in self.times]))[0:3])
"""   

"""
    The add_time and add_times method were removed because the AthleteList inherists from list which has all the methods of list including append (equivalent to add_time) and extend (equivalent to add_times)
"""

    #def add_time(self, time_value):
        #self.times.append(time_value)

    #def add_times(self, list_of_times):
        #self.times.extend(list_of_times)


james = get_coach_data('james2.txt')
print(james.name + "'s fastest times are: " + str(james.top3()))
#print(james['Name'] + "'s fastest times are: " + james['Times'])
sarah = get_coach_data('sarah.txt')
print(sarah.name + "'s fastest times are: " + str(sarah.top3()))
#print(sarah['Name'] + "'s fastest times are: " + sarah['Times'])
julie2 = get_coach_data('julie2.txt')
print(julie2.name + "'s fastest times are: " + str(julie2.top3()))
#print(julie2['Name'] + "'s fastest times are: " + julie2['Times'])
mikey2 = get_coach_data('mikey2.txt')
print(mikey2.name + "'s fastest times are: " + str(mikey2.top3()))
#print(mikey2['Name'] + "'s fastest times are: " + mikey2['Times'])
#sarah_data = {}
#sarah_data['Name'] = sarah.pop(0)
#sarah_data['DOB'] = sarah.pop(0)
#sarah_data['Times'] = sarah
#print(sarah_data['Name'] + "'s fastest times are: " + str(sorted(set([sanitize(t) for t in sarah_data['Times']]))[0:3]))

#(sarah_name, sarah_dob) = sarah.pop(0), sarah.pop(0)
#print(sarah_name + " 's fastest times are: " + str(sorted(set([sanitize(t) for t in sarah])) [0:3]))