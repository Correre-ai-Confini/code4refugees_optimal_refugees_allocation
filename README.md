# code4refugees_optimal_refugees_allocation
Project developed during code4refugees, on March 19-20, 2022.


Optimal_team project: Luigi D'Amico, Marco Lombardi, Simone Perrotta, Riccardo..

The goal of the project is to compute an index value that suggest to the camp's management how to distribute the refugees across the tent. <br>
## Application
The script is composed by two object and an allocation algorithm. The first object is the *Occupant* class, it is characterized by general info (eg name, surname, date of birth), gender, religion, nationality and relatives. The second object is the *Tent* class, characterized by an array of occupant and the distance from the sanitary service tent; some relevant method refer to the computation of descriprive statistic of the occupants.
### Algorithm
We would like to identify with a number how much a new occupant would fit inside an existing tent, so we are building a cost function linked to the uniformity between the new occupant and the tent composition.

## Occupant
Arguments: <br>
* string: Name
* string: Surname
* string: Date_of_birth
* bool: Gender
* string: Nationality/Language 
* string: Religion
* array(Object): Relative

## Tent
Arguments: <br>
* float: Health_distance
* array(Obj): Occupants -> int: N_occupants

Method: <br>
* descript (Tent) -> Gender_pct, Religion_pct, Nationality_pct
* fit (Tent,Occupant) -> degree_of_change_in_distribution 
