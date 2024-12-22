#!/bin/bash
sudo useradd -m ftpuser
echo "ftpuser:ftppass" | sudo chpasswd
sudo mkdir -p /home/ftpuser/files
sudo chown ftpuser:ftpuser /home/ftpuser/files
echo "Setup complete!"
