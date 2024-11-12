# Portfolio
Mon Portfolio

Le site est accessible via ce [Lien qui fait une Redirection d'URL vers mon site](https://raykesh-soneka.github.io/Portfolio/Le_Site_De_Raykesh)

Documentation : 
==========

### I. Architecture Du site

Page Principale 
- Le site est composé de 3 sections : Header, Main et Footer.
- Le Header contient le logo du site et un bouton de navigation vers la page principale
- Le Main contient les informations du site et les liens vers les autres pages du site.
- Le Footer contient les informations de contact, les liens vers les réseaux sociaux et les autres pages du site

Pages Cyber 
-Caché / Sécurité par Obfuscation

> [!NOTE]
> Cette partie n'est sûrement pas encore MAJ.

#### II. Fonctionalité qui sont implémenter et qui peuvent être tester


```sh
$ ls -R -a
```
Footer :octocat: :neckbeard: :bowtie: :shipit:

## Code : Explication / démonstration 
-----------------------------

### HTML [![My Skills](https://skillicons.dev/icons?i=html)](https://skillicons.dev)

le html est basic avec des classes ( pas de css intégré ).
Le code à aussi des raccourcis
```html
<!-- ul>(a>li)*3 -->
<ul>...
<!-- div.item*5 -->
...<div class="item">
<!-- .Colonne*3>h3+p*3 -->
...<div class="Colonne">
```

### CSS [![My Skills](https://skillicons.dev/icons?i=css)](https://skillicons.dev)

Le CSS est dans un fichier à part et dispose d'une partie réactive. Le `z-index` permet de corriger le bug de l'élément nav qui passe en dessous de l'image.
```CSS
@import '../style.css';  
/* Style css de base ↑ */
/* Style css override/surcharger ↓ */

body{
    background-color: none;
} 

```

### JS [![My Skills](https://skillicons.dev/icons?i=js)](https://skillicons.dev)

Le JS est à l'heure actuelle dans une balise script

```JS
var path = window.location.pathname;  // Le chemin actuel de la page
var page = path.split("/").pop();   // Le nom de la page actuelle
document.title  = " |" + page + "| Raykesh: Bienvenue dans mon protfolio.";//Le titre de la page
console.log(" Le titre de la page est : " + document.title);// Affiche le titre dans la console
console.log( page );   // Affiche le nom de la page actuelle dans la console

```

### Déploiment

Le Déploiement est un déploiement standard sur GitHub avec GitHub Pages suivi d'une redirection d'URL automatique grâce à `window.location.replace("")`.

<details>
<summary>:eyes: Montrer les Statistiques GitHub de Raykesh : </summary>

![Raykesh GitHub stats 1](https://github-readme-stats.vercel.app/api?username=Raykesh-Soneka\&show_icons=true\&bg_color=00000000\&locale=fr)
![Raykesh GitHub stats 2](https://github-readme-stats.vercel.app/api?username=RaykeshR\&show_icons=true\&bg_color=00000000\&locale=fr)

</details>
