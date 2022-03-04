import youtube_dl as yt

ydl_opts={}


def dwld():

    with yt.YoutubeDL(ydl_opts) as ydl:

        ydl.download([link])



link='https://youtu.be/T6OLDHAWjjA?list=PLIhvC56v63ILPDA2DQBv0IKzqsWTZxCkp'
link=link.strip()
print(link)
dwld()

