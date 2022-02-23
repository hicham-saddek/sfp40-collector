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

<p align="center"> 🤖 SFP40Collector est un logiciel de monitoring développé par Hicham SADDEK et Toufik MOUSSOUS dans le cadre du Master Ingénierie des Systèmes Complexes, afin de valider le projet du semestre 10. SFP40Collector fait partie du système à développer "SFP4.0Monitor". Ce logiciel autonome permet d'assurer la collecte des données sur les serveurs OPC-UA.
    <br> 
</p>

## 📝 Sommaire

- [A propos](#about)
- [Demo](#demo)
- [Comment ça marche](#working)
- [Usage](#usage)
- [Première utilisation](#getting_started)
- [Déploiement du bot](#deployment)
- [Développer en utilisant](#built_using)
- [Auteurs](#authors)

## 🧐 A Propos <a name = "about"></a>

🤖 SFP40Collector est un logiciel de monitoring développé par Hicham SADDEK et Toufik MOUSSOUS dans le cadre du Master Ingénierie des Systèmes Complexes, afin de valider le projet du semestre 10. SFP40Collector fait partie du système à développer "SFP4.0Monitor". Ce logiciel autonome permet d'assurer la collecte des données sur les serveurs OPC-UA.

## 🎥 Demo <a name = "demo"></a>

![demoRobot](https://media.giphy.com/media/20NLMBm0BkUOwNljwv/giphy.gif)
Vous pouvez voir une démo du système en cliquant sur le lien suivant:
<a href="https://sfp40monitor.milebits.com">Lien de la démo</a>

## 💭 Comment ça marche ? <a name = "working"></a>

Une fois votre canal configuré et créé, vous devrez <strong>copier</strong> la clé secrète générée par le logiciel <strong>SFP4.0 Monitor</strong>, et la <strong>coller</strong> dans le fichier de configuration `config.json` au niveau de 
```json
{
  "api": "Votre lien API",
  "key": "Votre clé secrète"
}
```
Le bot va ensuite s'occuper de tout.

Ce bot est entièrement développer en Python 3.10

## 🎈 Utilisation <a name = "usage"></a>

Pour lancer votre bot, il vous suffit d'utiliser la commande dans votre invite de commande :

```bash
python launcher.py
```

## 🏁 Première utilisation <a name = "getting_started"></a>

Ces instructions vont vous permettre de faire une copie du bot sur une machine qui a accès libre au système que vous voulez monitorer. Pour plus d'informations, merci de voir la rubrique [Deploiement](#deployment).

```bash
git clone https://github.com/hicham-saddek/sfp40-collector.git
cd sfp40-collector
```

## 🚀 Déploiement <a name = "deployment"></a>

Après avoir fait une copie du bot sur votre machine locale (voir la rubrique [Première utilisation](#getting_started) pour plus de détails), on installe tout premièrement un environnement virtuel Python afin d'isoler le bot.

```bash
python -m venv venv
```

Ensuite activer l'environnement virtuel
Pour les machines Linux ou MacOS

```bash
. /venv/bin/activate
```

Pour les machines Windows

```bash
.\venv\Scripts\activate
```

Ensuite installer les librairies python nécessaires, avec la commande suivante:
```bash
pip install -r req.txt
```
Ensuite configurer le lien de l'API ainsi que la clé secrète de votre bot (cela permet à l'API d'identifier votre bot) dans le fichier `config.json`. <br>
Ensuite lancez votre Bot

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
