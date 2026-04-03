#include <iostream>

int main() {
    //Formas de imprimir texto en pantalla
    std::cout << "Hola mundo\n"; //std::cout es un objeto de la biblioteca estándar de C++ que se utiliza para 
    //imprimir texto en la consola. El operador << se utiliza para enviar el texto al flujo de salida estándar (std::cout).
    //y vacía el búfer de salida

    std::cout << "Hola we" << std::endl; //std::endl es un manipulador de flujo que se utiliza para insertar un salto de línea 
    //en el flujo de salida.y vaciar el búfer de salida.

    printf("Hola mundo\n"); //printf es una función de la biblioteca estándar de C que se utiliza para imprimir
    //texto formateado en la consola. El "\n" es un carácter de escape que representa un salto de línea.
    return 0;
}
