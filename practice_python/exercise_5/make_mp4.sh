#! \usr\bin\sh
ffmpeg -r 3 -i ./figure/imag_%02d.png -vcodec libx264 -pix_fmt yuv420p -r 60 output.mp4
ffmpeg -i output.mp4 output.gif
rm output.mp4
