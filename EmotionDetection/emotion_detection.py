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

    # Parse the response from the API
    formatted_response = json.loads(response.text)

    # Check if 'emotionPredictions' is in the response
    if response.status_code == 200:
        emotions = formatted_response['emotionPredictions'][0]['emotion']
        anger_score = emotions.get('anger', 0)
        disgust_score = emotions.get('disgust', 0)
        fear_score = emotions.get('fear', 0)
        joy_score = emotions.get('joy', 0)
        sadness_score = emotions.get('sadness', 0)

        # Determine the dominant emotion
        dominant_emotion = max(emotions, key=emotions.get)

    return {
        'anger': anger_score,
        'disgust': disgust_score,
        'fear': fear_score,
        'joy': joy_score,
        'sadness': sadness_score,
        'dominant_emotion': dominant_emotion
    }

# from EmotionDetection.emotion_detection import emotion_detector
# emotion_detector("I hate working long hours")
# {"emotionPredictions":[{"emotion":{"anger":0.0132405795, "disgust":0.0020517302, 
# "fear":0.009090992, "joy":0.9699522, "sadness":0.054984167}, "target":"", 
# "emotionMentions":[{"span":{"begin":0, "end":26, "text":"I love this new technology"}, 
# "emotion":{"anger":0.0132405795, "disgust":0.0020517302, "fear":0.009090992, "joy":0.9699522, "sadness":0.054984167}}]}], 
# "producerId":{"name":"Ensemble Aggregated Emotion Workflow", "version":"0.0.1"}}