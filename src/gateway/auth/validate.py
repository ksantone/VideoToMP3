import os, requests

def token(request):
    print("Request in token function is: ", str(request))
    if not "Authorization" in request.headers:
        return None, ("missing credentials", 401)

    token = request.headers["Authorization"]

    if not token:
        return None, ("missing credentials", 401)

    auth_svc_address = os.environ.get('AUTH_SVC_ADDRESS')
    print(f"AUTH_SVC_ADDRESS: {auth_svc_address}")
    print(f"Token: {token}")

    try:
        response = requests.post(
            f"http://{auth_svc_address}/validate",
            headers={"Authorization": token}
        )
        print("Response in token function is: ", str(response))
    except Exception as e:
        print("Exception in token function: ", str(e))
        return None, ("internal server error", 500)

    print("Response in token function is: ", str(response))

    if response.status_code == 200:
        return response.text, None
    else:
        return None, (response.text, response.status_code)
