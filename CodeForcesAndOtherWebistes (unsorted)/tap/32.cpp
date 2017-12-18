#include <string>
#include <iostream>
#include <sstream>
#include <set>

//int completar(int x, int** allows_list, int* puntaje){
int completar(int x, std::set<int>* allows_set, int* puntaje){
	int c_score = 0;
	puntaje[x] -= 1;
	if (puntaje[x] == 0){
		c_score = 1;
		//for (int yv= 1; yv<= (allows_list[x][0]); ++yv){
		for (std::set<int>::iterator yv=allows_set[x].begin(); yv!=allows_set[x].end(); ++yv){
		    //int y = allows_list[x][yv];s
		    int y = *yv;
			c_score += completar(y, allows_list, puntaje);
		}
	}
	return c_score;
}

void leerLinea(std::string line, int* numeros){
	std::stringstream ss(line);
	int i = 0;
	while(ss >> numeros[i]) i++;
}

void function(std::string line){
	int* dimensiones = new int [2];
	leerLinea(line, dimensiones); 
	int n = dimensiones[0];
	int m = dimensiones[1];
	delete [] dimensiones;
    
    int**  allows_list = new int*[n]; 
    std::set<int>*  allows_set = new std::set<int>[n];
	for(int x=0; x<n ; x++){
		allows_list[x] = new int[n+1];
		allows_list[x][0] = 0;
		allows_set[x] = std::set<int>::set<int>();
	}
	
	int* puntaje = new int[n];
	for(int x=0; x < n; x++){
		puntaje[x] = 1;
	}
	  
	std::string lectura_m;
	for(int w = 0; w < m; w++){
		std::getline(std::cin, lectura_m);
		int* lectura_m_ints = new int [2];
		leerLinea(lectura_m, lectura_m_ints);
		int x = lectura_m_ints[0] - 1;
		int y = lectura_m_ints[1] - 1;
		delete [] lectura_m_ints;
		allows_list[x][0] += 1;
		allows_list[x][allows_list[x][0]] = y;
		allows_set[x].insert(y);
		puntaje[y] += 1;
	}
	
	std::getline(std::cin, lectura_m);
	int* materias = new int [n];
	leerLinea(lectura_m, materias);
	
	int score = 0;
	for(int p=0; p < n; p++){
		int cm = materias[p] - 1; 
		//score += completar(cm, allows_list, puntaje);*/
		score += completar(cm, allows_set, puntaje);
		std::cout << score << std::endl;
	}
	delete[] materias;
	delete[] allows_list;
	delete[] allows_set;
	delete[] puntaje;
}


int main(){
	std::string line;
	while (std::getline(std::cin, line)) function(line);
	return 0;
}
