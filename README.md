<p align="center">
  <a href="" rel="noopener">
 <img width=200px height=200px src="https://i.imgur.com/FxL5qM0.jpg" alt="SFP40Collector"></a>
</p>

<h3 align="center">SFP40Collector</h3>

<div align="center">

[![Status](https://img.shields.io/badge/status-active-success.svg)]()
[![License](https://img.shields.io/badge/license-MIT-blue.svg)](/LICENSE)

</div>

---

<p align="center"> 🤖 SFP40Collector est un logiciel de monitoring développer par M.Hicham SADDEK et M.Toufik MOUSSOUS dans le cadre <strong>Master Ingénierie des systèmes complexes</strong> afin de valider le projet du semestre 10, il fait partie du système développer <strong>SFP40Monitor</strong>, ce logiciel est un logiciel autonome de collecte de données afin d'assurer la collecte de données des serveurs OPC-UA. 
    <br> 
</p>

## 📝 Table of Contents

- [A propos](#about)
- [Demo](#demo)
- [Comment ça marche](#working)
- [Usage](#usage)
- [Première utilisation](#getting_started)
- [Déploiment du bot](#deployment)
- [Développer en utilisant](#built_using)
- [Contributions](../CONTRIBUTING.md)
- [Auteurs](#authors)

## 🧐 A Propos <a name = "about"></a>

🤖 SFP40Collector est un logiciel de monitoring développer par M.Hicham SADDEK et M.Toufik MOUSSOUS dans le cadre <strong>Master Ingénierie des systèmes complexes</strong> afin de valider le projet du semestre 10, il fait partie du système développer <strong>SFP40Monitor</strong>, ce logiciel est un logiciel autonome de collecte de données afin d'assurer la collecte de données des serveurs OPC-UA.

## 🎥 Demo <a name = "demo"></a>

![demoRobot](https://media.giphy.com/media/20NLMBm0BkUOwNljwv/giphy.gif)
Vous pouvez voir une démo du système en cliquant sur le lien suivant:
<a href="https://sfp40monitor.milebits.com">Lien de la démo</a>

## 💭 Comment àa marche ? <a name = "working"></a>

Le bot vous permets justement à collecter les données d'une infastructure locale qui n'a pas accès à internet de l'exterieur, il vous suffit justement de lui fournir de choses un lien de votre api SFP40Monitor et une clés secrète que le logiciel SFP40Monitor va vous fournir une fois que vous avez créer votre canal (Un tunel d'accès qui représente votre bot).
Le bot ensuite va se baser sur les configurations de votre logiciel SFP40Monitor pour faire ce que vous voulez :)
Ce bot est entièrement développer en Python 3.10

## 🎈 Utilisation <a name = "usage"></a>

Pour lancer votre bot, il vous suffit justement d'utiliser la commande dans votre invite de commande:

```bash
python launcher.py
```

## 🏁 Première utilisation <a name = "getting_started"></a>

Ces instruction vont vous permettre de faire une copie du bot sur une machine qui à accès libre au système que vous voulez monitorer. Pour plus d'information merci de voir la rubrique [Deploiment](#deployment) pour plus d'informations.

```bash
git clone https://github.com/hicham-saddek/sfp40-collector.git
cd sfp40-collector
```

### Prérequis

Vous aurez besoin d'avoir quelque prérequis afin de pouvoir lancer votre bot.

`Python` version `3.9` ou plus <br>
`aniso8601` version `9.0.1` ou plus <br>
`bson` version `0.5.10` ou plus <br>
`certifi` version `2021.10.8` ou plus <br>
`cffi` version `1.15.0` ou plus <br>
`charset-normalizer` version `2.0.12` ou plus <br>
`click` version `8.0.3` ou plus <br>
`colorama` version `0.4.4` ou plus <br>
`cryptography` version `36.0.1` ou plus <br>
`Flask` version `2.0.3` ou plus <br>
`Flask-Cors` version `3.0.10` ou plus <br>
`Flask-RESTful` version `0.3.9` ou plus <br>
`idna` version `3.3` ou plus <br>
`itsdangerous` version `2.0.1` ou plus <br>
`Jinja2` version `3.0.3` ou plus <br>
`lxml` version `4.8.0` ou plus <br>
`MarkupSafe` version `2.0.1` ou plus <br>
`opcua` version `0.98.13` ou plus <br>
`pycparser` version `2.21` ou plus <br>
`python-dateutil` version `2.8.2` ou plus <br>
`pytz` version `2021.3` ou plus <br>
`requests` version `2.27.1` ou plus <br>
`six version` `1.16.0` ou plus <br>
`urllib3` version `1.26.8` ou plus <br>
`Werkzeug` version `2.0.3` ou plus <br>
`wheel` version `0.37.1`ou plus <br>

## 🚀 Déploiment <a name = "deployment"></a>

Après avoir fait une copie du bot sur votre machine locale ( Voir la rubrique [Première utilisation](#getting_started) pour plus de détails), on installe tout premièrement un environnement virtuel Python afin d'isoler le bot.

```bash
python -m venv venv
```

Ensuite activer l'environnement virtuel
Pour les machines Linux ou MacOs

```bash
. /venv/bin/activate
```

Pour les machines Windows

```bash
.\venv\Scripts\activate
```

Ensuite configurer le lien de l'API ainsi que la clès secrète de votre bot (ça permet à l'API d'identifier votre bot) dans le fichier `config.json`. <br>
Ensuite lancer votre Bot

```bash
python launcher.py
```

Et vous êtes bon pour le reste.

## ⛏️ Développer avec <a name = "built_using"></a>

- [Python](https://python.org/) - Python
- [OPCUA](https://python-opcua.readthedocs.io/) - Python OPC-UA Documentation

## ✍️ Authors <a name = "authors"></a>

- [@hicham-saddek](https://github.com/hicham-saddek) - Responsable Technique
- [@toufik-moussous](https://github.com/hicham-saddek) - Responsable Ingénierie système
