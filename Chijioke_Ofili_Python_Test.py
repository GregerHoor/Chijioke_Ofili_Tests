import statistics as st
import random as ran

import os 
from dotenv import load_dotenv

# Please adopt use of your postgres db private dets
load_dotenv(r"C:\Users\USER\PostgreSQL.env")

import psycopg
from psycopg.types.json import Jsonb

conn = psycopg.connect(
    dbname=os.getenv('DB_NAME'),
    user=os.getenv('DB_USER'),
    password=os.getenv('DB_PASSD'),
)

cur = conn.cursor()

# Please change directory path to fit file position on your file manager
file = open(r'C:\Users\USER\Chijioke_Ofili_Tests\Chijioke_Ofili_Test.sql', 'r')

cur.execute(file.read())

All_lists = []
MONDAY = ['GREEN', 'YELLOW', 'GREEN', 'BROWN', 'BLUE', 'PINK', 'BLUE', 'YELLOW', 'ORANGE', 'CREAM', 'ORANGE', 'RED', 'WHITE', 'BLUE', 'WHITE', 'BLUE', 'BLUE', 'BLUE', 'GREEN']
TUESDAY = ['ARSH', 'BROWN', 'GREEN', 'BROWN', 'BLUE', 'BLUE', 'BLEW', 'PINK', 'PINK', 'ORANGE', 'ORANGE', 'RED', 'WHITE', 'BLUE', 'WHITE', 'WHITE', 'BLUE', 'BLUE', 'BLUE']
WEDNESDAY = ['GREEN', 'YELLOW', 'GREEN', 'BROWN', 'BLUE', 'PINK', 'RED', 'YELLOW', 'ORANGE', 'RED', 'ORANGE', 'RED', 'BLUE', 'BLUE', 'WHITE', 'BLUE', 'BLUE', 'WHITE', 'WHITE']
THURSDAY = ['BLUE', 'BLUE', 'GREEN', 'WHITE', 'BLUE', 'BROWN', 'PINK', 'YELLOW', 'ORANGE', 'CREAM', 'ORANGE', 'RED', 'WHITE', 'BLUE', 'WHITE', 'BLUE', 'BLUE', 'BLUE', 'GREEN']
FRIDAY = ['GREEN', 'WHITE', 'GREEN', 'BROWN', 'BLUE', 'BLUE', 'BLACK', 'WHITE', 'ORANGE', 'RED', 'RED', 'RED', 'WHITE', 'BLUE', 'WHITE', 'BLUE', 'BLUE', 'BLUE', 'WHITE']

# counting for monday...
mon_total_count = len(MONDAY)
mon_green_count = MONDAY.count('GREEN')
mon_yellow_count = MONDAY.count('YELLOW')
mon_brown_count = MONDAY.count('BROWN')
mon_blue_count = MONDAY.count('BLUE')
mon_pink_count = MONDAY.count('PINK')
mon_orange_count = MONDAY.count('ORANGE')
mon_cream_count = MONDAY.count('CREAM')
mon_red_count = MONDAY.count('RED')
mon_white_count = MONDAY.count('WHITE')

# checking accuracy per day...
#print('Monday:')
#print(mon_total_count)
#print(mon_green_count, mon_yellow_count, mon_brown_count, mon_blue_count, mon_pink_count, mon_cream_count, mon_orange_count, mon_red_count, mon_white_count)
#print(mon_green_count + mon_yellow_count + mon_brown_count + mon_blue_count + mon_pink_count + mon_cream_count + mon_orange_count + mon_red_count + mon_white_count)
#print(' ')

# counting for TUESDAY...
tues_total_count = len(TUESDAY)
tues_green_count = TUESDAY.count('GREEN')
tues_yellow_count = TUESDAY.count('YELLOW')
tues_brown_count = TUESDAY.count('BROWN')
tues_blue_count = TUESDAY.count('BLUE')
tues_pink_count = TUESDAY.count('PINK')
tues_orange_count = TUESDAY.count('ORANGE')
tues_cream_count = TUESDAY.count('CREAM')
tues_red_count = TUESDAY.count('RED')
tues_white_count = TUESDAY.count('WHITE')
tues_arsh_count = TUESDAY.count('ARSH')
tues_blew_count = TUESDAY.count('BLEW')

