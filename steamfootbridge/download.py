# SteamFootBridge
# Copyright (c) 2016 Bryan DeGrendel

import subprocess

from . import config

def do(appid):
  print "Downloading {}".format(appid)
  # NOTE: It appears that generated shortcuts are little more than
  #       C:\\Windows\command\start.exe steam://rungameid/<appid>
  #       Which I'm 90% sure is simply redirecting to Steam.exe steam://rungameid/<appid>
  #       - possibly with quotation marks.  If so, we probably don't need anything beyond this.
  # TODO: In the future, SteamFootBridge will cache the list of possible applications and their
  #       states.  Starting a download like this should trigger a refresh.
  subprocess.Popen(["wine", config.__wine_steam_path__, "-silent", "steam://install/{}".format(appid)])
