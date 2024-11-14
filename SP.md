# Cas d'utilisation

## Visiteur (non connecté)
- Consulter les prochains créneaux d'aide disponibles (anonymement, sans détails d'utilisateur).
- Consulter la liste des compétences disponibles dans l'application.

## Utilisateur connecté (U1)
1. Gérer son profil de compétences :
   - Sélectionner les compétences qu'il possède et souhaite offrir.
2. Définir ses disponibilités :
   - Ajouter des créneaux de disponibilité où il est prêt à offrir son aide.
   - Ajouter des créneaux où il cherche de l'aide dans une activité spécifique en indiquant la compétence recherchée.
3. Consulter les créneaux d'aide disponibles :
   - Afficher les créneaux où d'autres utilisateurs recherchent de l'aide dans une compétence qu'il possède.
   - Marquer un créneau comme réservé (le créneau ne sera plus proposé aux autres utilisateurs).
4. Consulter les offres d'aide disponibles :
   - Afficher les créneaux où d'autres utilisateurs offrent une compétence dont il a besoin.
   - Accéder aux informations de contact des utilisateurs liés aux créneaux réservés.


# Fonctionnalités de l'Application Django


- ### 1. Affichage des créneaux d'aide (Pour les visiteurs)  [DONE] 
  Les visiteurs peuvent voir les prochains créneaux où un utilisateur a proposé de l'aide, sans voir les informations de l'utilisateur. Cela peut être fait via une vue qui filtre les `Creneau` où `is_help_offered=True` et `is_reserved=False`.  

- ### 2. Liste des compétences disponibles [NOT DONE]
  Cette vue liste toutes les `Competence` existantes. Les visiteurs et utilisateurs connectés peuvent accéder à cette liste.  

- ### 3. Gestion des compétences pour un utilisateur [DONE] +/-
  Un utilisateur connecté peut gérer les compétences qu'il est prêt à offrir ou qu'il souhaite rechercher :
    - En ajoutant des compétences dans le modèle `UserCompetence` avec le champ `is_offering` mis à `True` ou `False`.

- ### 4. Créneaux d'aide et demandes d'aide [DONE]
  Les utilisateurs peuvent :
    - Créer un `Creneau` où ils offrent de l'aide sur une compétence donnée.
    - Créer un `Creneau` où ils demandent de l'aide pour une compétence manquante.
    - Une fois un créneau créé, il est visible dans les vues appropriées en fonction des compétences et de la disponibilité.

- ###  5. Recherche de créneaux correspondants [NOT DONE]
  Un utilisateur connecté peut :
    - Rechercher des créneaux où des utilisateurs demandent de l'aide dans une compétence qu'il possède (pour les offres de disponibilité).
    - Rechercher des créneaux où des utilisateurs offrent une compétence recherchée (pour les demandes d'aide).

- ### 6. Réservation d'un créneau [DONE]
  Lorsque l'utilisateur trouve un créneau qui l'intéresse, il peut le réserver :
    - Le champ `is_reserved` du `Creneau` est mis à `True`.
    - Les informations de contact des deux utilisateurs sont affichées pour qu'ils puissent organiser l'activité.
 

# Relations principales :

## [User] 1--1 [Profile]
Chaque `User` est associé à un unique `Profile` et vice-versa.

## [Profile] *--* [UserCompetence]
Un `Profile` peut être lié à plusieurs `UserCompetence` pour indiquer toutes les compétences qu'il offre ou recherche.

## [UserCompetence] *--1 [Competence]
Chaque `UserCompetence` est associé à une seule `Competence`, mais une compétence peut être recherchée ou offerte par plusieurs `UserCompetence`.

## [Profile] *--* [Creneau]
Un `Profile` peut avoir plusieurs `Creneau` pour gérer ses créneaux de disponibilité.

