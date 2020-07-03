from igmov.template import ig
from igmov.dl import getFile
import os
import os.path

title = "Test Video"
bgKeyword = "nature"

# download audio file
getFile(
  "https://mwafa.github.io/images/sample.ogg",
  "sample.ogg"
)

base = (ig.template1()
        .useRandomBg()
        .showSpotify()
        .useInstagramLogo()
        .useNgupukLogo())

if(not os.path.isdir('results')):
  os.makedirs('results')

base.makeVideo("sample.ogg", "results/sample_result.mp4")