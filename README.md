# BlogFlask

1. Install<pre>
<code class="bash">$ mkvirtualenv web
$ cd web
$ git clone https://github.com/tkliuxing/BlogFlask.git
$ # or
$ # git clone https://gitcafe.com/tkliuxing/BlogFlask.git
$ cd BlogFlask
$ python setup.py develop
$ pip install -r requirements.txt
</code></pre>
2. Run develop server<pre>
<code class="bash">$ python runserver.py --help
Usage: runserver.py [options]
Options:
  -h, --help            show this help message and exit
  -P PORT, --port=PORT
  -H HOST, --host=HOST
  --debug
<br>
$ python runserver.py # normal server
 \* Running on http://127.0.0.1:5000/
 ...
<br>
$ python runserver.py --debug # autoreload developer server
 \* Running on http://127.0.0.1:5000/
 \* Restarting with reloader
 ...
</code></pre>