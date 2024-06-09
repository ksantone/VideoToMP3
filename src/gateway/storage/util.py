import pika, json


def upload(f, fs, channel, access):
    print("In the upload function")
    try:
        fid = fs.put(f)
    except Exception as err:
        print(err)
        return "internal server error", 500

    message = {
        "video_fid": str(fid),
        "mp3_fid": None,
        "username": access["username"],
    }

    try:
        print("Publishing to channel")
        channel.basic_publish(
            exchange="",
            routing_key="video",
            body=json.dumps(message),
            properties=pika.BasicProperties(
                delivery_mode=pika.spec.PERSISTENT_DELIVERY_MODE
            ), # What would happen if this were removed?
        )
    except Exception as err:
        print(err)
        fs.delete(fid) # What would happen if we did not delete the file?
        return "internal server error", 500
