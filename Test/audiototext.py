import cmu_sphinx4
url = 'https://aacapps.com/lamp/sound/amy.wav'
transcriber = cmu_sphinx4.Transcriber(url)
for line in transcriber.transcript_stream():
    print(line)