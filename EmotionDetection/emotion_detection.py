import requests, json

def emotion_detector(text_to_analyze):
    # Blank itext
    if text_to_analyze is None or text_to_analyze.strip() == "":
        return {
            'anger': None,
            'disgust': None,
            'fear': None,
            'joy': None,
            'sadness': None,
            'dominant_emotion': None
        }

    # Define a function that takes a string input.
    # URL
    url = 'https://sn-watson-emotion.labs.skills.network/v1/watson.runtime.nlp.v1/NlpService/EmotionPredict'
    # Headers
    headers = {"grpc-metadata-mm-model-id": "emotion_aggregated-workflow_lang_en_stock"}
    # Dictionary
    myobj = { "raw_document": { "text": text_to_analyze } }
    # Response.
    response = requests.post(url, json = myobj, headers=headers)

    # Error.
    if response.status_code == 400:
        return {
            'anger': None,
            'disgust': None,
            'fear': None,
            'joy': None,
            'sadness': None,
            'dominant_emotion': None
        }
    
    # Correct answer.
    try:
        formatted_response = json.loads(response.text)
    except Exception:
        return {
            'anger': None,
            'disgust': None,
            'fear': None,
            'joy': None,
            'sadness': None,
            'dominant_emotion': None
        }

    if (
        not isinstance(formatted_response, dict) or
        'emotionPredictions' not in formatted_response or
        not formatted_response['emotionPredictions'] or
        len(formatted_response['emotionPredictions']) == 0
    ):
        return {
            'anger': None,
            'disgust': None,
            'fear': None,
            'joy': None,
            'sadness': None,
            'dominant_emotion': None
        }

    emotions = formatted_response['emotionPredictions'][0]['emotion']

    dominant_emotion = max(emotions, key = emotions.get)
    return {
        'anger': emotions['anger'],
        'disgust': emotions['disgust'],
        'fear': emotions['fear'],
        'joy': emotions['joy'],
        'sadness': emotions['sadness'],
        'dominant_emotion': dominant_emotion
    }
