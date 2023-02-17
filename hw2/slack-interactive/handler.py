import json
import urllib
def handle(req):
    """handle a request to the function
    Args:
        req (str): request body
    """
    data = {
        "attachments": [
            {
                "replace_original": True,
                "response_type": "ephemeral",
                "fallback": "Required plain-text summary of the attachment.",
                "color": "#FF0000",
                "pretext": "Cool! COEN 241 will be fun for you!",
                "author_name": "Yangzhang Zhou",
                "author_link": "https://github.com/LeonZYZReal/COEN_241_HW",
                "author_icon": "https://avatars.githubusercontent.com/u/118139042?s=400&v=4",
                "title": "COEN 241",
                "title_link": 
"https://www.scu.edu/engineering/academic-programs/department-of-computer-engineering/graduate/course-descriptions/",
                "text": "Head over to COEN 241",
                "image_url": 
"https://www.scu.edu/media/offices/umc/scu-brand-guidelines/visual-identity-amp-photography/visual-identity-toolkit/logos-amp-seals/Mission-Dont3.png",
                "thumb_url": 
"https://www.scu.edu/engineering/academic-programs/department-of-computer-engineering/graduate/course-descriptions/",
                "footer": "Slack Apps built on OpenFaas",
                "footer_icon": "https://a.slack-edge.com/45901/marketing/img/_rebrand/meta/slack_hash_256.png",
                "ts": 123456789
            }
        ]
    }
    return json.dumps(data)
