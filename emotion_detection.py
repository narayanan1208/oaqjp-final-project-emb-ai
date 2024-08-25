import requests
import json

def emotion_detector(text_to_analyse):
    # Define the URL for the sentiment analysis API
    url = 'https://sn-watson-emotion.labs.skills.network/v1/watson.runtime.nlp.v1/NlpService/EmotionPredict'

    # Create the payload with the text to be analyzed
    myobj = { "raw_document": { "text": text_to_analyse } }

    # Set the headers with the required model ID for the API
    header = {"grpc-metadata-mm-model-id": "emotion_aggregated-workflow_lang_en_stock"}

    # Make a POST request to the API with the payload and headers
    response = requests.post(url, json=myobj, headers=header)

    return response.text

def emotion_detector_new(text_to_analyse):
    # Define the URL for the sentiment analysis API
    url = 'https://sn-watson-emotion.labs.skills.network/v1/watson.runtime.nlp.v1/NlpService/EmotionPredict'

    # Create the payload with the text to be analyzed
    myobj = { "raw_document": { "text": text_to_analyse } }

    # Set the headers with the required model ID for the API
    header = {"grpc-metadata-mm-model-id": "emotion_aggregated-workflow_lang_en_stock"}

    # Make a POST request to the API with the payload and headers
    response = requests.post(url, json=myobj, headers=header)

    # Parse the response from the API
    formatted_response = json.loads(response.text)
    print(response.text)

    # Check if 'documentSentiment' is in the response
    if response.status_code == 200:
        label = formatted_response['emotionPredictions']['label']
        score = formatted_response['emotionPredictions']['score']

    # Return the label and score in a dictionary
    return {'label': label, 'score': score}

# from emotion_detection  import emotion_detector
# emotion_detector("I love this new technology")
# {"emotionPredictions":[{"emotion":{"anger":0.0132405795, "disgust":0.0020517302, 
# "fear":0.009090992, "joy":0.9699522, "sadness":0.054984167}, "target":"", 
# "emotionMentions":[{"span":{"begin":0, "end":26, "text":"I love this new technology"}, 
# "emotion":{"anger":0.0132405795, "disgust":0.0020517302, "fear":0.009090992, "joy":0.9699522, "sadness":0.054984167}}]}], 
# "producerId":{"name":"Ensemble Aggregated Emotion Workflow", "version":"0.0.1"}}