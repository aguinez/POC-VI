from google.cloud import videointelligence
import os

os.environ["GOOGLE_APPLICATION_CREDENTIALS"] = "/home/alex/sura-poc-analisis-de-sueno-297379928d09.json"

video_client = videointelligence.VideoIntelligenceServiceClient()
features = [videointelligence.enums.Feature.SPEECH_TRANSCRIPTION]

config = videointelligence.types.SpeechTranscriptionConfig(
    language_code='es-CL',
    enable_automatic_punctuation=True,
    enable_speaker_diarization=True)
video_context = videointelligence.types.VideoContext(
    speech_transcription_config=config)

operation = video_client.annotate_video(
    "gs://raw-video-files-89guyjhb5/VID-20190814-WA0031/VID-20190814-WA0031.mp4", features=features,
    video_context=video_context)

print('\nProcessing video for speech transcription.')

result = operation.result(timeout=600)

count = 1
annotation_results = result.annotation_results[0]
for speech_transcription in annotation_results.speech_transcriptions:
    for alternative in speech_transcription.alternatives:
        #print('Alternative level information:')
        #print('Transcript: {}'.format(alternative.transcript))
        #print('Confidence: {}\n'.format(alternative.confidence))
        #print('Word level information:')
        f = open("/home/alex/Imágenes/frases_WA0031.txt", "a+")
        f.write(alternative.transcript)
        f.close()
        subtitles = ''
        for word_info in alternative.words:
            word = word_info.word
            start_time = word_info.start_time
            end_time = word_info.end_time
            subtitles = subtitles + str(count) + '\n'
            subtitles = subtitles + '00:00:{} --> 00:00:{}'.format(
                str(start_time.seconds + start_time.nanos * 1e-9).replace(".", ","),
                str(end_time.seconds + end_time.nanos * 1e-9).replace(".", ","))
            subtitles = subtitles + '\n' + word + '\n\n'
            count = count + 1
    f = open("/home/alex/Imágenes/subtitles_31.srt", "a+")
    f.write(subtitles)
    f.close()


https://cloud.google.com/vision/docs/face-tutorial
https://cloud.google.com/vision/docs/detecting-faces#vision-face-detection-python
https://cloud.google.com/natural-language/docs/sentiment-tutorial