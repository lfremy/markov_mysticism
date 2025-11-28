# 🔮 Oracle de Delphes

Interface web pour consulter la Pythie et recevoir des prophéties générées par chaînes de Markov.

## Installation
```bash
pip install flask gtts markovify
```
**Linux (Ubuntu/Debian) :**
```bash
sudo apt-get update
sudo apt-get install sox libsox-fmt-all
```


## Lancement
```bash
python app.py
```

Ouvrir : `http://localhost:5000`

## Fonctionnement

1. L'utilisateur pose une question
2. Markovify génère une prophétie depuis le corpus (chaînes de Markov)
3. gTTS convertit le texte en audio français
4. sox fait les effets vocaux
5.. La prophétie s'affiche et se prononce automatiquement

## Technologies

- **Flask** : serveur web
- **Markovify** : génération de texte par chaînes de Markov
- **gTTS** : synthèse vocale
- **sox** : effet vocaux


## Chaînes de Markov vs IA

### Chaînes de Markov
- Analyse statistique du corpus : chaque mot est suivi d'un autre selon les probabilités observées
- Résultats imprévisibles mais limités au vocabulaire et structures du corpus

## Pourquoi Markov plutôt que l'IA pour cet oracle ?

### 1. Contrôle stylistique total
- Markov reproduit exactement le style du corpus surréaliste
- L'IA ajouterait sa propre "voix" et pourrait dévier du ton mystique
- Maîtrise totale du vocabulaire et des tournures

### 2. Authenticité du projet
- C'est le corpus personnalisé qui parle, pas un modèle générique
- Plus original qu'une IA entraînée sur internet


### 3. Aspect technique/pédagogique
- Démontre la compréhension des algorithmes classiques
- Plus intéressant techniquement qu'un simple appel d'API
- Markov est un concept informatique élégant

### 4. Gratuité et autonomie
- Aucun coût d'API
- Fonctionne hors ligne
- Pas de limite d'utilisation
- Aucune dépendance externe

### 5. Imprévisibilité poétique
- L'aspect aléatoire de Markov crée un effet oracle authentique
- Les associations étranges renforcent le côté mystique
- L'IA serait trop rationnelle pour un oracle

### 6. Performance
- Génération instantanée
- Léger (quelques Ko vs Go de modèle)
- Pas besoin de GPU

**En résumé** : Pour un oracle surréaliste, Markov préserve le style unique, reste imprévisible et mystérieux, et évite l'homogénéisation des LLM. L'IA rendrait le projet moins personnel et moins intéressant.