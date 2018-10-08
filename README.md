# FlaskTree

Zde najdete základní adresářovou strukturu pro aplikaci ve 
[Flasku](http://flask.pocoo.org/).

Dejme tomu že začínám nový projekt. Bude se jmenovat třeba *Kokos*.

* Vytvořím si pro něj adresář a vše ostatní se bude dít uvnitř tohoto adresáře.

```bash
mkdir kokos
cd kokos
```

1. Vytvořím si [virtuální prostředí](https://virtualenv.pypa.io/en/stable/)
   právě pro aplikaci *Kokos*.:

```bash
python3 -m venv .venv
```

2. Virtuální prostředí si aktivuji:

```bash
source venv_kokos/bin/activate
```
nebo na Windows:
```
venv_kokos\Scripts\activate

```

3. Do virtuálního prostředí nainstaluji potřebné moduly:

```bash
pip install flask flask-socketio
pip install flask-mail flask-markdown
pip install psycopg2 pony
```

4. Vytvoříte si adresářovou strukturu:

```bash
make-flask-tree.sh webface
```

5. Inicializujte si Git repositář nahrajte svou práci 
   do [nového prázdného repositáře](https://github.com/new) 
   na GitHubu.

   GitHub vám napoví co dělat. Příkazy můžou vypadat třeba takto:

```bash
git init
git add 'run-*.py' webface
git commit -m "Init commit"
git remote add origin git@github.com:GitHubNick/kokos.git
git push -u origin master
```

