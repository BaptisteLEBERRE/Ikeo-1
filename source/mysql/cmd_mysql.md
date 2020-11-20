### Afficher les nom et description de tous les produits.
```sql
SELECT nom_produit, desc_produit FROM produits;
```

#
### Afficher tous les meubles qui sont abandonnés.
```sql
SELECT * FROM produits WHERE abandon_produit = 1;
```

#
### Effacer le Bo Meuble de brest.
```sql
DELETE FROM clients WHERE (SELECT id_raison FROM raisons_socials WHERE libelle_raison='BoMeuble') AND Ville_client='Brest'
```

#
### Il y a une erreur sur le nom du meuble Apfelgluk, il faut le récrire Apfelgluck.
```sql
UPDATE produits SET nom_produit = "Apfelgluck" where nom_produit = "Apfelgluk";
```

#
### Ajouter un nouveau client : Tout à la maison, Place Terreaux, Lyon.
```sql
INSERT INTO clients 
VALUES(NULL, 
(SELECT id_type FROM types WHERE libelle_type='Magasin'),
(SELECT id_raison FROM raisons_socials WHERE libelle_raison='Tout A La Maison'),
'Place Terreaux', 'Lyon', (SELECT id_pays FROM pays WHERE nom_pays='France'));
```

#
### Ajouter une nouvelle facture pour le tout à la maison de Lyon , enregistré le 28/08/2018, à 18h. La commande est composé de 18 Naess.

* ajouter la facture.
```sql
INSERT INTO `factures` VALUES 
(NULL,
'MSQ299',
'2018-08-28', 
(SELECT id_client FROM clients WHERE 
(SELECT id_raison FROM raisons_socials WHERE 
libelle_raison='Tout A La Maison') AND
Ville_client='Lyon'))
```

* ajouter les produits
```sql
INSERT INTO `facutre_produit` VALUES
((SELECT id_facture FROM factures WHERE numero_facture='MSQ299'),
(SELECT id_produit FROM produits WHERE nom_produit ='Naess'),
'18');
```


#
### Retrouver tous les meubles achetés par le Bo Meuble de Paris.
```sql
SELECT nom_produit FROM produits WHERE
id_produit IN 
(SELECT id_produit FROM facutre_produit WHERE 
id_facture IN 
(SELECT id_facture FROM factures WHERE
client_facture = 
(SELECT id_client FROM clients WHERE 
raison_client IN 
(SELECT id_raison FROM raisons_socials WHERE 
libelle_raison='Bo Meuble')AND 
ville_client='Paris')))
```

#
### Retrouver toutes les factures enregistrée depuis le 1er juillet 2018.
```sql
SELECT * FROM factures WHERE >= 01/07/2018;
```