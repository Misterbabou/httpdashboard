# httpdashboard a simple dashboard for your website

---
[![Docker Pulls](https://img.shields.io/docker/pulls/misterbabou/httpdashboard.svg?logo=docker)](https://hub.docker.com/r/misterbabou/httpdashboard)
[![GitHub Release](https://img.shields.io/github/release/Misterbabou/httpdashboard.svg?logo=github&logoColor=959DA5)](https://github.com/Misterbabou/httpdashboard/releases/latest)
[![GitHub last commit](https://img.shields.io/github/last-commit/Misterbabou/httpdashboard?logo=github&logoColor=959DA5)](https://github.com/Misterbabou/httpdashboard/commits/main)
[![MIT Licensed](https://img.shields.io/github/license/Misterbabou/httpdashboard.svg?logo=github&logoColor=959DA5)](https://github.com/Misterbabou/httpdashboard/blob/main/LICENSE.md)
---

httpdashboard is a simple and lightweight dashboard for your sites.

## Screenshot 

![httpdashboard-gui.png](/assets/httpdashboard-gui.png)

## Features 

- Docker Image to deploy
- Multiple pages dashboard
- Pages editable from a simple yml file
- Search feature on Name or Menu

## Docker Conf

It's recommanded to use docker compose to run this application


Create `docker-compose.yml` file:
```
version: "3"
services:
  gptwol:
    container_name: httpdashboard
    image: misterbabou/httpdashboard:latest
    ports:
      - 8080:8000 #Change left port accordingly
    restart: unless-stopped
    volumes:
      - ./inventory.yml:/app/inventory.yml
```

Create the file to define your site configuration
```
touch inventory.yml
```

inventory.yml exemple, be carreful, if indentation is false this will not work [Check yml](https://www.yamllint.com/):
```
index.html: 					# Keep this name for your main page
  title: "Main Menu"				# Name of the page
  menu_list:
    Google:					# Name of the Menu
      icon: "fas fa-cog"			# Icon from https://fontawesome.com/v5/search?o=r&m=free
      link:
        - name: Google				# Name of the Link
          url: "https://www.google.com"		# URL
        - name: Youtube
          url: "https://www.youtube.com"
    Other:					# Name of the Menu
      icon: "fas fa-globe"
      link:
        - name: Twitter
          url: "https://twitter.com/"
        - name: Facebook
          url: "https://facebook.com/"
dashboard2.html:  #Name of an other the file should be unique
  title: Page2    
  menu_list:
    Google:
      icon: "fas fa-cog"
      link:
        - name: Google
          url: "https://www.google.com"
        - name: Youtube
          url: "https://www.youtube.com"
    Other:
      icon: "fas fa-globe"
      link:
        - name: Twitter
          url: "https://twitter.com/"
        - name: Facebook
          url: "https://facebook.com/"
```

Run the application
```
docker-compose up -d
```