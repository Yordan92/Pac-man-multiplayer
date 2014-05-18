PAC-MAN multi player
===================


Pac-Man е аркадна игра,където преследваш чудовище и трябва да изядеш всички малки точки  в лабиринта,  докато те гонят призраци. Ако те  хванат губиш един живот, освен ако не си изял голяма точка, тогава можеш за някакво определено време да преследваш и да изядеш даден призрак. Играта ще има графичен интерфейс. Ще предлага опция за multiplayer. В тази реализация на pac-man, призраците ще са малко по-умни(ще се стараят да те обградят и после безмилостно да те изядат :( ). Играта ще бъде реализирана чрез претеглен граф, като на всеки възел ще представлява една вратичка в картата. С помощта на алгоритъма на Dijkstra ще се пресмята най-кратките пътища от вратите, до които най-близко се намира packman-a, до призраците. Картата ще представлява една матрица, където ще са посочени, къде се намира, pacman-a, призраците, малките точките, който pacmana трябва да събира, големите точки, който дават възможност да бъдат изядени призраците, самите граници на стените и вратичките в тях.

Pacman-a ще си има собствен клас с променливи 
	- къде се намира
	- колко живота има
	- дали е изял голяма точка(даваща му правото да изяде призрак)
	
Призраците ще си имат един клас 
	- къде се намира
	- възела където трябва да отиде
	- най-краткия пат до мястото, където трябва да отиде

Планов за Milestone II: Създаване на картата или имплементация на Dijkstra.
