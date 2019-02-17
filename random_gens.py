import json
import urllib.request
import urllib.parse
import requests
import sys

def get_result(url: str) -> dict:
    response = None

    try:
        response = urllib.request.urlopen(url)
        json_text = response.read().decode(encoding = 'utf-8')
        result = json.loads(json_text)
        return result

    except:
        print('ERROR')
        sys.exit()

    finally:
        if response != None:
            response.close()
