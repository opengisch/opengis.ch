---
title: 'Das PostgreSQL Connection Service File und wieso wir es lieben – OPENGIS.ch'
date: 2024-05-28
slug: "the-postgresql-connection-service-file-and-why-we-love-it"
url: "/de/2024/05/28/the-postgresql-connection-service-file-and-why-we-love-it/"
source: "www.opengis.ch/de/2024/05/28/the-postgresql-connection-service-file-and-why-we-love-it/index.html"
---
**_Das PostgreSQL Connection Service File`pg_service.conf` ist nichts Neues. Es existiert seit einiger Zeit und vermutlich hast du es auch schon verwendet. Aber nicht nur das neue QGIS Plugin [PG service parser](<https://github.com/opengisch/qgis-pg-service-parser-plugin>) ist Grund genug, über unsere Liebe zu diesem File zu schreiben, auch weil wir generell denken, es ist an der Zeit zu zeigen, wie man es für ziemlich coole Sachen verwenden kann._**
## Was ist das Connection Service File?[](<https://gist.github.com/signedav/db434dec4bec1f84f2f280c0635d41b7#was-ist-das-connection-service-file>)
Das Connection Service File erlaubt Verbindungsoptionen pro sogenannten „Service“ lokal abzuspeichern.
Hast du also eine Datenbank namens `gis` auf einem lokalen PostgreSQL mit Port `5432` und Benutzername/Passwort `docker`/`docker` kannst du dies als einen Service namens `my-local-gis` abspeichern.
    
    # Lokale GIS Datenbank für Testzwecke
    [my-local-gis]
    host=localhost
    port=5432
    dbname=gis
    user=docker
    password=docker
Dieses Connection Service File heisst `pg_service.conf` und wird von den Client-Applikationen (wie [psql](<https://www.postgresql.org/docs/current/app-psql.html>) oder [QGIS](<https://qgis.org/en/site/>)) grundsätzlich direkt im Benutzerverzeichnis gesucht. Es heisst dann in Windows im Applikationsverzeichnis des Benutzers unter `postgresql\.pg_service.conf`. In Linux liegt es standardmässig direkt im Verzeichnis des Benutzers `~/.pg_service.conf`. 
Es muss aber nicht zwingend dort liegen. Es kann irgendwo auf dem System (oder einem Netzlaufwerk) liegen, solange du die Umgebungsvariable `PGSERVICEFILE` entsprechend konfigurierst:
    
    export PGSERVICEFILE=/home/dave/connectionfiles/pg_service.conf 
Hast du das gemacht, wird von den Client-Applikationen zuerst dort gesucht – und gefunden.
Ansonsten kann mit `PGSYSCONFDIR` auch ein Ordner definiert werden, wo das File `pg_service.conf` zu finden ist.
Hat man das, kann ein Service der Client-Applikation übergeben werden. Das heisst in [psql](<https://www.postgresql.org/docs/current/app-psql.html>) würde das so aussehen:
    
    ~$ psql service=my-local-gis
    psql (14.11 (Ubuntu 14.11-0ubuntu0.22.04.1), server 14.5 (Debian 14.5-1.pgdg110+1))
    SSL connection (protocol: TLSv1.3, cipher: TLS_AES_256_GCM_SHA384, bits: 256, compression: off)
    Type "help" for help.
    
    gis=#
Und in QGIS so:
![QGIS PostgreSQL connection dialog using a pg_service.conf service entry](./image38f5.png)
Wenn du dann in QGIS einen Layer hinzufügst, wird in das Projektfile nur der Name des Services geschrieben. Weder die Verbindungsparameter noch Benutzername/Passwort sind gespeichert. Das hat neben dem Sicherheitsaspekt verschiedene Vorteile, mehr dazu weiter unten.
Du musst aber nicht alle diese Parameter einem Service übergeben. Übergibst du nur Teile davon (zBs. ohne die Datenbank), dann musst du diese beim Aufruf der Verbindung noch mitgeben:
    
    $psql "service=my-local-gis dbname=gis"
    psql (14.11 (Ubuntu 14.11-0ubuntu0.22.04.1), server 14.5 (Debian 14.5-1.pgdg110+1))
    SSL connection (protocol: TLSv1.3, cipher: TLS_AES_256_GCM_SHA384, bits: 256, compression: off)
    Type "help" for help.
    
    gis=#
Du kannst aber auch Parameter übersteuern. Wenn du eine Datenbank `gis` im Service konfiguriert hast, aber auf die Datenbank `web` zugreiffen willst, kannst du den Service und die explizite Datenbank angeben:
    
    $psql "service=my-local-gis dbname=web"
    psql (14.11 (Ubuntu 14.11-0ubuntu0.22.04.1), server 14.5 (Debian 14.5-1.pgdg110+1))
    SSL connection (protocol: TLSv1.3, cipher: TLS_AES_256_GCM_SHA384, bits: 256, compression: off)
    Type "help" for help.
    
    web=#
Das Gleiche gilt natürlich auch für QGIS.
Und betreffend den genannten Umgebungsvariablen. Du kannst dir auch einen Standard-Service setzen.
    
    export PGSERVICE=my-local-gis
Besonders angenehm in der täglichen Arbeit mit immer derselben Datenbank.
    
    $ psql
    psql (14.11 (Ubuntu 14.11-0ubuntu0.22.04.1), server 14.5 (Debian 14.5-1.pgdg110+1))
    SSL connection (protocol: TLSv1.3, cipher: TLS_AES_256_GCM_SHA384, bits: 256, compression: off)
    Type "help" for help.
    
    gis=#
## Und weshalb ist es besonders cool?[](<https://gist.github.com/signedav/db434dec4bec1f84f2f280c0635d41b7#und-weshalb-ist-es-besonders-cool>)
Es gibt verschiedene Gründe, weshalb ein solches File nützlich ist:
  - Sicherheit: Man muss die Verbindungsparameter nirgendwo in den Client Files (sBs. QGIS Projektfiles) abspeichern. Beachte aber, dass es noch immer plaintext im Service File steht.
  - Abkopplung: Man kann die Verbindungsparameter ändern, ohne die Settings in Client Files (sBs. QGIS Projektfiles) ändern zu müssen
  - Multi-User: Man kann das File auf einem Netzlaufwerk abspeichern. Solange die Umgebungsvariable der lokalen Systeme auf dieses File zeigt, können alle Benutzer mit den gleichen Logins darauf zugreiffen.
  - Diversität: Man kann mit demselben Projektfile auf verschiedene Datenbanken mit gleicher Struktur zugreiffen, wenn lediglich der Name des Services gleich bleibt.


Zum letzten Grund hier drei Use Cases.
### **Support-Case**
Jemand meldet uns ein Problem in QGIS bei einem spezifischen Fall mit ihrer Datenbank. Da das Problem nicht zu reproduzieren ist, schicken sie uns einen DB-Dump eines Schemas und ein QGIS Projektfile. Die Layer im QGIS Projektfile sind einem Service verknüpft. Nun können wir den Dump auf unserer lokalen Datenbank wiederherstellen und mit unserem eigenen, gleichnamigen Service darauf zugreiffen. Das Problem kann so reproduziert werden.
### **INTERLIS**
Mit INTERLIS wird die Struktur eines Datenbankschemas genau spezifiziert. Wenn nun der Kanton dieses Modell bei sich erstellt hat und ein QGIS Projekt dazu konfiguriert, kann er das Projektfile einer Firma weitergeben, ohne auch die Datenbankstruktur mitzugeben. Die Firma kann auf ihrer eigenen PostgreSQL Datenbank das Schema aufgrund des INTERLIS Modells aufbauen und anhand ihres eigenen, gleichnamigen Services darauf zugreiffen.
### **Test/Prod Switching**
Du kannst mit demselben QGIS Projekt auf eine Test und eine Produktivdatenbank zugreiffen, wenn du pro[ QGIS Profil](<https://docs.qgis.org/3.34/de/docs/user_manual/introduction/qgis_configuration.html#user-profiles>) die Umgebungsvariable für das Connection Service File anders setzst.
Du erstellst zwei Connection Service Files.
Das zur Testdatenbank in `/home/dave/connectionfiles/test/pg_service.conf`:
    
    [my-local-gis]
    host=localhost
    port=54322
    dbname=gis-test
Und das für die Produktivdatenbank in `/home/dave/connectionfiles/prod/pg_service.conf`:
    
    [my-local-gis]
    host=localhost
    port=54322
    dbname=gis-productive
In QGIS erstellst du zwei Profile „Test“ und „Prod“:
![QGIS profile chooser showing separate Test and Prod profiles for PostgreSQL services](https://lh7-us.googleusercontent.com/P5tG5kloX-sTGLtJjItVhTwQzGjhMugMEhgkUTfUfO4jblPxurVHGRdRcMkH2BGLyMrAPNZtOdaRO5OzeMvxR4CUC38gY23c9uGjXPn_65qSRRddeohzlDU4bQdPlbg5q9yGozwMjzuz9GeP-CTCPN8)
Und pro Profil setzst du die Umgebungsvariable `PGSERVICEFILE` die verwendet werden soll (im Menu  _Settings > Options…_ und dort unter  _System_ herunterscrollen bis  _Environment_).
![QGIS profile environment settings for PGSERVICEFILE, screenshot 1](https://lh7-us.googleusercontent.com/BZQzdWMsz1dbNf43syK1wkViu_uiOjitDu3a2wnJw7NElQ-OyvVwc26BR2y9rIW7ol_ocLGPOeRhfsjliIj9yWhUYqColQnwIpGfwVcMX2kPtFebDymTlFJjmbxDehH9QJ2MshLFu5TaULQfgOW-VZk)
bzw.
![QGIS profile environment settings for PGSERVICEFILE, screenshot 2](https://lh7-us.googleusercontent.com/1KSjiGIKgFBxD13G7FYB_6wz6BRt2XbYmNJVdsgoCzptjN9K6PoR-Q5Ttxxnf6XAKXLYjWFL6PacuroU6klaW0EZJZtPDGVkLHPYQYUA1kACMMmJz7TZkQpGp-yvRaAaqN0j3sYJsZTXT2EXQACtdIc)
Wenn du nun in QGIS den Service `my-local-gis` nutzst, verbindet es im Profil „Prod“ mit der Datenbank `prod` und im Profil „Test“ mit der Datenbank `test`.
## **Die Authentifizierungskonfiguration**
Nun noch zur Authentifizierung. Hat man das Connection Service File auf einem Netzlaufwerk und stellt es mehreren Usern zur Verfügung, möchte man ja vielleicht eher nicht, dass alle mit demselben Login zugreiffen. Oder man möchte generell keine Benutzerinformation in diesem File drin haben. Das lässt sich in QGIS elegant mit der Authentifizierungskonfiguration kombinieren.
Möchtest du eine QGIS Projektfile mehreren Usern zur Verfügung stellen, erstellst du die Layer mit einem Service. Dieser Service enthält alle Verbindungsparameter, bis auf die Login-Information.
Diese Login-Information übergibt man mit einer QGIS Authentifizierung.
![QGIS authentication configuration for a PostgreSQL service connection](https://lh7-us.googleusercontent.com/RGByDYJr2czDGs4XKQD6SzCbsgiM318UdYav1m0z9fzX9_vQcFNjnZ5zqqg2X5hQ6HnJhwNGuszKYPpVSE5L53mxrpSTlLhGw5J8TAOB43IhTXFJlfII3ICPmX9ztbEOlR-TpJrlW5jfOy42-Dbx_Os)
Diese Authentifizierung konfigurierst du ebenfalls pro obengenanntem QGIS-Profil. Dieses wird über Menu  _Settings > Options…_ und dort unter  _Authetification_ mit dem  _+_ erstellt:
![QGIS authentication settings dialog](https://lh7-us.googleusercontent.com/nnQe3fm9iMDFxG5QCxV_kpeBKjiUUefXx5B0dcNvMF7v0ObW_5051hXBBldC_CKSTrNPblJzwDo0zK2aQBKyz9ZM_27wIPtOY1i7srhpJLMr84VHWevuy4F1hj93ZjzJXbAKlt80gw0HuHtHaqcuigQ)
(oder auch direkt dort, wo man die PostgreSQL Verbindung erstellt)
Wenn du so einen Layer hinzufügst, werden im QGIS Projektfile einerseits der Service wie auch die Id der Authentifizierungskonfiguration gespeichert. Diese ist in diesem Fall `mylogin` und muss natürlich den anderen Usern mitgeteilt werden, damit auch sie für ihr Login die Id `mylogin` konfigurieren.
Pro Profil kann man natürlich mehrere Authetifizierungkonfigurationen verwenden.
## **QGIS Plugin**
Übrigens gibt es neu ein tolles Plugin, um diese Services direkt in QGIS zu konfigurieren. So musst du dich nicht mehr mit Textbasierten INI-Files herumschlagen. Es heisst [PG service parser](<https://github.com/opengisch/qgis-pg-service-parser-plugin>):
![PG service parser plugin interface in QGIS](https://lh7-us.googleusercontent.com/3JNSq_fmD2g33fLls2FGklpoCRo-M4Pyuts7z4dP56wKK7_tRj3hGyakJSQHTHBxWyQNkBfJQggaPl_InrOdY58b-6GN8eGBH9oOgJYLkq6XMApgGBrboR_FQ5dZwJZFiBpZZ4_oBg2_BTNUAGiuPkk)
Es findet das Connection Service File anhand den erwähnten Umgebungsvariabeln `PGSERVICEFILE` or `PGSYSCONFDIR` oder in den Standardverzeichnissen.
Ebenso ist es supereasy neue Services zu erstellen, indem man bestehende dupliziert und bearbeitet.
![PG service parser plugin duplicating an existing service](https://lh7-us.googleusercontent.com/FvLhRVplNNN5EGo8OYmED9L786WKZOxxBZy98wVnJq6vywqo_Ny2wHQaKUbcMMaiyEVTD8BNKAeD0kAY_4HgmJ39NvEF9z20PPlbwPNIgVFRXwNQTYn5KgGOzJ8iUGJ4PnY7l1y0rNzOTrdOqMtbcNY)
### Und für die Devs
Was wäre ein Blogpost ohne Geek-Futter? Das backend des Plugins ist in [PYPI](<https://pypi.org/project/pgserviceparser/>) publiziert und kann einfach mit `pip install pgserviceparser `installiert und in Python genutzt werden.
Zum Beispiel um die Services aufzulisten.
    
    >>> import pgserviceparser
    >>> pgserviceparser.service_names()
    ['my-local-gis', 'another-local-gis', 'opengisch-demo-pg']
Optional kann auch das Servicefile übergeben werden. Ansonsten wird es mit dem erwähnten Mechanismus gefunden.
Oder um die Konfiguration eines bestimmten Services in einem Dict zu kriegen:
    
    >>> pgserviceparser.service_config('my-local-gis')
    {'host': 'localhost', 'port': '54322', 'dbname': 'gis', 'user': 'docker', 'password': 'docker'}
Da gibt es aber noch mehr Funktionen. Finde sie auf [GitHub](<https://github.com/opengisch/pgserviceparser>) oder in der [Dokumentation](<https://opengisch.github.io/pgserviceparser/>).
## Nun dann
Wir hoffen du Teilst – zumindest nach diesem Blogpost – unser Enthusiasmus für dieses tolle File. Und falls nicht, dann sag uns doch weshalb in den Kommentaren 🙂
### _Related_
