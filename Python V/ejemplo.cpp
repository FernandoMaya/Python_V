#include <iostream>
#include<stdio.h>
#include<conio.h>
#include <math.h>
#include <stdlib.h>

int a,dia;
char mes; 
int main (){
	
	//signos zodiacales
	printf ("\n Daniel Moreno Maya");
	
	
	
	for(a=1;a<=12;a++){
	
	
		printf("\n a.- ENERO  ");
		printf("\n b.-FEBRERO ");
		printf("\n c.-MARZO ");
		printf("\n d.-ABRIL ");
		printf("\n e.-MAYO");
		printf("\n f.-JUNIO ");
		printf("\n g.-JULIO ");
		printf("\n h.-AGOSTO ");
		printf("\n i.-SEPTIEMBRE");
		printf("\n j.-OCTUBRE ");
		printf("\n k.-NOVIEMBRE");
		printf("\n l.-DICIEMBRE ");
		printf("\n \n ingrese el mes que nacio:_ ");
		scanf("%c",&mes);
		printf("\n \n ingrese el dia que nacio:_ ");
		scanf("%i",&dia);
	
	
		switch(mes){
		
		
			case 'a': if (dia<22){ 
				printf ("capricornio");
						} else {
							printf("acuario");
						}
							
						
				
			break;
			
			
			case 'b':
				if (dia<22){ 
				printf ("capricornio");
						} else {
							printf("acuario");
						}
			break;
			case 'c':
				if (dia<22){ 
				printf ("capricornio");
						} else {
							printf("acuario");
						}
			
			break;
			case 'd': 
			
			if (dia<22){ 
				printf ("capricornio");
						} else {
							printf("acuario");
						}
			
			break;
			case 'e':
			if (dia<22){ 
				printf ("capricornio");
						} else {
							printf("acuario");
						}
			
			break;
			case 'f':
			if (dia<22){ 
				printf ("capricornio");
						} else {
							printf("acuario");
						}
			
			break;
			case 'g':
			if (dia<22){ 
				printf ("capricornio");
						} else {
							printf("acuario");
						}
			
			break;
			case 'h': 
			if (dia<22){ 
				printf ("capricornio");
						} else {
							printf("acuario");
						}
			
			break;
			case 'i':
			if (dia<22){ 
				printf ("capricornio");
						} else {
							printf("acuario");
						}
			
			break;
			case 'j':
			if (dia<22){ 
				printf ("capricornio");
						} else {
							printf("acuario");
						}
			
			
			break;
			case 'k': 
			if (dia<22){ 
				printf ("capricornio");
						} else {
							printf("acuario");
						}
			
			
			break;
			case 'l':
			if (dia<22){ 
				printf ("capricornio");
						} else {
							printf("acuario");
						}
			
			
			break;
			 
			 default:("upsss, se equivoco, inetntelo de nuevo :)");
			 a--;
			}
				}
	return 0;
}