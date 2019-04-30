# Utilisation projet ODOO: Bieraubeurre

Vous pouvez accéder au [code source](https://github.com/RexT2507/product_type) du module.

#

## Créer des produits avec le nouveaux type

#

Pour la création d'un article, il faut se rendre dans l'écran facturation puis dans l'onglet client et enfin sur article.

![Screenshot](img/menu_article.PNG)

Une fois que l'on est dans l'écran Articles on peut voir une liste des articles déjà créer ainsi qu'un menu, nous donnant la possibilité de créer ou d'importer des articles.

![Screenshot](img/liste_article.PNG)

Prenons un exemple, nous voulons créer un nouvel article, on clique donc sur "créer", on arrive sur un écran de création de notre nouvel article.

![Screenshot](img/ecran_article.PNG)

On peut remarquer l'ajout du champ "Mes types de produits" par le module product_type que nous avons réalisé.

![Screenshot](img/type_article.png)

Il vous suffit de saisir le nom et les autres informations de votre article et de sauvegarder, l'article apparaîtra dans la liste.

#

## Créer un nouveau type

#

On peut accèder à l'interface de création depuis l'interface de modification/création de l'article ou du menu principal d'Odoo.

![Screenshot](img/type_article.png)

![Screenshot](img/menu_odoo_type.png)

Pour créer un nouveau type, il suffit de saisir le nom du nouveau type et de sauvegarder.

![Screenshot](img/interface_creation_type.png)

Si on prend l'exemple de tout à l'heure en affichant la liste des types, on remarque bien que "exemple" a été ajouté.

![Screenshot](img/creation_type.png)

## Créer des clients

#

Pour la création d'un client, il faut se rendre dans l'écran facturation puis dans l'onglet client et enfin sur client.

![Screenshot](img/menu_client.PNG)

Une fois que l'on est dans l'écran Clients on peut voir une liste des clients déjà créer ainsi qu'un menu, nous donnant la possibilité de créer ou d'importer des clients.

![Screenshot](img/liste_client.PNG)

Prenons un exemple, nous voulons créer un nouveau client, on clique donc sur "créer", on arrive sur un écran de création de notre nouveau client.

![Screenshot](img/ecran_client.PNG)

Il vous suffit de saisir le nom et les autres informations de votre client et de sauvegarder, le client apparaîtra dans la liste.

#

## Créer des contacts

#

Pour créer d'un contact, au démarrage d'Odoo cliquez sur le menu en haut à gauche puis, dans l'onglet contacts.

![Screenshot](img/menu_contact.PNG)

Une fois que l'on est dans l'écran Contacts on peut voir une liste des contacts déjà créer ainsi qu'un menu, nous donnant la possibilité de créer ou d'importer des contacts.

![Screenshot](img/liste_contact.PNG)

Prenons un exemple, nous voulons créer un nouveau contact, on clique donc sur "créer", on arrive sur un écran de création de notre nouveau contact.

![Screenshot](img/ecran_contact.PNG)

Il vous suffit de saisir le nom et les autres informations de votre contact et de sauvegarder, le contact apparaîtra dans la liste.

#

Il est possible de lui préciser une société, ou d'en créer une, en effet si on clique sur le menu déroulant de Société on peut attribuer une société ou en créer une.

![Screenshot](img/champ_societe.png)

## Ajouter des contacts dans le CRM

#

Pour ajouter des contacts dans notre CRM, il suffit de cliquer sur le menu en haut à gauche puis sur l'onglet CRM.

![Screenshot](img/menu_CRM.PNG)

Une fois que l'on est dans l'écran CRM on peut voir une liste des pipelines déjà créer ainsi qu'un menu, nous donnant la possibilité de créer ou d'importer des pipelines.

![Screenshot](img/liste_CRM.PNG)

Prenons un exemple, nous voulons créer un nouveau pipeline, on clique donc sur "créer", on arrive sur un écran de création de notre nouveau pipeline.

![Screenshot](img/ecran_CRM.PNG)

Par la suite il vous faut saisir l'opportunité, le client, le revenu espéré et enfin la priorité de l'étiquette.

#

## Effectuer des conversion de piste en gagné (demande de devis) et perdu

#

Il est possible que des pistes soient gagnées et amène à une demande de devis ou bien perdu et donc abandonnées.

#

Prenons un exemple j'ai deux pistes une avec Serpentard de 150 euros et une avec Gryffondor de 200 euros,

![Screenshot](img/nouv_piste.PNG)

Gryffondor est perdu je clique sur l'étiquette pour spécifier l'échec de cette piste.

![Screenshot](img/perdu_piste.PNG)

On précise le motif de cette perte, avec les motifs par défault ou on peut en créer un particulier.

![Screenshot](img/perdu_piste_motif.png)

On peut voir qu'un bagde perdu apparaît sur l'étiquette.

![Screenshot](img/piste_perdu_badge.PNG)

Si on rafraichit notre liste on remarque que la piste de Gryffondor a été supprimée.

![Screenshot](img/liste_CRM_refresh.PNG)

Maitenenant on prend la piste de Serpentard et on l'a gagnée on clique donc sur l'étiquette et on la marque comme gagné !

![Screenshot](img/gagne_piste.PNG)

On peut voir qu'un bagde gagné apparaît sur l'étiquette.

![Screenshot](img/piste_gagne_badge.PNG)

Si on rafraichit notre liste on remarque que la piste de Serpentard a bougé vers Gagné.

![Screenshot](img/liste_CRM_gagne.PNG)

On peut maitenant cliquer sur l'étiquette et effectuer une demande de devis.

![Screenshot](img/demande_devis.PNG)

## Créer des devis

#

Une fois que nous avons effectué une demande de devis il est temps de créer le devis, une fois qu'on a appuyé sur "nouveau devis", on arrive sur l'interface de création du devis.

![Screenshot](img/ecran_devis.PNG)

Il nous suffit de saisir les différentes informations comme la validité, les conditions de paiement et bien sûr les articles de la commande.

![Screenshot](img/ecran_devis_complet.PNG)

Nous avons ensuite accès à différentes fonctions du menu comme l'envoi par email ou encore l'impression.

![Screenshot](img/ecran_devis_menu.PNG)

Maitenant on peut valider et un bouton créer une facture apparait dans le menu.

![Screenshot](img/menu_devis_facture.PNG)

## Faire une impression du report que vous avez créer

#

Une fois que le devis est créé on peut effectuer une impression en cliquant sur le bouton imprimer ce qui nous donne ce pdf.

![Screenshot](img/devis_pdf.png)

## Valider le payement et vérifier que la transaction est opérationnelle dans la base de donnée

# 

Une fois que le devis et validé et que la facture a été créée on peut procéder à la validation du paiement.

![Screenshot](img/facture_vald.PNG)

On arrive alors sur une interface qui nous récapitule toutes les informations et une fois fait on valide.

![Screenshot](img/facture_vald_inter.PNG)

On voit maintenant que la facture a été payé avec la date du paiement ! 

![Screenshot](img/facture_paye.PNG)


### Vous savez maintenant vous servir des fonctions les plus importantes d'Odoo félicitation !