# checking accuracy per day...
#print('Tuesday:')
#print(tues_total_count)
#print(tues_green_count, tues_yellow_count, tues_brown_count, tues_blue_count, tues_pink_count, tues_cream_count, tues_orange_count, tues_red_count, tues_white_count, tues_arsh_count, tues_blew_count)
#print(tues_green_count + tues_yellow_count + tues_brown_count + tues_blue_count + tues_pink_count + tues_cream_count + tues_orange_count + tues_red_count + tues_white_count + tues_arsh_count + tues_blew_count)
#print(' ')

# counting for WEDNESDAY...
wed_total_count = len(WEDNESDAY)
wed_green_count = WEDNESDAY.count('GREEN')
wed_yellow_count = WEDNESDAY.count('YELLOW')
wed_brown_count = WEDNESDAY.count('BROWN')
wed_blue_count = WEDNESDAY.count('BLUE')
wed_pink_count = WEDNESDAY.count('PINK')
wed_orange_count = WEDNESDAY.count('ORANGE')
wed_cream_count = WEDNESDAY.count('CREAM')
wed_red_count = WEDNESDAY.count('RED')
wed_white_count = WEDNESDAY.count('WHITE')

# checking accuracy per day...
#print('Wednesday:')
#print(wed_total_count)
#print(wed_green_count, wed_yellow_count, wed_brown_count, wed_blue_count, wed_pink_count, wed_cream_count, wed_orange_count, wed_red_count, wed_white_count)
#print(wed_green_count + wed_yellow_count + wed_brown_count + wed_blue_count + wed_pink_count + wed_cream_count + wed_orange_count + wed_red_count + wed_white_count)
#print(' ')

# counting for THURSDAY...
thurs_total_count = len(THURSDAY)
thurs_green_count = THURSDAY.count('GREEN')
thurs_yellow_count = THURSDAY.count('YELLOW')
thurs_brown_count = THURSDAY.count('BROWN')
thurs_blue_count = THURSDAY.count('BLUE')
thurs_pink_count = THURSDAY.count('PINK')
thurs_orange_count = THURSDAY.count('ORANGE')
thurs_cream_count = THURSDAY.count('CREAM')
thurs_red_count = THURSDAY.count('RED')
thurs_white_count = THURSDAY.count('WHITE')

# checking accuracy per day...
#print('Thursday:')
#print(thurs_total_count)
#print(thurs_green_count, thurs_yellow_count, thurs_brown_count, thurs_blue_count, thurs_pink_count, thurs_cream_count, thurs_orange_count, thurs_red_count, thurs_white_count)
#print(thurs_green_count + thurs_yellow_count + thurs_brown_count + thurs_blue_count + thurs_pink_count + thurs_cream_count + thurs_orange_count + thurs_red_count + thurs_white_count)
#print(' ')

# counting for FRIDAY...
fri_total_count = len(FRIDAY)
fri_green_count = FRIDAY.count('GREEN')
fri_yellow_count = FRIDAY.count('YELLOW')
fri_brown_count = FRIDAY.count('BROWN')
fri_blue_count = FRIDAY.count('BLUE')
fri_pink_count = FRIDAY.count('PINK')
fri_orange_count = FRIDAY.count('ORANGE')
fri_cream_count = FRIDAY.count('CREAM')
fri_red_count = FRIDAY.count('RED')
fri_white_count = FRIDAY.count('WHITE')
fri_black_count = FRIDAY.count('BLACK')

# checking accuracy per day...
#print('Friday:')
#print(fri_total_count)
#print(fri_green_count, fri_yellow_count, fri_brown_count, fri_blue_count, fri_pink_count, fri_cream_count, fri_orange_count, fri_red_count, fri_white_count, fri_black_count)
#print(fri_green_count + fri_yellow_count + fri_brown_count + fri_blue_count + fri_pink_count + fri_cream_count + fri_orange_count + fri_red_count + fri_white_count + fri_black_count)
#print(' ')



# MAIN Test Answers
All_lists.extend(MONDAY)
All_lists.extend(TUESDAY)
All_lists.extend(WEDNESDAY)
All_lists.extend(THURSDAY)
All_lists.extend(FRIDAY)

