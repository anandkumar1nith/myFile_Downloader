import urllib2
dwn_link = 'https://class.coursera.org/textanalytics-001/lecture/download.mp4?lecture_id=73'

file_name = 'trial_video.mp4' 
rsp = urllib2.urlopen(dwn_link)
with open(file_name,'wb') as f:
    f.write(rsp.read())
