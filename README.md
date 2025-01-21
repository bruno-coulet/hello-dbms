# <spanllo-dbms</span>

## <span> Sommaire</span>
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

## <span> Contexte <a id="contexte"></a></span>


"""""""""""""""""""

""""

""""""

## <span> Veille scientifique <a id="veille-scientifique"></a></span>

###  <span>A.</span><span> Qu'est-ce qu'une donnée ? Sous quelle forme peut-elle se présenter ? <a id="a-quest-ce-quune-donnee"></a></span>

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

<span><u>**La valeur des données :**</u> </span>

La valorisation de la donnée s fait à travers un processus capable à cahque étape de la transformation d'augmenter sa vlaeur directement ou par combinaison avec d'autres données. En général la finalité est l'exploitation par l'homme por la price de décision ou par un autre système permettant une commande de processus. 

Le calcul fait partie du processus de transformation par la machine et le jugement qualitatif qui appartient à l'humain fait partie de l'interprétation et donne la valeur objective à l'information finale. 

Simon Chignard et Louis-David Benyayer ont essayé de créer une grille de lecture pour la quatification des données en partant de trois conceptions de la valeur : 

* 1. La valeur est subjective : elle dépend de l'intérêt porté par l'humain qui va l'utiliser directement ou après transformation. 

* 2. La valeur est co-construire : elle augmente à partir de l'instant ou elle rentre dans un processus de transformation, notemment à travers des études croisées, capables d'exprimer des concerpt, d'où l'importance de la collaboration et de la cooridnation dans le processus de la valorisation des données.

* 3. La valeur est potentielle : elle donne ou pas un avantage futur à ceux qui la détiennent. 

A partir de ces axiomes, les données peuvent être interprétées à la lumire de trois formes de valeur. 


### <span>B.</span> Donnez et expliquez les critères de mesure de qualité des données. <a id="b-criteres-de-qualite"></a>

Les critères de mesure de la qualité des données permettent de s'assurer que les données sont fiables, précises et utilisables, en d'autres termes, de maximiser la valeur des données pour l'organisation afin de s'assurer qu'elles peuvent être utilisées efficacement pour des analyses et prises de décisions. 

<span><u>**1. Exactitude (précision) :**</u></span>

  * Les données doivent refléter correctement la réalité.   
    * Par exemple, un chffre d'affaire incorrect fausserait les analyses finnancières.

<span><u>**2. Complétude :**</u></span>
  
  * Les données doivent petre complètes et ne pas contenir de champs vides lorsque ces informations sont essentielles. 
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

<span><u>**Les différents modèles de bases de données :**</u></span>

Il existe cinq modèles de SGBD, différenciées selon la représentation des données qu'elle contient :

* **Le modèle hiérarchique :** Les données sont classées hiérarchiquement, selon une arborescence descendante. Ce modèle utilise 


### <span>F.</span> Définissez les notions de clé étrangère et clé primaire. <a id="f-cles-etrangeres-et-cles-primaires"></a>

<span><u>**Clé primaire :**</u></span>

Une clé primaire est un champ ou ensemble de champ d'une table dans une base de données relationnelle qui identifie de manière unique chaque enregistrement de cette table. Chaque table peut avoir une seule clé primaire, et celle-ci ne peut pas contenir de valeurs nulles. Voici ses principales caractéristiques : 
  * **Unicité :** Chaque valeur de la clé primaire doit être unique dans la table.
  * **Non-nullité :** Les baleurs de la clé primaire ne peuvent pas être nulles.
  * **Immutabilité :** Les valeurs de la clé primaire ne doivent pas être modifiée une fois définies.  

<span><u>**Clé étrangère:**</u></span>

Une clé étrangère est un champ ou ensemble de champs dans une table qui crée un lien entre cete table et une autre table. La clé étrangère fait référence à la clé primaire de l'autre table, établissant ainsi une relation entre les enregistrements des deux tables. Voici ses principales caractéristiques : 
  * **Relation :** Elle établit une relation entre deux tables en faisant référence à la clé primaire de l'autre table.
  * **Intégrité référentielle :** Elle assure que les valeurs des champs de la clé étrangère correspondent à des valeurs exsistantes de la clé primaire dans la table référencée. 
  * **Peut contenir des valeurs nulles :** Contrairement à la clé primaire, une clé étrangère peut contenir des valeurs nulles si cela est autorisé par la logique de la base de données. 

### <span>G.</span> Quelles sont les propriétés ACID ? <a id="g-proprietes-acid"></a>

![ACID](https://datascientest.com/wp-content/uploads/2021/06/illu_ACID-10-1024x562.png)

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

### <span>I.</span> Définissez le langage SQL. Donnez les commandes les plus utilisées de ce langage et les différentes jointures qu'il est possible de faire. <a id="i-langage-sql-commandes"></a>

## <span>Conclusion <a id="conclusion"></a></span>
