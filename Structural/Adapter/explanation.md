__Adapter__ is a structural design pattern that allows objects 
with incompatible interfaces to collaborate.

Nell'esempio, vedremo un Character che brandisce una Weapon. 
Una Weapon però può NON ESSERE compatibile con tutti i Characters. 
Ma il Character deve essere libero di utilizzarla, senza avvedersi che sta usando
un oggetto anziché un altro. Un Character usa una Weapon, fine. Come
questo Character debba accludere una Weapon, non dev'essere un problema del Character. 


Si vede come i metodi _provide_damage_ (volutamente non messi in Weapon, per indicare
un "buco" di qualche genere) in Axe e Helmet siano diversi: uno restituisce un 
valore effettivo (Axe), l'altro restituisce una CLASSE di danno, in lettere che vanno
da 'a' a 'j'. 
Ma nel computo del danno da attacco, io avrò bisogno di calcolare anche l'apporto
di Helmet!! E mò che si fa? Si modifica la classe pre-esistente?