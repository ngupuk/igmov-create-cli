from igmov.template import ig
from igmov.dl import getFile
import os
import os.path
import instapy_cli

title = "Test Video"
bgKeyword = "nature"
igCaption = """
Video ini di upload dari github.
"""
pathVideo = "results/sample.mp4"

# download audio file
getFile(
  "https://mwafa.github.io/images/sample.ogg",
  "sample.ogg"
)

base = (ig.template1()
        .useRandomBg(bgKeyword)
        .showSpotify()
        .setTitle(title)
        .useInstagramLogo()
        .useNgupukLogo())

if(not os.path.isdir('results')):
  os.makedirs('results')

base.makeVideo("sample.ogg", pathVideo)

# upload to ig
username = 'ngupuk.id'
password = os.environ['IG_PASSWORD']

with instapy_cli.client(username, password) as cli:
  cli.upload(pathVideo, igCaption)