## PYTHON GUI TO DOWNLOAD YOUTUBE VIDEOS AS AUDIO FILE

'youtube_dl' module can be used to download Youtube Video as Audio File.

### The module can be installed using the command - pip install youtube_dl

When running the following program, an error may occur stating ERROR: ffprobe/avprobe and ffmpeg/avconv not found. Please install one.

To resolve this error download FFmpeg zip, from the link https://ffmpeg.zeranoe.com/builds/

Extract the contents of the zip folder downloaded from the above link. Copy and Paste them in the following locations

For WINDOWS - C:\Python37\Scripts <br>
For MAC/LINUX - Paste the Contents in the folder where youtube-dl is located.<br>
In my case it is /Library/Frameworks/Python.framework/Versions/3.7/bin/

For me it also showed an error 'ffmpeg cannot be opened because the manufacturer cannot be verified'. In that case navigate to the directory '/Library/Frameworks/Python.framework/Versions/3.7/bin/' where the ffmpeg and ffprobe executables are located and right-click on the ffmpeg file and click on Open. On the next window, again click on Open. Perform the same steps, if it shows the error for ffprobe as well
