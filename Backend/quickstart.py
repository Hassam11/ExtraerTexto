import os
import azure.ai.vision as sdk
import json

def Analizar(url):
    service_options = sdk.VisionServiceOptions(os.environ["VISION_ENDPOINT"], os.environ["VISION_KEY"])
    vision_source = sdk.VisionSource(url= url)

    analysis_options = sdk.ImageAnalysisOptions()
    analysis_options.features = ( sdk.ImageAnalysisFeature.CAPTION | sdk.ImageAnalysisFeature.TEXT )
    analysis_options.language = "en"
    analysis_options.gender_neutral_caption = True
    ## Esto es importante
    image_analyzer = sdk.ImageAnalyzer(service_options, vision_source, analysis_options)
    #Realiza una operación de análisis de imagen utilizando la fuente de imagen proporcionada al crear esta instancia de ImageAnalyzer.
    result = image_analyzer.analyze()

    if result.reason == sdk.ImageAnalysisResultReason.ANALYZED:
        #Lo que capta o lo que "Ve"
        def Vision():
            if result.caption is not None:
            # response = {'message': 'Contenedio:' + result.caption.content, "confidence": result.caption.confidence }
                response = {
                    "Contenido" : result.caption.content,
                    "Confianza" : result.caption.confidence 
                }
                # print(response)
            return response

        vision_result = Vision()
        # # "Lee el texto que aparece en la iamgen"
        def Texto():
            word_data = []
            if result.text is not None:
                for line in result.text.lines:
                    word_data.append({"content": line.content})
                    print(word_data)
            return word_data

        texto_result = Texto()
        return { "vision_result": vision_result, "texto_result": texto_result}

    else:

        error_details = sdk.ImageAnalysisErrorDetails.from_result(result)
        print(" Analysis failed.")
        print("   Error reason: {}".format(error_details.reason))
        print("   Error code: {}".format(error_details.error_code))
        print("   Error message: {}".format(error_details.message))
    

#"https://th.bing.com/th/id/R.43de4e8cfa1ff1fef2923e2c95bcbb5d?rik=2NdKMTOUHG7bNw&riu=http%3a%2f%2ftusimagenesde.com%2fwp-content%2fuploads%2f2014%2f09%2ffotos-de-risa-1.jpg&ehk=HXEi0WQPQNlo4mf5S9UYB8vzUkPvozqpN2jZQuYWx2Q%3d&risl=&pid=ImgRaw&r=0"
# Analizar("https://th.bing.com/th/id/R.43de4e8cfa1ff1fef2923e2c95bcbb5d?rik=2NdKMTOUHG7bNw&riu=http%3a%2f%2ftusimagenesde.com%2fwp-content%2fuploads%2f2014%2f09%2ffotos-de-risa-1.jpg&ehk=HXEi0WQPQNlo4mf5S9UYB8vzUkPvozqpN2jZQuYWx2Q%3d&risl=&pid=ImgRaw&r=0")