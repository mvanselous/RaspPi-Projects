from sense_hat import SenseHat
import time

sense = SenseHat()

event = sense.stick.wait_for_event()
#the line above does not complete until there is a joystick input.
#But it will run if there are any stored inputs

print("The joystick was {} {}".format(event.action, event.direction))
time.sleep(2)
event = sense.stick.wait_for_event(emptybuffer=True)
#Emptybuffer will clear any inputs before the command is called.

print("The joystick was {} {}".format(event.action, event.direction))
time.sleep(3)

event_list = sense.stick.get_events()
print(event_list)



