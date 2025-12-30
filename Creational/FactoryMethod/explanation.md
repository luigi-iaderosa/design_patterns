__Factory Method__ is a creational design pattern that provides an interface
for creating objects in a superclass,
but allows subclasses to alter the type of objects that will be created.

Nell'esempio, creeremo un Motore che genera nemici di un videogame. 
I nemici hanno un loro "metodo" di attacco (enemy.attack()). 
Poiché il motore deve generare casualmente nemici che interagiscono con l'eroe, 
noi non possiamo pensare di scrivere una logica di interazione con ogni nemico, né tantomeno
pensare di dover cambiare la logica di tutto il progetto solo perché in un secondo momento, 
ci viene chiesto di aggiungere un nuovo nemico al rooster. 

Semmai, dobbiamo 1. astrarre interazione 2. astrarre creazione (non ci possono essere nemici che vengono creati in maniera
diversa, sebbene siano entità DIVERSE). 

