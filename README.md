# Portfolio
Mon Portfolio

Le site est accessible via ce [Lien ](https://raykesh-soneka.github.io/Portfolio/Le_Site_De_Raykesh)

Documentation : 
==========

### I. Architecture Du site

Page Principale 
- Le site est composé de 3 sections : Header, Main et Footer.
- Le Header contient le logo du site et un bouton de navigation vers la page principale
- Le Main contient les informations du site et les liens vers les autres pages du site.
- Le Footer contient les informations de contact, les liens vers les réseaux sociaux et les autre pages du site


> [!NOTE]
> Cette partie n'est sûrement pas encore MAJ.

#### II. Fonctionalité qui sont implémenter et qui peuvent être tester


```sh
$ ls -R -a
```
Footer :octocat: :neckbeard: :bowtie: :shipit:

## Code : Explication / démonstration 
-----------------------------

### HTML

le html est basic avec des classes ( pas de css intégré ).
Le code à aussi des ra
```html
<!-- ul>(a>li)*3 -->
<ul>...
<!-- div.item*5 -->
...<div class="item">
<!-- .Colonne*3>h3+p*3 -->
...<div class="Colonne">
```

### CSS

Le CSS est dans un fichier à part et dispose d'une partie réactive. Le `z-index` permet de corriger le bug de l'element nav qui passe en dessous de l'image.


### JS

Le JS est à l'heure actuelle dans une balise script

### Déploiment

Le Déploiment est un déploiment standard sur GitHub avec GitHub Pages suivi d'une redirection d'URL automatique grâce à `window.location.replace("")`.
