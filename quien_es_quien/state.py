#import reflex as rx
import random

personajes = ['Susan', 'Claire', 'David', 'Anne', 'Robert', 'Anita',
              'Joe', 'George', 'Bill', 'Alfred', 'Max', 'Tom',
              'Alex', 'Sam', 'Richard', 'Paul', 'Maria', ' Frans' ,
              'Herman' , 'Bernardo', 'Philip', 'Eric', 'Charlis', 'Peter']


def escoger_carta():
    return personajes[random.randint(0, 23)]