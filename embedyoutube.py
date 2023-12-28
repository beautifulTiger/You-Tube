'''Python program to bypass school filter by embedding YouTube video into a blank HTML file.'''

import webbrowser



def main():
    video = input("Please paste the link of the youtube video you wish to embed: ")
    video_id = video[32:]
    link = 'https://www.youtube.com/embed/' + video_id
    text = '<iframe width="720" height="405" src='+link+' title="Go Programming Tutorial – 3 Beginner Projects"\
    frameborder="0" allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture; web-share" allowfullscreen></iframe>'

    read = open('readme.html', 'w')
    read.write(text)
    read = open("readme.html", "r")
    read.read()
    webbrowser.open('readme.html') 


on = True
while on == True:
    main()
