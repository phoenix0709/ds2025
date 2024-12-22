from flask import Flask, request
from ftplib import FTP
import os

app = Flask(__name__)

FTP_SERVER = "<FTP_SERVER_IP>"
FTP_USER = "ftpuser"
FTP_PASS = "ftppass"

@app.route('/upload', methods=['POST'])
def upload_file():
    file = request.files['file']
    file_path = f"/tmp/{file.filename}"
    file.save(file_path)

    try:
        ftp = FTP(FTP_SERVER)
        ftp.login(user=FTP_USER, passwd=FTP_PASS)
        with open(file_path, "rb") as f:
            ftp.storbinary(f"STOR {file.filename}", f)
        ftp.quit()
        os.remove(file_path)
        return "File uploaded to FTP Server successfully!"
    except Exception as e:
        return f"Failed to upload file: {e}"

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
