---
title: 'WIP: Learning to Extract Coherent Summary via Deep Reinforcement Learning'
date: 2021-06-24
---

Introduction
======
Een populair probleem is het ophalen van de belangrijkste zinnen uit een document. Dit kan je met een gerative model 
doen maar het makkelijkste is om een extractive methode te gebruiken. In een extractive methode maak je geen nieuwe zinnen
maar haal je alleen de belangerijkste zinnen eruit. Een probleem hiermee is dat je het probleem dat het kan gebeuren
dat de relatie tussen de zinnen niet coherent is. In deze blog post gaan we een methode bespreken zoals besproken in 
het artikel "Learning to Extract Coherent Summary via Deep Reinforcement Learning".

Deze paper pakt het probleem aan dat huidige methodes vooral toegespitst zijn op korte documenten en zijn gebasseerd op
sequence to sequence modellen zoals gebruikt in vertalingen. Deze methode gaat dit aanpakken. De methodes obv word 
embeddings die er nu zijn werken prima om de belangrijkste zinnen op te halen maar doen niks voor een leesbaar stukje. 
Door het gebruiken van reinforcement learning is het mogelijk om deze niet differentieerbare objective (namelijk het maken
van een coherent samenvatting) to optimalizeren. Het eerste deel is een neural coherence model waarbij je gegeven een zin
automatisch de volgende zin kan kiezen die er dan goed achter past. De output van dit model is vervolgens als input gegeven
voor een reinforcemnt learning model die de ROUGE evaluatie optimaliseert. 

Neural Extractive Summarization Model
======

