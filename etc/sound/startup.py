import vlc
import time

#Defince startup sound
startup = vlc.Media("/etc/sound/startup.mp3")

#Define volume
volume = 45

#Create startupsoundplayer
media_player = vlc.MediaPlayer()

#Set sound file
media_player.set_media(startup)

#Set volume
media_player.audio_set_volume(volume)

#Play startup sound
media_player.play()
time.sleep(4)
print("End")
media_player.stop()