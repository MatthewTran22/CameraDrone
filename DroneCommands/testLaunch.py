from djitellopy import tello

camdroid = tello.Tello()

camdroid.connect()
camdroid.takeoff()
camdroid.move_left(20)
camdroid.move_right(30)
print(camdroid.get_battery())

camdroid.land()