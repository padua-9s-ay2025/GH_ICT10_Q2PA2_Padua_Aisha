# Drill 2: Using Lists

from pyscript import display, document 

def add2_list (e): 
    document.getElementById('result').innerHTML = ' '

    given_name = document.getElementById('first_name').value.title().strip()
    surname = document.getElementById('last_name').value.title().strip()
    new_member = {given_name + " " + surname} 

    grade_seven_members = {'Maria Julia Cortes', 'Alekos Canares', 'Shiloh Jolie'}
    grade_eight_members = {'Charles Villar', 'Victoria Pascual', 'Henry Tolentino'}
    grade_nine_members = {'Sheldon Cooper', 'Missy Cooper', 'George Cooper'}
    grade_ten_members = {'Aisha Padua', 'Tori Vega', 'Ray Ben'}

    all_members = grade_seven_members | grade_eight_members |  grade_nine_members |grade_ten_members | new_member

    display(f'The people in Math Club are {all_members}.', target='result')
    display(f'The total number of people in Math Club is {len(all_members)}', target='result')