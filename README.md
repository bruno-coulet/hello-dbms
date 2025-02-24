# <span>HELLO-DBMS</span>

## <span> Sommaire</span>
- [Contexte](#contexte)
- [ Schéma et utilisation de l'application](#app-schema)
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

## <span> Contexte <a id="contexte"></a></span>


Aujourd’hui, les données sont partout : elles guident nos décisions, alimentent nos applis et transforment nos métiers. Mais avant de manipuler ces données, il faut en comprendre les bases. Ce projet est là pour ça !

On y explore tout ce qu’il faut savoir : qu’est-ce qu’une donnée, comment évaluer sa qualité, où et comment on les stocke, et quels outils utiliser pour les gérer efficacement. On va aussi parler de bases de données (relationnelles et non relationnelles), d’architectures comme le Data Lake ou le Data Warehouse, et même de méthodes comme Merise et UML. Bref, tout ce qu’il faut pour avoir une vision claire et structurée, avec des exemples et des schémas pour rendre ça concret et compréhensible.

## <span> Schéma et utilisation de l'application <a id="app-schema"></a></span>

| Dossier/Fichier                | Description                                      |
|--------------------------------|--------------------------------------------------|
| HELLO-DBMS                     | Racine du projet                                 |
| ├── carbon_footprin_app        | Dossier de l'application principale              |
| │   ├── templates              | Dossier des templates HTML                       |
| │   │   ├── ***.html           | Fichiers HTML pour les templates de l'application|
| │   ├── app.py                 | Script principal de l'application                |
| │   └── config.py              | Fichier de configuration de l'application        |
| ├── data_analysis              | Dossier pour l'analyse de données                |
| │   └── first_analyse.sql      | Script SQL pour la première analyse de données   |
| ├── database_manager           | Dossier pour la gestion de la base de données    |
| │   ├── config.py              | Fichier de configuration pour la gestion de la base de données |
| │   ├── data_processing.py     | Script pour le traitement des données            |
| │   ├── database.py            | Script pour les opérations de base de données    |
| │   ├── insert_data.py         | Script pour insérer des données dans la base de données |
| │   └── main.py                | Script principal pour la gestion de la base de données |
| ├── jobs                       | Dossier pour les scripts de jobs                 |
| │   ├── job1.sql               | Script SQL pour un job spécifique                |
| │   ├── ...                    | D'autres scripts SQL pour différents jobs        |
| ├── pre_processed_data         | Dossier pour les données pré-traitées            |
| │   ├── country.csv            | Données pré-traitées pour les pays               |
| │   └── world.csv              | Données pré-traitées pour le monde               |
| ├── raw_data                   | Dossier pour les données brutes                  |
| │   └── carbon-footprint-data.csv | Données brutes sur l'empreinte carbone        |
| ├── .gitignore                 | Fichier pour ignorer certains fichiers dans Git  |
| ├── README.md                  | Fichier de documentation du projet               |
| ├── requirements.txt           | Fichier listant les dépendances du projet        |
| ├── .env                       | Fichier d'environnement (ignoré mais nécessaire) |
| └── app.log                    | Fichier de log (ignoré mais généré au lancement de l'application) |

Pour pouvoir lancer l'application, il faut nécessairement :
* Avoir MySQL pour la création de la DB et la génération automatique des tables
* Avoir dans le dossier pre_processed_data
  * Un fichier de données au format CSV nommé country ayant comme structure 

  | Colonne     | Description                                                                 |
  |-------------|-----------------------------------------------------------------------------|
  | Country     | Le nom du pays                                                              |
  | Coal        | Pourcentage d'utilisation du charbon                                        |
  | Gas         | Pourcentage d'utilisation du gaz naturel                                    |
  | Oil         | Pourcentage d'utilisation du pétrole                                        |
  | Hydro       | Pourcentage d'utilisation de l'énergie hydroélectrique                      |
  | Renewable   | Pourcentage d'utilisation des énergies renouvelables (solaire, éolienne, etc.) |
  | Nuclear     | Pourcentage d'utilisation de l'énergie nucléaire |

  * Un fichier de données au format CSV nommé wolrd ayant comme structure

  | Colonne                     | Description                                                                 |
  |-----------------------------|-----------------------------------------------------------------------------|
  | World                       | Le nom de la région                                                         |
  | Coal                        | Pourcentage d'utilisation du charbon                                        |
  | Gas                         | Pourcentage d'utilisation du gaz naturel                                    |
  | Oil                         | Pourcentage d'utilisation du pétrole                                        |
  | Hydro                       | Pourcentage d'utilisation de l'énergie hydroélectrique                      |
  | Renewable                   | Pourcentage d'utilisation des énergies renouvelables (solaire, éolienne, etc.) |
  | Nuclear                     | Pourcentage d'utilisation de l'énergie nucléaire                            |

* Indiquer dans un fichier .env dans le dossier principal les informations pour la connexion à la db MySQL suivantes :  
  * DB_HOST=****
  * DB_USER=****
  * DB_PASSWORD=****
  * DB_NAME=carbon_footprint

Ensuite : 
* Lancer le script main.py situé dans le dossier database_manager qui créera automatiquement les tables graces aux données des fichiers présents dans pre_processed_data.
* Lancer l'application de data visualisation via le script app.py dans le dossier carbon_footprint_app


## <span> Veille scientifique <a id="veille-scientifique"></a></span>

###  <span>A.</span><span> Qu'est-ce qu'une donnée ? Sous quelle forme peut-elle se présenter ? <a id="a-quest-ce-quune-donnee"></a></span>

<img src="https://3.bp.blogspot.com/-rlfbTrL2prE/Wx6N-BeZjYI/AAAAAAAAA3k/lL0rYDbGqGgTH4cSQNh9MbkCTvNremG6gCLcBGAs/s1600/data_1.jpg" alt="DATA" style="width:500px;"/>

<span><u>**Etymologie :**</u> </span>

Étymologiquemen, le terme donnée provient du latin *datum* signifiant " donner " .

Cependant, comme le soulève Jenser en 1950, l'histoire aurait dû retenir *capere*, soit " capturer ". En effet, pour la science il s'agit de sélecitonner, de capturer dans l'existant plutôt que de comprendre la donnée comme quelque-chose de préalablement " donné ". 

Cette différence historique met en évidence le caractère sélectif et partiel, voir réductionniste, inhérent à la donnée. 

<span><u>**Définitions :**</u> </span>
* 1 GLOBALE :

<span>Fait ou principe </span>**indiscuté**<span>, ou considéré comme tel, sur lequel se fonde un</span> **raisonnement**<span> ; constatation servant de base à un examen, une recherche, une découverte.</span>

* 2 PSYCHOLOGIE : 

<span>Ce qui est</span> **connu immédiatement**<span> par le sujet, indépendamment de toute élaboration de l'esprit, par opposition à ce qui est connu par induction ou déduction, par raisonnement, par calcul.</span>

* 3 MATHEMATIQUES :

<span>Souvent au pluriel. Chacune des</span> **quantités ou propriétés**<span> mentionnées dans l'énoncé d'un problème et qui permettent de le résoudre.</span> 

* 4 INFORMATIQUE :

<span>Représentation d'une</span>  **information sous une forme conventionelle** <span>adaptée à son exploitation.</span> 

<span><u>**En résumé :**</u> </span>

Une donnée est ce qui est connu et qui sert de point de départ à un raisonnement ayant pour objet la détermination d'une solution à un problème en relation avec cette donnée.
Cela peut être une description élémentaire qui vise à objectiver une réalité, le résultat d'une comparaison entre deux événements du même ordre (mesure) soit en d'autres termes une observation ou une mesure. 

La donnée brute est dépourvue de tout raisonnement, supposition, constatation, probabilité.

Si elle est considérée comme indiscutable ou même si elle est indiscutée par méconnaissance, elle peut servir de base à une recherche, à un examen quelconque. 

La nature des données pouvant différer en fonction de leur source, elles doivent souvent faire l'objet d'une transformation préalable avant traitement. 

La technique contemporaine est la qualification numérique dans un système binaire, associée à des machines de traitement à deux états de fonctionnement. Cela veut dire que le monde réel est vu par des capteurs dont la réponse continue ou discrète est traduite en nombres qui sont traités, c'est à dire traduits, par des ordinateurs. 

Un travail est souvent fait sur les données brutes pour leur donner un sens, plus précisément un contexte, afin de pouvoir les transformer en information. 

Les données peuvent être : 

* Des résultats de mesure fonction d'un étalon de référence pouvant, associé à la manière de traiter les données, générer des biais sur l'interprétations finale (limites des sondages).

* Des valeurs discrètes représentant l'état d'un système. 

* Des informations logiques représentant un contexte non réel. 

* ... 

Le résultat du traitement sera souvent *in fine* soumis à l'interprétation d'un être humain et devra de ce fait être présenté sous forme adéquate, par exemple un graphique ou une liste de choix, pour donner un sens (interprétation) et ainsi créer une nouvelle information. 

<span><u>**La valeur des données :**</u> </span>

La valorisation de la donnée se fait à travers un processus capable à chaque étape de la transformation d'augmenter sa valeur directement ou par combinaison avec d'autres données. En général la finalité est l'exploitation par l'homme pour la prise de décision ou par un autre système permettant une commande de processus. 

Le calcul fait partie du processus de transformation par la machine et le jugement qualitatif qui appartient à l'humain fait partie de l'interprétation et donne la valeur objective à l'information finale. 

Simon Chignard et Louis-David Benyayer ont essayé de créer une grille de lecture pour la qualification des données en partant de trois conceptions de la valeur : 

1. La valeur est subjective : elle dépend de l'intérêt porté par l'humain qui va l'utiliser directement ou après transformation. 

2. La valeur est co-construire : elle augmente à partir de l'instant ou elle rentre dans un processus de transformation, notemment à travers des études croisées, capables d'exprimer des concepts, d'où l'importance de la collaboration et de la coordination dans le processus de la valorisation des données.

3. La valeur est potentielle : elle donne ou pas un avantage futur à ceux qui la détiennent. 

A partir de ces axiomes, les données peuvent être interprétées à la lumière de trois formes de valeur. 


### <span>B.</span> Donnez et expliquez les critères de mesure de qualité des données. <a id="b-criteres-de-qualite"></a>

<img src="https://datavalue-consulting.com/wp-content/uploads/2021/10/Criteres-qualite-donnees.png" alt="Mesure qualité" style="width:500px;"/>

Les critères de mesure de la qualité des données permettent de s'assurer que les données sont fiables, précises et utilisables, en d'autres termes, de maximiser la valeur des données pour l'organisation afin de s'assurer qu'elles peuvent être utilisées efficacement pour des analyses et prises de décisions. 

<span><u>**1. Exactitude (précision) :**</u></span>

  * Les données doivent refléter correctement la réalité.   
    * Par exemple, un chffre d'affaire incorrect fausserait les analyses finnancières.

<span><u>**2. Complétude :**</u></span>
  
  * Les données doivent être complètes et ne pas contenir de champs vides lorsque ces informations sont essentielles. 
    * Par exemple, une base de données de clients sans adresses email serait incomplète pour une campagne marketing par courriel.  

<span><u>**3. Cohérence :**</u></span> 

  * Les données doivent être cohérentes entre différentes systèmes et bases de données. 
    * Par exemple, un même produit ne devrait pas avoir des prix différents dans deux bases de données différentes. 

<span><u>**4. Actualité :**</u></span> 

  * Les données doivent être à jour pour le moment présent. 
    * Des informations obsolètes peuvent entraîner des décisions inappropriées.

<span><u>**5. Pertinence :**</u></span>

  * Les données doivent être pertinentes et adaptées aux besoins de l'utilisateur. 
    * Par exemple, pour une analyse des ventes, seules les données pertinentes aux ventes doivent être incluses.

<span><u>**6. Accessibilité :**</u></span>

  * Les données doivent petre facilement accessibles et compréhensibles pour les utilisateurs autorisés. 
    * Une mauvaise accessibilité peut freiner les opérations et analyses.

<span><u>**7. Traçabilité :**</u></span>

  * Il doit être possible de retracer l'origine et les modifications apportées aux données pour garentir leur intégrité et leur fiabilité. 
    * Par exemple, pour garantir la sécurité et la qualité de produits d'une entreprise de produits alimentaires, elle doit pouvoir retracer l'origine de chaque ingrédient utilisé dans la fabrication. 


### <span>C.</span> Définissez et comparez les notions de Data Lake, Data Warehouse et Lake House. Illustrez les différences à l’aide de schémas. <a id="c-data-lake-vs-data-warehouse"></a>

<span><u>**Data Lake :**</u></pan>

Un **data lake** est un système de stockage de données brutes, non structurées ou semi-structurées, à leur échelle d'origine.

Il donne la priorité au stockage rapide et volumineux de données hétérogènes en adoptant une architecture en cluster (grappe de calcul), qui est une approche d'architecture distribuée où un ensemble d'ordinateurs étroitement connectés travaillent ensemble et son vus comme un seul ordinateur par l'utilisateur.

Il n'est pas optimisé pour les requêtes SQL comme les SGBD relationnels classiques, et s'écarte des propriétés ACID traditionnelles. On parle depuis 2010 de SGBD NoSQL.

<span><u>**Data Warehouse :**</u></pan>

Une **data warehouse** (entrepôt de données ou base de données décisionnelle) désigne une base de données utilisée pour collecter, ordoner, journaliser et stocker des informations provenant de base de données opérationnelles et fournir ainsi un socle à l'aide à la décision en entreprise. 

<span><u>**Lake House :**</u></pan>

Un **data lake house** est un système de gestion des données qui combine les avantages des lacs de données et des entrpôts de données. 

Il fournit des capacités de stockage et de traitement évolutive pour les organisaitons modernes qui souhaitent éviter un système isolé pour le traitement de différentes charges de travail, telles que le Machine Learning (ML) et le décisionnel (BI). 

Il permet d'établir une source unique de vérité, d'éliminer les côuts redondants et de garantir l'actualisation des données. 

Il utilise souvent un modèle de conception de données qui améliore, enrichit et affine les données de façon incrémentielle au fur et à mesure qu'elles passent par des couches de mise en lots de transformation. (Architecture en médaillon)


<span><u>**Illustration des différences clés :**</u></pan>

| Type de stockage | Description | Utilisation | Avantages | Inconvénients |
|------------------|-------------|-------------|-----------|---------------|
| **Data Lake**    | Données brutes, non structurées ou semi-structurées | Analyse de données massives, machine learning | Flexibilité, coût réduit | Complexité de gestion, qualité des données variable |
| **Data Warehouse** | Données structurées, organisées en tables et schémas | Reporting, Business Intelligence | Performance, qualité des données | Coût élevé, moins flexible |
| **Lake House**   | Combinaison de données brutes et structurées | Analyse avancée, machine learning, reporting | Flexibilité, performance, qualité des données | Complexité de mise en œuvre |


### <span>D.</span> Donnez une définition et des exemples de systèmes de gestion de bases de données avec des illustrations. <a id="d-systemes-de-gestion"></a>

Un système de gestion de bases de données (SGBD) est un logiciel qui permet de créer, gérer et manipuler des bases de données. Il offre des outils pour stocker, récupérer, modifier et supprimer des données de manière efficace et sécurisée.

  <div style="text-align: center;">
   <img src="https://sgbd.developpez.com/tutoriels/cours-complet-bases-de-donnees/images/42_img01.jpg" alt="Architecture type SGBD" style="width:450px;"/>
  </div>

<span><u>**Exemples de SGBD**</u></span>

1. **MySQL**
   - **Description** : SGBD relationnel open-source très utilisé pour les applications web.

   <img src="https://upload.wikimedia.org/wikipedia/commons/0/0a/MySQL_textlogo.svg" alt="MySQL" style="width:200px;"/>

2. **PostgreSQL**
   - **Description** : SGBD relationnel open-source connu pour sa robustesse et ses fonctionnalités avancées.

   <img src="https://upload.wikimedia.org/wikipedia/commons/2/29/Postgresql_elephant.svg" alt="PostgreSQL" style="width:200px;"/>

3. **MongoDB**
   - **Description** : SGBD NoSQL orienté documents, idéal pour les applications nécessitant une grande flexibilité des données.

   <img src="https://upload.wikimedia.org/wikipedia/fr/thumb/4/45/MongoDB-Logo.svg/791px-MongoDB-Logo.svg.png?20190421175613" alt="MongoDB" style="width:200px;"/>

4. **Oracle Database**
   - **Description** : SGBD relationnel commercial très performant, utilisé par de grandes entreprises pour des applications critiques.

   <img src="https://upload.wikimedia.org/wikipedia/commons/5/50/Oracle_logo.svg" alt="Oracle" style="width:200px;"/>

5. **Microsoft SQL Server**
   - **Description** : SGBD relationnel commercial développé par Microsoft, utilisé pour des applications d'entreprise.

   <img src="https://upload.wikimedia.org/wikipedia/commons/8/87/Sql_data_base_with_logo.png" alt="SQL Server" style="width:200px;"/>



### <span>E.</span> Qu'est-ce qu'une base de données relationnelle ? Qu'est-ce qu'une base de données non relationnelle ? Donnez la différence entre les deux avec des exemples d'applications. <a id="e-bases-relationnelles-vs-non-relationnelles"></a>

<span><u>**Bases de Données Relationnelles et Non Relationnelles :**</u></span>

* **Base de Données Relationnelle :** Une base de données relationnelle (SGBDR) est un type de base de données qui organise les données en tables, où chaque table est composée de lignes et de colonnes. Les relations entre les tables sont définies par des clés étrangères. Les SGBDR utilisent le langage SQL (Structured Query Language) pour interroger et manipuler les données.

  * Exemples de SGBDR
    - **MySQL** : Utilisé pour les applications web, comme les sites de commerce électronique et les blogs.
    - **Oracle Database** : Utilisé par les grandes entreprises pour les applications critiques, comme les systèmes de gestion des ressources humaines et les systèmes financiers.

* **Base de Données Non Relationnelle :** Une base de données non relationnelle (NoSQL) est un type de base de données qui ne suit pas le modèle tabulaire des bases de données relationnelles. Les données peuvent être stockées sous forme de documents, de paires clé-valeur, de colonnes ou de graphes. Les bases de données NoSQL sont conçues pour gérer des volumes massifs de données non structurées ou semi-structurées.

  * Exemples de bases de données NoSQL
    - **MongoDB** : Utilisé pour les applications nécessitant une grande flexibilité des données, comme les plateformes de réseaux sociaux et les applications mobiles.
    - **Cassandra** : Utilisé pour les applications de big data, comme les systèmes de recommandation et les analyses en temps réel.


<span><u>**Différences entre bases de données relationnelles et non relationnelles :**</u></span>

| Caractéristique       | Base de données relationnelle | Base de données non relationnelle |
|-----------------------|-------------------------------|-----------------------------------|
| **Modèle de données** | Tables avec lignes et colonnes | Documents, paires clé-valeur, colonnes, graphes |
| **Langage de requête**| SQL                           | Langages spécifiques à chaque SGBD NoSQL |
| **Schéma**            | Schéma fixe et rigide         | Schéma flexible et dynamique      |
| **Scalabilité**       | Scalabilité verticale (ajout de ressources à un seul serveur) | Scalabilité horizontale (ajout de serveurs supplémentaires) |
| **Cas d'utilisation** | Applications transactionnelles, systèmes de gestion d'entreprise | Applications nécessitant une grande flexibilité des données, big data, applications en temps réel |

<img src="https://th.bing.com/th/id/R.155a9e4413a56fdd4b210f68e4dbf0c1?rik=M6AYCE3MIpZ8zA&riu=http%3a%2f%2finfodecisionnel.com%2fwp-content%2fuploads%2f2014%2f06%2fcomparaison_SQL_NoSQL_BDD1.jpg&ehk=RIdVmJCGKajLpVOunuYKjTGf0RSyoHyoIb30bEATQek%3d&risl=&pid=ImgRaw&r=0" alt="SGBDR/NoSQL" style="width:500px;"/>

<span><u>**Les différents modèles de bases de données :**</u></span>

Il existe cinq modèles de SGBD, différenciées selon la représentation des données qu'elle contient :

* **Le modèle hiérarchique :** Les données sont classées hiérarchiquement, selon une arborescence descendante. Ce modèle utilise des pointeurs entre les différents enregistrements. Il s'agit du premier modèle de SGDB.

   <img src="https://web.maths.unsw.edu.au/~lafaye/CCM/bdd/images/hierarch.gif" alt="Modèle Hiérarchique" style="width:200px;"/>

* **Le modèle réseau :** Comme le modèle hiérarchique ce modèle utilise des pointeurs vers des enregistrements. Toutefois la structure n'est plus forcément arborescente dans le sens descendant. 

   <img src="https://web.maths.unsw.edu.au/~lafaye/CCM/bdd/images/reseau.gif" alt="Modèle Réseau" style="width:200px;"/>

* **Le modèle relationnel (SGBDR): ** Les données sont enregistrées dans des tableaux à deux dimensions. La manipulation de ces données se fait selon la théorie mathématique des relations. 

   <img src="https://web.maths.unsw.edu.au/~lafaye/CCM/bdd/images/relation.gif" alt="SGBDR" style="width:200px;"/>

* **Le modèle déductif :** Les données sont représentées sous forme de table, mais leur manipulation se fait par calcul de prédicats

* **Le modèle objet (SGBDO) :** Les données sont stockées sous forme d'objets, c'est-à-dire appelées *classes* présentant des données membres. Les champs sont des instances de ces classes. 

   <img src="https://web.maths.unsw.edu.au/~lafaye/CCM/bdd/images/objet.gif" alt="SGBDO" style="width:200px;"/>

### <span>F.</span> Définissez les notions de clé étrangère et clé primaire. <a id="f-cles-etrangeres-et-cles-primaires"></a>

<img src="https://uploads-ssl.webflow.com/60ec34540d013784844d2ee2/620d2c84b6025f2c63568341_D%C3%A9finir%20une%20cl%C3%A9%20%C3%A9trang%C3%A8re%20sur%20une%20table%20existante.png" alt="KEYS" style="width:500px;"/>

<span><u>**Clé primaire :**</u></span>

Une clé primaire est un champ ou ensemble de champ d'une table dans une base de données relationnelle qui identifie de manière unique chaque enregistrement de cette table. Chaque table peut avoir une seule clé primaire, et celle-ci ne peut pas contenir de valeurs nulles. Voici ses principales caractéristiques : 
  * **Unicité :** Chaque valeur de la clé primaire doit être unique dans la table.
  * **Non-nullité :** Les baleurs de la clé primaire ne peuvent pas être nulles.
  * **Immutabilité :** Les valeurs de la clé primaire ne doivent pas être modifiée une fois définies.  

<span><u>**Clé étrangère:**</u></span>

Une clé étrangère est un champ ou ensemble de champs dans une table qui crée un lien entre cette table et une autre table. La clé étrangère fait référence à la clé primaire de l'autre table, établissant ainsi une relation entre les enregistrements des deux tables. Voici ses principales caractéristiques : 
  * **Relation :** Elle établit une relation entre deux tables en faisant référence à la clé primaire de l'autre table.
  * **Intégrité référentielle :** Elle assure que les valeurs des champs de la clé étrangère correspondent à des valeurs exsistantes de la clé primaire dans la table référencée. 
  * **Peut contenir des valeurs nulles :** Contrairement à la clé primaire, une clé étrangère peut contenir des valeurs nulles si cela est autorisé par la logique de la base de données. 

### <span>G.</span> Quelles sont les propriétés ACID ? <a id="g-proprietes-acid"></a>

<img src="https://datascientest.com/wp-content/uploads/2021/06/illu_ACID-10-1024x562.png" alt="ACID" style="width:600px;"/>

Les propriétés **ACID** sont fondamentales pour garantir la fiabilité des transactions dans les bases de données.

**ACID**
1. **Atomicité :**
    * Toutes les opérations d'une transatcion sont considérées comme une seule unité indivisible. Soit toutes les opérations sont effectuées avec succès, soit aucune ne l'est. 

2. **Cohérence :**
    * Une transaction transforme le système d'un état cohérent à un autre. Elle doit respecter toutes les règles et contraintes définies dans la base de données.

3. **Isolation :**
    * Les modifications apportées par une transaction en cours ne doivent pas être visibles par d'autres transactions jusqu'à ce que la transaction soit terminée. CEla prévient les interférences entre transcations simultanées.

4. **Durabilité :**
    * Une fois qu'une transaction est validée, ses modifications sont permanentes et suirvivent à tout type de panne. 


### <span>H.</span> Définissez les méthodes Merise et UML. Quelles sont leur utilité dans le monde de l'informatique ? Donnez des cas précis d'utilisation avec des schémas. <a id="h-methodes-merise-et-uml"></a>

<span><u>**Méthode Merise :**</u></span>

<img src="https://static.techno-science.net/illustration/Definitions/1200px/m/merise_8470372e1293dcc141ecdb59c160a6f8.jpg" alt="MERISE" style="width:400px;"/>


La méthode Merise est une méthode de conception et de gestion de projets informatiques, principalement utiliées en France. Elle se concentre sur la modélisation des données et des traitements. Merise utilise trois niveauc de modélisation : 

* **Modèle Conceptuel des Données (MCD) :** Représente les entités et les relations entre elles.

* **Modèle Logique des Données (MLD) :** Transofrme le MDC en un modèle adapté à un SGDB.

* **Modèle Physique des Données (MDP) :** Décrit la structure physique de la base de données. 

**Utilité**

* **Analyse et conception de système d'information :** Permet de structurer et de formaliser les besoins. 

* **Documentation :** Fournit une documentaiton claire et détaillée du système.

* **Communication :** Facilite la communication entre les différents acteurs du projet. 

**Exemple d'utilisation**

* **Gestion de projet :** Concevoir un système de gestion des ressourves humaines.

| Entité | Attributs | Relations |
|--------|-----------|-----------|
| Employé | ID, Nom, Prénom, Poste | Travaille dans |
| Département | ID, Nom | Contient |

<span><u>**Méthode Unified Modeling Language (UML) :**</u></span>

<img src="https://upload.wikimedia.org/wikipedia/commons/thumb/9/9a/DiagrammesUML.svg/1280px-DiagrammesUML.svg.png" alt="UML" style="width:500px;"/>

UML est un langage de modélisation standardisé utilisé pour spécifier, visualiser, construire et documenter les artefacts d'un système logiciel. UML comprend plusieurs types de diagrammes, tels que les diagrammes de cas d'utilisation, les diagrammes de calsses, les diagrammes de séquences, etc.

**Utilité**

* **Conception de logiciels :** Aide à la conception et à la documentation des systèmes logiciels.

* **Communication :** Facilite la communication entre les développeurs et les autres parties prenantes.

* **Standardisation :** Fournit un langage commun pour la modélisation des systèmes.

**Exemple d'utilisation** 

* **développement de logiciels :** Utilisé pour modéliser les fonctionnalités d'une application de gestion de bibliothèque. 


| Classe         | Attributs                        | Méthodes                     |
|----------------|----------------------------------|------------------------------|
| **Livre**      | - titre : String                 | - emprunter()                |
|                | - auteur : String                | - retourner()                |
|                | - ISBN : String                  |                              |
|                | - estDisponible : boolean        |                              |
| **Membre**     | - nom : String                   | - emprunterLivre(Livre)      |
|                | - identifiant : String           | - retournerLivre(Livre)      |
|                | - adresse : String               |                              |
| **Bibliothecaire** | - nom : String               | - ajouterLivre(Livre)        |
|                | - identifiant : String           | - supprimerLivre(Livre)      |
| **Bibliotheque** | - livres : List~Livre~         | - ajouterMembre(Membre)      |
|                | - membres : List~Membre~         | - supprimerMembre(Membre)    |

**Relations**
- Livre --> Membre : "emprunté par"
- Livre --> Bibliothecaire : "géré par"
- Bibliotheque --> Livre : "contient"
- Bibliotheque --> Membre : "a"
- Bibliothecaire --> Bibliotheque : "travaille pour"

### <span>I.</span> Définissez le langage SQL. Donnez les commandes les plus utilisées de ce langage et les différentes jointures qu'il est possible de faire. <a id="i-langage-sql-commandes"></a>

Le langage SQL (Structured Query Language) est un langage de programmation utilisé pour gérer et manipuler des bases de données relationnelles. Il permet d'effectuer diverses opérations telles que la création, la modification, la suppression et la récupération des données dans une base de données.

**Commandes les plus utilisés en SQL**

<img src="https://media.geeksforgeeks.org/wp-content/cdn-uploads/20190826175059/Types-of-SQL-Commands.jpg" alt="SQL COMMANDS" style="width:500px;"/>

* **SELECT :** Récupérer des données à partir d'une base de données. 
```
SELECT colonne1, colonne2 FROM table;
```
* **INSERT :** Insérer des données existantes dans une table. 
```
INSERT INTO table (colonne1, colonne2) VALUES (valeur1, valeur2);
```
* **UPDATE :** Modifier des données existantes dans une table.
```
UPDATE table SET colonne1 = valeur1 WHERE condition;
```
* **DELETE :** Supprimmer des données d'une table. 
```
DELETE FROM table WHERE condition;
```
* **CREATE TABLE :** Créer une table dans une base de données.
```
CREATE TABLE table (
    colonne1 type_donnée,
    colonne2 type_donnée
);
```
* **DROP TABLE :** Supprimer une table de la base de données.
```
DROP TABLE table;
```

**Différentes jointures en SQL**

<img src="https://uploads-ssl.webflow.com/60ec34540d013784844d2ee2/620180a62fdeef97b206b558_Jointures%20SQL.PNG" alt="SQL JOIN" style="width:500px;"/>

* **INNER JOIN :** Retourne les enregistrements qui ont des valeurs correspondantes dans les deux tables. 
```
SELECT colonne1, colonne2
FROM table1
INNER JOIN table2 ON table1.colonne = table2.colonne;
```
* **LEFT JOINT (ou LEFT OUTER JOIN) :** Retourne tous les enregistrements de la table de gauche et les enregistrements correspondants dans la table de droite. Si aucunes correspondances n'est trouvée, les résultats de la table de droite seront NULL.
```
SELECT colonne1, colonne2
FROM table1
LEFT joint table2 ON table1.colonne = table2.colonne;
```
* **RIGHT JOINT (ou RIGHT OUTER JOIN) :** Retourne tous les enregistrements de la table de droite et les enregistrements correspondants de la table de gauche. SI aucune correspondance n'est trouvée, les résultats de la table de gauche seront NULL.
```
SELECT colonne1, colonne2
FROM table1
RIGHT JOIN table2 ON table1.colonne = table2.colonne;
```
* **FULL JOIN (ou FULL OUTER JOIN) :** Retourne tous les enregistrements lorsqu'il y a une correspondance dans l'un des tables. Si aucune correspondance n'est trouvée, les résultats seront NULL pour la table sans correpondance.
```
SELECT colonne1, colonne2
FROM table1
FULL JOIN table2 ON table1.colonne = table2.colonne;
```

Ces commandes et jointures sont essentielles pour travailler efficacement avec des bases de données relationelles en SQL.
## <span>Conclusion <a id="conclusion"></a></span>

Ce projet vous a permis de découvrir les bases essentielles autour des données et des systèmes qui les gèrent. Que ce soit pour comprendre ce qu’est une donnée, explorer les différentes architectures de stockage comme le Data Lake ou le Lake House, ou encore différencier les bases relationnelles et non relationnelles, chaque notion abordée vise à vous donner une vision claire et structurée du sujet.

Vous avez également pu voir l’importance de la qualité des données, des clés primaires et étrangères, et des propriétés ACID pour garantir la fiabilité des systèmes. Enfin, les outils méthodologiques comme Merise et UML, ainsi que le langage SQL, offrent des moyens concrets pour concevoir et interagir avec des bases de données de manière efficace.

En résumé, que vous soyez débutant ou curieux d’approfondir vos connaissances, ce projet vous donne les bases pour naviguer dans le vaste univers des données et mieux comprendre leur rôle dans notre monde numérique. Il ne vous reste plus qu’à mettre ces concepts en pratique et continuer à explorer ! 
