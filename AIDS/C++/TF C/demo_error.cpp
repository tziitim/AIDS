/*
 * demo_error.cpp
 * 
 * Copyright 2019 Tim's Laptop <Tim's Laptop@LAPTOP-7R2QALN5>
 * 
 * This program is free software; you can redistribute it and/or modify
 * it under the terms of the GNU General Public License as published by
 * the Free Software Foundation; either version 2 of the License, or
 * (at your option) any later version.
 * 
 * This program is distributed in the hope that it will be useful,
 * but WITHOUT ANY WARRANTY; without even the implied warranty of
 * MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
 * GNU General Public License for more details.
 * 
 * You should have received a copy of the GNU General Public License
 * along with this program; if not, write to the Free Software
 * Foundation, Inc., 51 Franklin Street, Fifth Floor, Boston,
 * MA 02110-1301, USA.
 * 
 * 
 */


#include <iostream>

int main(int argc, char **argv){
	
	char array[25];
	
	int *pointer_o_death = (int*)(0);
	
	*pointer_o_death = 1;
	
	printf("Lets try...\n");
	array[30] = 'P';
	printf("Tada!\n");
	
	for(int i=0;i<40;i++){
		printf("%c",array[i]);
	}
	
	return 0;
}

