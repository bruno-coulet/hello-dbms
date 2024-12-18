# <span style="color:gray">hello-dbms</span>

## <span style="color:skyblue"> Sommaire</span>
- [Contexte](#contexte)
- [Veille scientifique](#veille-scientifique)
  - [A. Qu'est-ce qu'une donnée ? Sous quelle forme peut-elle se présenter ?](#a-quest-ce-quune-donnee)
  - [B. Donnez et expliquez les critères de mesure de qualité des données.](#b-criteres-de-qualite)
  - [C. Définissez et comparez les notions de Data Lake, Data Warehouse et Lake House. Illustrez les différences à l’aide de schémas.](#c-data-lake-vs-data-warehouse)
  - [D. Donnez une définition et des exemples de systèmes de gestion de bases de données avec des illustrations.](#d-systemes-de-gestion)
  - [E. Qu'est-ce qu'une base de données relationnelle ? Qu'est-ce qu'une base de données non relationnelle ? Donnez la différence entre les deux avec des exemples d'applications.](#e-bases-relationnelles-vs-non-relationnelles)
  - [F. Définissez les notions de clé étrangère et clé primaire.](#f-cles-etrangeres-et-cles-primaires)
  - [G. Quelles sont les propriétés ACID ?](#g-proprietes-acid)
  - [H. Définissez les méthodes Merise et UML. Quelles sont leur utilité dans le monde de l'informatique ? Donnez des cas précis d'utilisation avec des schémas.](#h-methodes-merise-et-uml)
  - [I. Définissez le langage SQL. Donnez les commandes les plus utilisées de ce langage et les différentes jointures qu'il est possible de faire.](#i-langage-sql-commandes)
- [Conclusion](#conclusion)

## <span style="color:skyblue"> Contexte <a id="contexte"></a></span>


"""""""""""""""""""

""""

""""""

## <span style="color:skyblue"> Veille scientifique <a id="veille-scientifique"></a></span>

###  <span style="color:#9bf0a6">A.</span><span style="color:#aa9bf0"> Qu'est-ce qu'une donnée ? Sous quelle forme peut-elle se présenter ? <a id="a-quest-ce-quune-donnee"></a></span>

<span style="color:#178a6e"><u>**Etymologie :**</u> </span>

Etymologiquemen, le terme donnée provient du latin *datum* signifiant " donner " .

Cependant, comme le soulève Jenser en 1950, l'histoire aurait dû retenir *capere*, soit " capturer ". En effet, pour la science il s'agit de sélecitonner, de capturer dans l'existant plutôt que de comprendre la donnée comme quelque-chose de préalablement " donné ". 

Cette différence historique met en évidence le caractère sélectif et partiel, voir réductionniste, inhérent à la donnée. 

<span style="color:#178a6e"><u>**Définitions :**</u> </span>
* 1 GLOBALE :

<span style="color:#95b5ad">Fait ou principe </span>**indiscuté**<span style="color:#95b5ad">, ou considéré comme tel, sur lequel se fonde un</span> **raisonnement**<span style="color:#95b5ad"> ; constatation servant de base à un examen, une recherche, une découverte.</span>

* 2 PSYCHOLOGIE : 

<span style="color:#95b5ad">Ce qui est</span> **connu immédiatement**<span style="color:#95b5ad"> par le sujet, indépendamment de toute élaboration de l'esprit, par opposition à ce qui est connu par induction ou déduction, par raisonnement, par calcul.</span>

* 3 MATHEMATIQUES :

<span style="color:#95b5ad">Souvent au pluriel. Chacune des</span> **quantités ou propriétés**<span style="color:#95b5ad"> mentionnées dans l'énoncé d'un problème et qui permettent de le résoudre.</span> 

* 4 INFORMATIQUE :

<span style="color:#95b5ad">Représentation d'une</span>  **information sous une forme conventionelle** <span style="color:#95b5ad">adaptée à son exploitation.</span> 

<span style="color:#178a6e"><u>**En résumé :**</u> </span>

Une donnée est ce qui est connu et qui sert de point de départ à un raisonnement ayant pour objet la détermination d'une solution à un problème en relaiton avec cette donnée. Cela peut être une description élémentaire qui vise à objectiver une réalité, le résultat d'une comparaison entre deux événements du même ordre (mesure) soit en d'autres termes une observation ou une mesure. 

La donnée brute est dépourvue de tout raisonnement, supposition, constatation, probabilité.

Si elle est considérée comme indiscutable ou même si elle est indiscutée par méconnaissance, elle peut servir de base à une recherche, à un examen quelconque. 

La nature des données pouvant différer en fonction de leur source, elles doivent souvent faire l'objet d'une transformation préalable avant traitement. 

La technique contemporaine est la quatification numérique dans un système binaire, associée à des machines de traitement à deux états de fonctionnement. Cela veut dire que le monde réel est vu par des capteurs dont la réponse continue ou discrète est traduite en nombres qui sont traités, c'est à dire traduits, par des ordinateurs. 

Un travail est souvent fait sur les données burtes pour leur donner un sens, plus précisément un contexte, afin de pouvoir les transformer en information. 

Les données peuvent être : 

* Des résultats de mesure fonction d'un étalon de référence pouvant, associé à la manire de traiter les données, générer des biais sur l'interprétations finale (limites des sondages).

* Des valeurs discrètes représentant l'état d'un système. 

* Des informations logiques représentant un contexte non réel. 

* ... 

Le résultat du traitement sera souvent *in fine* soumis à l'interprétation d'un être humain et devra de ce fait être présenté sous forme adéquate, par exemple un graphique ou une liste de choix, pour donner un sens (interprétation) et ainsi créer une nouvelle information. 

<span style="color:#178a6e"><u>**La valeur des données :**</u> </span>

La valorisation de la donnée s fait à travers un processus capable à cahque étape de la transformation d'augmenter sa vlaeur directement ou par combinaison avec d'autres données. En général la finalité est l'exploitation par l'homme por la price de décision ou par un autre système permettant une commande de processus. 

Le calcul fait partie du processus de transformation par la machine et le jugement qualitatif qui appartient à l'humain fait partie de l'interprétation et donne la valeur objective à l'information finale. 

Simon Chignard et Louis-David Benyayer ont essayé de créer une grille de lecture pour la quatification des données en partant de trois conceptions de la valeur : 

* 1. La valeur est subjective : elle dépend de l'intérêt porté par l'humain qui va l'utiliser directement ou après transformation. 

* 2. La valeur est co-construire : elle augmente à partir de l'instant ou elle rentre dans un processus de transformation, notemment à travers des études croisées, capables d'exprimer des concerpt, d'où l'importance de la collaboration et de la cooridnation dans le processus de la valorisation des données.

* 3. La valeur est potentielle : elle donne ou pas un avantage futur à ceux qui la détiennent. 

A parti de ces axiomes, les données peuvent être interprétées à la lumire de trois formes de valeur. 

**Les données comme matière première**

zefgzfazdadazdazd
azdazdazd
azdazd

**Les données comme levier**

adzzadazdazdazd

**Les données comme actif stratégique**

cazczeczeczecezczecececzed

### <span style="color:#9bf0a6">B.</span> Donnez et expliquez les critères de mesure de qualité des données. <a id="b-criteres-de-qualite"></a>

### <span style="color:#9bf0a6">C.</span> Définissez et comparez les notions de Data Lake, Data Warehouse et Lake House. Illustrez les différences à l’aide de schémas. <a id="c-data-lake-vs-data-warehouse"></a>

### <span style="color:#9bf0a6">D.</span> Donnez une définition et des exemples de systèmes de gestion de bases de données avec des illustrations. <a id="d-systemes-de-gestion"></a>

### <span style="color:#9bf0a6">E.</span> Qu'est-ce qu'une base de données relationnelle ? Qu'est-ce qu'une base de données non relationnelle ? Donnez la différence entre les deux avec des exemples d'applications. <a id="e-bases-relationnelles-vs-non-relationnelles"></a>

### <span style="color:#9bf0a6">F.</span> Définissez les notions de clé étrangère et clé primaire. <a id="f-cles-etrangeres-et-cles-primaires"></a>

### <span style="color:#9bf0a6">G.</span> Quelles sont les propriétés ACID ? <a id="g-proprietes-acid"></a>

### <span style="color:#9bf0a6">H.</span> Définissez les méthodes Merise et UML. Quelles sont leur utilité dans le monde de l'informatique ? Donnez des cas précis d'utilisation avec des schémas. <a id="h-methodes-merise-et-uml"></a>

### <span style="color:#9bf0a6">I.</span> Définissez le langage SQL. Donnez les commandes les plus utilisées de ce langage et les différentes jointures qu'il est possible de faire. <a id="i-langage-sql-commandes"></a>

## <span style="color:skyblue">Conclusion <a id="conclusion"></a></span>
