# Open Streaming Platform

[![N|Solid](https://i.imgur.com/iKfwtyS.jpg)](https://i.imgur.com/4RV5IXH.jpg)

**Open Streaming Platform (OSP) is an open-source, RTMP streamer software front-end for [Arut's NGINX RTMP Module](https://github.com/arut/nginx-rtmp-module).**

OSP was designed a self-hosted alternative to services like Twitch.tv, Ustream.tv, and Youtube Live.

**OSP is still considered Alpha and is not complete**

## Features:
 - RTMP Streaming from an input source like Open Broadcast Software (OBS).
 - Multiple Channels per User, allowing a single user to broadcast multiple streams at the same time without needing muiltiple accounts.
 - Video Stream Recording and On-Demand Playback. [![N|Solid](https://i.imgur.com/4RV5IXH.jpg)](https://i.imgur.com/4RV5IXH.jpg)
 - Per Channel Real-Time Chat for Video Streams. [![N|Solid](https://i.imgur.com/c598KLa.jpg)](https://i.imgur.com/c598KLa.jpg)
 - Real-Time Chat Moderation by Channel Owners (Banning/Unbanning)

## Planned Features:
 - Subscribe to a Channel and Get Notified on When a New Stream Starts.
 - Password Protected Channels & Live Streams

## Tech

Open Streaming Platform uses a number of open source projects to work properly:

* [Python 2.7] - Because I'm too lazy to learn Python 3.
* [Gunicorn] - Python WSGI HTTP Server, Acts as a Reverse Proxy for Flask
* [Flask] - Microframework for Python based on Werkzeug & Jinja 2
* [Flask SQL-Alchemy] - Provide the Database for OSP
* [Flask Security] - Handle User Accounts, Login, and Registration
* [Flask Uploads] - Manage User Uploads, such as Pictures
* [Flask-RestPlus] - Handling and Documentation of the OSP API
* [Bootstrap] - For Building responsive, mobile-first projects on the web 
* [NGINX] - Open-Source, high-performance HTTP server and reverse proxy
* [NGINX-RTMP-Module] - NGINX Module for RTMP/HLS/MPEG-DASH live streaming
* [Socket.io] - Real-Time Communications Engine Between Client and Server
* [Flask Socket.io] - Interface Socket.io with Flask
* [Video.js] - Handles the HTML5 Video Playback of HLS video streams and MP4 Files
* [Font Awesome] - Interface Icons and Such

And OSP itself is open source with a [public repository](https://gitlab.com/Deamos/flask-nginx-rtmp-manager) on Gitlab.

## Installation

### Standard Install
OSP has only been tested on Ubuntu 16.04 and the installation script may not work properly on other OS's.

Clone the Gitlab Repo
```sh
git clone https://gitlab.com/Deamos/flask-nginx-rtmp-manager.git
```
Chmod setup-osp.sh to be Executable.
```sh
cd flask-nginx-rtmp-manager
chmod +x setup-osp.sh
```
Run the install script
```sh
sudo ./setup-osp.sh
```

The installation script will install the files in the following location:
* **Video Files, Video Stream Files, and User Uploaded Images**: /var/www
* **OSP Files**: /opt/osp

Rename the Configuration File
```sh
cd /opt/osp
sudo mv config.py.dist config.py
```
Edit the Default Values in the Configuration File
```sh
vi config.py
```
Change the following values from their Default:
* dbLocation - By Default, OSP uses SQLite, but you can change this value to use MySQL if you would like.
* secretKey - Flask Secret Key, change this!
* passwordSalt - Flask Security uses this value for Salting User Passwords, change this!

Restart the OSP service
```sh
sudo systemctl restart osp
```
Open a Web Browser and configure OSP
```
http://[SERVER IP]/
```

### Docker Install

A Dockerfile has been provided for running OSP in a container.  However due to the way NginX, Gunicorn, Flask, and Docker work, for OSP to work properly, the Frontend must be exposed using Port 80 or 443 and the RTSP port from OBS or other streaming software must be exposed on Port 1435.

This accomplished easily by using a reverse proxy in Docker such as Traefik.  However, Port 1435 will not be proxied and must be mapped to the same port on the host.

**Recommended Volumes/Mount Points**
* /var/www - Storage of Images, Streams, and Stored Video Files
* /opt/osp/config.py - DB configuration and Password Salt Settings
* /opt/osp/database.db - Initial SQLite DB File
* /usr/local/nginx/conf - Contains the NginX Configuration files which can be altered to suit your needs (HTTPS without something like Traefik)

### Usage

**A Channel and Stream key must be created prior to streaming.**

Set your OBS client to stream at:
```
rtsp://[serverip]/stream
```

**Important Note**: 
- By default, OSP uses HTTP instead of HTTPS.  It is recommend to get a TLS certificate and configure NGINX to use HTTPS prior to production use.
- NGINX Conf Files located at /usr/local/nginx/conf/
- If you plan on using Lets Encrypt, please use the Cert Only method for verification, as NGINX is configured from source and can cause problems with the Certbot automated process.

## API
OSP's API can be reached at the following Endpoint:
```
http://[serverIP/FQDN]/apiv1/
```
Usage of the API required a streamer create an API key.

The API is self-documenting using Swagger-UI.

To use an authenticated endpoint, ensure you are adding 'X-API-KEY':'\<Your API KEY>' to the request headers.


## Other Info
### Chat Comands
- /ban <username> - Bans a user from chatting in a chat room
- /unban <username> - Unbans a user who has been banned


License
----

MIT License
