
# Odoo DAM Module

## Présentation du Projet

**Odoo DAM Module** est un module de gestion de bibliothèque multimédia (DAM - Digital Asset Management) conçu pour l'écosystème Odoo. Il vise à centraliser, organiser et faciliter la recherche de ressources numériques (images, vidéos, documents) dans un environnement collaboratif.

---

## Fonctionnalités à Développer

### 1. **Gestion des Ressources**
- Importation et organisation des fichiers multimédias.
- Support des types de fichiers : images, vidéos, documents PDF.
- Association des ressources à des projets spécifiques.

### 2. **Recherche et Filtres**
- Barre de recherche avancée avec autocomplétion.
- Filtres par type de fichier, projet associé, et date de création.
- Prévisualisation des fichiers (miniatures et extraits).

### 3. **Gestion des Permissions**
- Contrôle d'accès selon les rôles utilisateurs :
  - Visiteur : Lecture seule.
  - Éditeur : Modification des ressources.
  - Administrateur : Gestion complète, y compris suppression et permissions.

### 4. **Interface Utilisateur**
- Vue formulaire et vue liste pour gérer les ressources.
- Menus et navigation intuitive via l'interface Odoo.

### 5. **Automatisation et Tests**
- Intégration d’un pipeline CI/CD avec GitHub Actions.
- Tests unitaires et fonctionnels pour garantir la fiabilité.

---

## Roadmap

- **Phase 1 : Initialisation**  
  Création de la structure du module et configuration de l'environnement Docker.

- **Phase 2 : Modèle de Données**  
  Développement des modèles pour gérer les ressources et leurs relations avec les projets.

- **Phase 3 : Interfaces Utilisateur**  
  Conception des vues XML pour l’ajout, la modification et la recherche des ressources.

- **Phase 4 : Sécurité et Permissions**  
  Mise en place des rôles et des contrôles d'accès.

- **Phase 5 : Tests et Intégration Continue**  
  Automatisation des tests et déploiement via GitHub Actions.

---

## Installation

### Prérequis
- Odoo 16
- Docker et Docker Compose

### Étapes
1. Clonez le repository :
   ```bash
   git clone https://github.com/hericlibong/odoo-dam-module.git
   ```
2. Placez le module dans le dossier `addons` de votre environnement Odoo :
   ```bash
   mv odoo-dam-module /path/to/your/odoo/addons/
   ```
3. Redémarrez vos conteneurs Docker :
   ```bash
   docker-compose down
   docker-compose up -d
   ```
4. Installez le module depuis l'interface Odoo.

---

## Contributions

Les contributions sont les bienvenues !  
Veuillez soumettre vos suggestions ou corrections via des **issues** ou des **pull requests** sur ce repository.

---

## Auteur

**Heric Libong**  
_Développeur Python/Odoo_

---

## Licence

Ce projet est sous licence LGPL-3.0. Consultez le fichier `LICENSE` pour plus d'informations.


