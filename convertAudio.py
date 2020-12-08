import cherrypy
import pandas as pd
import runmodel
p = runmodel.runmodel()

class convertAudio(object):

  @cherrypy.expose
  @cherrypy.tools.json_out()
  @cherrypy.tools.json_in()
  def index(self):
      #data = cherrypy.request.json
      #df = pd.DataFrame(data)
      model_path = "path/to/model/dir"
      w2l_bin = "path/to/interactive_streaming_asr_example"
      path_to_audio_file = '/content/wav2letterInference/numbersAudioMale.wav'
      output = p.run(model_path,w2l_bin,path_to_audio_file)
      return output#.to_json()
  index.exposed = True

if __name__ == '__main__':
   config = {'server.socket_host': '0.0.0.0','server.socket_port' : int(sys.argv[1])}
   cherrypy.config.update(config)
   cherrypy.quickstart(convertAudio())