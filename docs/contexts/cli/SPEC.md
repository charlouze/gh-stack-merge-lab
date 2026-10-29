# cli

## Boundary

Le paquet `textkit_cli/` : les commandes du terminal. Il lit ses arguments,
appelle `textkit` et affiche le résultat ; il ne transforme aucun texte lui-même.

## squeeze

`squeeze "<texte>"` affiche le texte resserré, suivi d'un saut de ligne, et sort
avec le code 0.

## Commande inconnue

Une commande inconnue, ou l'absence de commande, affiche la liste des commandes
sur la sortie d'erreur et sort avec le code 2.