all_lists_total_count = len(All_lists)
all_lists_green_count = All_lists.count('GREEN')
all_lists_yellow_count = All_lists.count('YELLOW')
all_lists_brown_count = All_lists.count('BROWN')
all_lists_blue_count = All_lists.count('BLUE')
all_lists_pink_count = All_lists.count('PINK')
all_lists_orange_count = All_lists.count('ORANGE')
all_lists_cream_count = All_lists.count('CREAM')
all_lists_red_count = All_lists.count('RED')
all_lists_white_count = All_lists.count('WHITE')
all_lists_arsh_count = All_lists.count('ARSH')
all_lists_blew_count = All_lists.count('BLEW')
all_lists_black_count = All_lists.count('BLACK')

all_num_list = [all_lists_green_count, all_lists_yellow_count, all_lists_brown_count, all_lists_blue_count, all_lists_pink_count, all_lists_cream_count, all_lists_orange_count, all_lists_red_count, all_lists_white_count, all_lists_arsh_count, all_lists_blew_count, all_lists_black_count]
probability_of_picking_red = all_lists_red_count / all_lists_total_count

cur.execute(f"""INSERT INTO shirt_color (name, frequency) VALUES ('GREEN', {all_lists_green_count}) ON CONFLICT (name) DO NOTHING """)
cur.execute(f"""INSERT INTO shirt_color (name, frequency) VALUES ('YELLOW', {all_lists_yellow_count}) ON CONFLICT (name) DO NOTHING """)
cur.execute(f"""INSERT INTO shirt_color (name, frequency) VALUES ('BROWN', {all_lists_brown_count}) ON CONFLICT (name) DO NOTHING """)
cur.execute(f"""INSERT INTO shirt_color (name, frequency) VALUES ('BLUE', {all_lists_blue_count}) ON CONFLICT (name) DO NOTHING """)
cur.execute(f"""INSERT INTO shirt_color (name, frequency) VALUES ('PINK', {all_lists_pink_count}) ON CONFLICT (name) DO NOTHING """)
cur.execute(f"""INSERT INTO shirt_color (name, frequency) VALUES ('ORANGE', {all_lists_orange_count}) ON CONFLICT (name) DO NOTHING """)
cur.execute(f"""INSERT INTO shirt_color (name, frequency) VALUES ('CREAM', {all_lists_cream_count}) ON CONFLICT (name) DO NOTHING """)
cur.execute(f"""INSERT INTO shirt_color (name, frequency) VALUES ('RED', {all_lists_red_count}) ON CONFLICT (name) DO NOTHING """)
cur.execute(f"""INSERT INTO shirt_color (name, frequency) VALUES ('WHITE', {all_lists_white_count}) ON CONFLICT (name) DO NOTHING """)
cur.execute(f"""INSERT INTO shirt_color (name, frequency) VALUES ('ARSH', {all_lists_arsh_count}) ON CONFLICT (name) DO NOTHING """)
cur.execute(f"""INSERT INTO shirt_color (name, frequency) VALUES ('BLEW', {all_lists_blew_count}) ON CONFLICT (name) DO NOTHING """)
cur.execute(f"""INSERT INTO shirt_color (name, frequency) VALUES ('BLACK', {all_lists_black_count}) ON CONFLICT (name) DO NOTHING """)
conn.commit()

cur.close()
conn.close()

print('All List:')
print(all_lists_total_count)
print(all_num_list)
print(sum(all_num_list))
print(' ')

print('Mean color through the week:', st.mean(all_num_list))
print('Most worn color through the week:', st.mode(All_lists))
print('Median color through the week:', st.median(All_lists))
print('Variance of the colors:', st.variance(all_num_list))
print('Probability of picking a red shirt:', probability_of_picking_red)
print(' ')


def four_digit_binary(n):
    bin_list =''
    decimal_u = 0
    power = 0
    
    for x in range(n):
        random_num = ran.randint(0, 1)
        bin_list += str(random_num)
    print('Binary Form:', bin_list)
        
    for d in bin_list:
        decimal_u += int(d) * 2 ** power
        power += 1
        
    print('Decimal Form:', decimal_u)
    print(' ')

four_digit_binary(4)

def fibonacci_sequence(n):
    a, b = 0, 1
    
    all_nums = []
    sum_all_nums = int(0)
    for x in range(n):
        fs_num = a
        all_nums.append(fs_num)
        sum_all_nums += int(fs_num)
        a, b = b, a + b
        
    print('List of', n, 'fibonacci num =', all_nums)
    print(' ')
    print('Sum of', n, 'fibonacci num =', sum_all_nums)
    print(' ')

fibonacci_sequence(50)

#Thank you :)