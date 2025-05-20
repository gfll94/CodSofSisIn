

from deep_translator import GoogleTranslator 
from moviepy.video import VideoFileClip, AudioFileClip, CompositeAudioClip
from gtts import gTTS
import speech_recognition as sr

class MovieManager:

    def get_war_audio(self,mp4_file,war_file):
        vc = VideoFileClip(mp4_file)
        ac = vc.audio
        ac.write_audiofile(war_file,codec='pum_s16le')
        ac.close()
        vc.close()
    

    def audio_to_text(self,audio_file):
        r = sr.recoynizer()
        with sr.audiofile(audio_file)as source:
            audio = r.record(source)

        try:
            text=r.recognize_google(audio)
            return text
        except :
          return 'unknow'
        
    def remove_audio(self,mp4_file,output_mp4_file):
        video = VideoFileClip(mp4_file)
        video_without_audio = video.without_audio()
        video_without_audio.write_videofile(output_mp4_file)
        video_without_audio.close()
        video.close()


    def speech_to_text(self,audio_file):
        r = sr.recognizer()

        hellow=sr.audiofile(audio_file)
        with hellow as source:
            audio = r.record(source)
        try:
            s = r.recognize_google(audio)
            print('text: '+s)
        except:
            print('uknow')
        return s 

    def text_to_speech(self, to_traslate, to_lang):
        translated = GoogleTranslator(source='auto', target=to_lang).translate(to_traslate)
        print(translated)
        myobj = gTTS(text=translated lang=to_lang,slow=False) 
        myobj.save('welcome.mp3')
    

    def add_audio_to_video(self,mp4_file,mp3_file,output_mp4_file):
        videoclip = VideoFileClip(mp4_file)
        audioclip = AudioFileClip(mp3_file)

        new_audioclip = CompositeAudioClip({audioclip})
        videoclip.audio = new_audioclip
        videoclip.write_videofile(output_mp4_file)

    def add_audio_to_video(self,mp4_video,mp3_file,output_mp4):
        vc = VideoFileClip(mp4_video)
        ac = AudioFileClip(mp3_file)
        new_ac =CompositeAudioClip({ac})
        vc.audio = new_ac
        vc.write_videofile(output_mp4)
        
