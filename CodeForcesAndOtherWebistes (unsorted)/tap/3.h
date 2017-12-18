#include <string>
#include <iostream>
#include <sstream>
#include <set>

int completar(int x, std::set<int>** allows_list, int* puntaje){
	int c_score = 0;
	puntaje[x] -= 1;
	if (puntaje[x] == 0){
		c_score = 1;
		for (std::set<int>::iterator y=(*allows_list[x]).begin(); y!=(*allows_list[x]).end(); ++y){
      c_score += completar(*y, allows_list, puntaje);
		}
	}
	return c_score;
}

int* leerLinea(std::string line, int elementos){
	int i = 0;
	int* numeros = new int(elementos);
  std::stringstream ss(line);
	while(ss >> numeros[i]) i++;
	return numeros;
}

void function(std::string line){
	int* dimensiones = leerLinea(line, 2); 
	int n = dimensiones[0];
	int m = dimensiones[1];
	delete [] dimensiones;

	std::set<int>**  allows_list = new std::set<int>*[n];

	for(int x=0; x<n ; x++){
	  allows_list[x] = new std::set<int>;
	}
	
	
	int* puntaje = new int[n];
  	
	for(int x=0; x < n; x++){
		puntaje[x] = 1;
	}
	  
	std::string lectura_m;
	for(int w = 0; w < m; w++){
		std::getline(std::cin, lectura_m);
		
		int* lectura_m_ints = leerLinea(lectura_m, 2);
		int x = lectura_m_ints[0] - 1;
		int y = lectura_m_ints[1] - 1;
		delete [] lectura_m_ints;
		
		(*allows_list[x]).insert(y);
		puntaje[y] += 1;
	}
	
	std::getline(std::cin, lectura_m);
	int* materias = leerLinea(lectura_m, n);
	
	int score = 0;
	for(int p=0; p < n; p++){
	  int cm = materias[p] - 1;
		score += completar(cm, allows_list, puntaje);
		std::cout << score << std::endl;
	}

	delete[] materias;
	delete[] allows_list;
	delete[] puntaje;
}


int main(){
	std::string line;
	while (std::getline(std::cin, line))
	{
		function(line);
	}
	return 0;
}
