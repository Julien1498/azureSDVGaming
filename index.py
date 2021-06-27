#!~\Appdata\Local\Microsoft\WindowsApps\python3.7.exe
#coding:utf-8

import os
import cgi 
from http import cookies
C = cookies.SimpleCookie()
C["pseudo"] = "0"
C["access"] = "0"
if os.environ['HTTP_COOKIE']:
    cookies = os.environ['HTTP_COOKIE']
    cookies = cookies.split('; ')

    for cookie in cookies:
        cookie = cookie.split('=')
        C[cookie[0]] = cookie[1]

form = cgi.FieldStorage()
if form.getvalue("pseudo") == "Julien" and form.getvalue("pass") == "sdvnul":
    C["pseudo"] = "Julien"
    C["access"] = "0"
    print(C)

if form.getvalue("pseudo") == "Yves" and form.getvalue("pass") == "sdv42":
    C["pseudo"] = "Yves"
    C["access"] = "1"
    print(C)

print("Content-type: text/html; charset=utf-8\n")

html = """<!DOCTYPE html>
<head>
    <title>Mon jeu Unity</title>
</head>
<body>
"""
if C["pseudo"].value == "Yves" or C["pseudo"].value == "Julien":
    html += """
    <div>
        Bonjour """ + C["pseudo"].value + """
    </div>
    """
    if C["access"].value == "1":
        html += """
        <div id="div42">
            <div>
                Clic pour lancer la VM
            </div>
            <input type="button" id='script' name="scriptbutton" value="Start VM" onclick="startPy()">
            </br><input type="button" id="rdpd3" name="rdpd3" value="Deconnexion" onclick="disco()">
        </div>
        """
    if C["access"].value == "0":
        html += """
        <div>
            Vous ne disposez pas des droits necessaire pour jouer !
            </br><input type="button" id="rdpd3" name="rdpd3" value="Deconnexion" onclick="disco()">
        </div>
        """
else:
    html += """
    <form action="/index.py" method="post">
        <input type="text" name="pseudo" placeholder="Pseudo" />
        <input type="password" name="pass" placeholder="Password" />
        <input type="submit" name="send" value="Connexion">
    </form>
    """

html += """
<script>
    function startPy(){
        fetch("start.py")
            .then(function(response) {
                var element = document.getElementById("div42");
                element.innerHTML = '<p>Prenez le fichier RDP ou connectez vous en RDP a l ip suivante: 51.103.35.68</p><p>Identifiant: JulienG</p><p>Password: iARH6AKAcn3tidb</p><label for="rdpdl">Prendre le fichier rdp: </label><input type="button" id="rdpdl" name="rdpdl" value="Download" onclick="takeFile()"><label for="rdpd2"></br>Eteindre la VM: </label><input type="button" id="rdpd2" name="rdpd2" value="Turn off" onclick="stopPy()"></br><input type="button" id="rdpd3" name="rdpd3" value="Deconnexion et eteindre la VM" onclick="disconnect()">';
            });
    }
    
    function stopPy(){
        fetch("stop.py")
            .then(function(response) {
                var element = document.getElementById("div42");
                element.innerHTML = '<div>Clic pour lancer la VM</div><input type="button" id="script" name="scriptbutton" value="Start VM" onclick="startPy()">';
            });
    }

    function disconnect(){
        document.cookie = "pseudo=; expires=Thu, 01 Jan 1970 00:00:00 UTC; path=/;";
        document.cookie = "access=; expires=Thu, 01 Jan 1970 00:00:00 UTC; path=/;";
        fetch("stop.py")
            .then(function(response) {
                var element = document.getElementById("div42");
                element.innerHTML = ' <meta http-equiv="refresh" content="0;URL=/index.py"> ';
            });
    }
    function disco(){
        document.cookie = "pseudo=; expires=Thu, 01 Jan 1970 00:00:00 UTC; path=/;";
        document.cookie = "access=; expires=Thu, 01 Jan 1970 00:00:00 UTC; path=/;";
        var element = document.getElementById("rdpd3");
        element.innerHTML = ' <meta http-equiv="refresh" content="0;URL=/index.py"> ';
    }
    function takeFile(){
        var element = document.createElement('a');
        var text = "full address:s:51.103.35.68:3389 prompt for credentials:i:1 administrative session:i:1";
        element.setAttribute('href', 'data:text/plain;charset=utf-8,' + encodeURIComponent(text));
        element.setAttribute('download', "Game.rdp");

        element.style.display = 'none';
        document.body.appendChild(element);

        element.click();

        document.body.removeChild(element);
        }

        // Start file download.
        
</script>
</body>
</html>
"""

print(html)
