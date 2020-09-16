# Start Flask

* [Jak psát web, návod na html stránky](https://www.jakpsatweb.cz/)
* [Flask docs](https://flask.palletsprojects.com)
* [Flask Quick start](https://flask.palletsprojects.com/quickstart/)
* [Template Designer Documentation](https://jinja.palletsprojects.com/templates/)

Zde najdete základní adresářovou strukturu pro aplikaci ve 
[Flasku](http://flask.pocoo.org/).

0. Dejme tomu že začínám nový projekt. Bude se jmenovat třeba *Foo*.
Můžete si [forknout](htts://help.github.com/articles/fork-a-repo/)
nebo prostě jen 
[naklonovat](https://help.github.com/articles/cloning-a-repository/)
tento repositář:


```bash
git clone https://github.com/spseol/startflask.git Foo
```

nebo 

```bash
git clone git@github.com:NICK/Foo.git
```

a potom:

```bash
cd Foo
```

1. Vytvořím si [virtuální prostředí](https://virtualenv.pypa.io/en/stable/)
   právě pro aplikaci *Foo*.:

```bash
python3 -m venv .venv-foo
```

2. Virtuální prostředí si aktivuji:

```bash
source venv-foo/bin/activate
```
nebo na Windows:
```
venv-foo\Scripts\activate

```

3. Do virtuálního prostředí nainstaluji potřebné moduly:

```bash
pip install flask flask-socketio
pip install flask-mail flask-misaka
pip install psycopg2 pony
```

4. A teď stačí spustit vývojový server:

```
./startapp.py
```
