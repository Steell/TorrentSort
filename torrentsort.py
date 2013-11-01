import win32service
import win32serviceutil
import win32event

import bencode
import glob
import os

from torrentparse.torrentparser import TorrentParser
from subprocess import call

class TorrentSortService(win32serviceutil.ServiceFramework):
  # name for NET START/STOP
  _svc_name_ = "TorrentSort"

  # Service Name
  _svc_disp_name_ = "Torrent Sort"

  # Service Description
  _svc_desc_ = "Automatically loads and sorts torrents from watched folders."

  def __init__(self, args):
    win32serviceutil.ServiceFramework.__init__(self, args)

    # Listen for stop requests
    self.wait_stop = win32event.CreateEvent(None, 0, 0, None)

  # Core service logic
  def SvcDoRun(self):
    import servicemanager

    rc = None

    while rc != win32event.WAIT_OBJECT_0:
      self.run()
      rc = win32event.WaitForSingleObject(self.wait_stop, 20000)

  # Closing
  def SvcStop(self):
    self.ReportServiceStatus(win32service.SERVICE_STOP_PENDING)
    win32event.SetEvent(self.wait_stop)

  # Custom logic to run
  def run(self):
    with open('rules') as rules_file:
      

    with open('dirs') as dir_file:
      dirs = [d for d in dir_file]

    for d in dirs:
      for torrent in glob.glob(os.path.join(d, "*.torrent")):
        tp = TorrentParser(torrent)

if __name__ == '__main__':  
    win32serviceutil.HandleCommandLine(PySvc)  