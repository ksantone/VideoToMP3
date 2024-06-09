import os, requests

def token(request):
    print("Request in token function is: ", str(request))
    if not "Authorization" in request.headers:
        return None, ("missing credentials", 401)

    token = request.headers["Authorization"]

    if not token:
        return None, ("missing credentials", 401)

    response = requests.post(
        f"http://{os.environ.get('AUTH_SVC_ADDRESS')}/validate",
        headers={"Authorization": token}
    )

    print("Response in token function is: ", str(response))

    if response.status_code == 200:
        return response.text, None
    else:
        return None, (response.text, response.status_code)
