import json
def handle(req):
    """handle a request to the function
    Args:
        req (str): request body
    """
    data = {
        "text": "Serverless Message",
        "attachments": [{
            "title": "====> COEN 241 <====",
            "fields": [{
                "title": "Difficulty",
                "value": "Medium",
                "short": True
            }],
            "author_name": "Yangzhang Zhou",
            "image_url": "https://avatars.githubusercontent.com/u/118139042?s=400&v=4"
        },
        {
            "title": "COEN 241 INFO",
            "text": "COEN 241 is about cloud computing."
        },
        {
            "fallback": "Would you recommend COEN 241 to your friends?",
            "title": "Would you recommend COEN 241 to your friends?",
            "callback_id": "response123",
            "color": "#FF0000",
            "attachment_type": "default",
            "actions": [
                {
                    "name": "recommend",
                    "text": "Of Course!",
                    "type": "button",
                    "value": "recommend"
                },
                {
                    "name": "definitely",
                    "text": "Most Definitely!",
                    "type": "button",
                    "value": "definitely"
                }
            ]
        }]
    }
    return json.dumps(data)
