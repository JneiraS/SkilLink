# import os
#
# import django
#
# os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'core.settings')
# django.setup()
#
# from mutual_support.models import Competence
#
#
# def create_competence(name, category=None):
#     competence, created = Competence.objects.get_or_create(name=name, category=category)
#     return competence
#
#
# comp: list = [{"Techniques d'apprentissage accéléré (mind-mapping, etc.)": "Éducation et Apprentissage"},
#               {"Méthodes de travail et d’organisation personnelle": "Éducation et Apprentissage"},
#               {
#                   "Soutien scolaire dans les matières principales (mathématiques, sciences, histoire, etc.)": "Éducation et Apprentissage"},
#               {"Coaching de préparation aux examens": "Éducation et Apprentissage"},
#               {"Langage des signes": "Éducation et Apprentissage"},
#               {"Dessin, peinture, illustration": "Art et Créativité"},
#               {"Écriture créative (poésie, scénarios, romans)": "Art et Créativité"},
#               {"Musique (apprendre un instrument, composition musicale)": "Art et Créativité"},
#               {"Artisanat (sculpture, couture, création de bijoux)": "Art et Créativité"},
#               {"Photographie (prise de vue, retouche)": "Art et Créativité"},
#               {"Décoration intérieure et design": "Art et Créativité"},
#               {"Cours de cuisine (recettes spécifiques, cuisine du monde)": "Cuisine et Art Culinaire"},
#               {"Techniques de pâtisserie": "Cuisine et Art Culinaire"},
#               {"Nutrition et alimentation équilibrée": "Cuisine et Art Culinaire"},
#               {"Décoration de gâteaux": "Cuisine et Art Culinaire"},
#               {"Sommellerie (dégustation et accords mets-vins)": "Cuisine et Art Culinaire"},
#               {"Planification de menus et cuisine de batch-cooking": "Cuisine et Art Culinaire"},
#               {"Coaching personnel et gestion du stress": "Bien-être et Développement Personnel"},
#               {"Techniques de relaxation (méditation, yoga)": "Bien-être et Développement Personnel"},
#               {"Prise de parole et confiance en soi": "Bien-être et Développement Personnel"},
#               {"Conseils en organisation et minimalisme": "Bien-être et Développement Personnel"},
#               {"Gestion du temps et productivité": "Bien-être et Développement Personnel"},
#               {
#                   "Santé mentale (techniques de résilience, gestion des émotions)": "Bien-être et Développement Personnel"},
#               {"Petits travaux domestiques (plomberie, électricité de base)": "Bricolage et DIY"},
#               {"Réparation de meubles ou d'appareils": "Bricolage et DIY"},
#               {"Jardinage et entretien de plantes": "Bricolage et DIY"},
#               {"Couture et retouche de vêtements": "Bricolage et DIY"},
#               {"Conception de meubles ou objets en bois": "Bricolage et DIY"},
#               {"Aménagement extérieur et intérieur": "Bricolage et DIY"},
#               {"Gestion des finances personnelles": "Compétences en Finance et Gestion"},
#               {"Initiation aux investissements (bourse, immobilier)": "Compétences en Finance et Gestion"},
#               {"Conseils fiscaux de base": "Compétences en Finance et Gestion"},
#               {"Utilisation d'outils financiers (budget, prévisions)": "Compétences en Finance et Gestion"},
#               {"Comptabilité et gestion de trésorerie": "Compétences en Finance et Gestion"},
#               {"Crowdfunding et levée de fonds pour projets": "Compétences en Finance et Gestion"},
#               {"Physique et mathématiques appliquées": "Compétences en Sciences et Technologie"},
#               {"Introduction à l’IA et au Machine Learning": "Compétences en Sciences et Technologie"},
#               {"Biologie et sciences de la vie": "Compétences en Sciences et Technologie"},
#               {"Écologie et développement durable": "Compétences en Sciences et Technologie"},
#               {"Robotique et électronique de base": "Compétences en Sciences et Technologie"},
#               {"Astronomie et observation de l’espace": "Compétences en Sciences et Technologie"},
#               {"Cours de fitness et musculation": "Sports et Activités Physiques"},
#               {"Techniques de course et cardio-training": "Sports et Activités Physiques"},
#               {"Yoga et pilates": "Sports et Activités Physiques"},
#               {"Sports de combat (boxe, judo, etc.)": "Sports et Activités Physiques"},
#               {"Sports de plein air (randonnée, escalade)": "Sports et Activités Physiques"},
#               {"Danse (salsa, hip-hop, danse contemporaine)": "Sports et Activités Physiques"}]
#
# for c in comp:
#     for k, v in c.items():
#         create_competence(k, v)
