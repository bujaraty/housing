#!/usr/bin/python


import re, time, subprocess, pygame, datetime, sys


LOCATION_WGET_SCRIPT    = '/home/jessada/development/personal/20111227_sssb/sssb.sh'
LOCATION_APARTMENT_PAGE = '/home/jessada/development/personal/20111227_sssb/apartment.html' 

PARSE_LAST_MINUTE_ROOM  = 'LastMinuteRoom'

def last_minute_room(apartment_page):
    parser_sssb = re.compile(r".*(of which.*(?P<" + PARSE_LAST_MINUTE_ROOM + ">[0-9]+).*last-minute apartments\.)", re.DOTALL)
    match_result = parser_sssb.match(open(apartment_page).read())
    if match_result:
        return int(match_result.group(PARSE_LAST_MINUTE_ROOM))
    else:
        return 0

f1=open('./sssb.log', 'w+')
f1.close()
count = 0    
while (1):
    f1=open('./sssb.log', 'a')
    f1.write("************** check last minute round % 4d at %s ****************\n" % (count, str(datetime.datetime.now())))
    f1.close()
    print '************** check last minute round', count, ' at', str(datetime.datetime.now()), '****************'
    subprocess.call(LOCATION_WGET_SCRIPT)
    
    room = last_minute_room(LOCATION_APARTMENT_PAGE)
    f1=open('./sssb.log', 'a')
    f1.write("%d\n" % (room))
    f1.close()
    print room
    if room > 0:
        pygame.init()
        pygame.mixer.music.load('/home/jessada/development/personal/20111227_sssb/iq.mp3')
        
        pygame.mixer.music.play()
        pygame.event.wait()        
        
    
    time.sleep(1)
    
    count += 1 
