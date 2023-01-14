from math import degrees, radians, sqrt, sin, cos, asin, acos
from tkinter import *

while True:
    cycle = 0 #Resetting the calculation cycle counter

    def result(): #Completion of the program
        global cycle, smaller_base, bigger_base, left_side, right_side, middle_line, height, lower_left_corner, lower_right_corner, upper_left_corner, upper_right_corner, first_diagonal, second_diagonal, first_angle_between_diagonals, second_angle_between_diagonals, square, perimeter, isosceles, rectangular, radius_inscribed_circle, radius_circumscribed_circle

        if cycle == 1: #The first cycle - due to recursion, there is a check

            def check_1():
                print(f'\nStarted anew!')
                window.destroy() #Destroying the current window

            #Destruction of unnecessary fields

            isosceles_True.destroy()
            isosceles_False.destroy()
            isosceles_Unknown.destroy()

            rectangular_True.destroy()
            rectangular_False.destroy()
            rectangular_Unknown.destroy()

            smaller_base_selected.destroy()

            bigger_base_selected.destroy()

            height_selected.destroy()

            left_side_selected.destroy()

            right_side_selected.destroy()

            middle_line_selected.destroy()

            square_selected.destroy()

            perimeter_selected.destroy()

            first_diagonal_selected.destroy()

            second_diagonal_selected.destroy()

            lower_left_corner_selected.destroy()

            lower_right_corner_selected.destroy()

            upper_left_corner_selected.destroy()

            upper_right_corner_selected.destroy()

            first_angle_between_diagonals_selected.destroy()

            second_angle_between_diagonals_selected.destroy()

            radius_inscribed_circle_True.destroy()
            radius_inscribed_circle_False.destroy()
            radius_inscribed_circle_Known.destroy()

            radius_circumscribed_circle_True.destroy()
            radius_circumscribed_circle_False.destroy()
            radius_circumscribed_circle_Known.destroy()

            #Replacing null values with a skip

            if isosceles == -1:
                isosceles = ''
            if rectangular == -1:
                rectangular = ''
            if smaller_base == -1:
                smaller_base = ''
            if bigger_base == -1:
                bigger_base = ''
            if left_side == -1:
                left_side = ''
            if right_side == -1:
                right_side = ''
            if middle_line == -1:
                middle_line = ''
            if height == -1:
                height = ''
            if square == -1:
                square = ''
            if perimeter == -1:
                perimeter = ''
            if first_diagonal == -1:
                first_diagonal = ''
            if second_diagonal == -1:
                second_diagonal = ''
            if lower_left_corner == -1:
                lower_left_corner = ''
            if lower_right_corner == -1:
                lower_right_corner = ''
            if upper_left_corner == -1:
                upper_left_corner = ''
            if upper_right_corner == -1:
                upper_right_corner = ''
            if first_angle_between_diagonals == -1:
                first_angle_between_diagonals = ''
            if second_angle_between_diagonals == -1:
                second_angle_between_diagonals = ''
            if radius_inscribed_circle == -1:
                radius_inscribed_circle = ''
            if radius_circumscribed_circle == -1:
                radius_circumscribed_circle = ''

            # Output of results

            first_top_button.configure(text = 'Clear fields', command = check_1) #Editing the button, when calculating values

            isosceles_Label = Label(text = str(isosceles))
            isosceles_Label.grid(column = 1, row = 1)

            rectangular_Label = Label(text = str(rectangular))
            rectangular_Label.grid(column = 1, row = 2)

            smaller_base_Label = Label(text = smaller_base)
            smaller_base_Label.grid(column = 1, row = 3)

            bigger_base_Label = Label(text = bigger_base)
            bigger_base_Label.grid(column = 1, row = 4)

            height_Label = Label(text = height)
            height_Label.grid(column = 1, row = 5)

            left_side_Label = Label(text = left_side)
            left_side_Label.grid(column = 1, row = 6)

            right_side_Label = Label(text = right_side)
            right_side_Label.grid(column = 1, row = 7)

            middle_line_Label = Label(text =  middle_line)
            middle_line_Label.grid(column = 1, row = 8)

            square_Label = Label(text = square)
            square_Label.grid(column = 1, row = 9)

            perimeter_Label = Label(text = perimeter)
            perimeter_Label.grid(column = 1, row = 10)

            first_diagonal_Label = Label(text = first_diagonal)
            first_diagonal_Label.grid(column = 1, row = 11)

            second_diagonal_Label = Label(text = second_diagonal)
            second_diagonal_Label.grid(column = 1, row = 12)

            upper_left_corner_Label = Label(text = upper_left_corner)
            upper_left_corner_Label.grid(column = 1, row = 13)

            upper_right_corner_Label = Label(text = upper_right_corner)
            upper_right_corner_Label.grid(column = 1, row = 14)

            lower_left_corner_Label = Label(text = lower_left_corner)
            lower_left_corner_Label.grid(column = 1, row = 15)

            lower_right_corner_Label = Label(text = lower_right_corner)
            lower_right_corner_Label.grid(column = 1, row = 16)

            first_angle_between_diagonals_Label = Label(text = first_angle_between_diagonals)
            first_angle_between_diagonals_Label.grid(column = 1, row = 17)

            second_angle_between_diagonals_Label = Label(text = second_angle_between_diagonals)
            second_angle_between_diagonals_Label.grid(column = 1, row = 18)

            radius_inscribed_circle_Label = Label(text = str(radius_inscribed_circle))
            radius_inscribed_circle_Label.grid(column = 1, row = 19)

            radius_circumscribed_circle_Label = Label(text = str(radius_circumscribed_circle))
            radius_circumscribed_circle_Label.grid(column = 1, row = 20)

            print('All the information that was calculated as a result of the program: ')
            print(f'Trapezoid isosceles = {isosceles}')
            print(f'The trapezoid is rectangular = {rectangular}')
            print(f'Smaller base = {smaller_base}')
            print(f'Bigger base = {bigger_base}')
            print(f'Trapezoid height = {height}')
            print(f'Left side = {left_side}')
            print(f'Right side = {right_side}')
            print(f'Middle line = {middle_line}')
            print(f'Trapezoid area = {square}')
            print(f'Perimeter of the trapezoid = {perimeter}')
            print(f'Diagonal from the lower left corner to the upper right = {first_diagonal}')
            print(f'Diagonal from the lower right corner to the upper left = {second_diagonal}')
            print(f'Left corner with a larger base, in degrees = {lower_left_corner}')
            print(f'Right angle with a larger base, in degrees = {lower_right_corner}')
            print(f'Left corner with a smaller base, in degrees = {upper_left_corner}')
            print(f'Right angle with a smaller base, in degrees= {upper_right_corner}')
            print(f'The angle between the diagonals, resting on the side = {first_angle_between_diagonals}')
            print(f'The angle between the diagonals, resting on the base = {second_angle_between_diagonals}')
            print(f'Radius of the inscribed circle = {radius_inscribed_circle}')
            print(f'The radius of the circumscribed circle = {radius_circumscribed_circle}\n\n')

    def check(): #Calculating values
        global cycle, smaller_base, bigger_base, left_side, right_side, middle_line, height, lower_left_corner, lower_right_corner, upper_left_corner, upper_right_corner, first_diagonal, second_diagonal, first_angle_between_diagonals, second_angle_between_diagonals, square, perimeter, isosceles, rectangular, radius_inscribed_circle, radius_circumscribed_circle

        if False != isosceles != True: #It is unknown whether the trapezoid is isosceles or not
            if left_side == right_side > 0:
                isosceles = True
                print(f'Condition left_side == right_side > 0 completed, then:\nisosceles = True\nTrapezoid isosceles = {isosceles}\n')

            elif lower_left_corner == lower_right_corner > 0:
                isosceles = True
                print(f'Condition lower_left_corner == lower_right_corner > 0 completed, then:\nisosceles = True\nTrapezoid isosceles = {isosceles}\n')

            elif first_diagonal == second_diagonal > 0:
                isosceles = True
                print(f'Condition first_diagonal == second_diagonal > 0 completed, then:\nisosceles = True\nTrapezoid isosceles = {isosceles}\n')

            elif first_angle_between_diagonals == second_angle_between_diagonals > 0:
                isosceles = True
                print(f'Condition first_angle_between_diagonals == second_angle_between_diagonals > 0 completed, then:\nisosceles = True\nTrapezoid isosceles = {isosceles}\n')

            elif radius_circumscribed_circle > 0:
                isosceles = True
                print(f'Condition radius_circumscribed_circle > 0 completed, then:\nisosceles = True\nTrapezoid isosceles = {isosceles}\n')

            elif left_side > 0 < right_side and left_side != right_side:
                isosceles = False
                print(f'Condition left_side > 0 < right_side and left_side != right_side completed, then:\nisosceles = False\nTrapezoid isosceles = {isosceles}\n')

            elif first_diagonal > 0 < second_diagonal and first_diagonal != second_diagonal:
                isosceles = False
                print(f'Condition first_diagonal > 0 < second_diagonal and first_diagonal != second_diagonal completed, then:\nisosceles = False\nTrapezoid isosceles = {isosceles}\n')

            elif lower_left_corner > 0 < lower_right_corner and lower_left_corner != lower_right_corner:
                isosceles = False
                print(f'Condition lower_left_corner > 0 < lower_right_corner and lower_left_corner != lower_right_corner completed, then:\nisosceles = False\nTrapezoid isosceles = {isosceles}\n')

            if isosceles == False or isosceles == True:
                check()

        if False != rectangular != True: #It is unknown whether the trapezoid is rectangular or not
            if left_side == height > 0:
                rectangular = True
                print(f'Condition left_side == height > 0 completed, then:\nrectangular == True\nTrapezoid isosceles = {rectangular}\n')

            elif right_side == height > 0:
                rectangular = True
                print(f'Condition right_side == height > 0 completed, then:\nrectangular == True\nTrapezoid isosceles = {rectangular}\n')

            elif lower_left_corner == 90:
                rectangular = True
                print(f'Condition lower_left_corner == 90 completed, then:\nrectangular == True\nTrapezoid isosceles = {rectangular}\n')

            elif lower_right_corner == 90:
                rectangular = True
                print(f'Condition lower_right_corner == 90 completed, then:\nrectangular == True\nTrapezoid isosceles = {rectangular}\n')

            elif lower_left_corner > 0 < lower_right_corner and lower_left_corner != 90 != lower_right_corner:
                rectangular = False
                print(f'Condition lower_left_corner > 0 < lower_right_corner and lower_left_corner != 90 != lower_right_corner completed, then:\nrectangular == False\nTrapezoid isosceles = {rectangular}\n')

            if rectangular == False or rectangular == True:
                check()

        if smaller_base <= 0: #Smaller base is unknown
            if bigger_base > 0 and middle_line > 0:
                smaller_base = 2 * middle_line - bigger_base * cos(radians(lower_right_corner))
                print(f'Condition bigger_base > 0 and middle_line > 0 completed, then:\nsmaller_base = 2 * middle_line - bigger_base * cos(radians(lower_right_corner))\nSmaller base = {smaller_base}\n')

            elif bigger_base > 0 and first_diagonal > 0 < second_diagonal and first_angle_between_diagonals > 0:
                smaller_base = first_diagonal * second_diagonal / height * sin(radians(first_angle_between_diagonals)) - bigger_base
                print(f'Condition bigger_base > 0 and first_diagonal > 0 < second_diagonal and first_angle_between_diagonals > 0 completed, then:\nsmaller_base = first_diagonal * second_diagonal / height * sin(radians(first_angle_between_diagonals)) - bigger_base\nSmaller base = {smaller_base}\n')

            elif bigger_base > 0 and height > 0 and lower_left_corner > 0 < lower_right_corner:
                smaller_base = bigger_base - height * (cos(radians(lower_left_corner)) / sin(radians(lower_left_corner)) + cos(radians(lower_right_corner)) / sin(radians(lower_right_corner)))
                print(f'Condition bigger_base > 0 and height > 0 and lower_left_corner > 0 < lower_right_corner completed, then:\nsmaller_base = bigger_base - height * (cos(radians(lower_left_corner)) / sin(radians(lower_left_corner)) + cos(radians(lower_right_corner)) / sin(radians(lower_right_corner)))\nSmaller base = {smaller_base}\n')

            elif bigger_base > 0 and left_side > 0 < right_side and lower_left_corner > 0 < lower_right_corner:
                smaller_base = bigger_base - left_side * cos(radians(lower_left_corner)) - right_side * cos(radians(lower_right_corner))
                print(f'Condition bigger_base > 0 and left_side > 0 < right_side and lower_left_corner > 0 < lower_right_corner completed, then:\nsmaller_base = bigger_base - left_side * cos(radians(lower_left_corner)) - right_side * cos(radians(lower_right_corner))\nSmaller base = {smaller_base}\n')

            elif bigger_base > 0 and left_side > 0 < right_side and height > 0:
                bigger_base = bigger_base - sqrt(left_side**2 - height**2) - sqrt(right_side**2 - height**2)
                print(f'Condition bigger_base > 0 and left_side > 0 < right_side and height > 0 completed, then:\nbigger_base = bigger_base - sqrt(left_side**2 - height**2) - sqrt(right_side**2 - height**2)\nSmaller base = {smaller_base}\n')

            elif isosceles == True:
                if bigger_base > 0 and height > 0 and lower_left_corner > 0:
                    smaller_base = bigger_base - 2 * height * (cos(radians(lower_left_corner)) / sin(radians(lower_left_corner)))
                    print(f'Condition isosceles == True and bigger_base > 0 and height > 0 and lower_left_corner > 0 completed, then:\nsmaller_base = bigger_base - 2 * height * (cos(radians(lower_left_corner)) / sin(radians(lower_left_corner)))\nSmaller base = {smaller_base}\n')

                elif bigger_base > 0 and left_side > 0 and second_diagonal > 0:
                    smaller_base = (second_diagonal**2 - left_side**2) / bigger_base
                    print(f'Condition isosceles == True and bigger_base > 0 and left_side > 0 and second_diagonal > 0 completed, then:\nsmaller_base = (second_diagonal**2 - left_side**2) / bigger_base\nSmaller base = {smaller_base}\n')

                elif bigger_base > 0 and height > 0 and first_diagonal > 0 and first_angle_between_diagonals > 0:
                    smaller_base = first_diagonal**2 / height * sin(radians(first_angle_between_diagonals)) - bigger_base
                    print(f'Condition isosceles == True and bigger_base > 0 and height > 0 and first_diagonal > 0 and first_angle_between_diagonals > 0 completed, then:\nsmaller_base = first_diagonal**2 / height * sin(radians(first_angle_between_diagonals)) - bigger_base\nSmaller base = {smaller_base}\n')

                elif bigger_base > 0 and height > 0 and square > 0:
                    smaller_base = 2 * square / height - bigger_base
                    print(f'Conditions isosceles == True and bigger_base > 0 and height > 0 and square > 0 completed, then:\nsmaller_base = 2 * square / height - bigger_base\nSmaller base = {smaller_base}\n')

                elif bigger_base > 0 and radius_inscribed_circle > 0 and radius_inscribed_circle != True:
                    smaller_base = 4 * radius_inscribed_circle**2 / bigger_base
                    print(f'Conditions isosceles == True and bigger_base > 0 and radius_inscribed_circle > 0 and radius_inscribed_circle != True completed, then:\nsmaller_base = 4 * radius_inscribed_circle**2 / bigger_base\nSmaller base = {smaller_base}\n')

            elif rectangular == True:
                if bigger_base > 0 and height > 0 and lower_left_corner > 0 < lower_right_corner:
                    smaller_base = bigger_base - height * cos(radians(min(lower_left_corner, lower_right_corner))) / sin(radians(min(lower_left_corner, lower_right_corner)))
                    print(f'Conditions rectangular == True and bigger_base > 0 and height > 0 and lower_left_corner > 0 < lower_right_corner completed, then:\nsmaller_base = bigger_base - height * cos(radians(min(lower_left_corner, lower_right_corner))) / sin(radians(min(lower_left_corner, lower_right_corner)))\nSmaller base = {smaller_base}\n')

                elif bigger_base > 0 and left_side > 0 < right_side and lower_left_corner > 0 < lower_right_corner:
                    smaller_base = bigger_base - max(left_side, right_side) * cos(radians(min(lower_left_corner, lower_right_corner)))
                    print(f'Conditions rectangular == True and bigger_base > 0 and left_side > 0 < right_side and lower_left_corner > 0 < lower_right_corner completed, then:\nsmaller_base = bigger_base - max(left_side, right_side) * cos(radians(min(lower_left_corner, lower_right_corner)))\nSmaller base = {smaller_base}\n')

                elif bigger_base > 0 and left_side > 0 < right_side:
                    smaller_base = bigger_base - sqrt(max(left_side, right_side)**2 - height**2)
                    print(f'Conditions rectangular == True and bigger_base > 0 and left_side > 0 < right_side completed, then:\nsmaller_base = bigger_base - sqrt(max(left_side, right_side)**2 - height**2)\nSmaller base = {smaller_base}\n')

                elif bigger_base > 0 and height > 0 and first_diagonal > 0 < second_diagonal and first_angle_between_diagonals > 0:
                    smaller_base = first_diagonal * second_diagonal / height * sin(radians(first_angle_between_diagonals)) - bigger_base
                    print(f'Conditions rectangular == True and bigger_base > 0 and height > 0 and first_diagonal > 0 < second_diagonal and first_angle_between_diagonals > 0 completed, then:\nsmaller_base = first_diagonal * second_diagonal / height * sin(radians(first_angle_between_diagonals)) - bigger_base\nSmaller base = {smaller_base}\n')

                elif bigger_base > 0 and height > 0 and square > 0:
                    smaller_base = 2 * square / height - bigger_base
                    print(f'Conditions rectangular == True and bigger_base > 0 and height > 0 and square > 0 completed, then:\nsmaller_base = 2 * square / height - bigger_base\nSmaller base = {smaller_base}\n')

            if smaller_base > 0:
                check()

        if bigger_base <= 0: #Bigger base is unknown
            if smaller_base > 0 and middle_line > 0:
                bigger_base = 2 * middle_line - smaller_base
                print(f'Condition smaller_base > 0 and middle_line > 0 completed, then:\nbigger_base = 2 * middle_line - smaller_base\nBigger base = {bigger_base}\n')

            elif smaller_base > 0 and height > 0 and first_diagonal > 0 < second_diagonal and first_angle_between_diagonals > 0:
                bigger_base = first_diagonal * second_diagonal / height * sin(radians(first_angle_between_diagonals)) - smaller_base
                print(f'Condition smaller_base > 0 and height > 0 and first_diagonal > 0 < second_diagonal and first_angle_between_diagonals > 0 completed, then:\nbigger_base = first_diagonal * second_diagonal / height * sin(radians(first_angle_between_diagonals)) - smaller_base\nBigger base = {bigger_base}\n')

            elif smaller_base > 0 and height > 0 and lower_left_corner > 0 < lower_right_corner:
                bigger_base = smaller_base + height * (cos(radians(lower_left_corner)) / sin(radians(lower_left_corner)) + cos(radians(lower_right_corner)) / sin(radians(lower_right_corner)))
                print(f'Condition smaller_base > 0 and height > 0 and lower_left_corner > 0 < lower_right_corner completed, then:\nbigger_base = smaller_base + height * (cos(radians(lower_left_corner)) / sin(radians(lower_left_corner)) + cos(radians(lower_right_corner)) / sin(radians(lower_right_corner)))\nBigger base = {bigger_base}\n')

            elif smaller_base > 0 and left_side > 0 < right_side and lower_left_corner > 0 < lower_right_corner:
                bigger_base = smaller_base + left_side * cos(radians(lower_left_corner)) + right_side * cos(radians(lower_right_corner))
                print(f'Condition smaller_base > 0 and left_side > 0 < right_side and lower_left_corner > 0 < lower_right_corner completed, then:\nbigger_base = smaller_base + left_side * cos(radians(lower_left_corner)) + right_side * cos(radians(lower_right_corner))\nBigger base = {bigger_base}\n')

            elif smaller_base > 0 and left_side > 0 < right_side and height > 0:
                bigger_base = smaller_base + sqrt(left_side**2 - height**2) + sqrt(right_side**2 - height**2)
                print(f'Condition smaller_base > 0 and left_side > 0 < right_side and height > 0 completed, then:\nbigger_base = smaller_base + sqrt(left_side**2 - height**2) + sqrt(right_side**2 - height**2)\nBigger base = {bigger_base}\n')

            elif isosceles:
                if smaller_base > 0 and height > 0 and lower_left_corner > 0:
                    bigger_base = smaller_base + 2 * height * (cos(radians(lower_left_corner)) / sin(radians(lower_left_corner)))
                    print(f'Conditions isosceles == True and smaller_base > 0 and height > 0 and lower_left_corner > 0 completed, then:\nbigger_base = smaller_base + 2 * height * (cos(radians(lower_left_corner)) / sin(radians(lower_left_corner)))\nBigger base = {bigger_base}\n')

                elif smaller_base > 0 and left_side > 0 and second_diagonal > 0:
                    bigger_base = (second_diagonal**2 - left_side**2) / smaller_base
                    print(f'Conditions isosceles == True and smaller_base > 0 and left_side > 0 and second_diagonal > 0 completed, then:\nbigger_base = (second_diagonal**2 - left_side**2) / smaller_base\nBigger base = {bigger_base}\n')

                elif smaller_base > 0 and height > 0 and first_diagonal > 0 and first_angle_between_diagonals > 0:
                    bigger_base = first_diagonal**2 / height * sin(radians(first_angle_between_diagonals)) - smaller_base
                    print(f'Conditions isosceles == True and smaller_base > 0 and height > 0 and first_diagonal > 0 and first_angle_between_diagonals > 0 completed, then:\nbigger_base = first_diagonal**2 / height * sin(radians(first_angle_between_diagonals)) - smaller_base\nBigger base = {bigger_base}\n')

                elif smaller_base > 0 and height > 0 and square > 0:
                    bigger_base = 2 * square / height - smaller_base
                    print(f'Conditions isosceles == True and smaller_base > 0 and height > 0 and square > 0 completed, then:\nbigger_base = 2 * square / height - smaller_base\nBigger base = {bigger_base}\n')

                elif smaller_base > 0 and radius_inscribed_circle > 0 and radius_inscribed_circle != True:
                    bigger_base = 4 * radius_inscribed_circle**2 / smaller_base
                    print(f'Conditions isosceles == True and smaller_base > 0 and radius_inscribed_circle > 0 and radius_inscribed_circle != True completed, then:\nbigger_base = 4 * radius_inscribed_circle**2 / smaller_base\nBigger base = {bigger_base}\n')

            elif rectangular == True:
                if smaller_base > 0 and height > 0 and lower_left_corner > 0 < lower_right_corner:
                    bigger_base = smaller_base + height * cos(radians(min(lower_left_corner, lower_right_corner))) / sin(radians(min(lower_left_corner, lower_right_corner)))
                    print(f'Conditions rectangular == True and smaller_base > 0 and height > 0 and lower_left_corner > 0 < lower_right_corner completed, then:\nbigger_base = smaller_base + height * cos(radians(min(lower_left_corner, lower_right_corner))) / sin(radians(min(lower_left_corner, lower_right_corner)))\nBigger base = {bigger_base}\n')

                elif smaller_base > 0 and left_side > 0 < right_side and lower_left_corner > 0 < lower_right_corner:
                    bigger_base = smaller_base + max(left_side, right_side) * cos(radians(min(lower_left_corner, lower_right_corner)))
                    print(f'Conditions rectangular == True and smaller_base > 0 and left_side > 0 < right_side and lower_left_corner > 0 < lower_right_corner completed, then:\nbigger_base = smaller_base + max(left_side, right_side) * cos(radians(min(lower_left_corner, lower_right_corner)))\nBigger base = {bigger_base}\n')

                elif smaller_base > 0 and left_side > 0 < right_side:
                    bigger_base = smaller_base + sqrt(max(left_side, right_side)**2 - height**2)
                    print(f'Conditions rectangular == True and smaller_base > 0 and left_side > 0 < right_side completed, then:\nbigger_base = smaller_base + sqrt(max(left_side, right_side)**2 - height**2)\nBigger base = {bigger_base}\n')

                elif smaller_base > 0 and height > 0 and square > 0:
                    bigger_base = 2 * square / height - smaller_base
                    print(f'Conditions rectangular == True and smaller_base > 0 and height > 0 and square > 0 completed, then:\nbigger_base = 2 * square / height - smaller_base\nBigger base = {bigger_base}\n')

            if bigger_base > 0:
                check()

        if height <= 0: #Height unknown
            if smaller_base > 0 < bigger_base and left_side > 0 < right_side:
                height = sqrt(right_side**2 - (((bigger_base - smaller_base)**2 + right_side**2 - left_side**2) / (2 * (bigger_base - smaller_base)))**2)
                print(f'Condition smaller_base > 0 < bigger_base and left_side > 0 < right_side completed, then:\nheight = sqrt(right_side**2 - (((bigger_base - smaller_base)**2 + right_side**2 - left_side**2) / (2 * (bigger_base - smaller_base)))**2)\nTrapezoid height = {height}\n')

            elif left_side > 0 and lower_left_corner > 0:
                height = left_side * sin(radians(lower_left_corner))
                print(f'Condition left_side > 0 and lower_left_corner > 0 completed, then:\nheight = left_side * sin(radians(lower_left_corner))\nTrapezoid height = {height}\n')

            elif right_side > 0 and lower_right_corner > 0:
                height = right_side * sin(radians(lower_right_corner))
                print(f'Condition right_side > 0 and lower_right_corner > 0 completed, then:\nheight = right_side * sin(radians(lower_right_corner))\nTrapezoid height = {height}\n')

            elif smaller_base > 0 < bigger_base and first_diagonal > 0 < second_diagonal and first_angle_between_diagonals > 0:
                height = first_diagonal * second_diagonal / (smaller_base + bigger_base) * sin(radians(first_angle_between_diagonals))
                print(f'Condition smaller_base > 0 < bigger_base and first_diagonal > 0 < second_diagonal and first_angle_between_diagonals > 0 completed, then:\nheight = first_diagonal * second_diagonal / (smaller_base + bigger_base) * sin(radians(first_angle_between_diagonals))\nTrapezoid height = {height}\n')

            elif middle_line > 0 and first_diagonal > 0 < second_diagonal and first_angle_between_diagonals > 0:
                height = first_diagonal * second_diagonal / (2 * middle_line) * sin(radians(first_angle_between_diagonals))
                print(f'Condition middle_line > 0 and first_diagonal > 0 < second_diagonal and first_angle_between_diagonals > 0 completed, then:\nheight = first_diagonal * second_diagonal / (2 * middle_line) * sin(radians(first_angle_between_diagonals))\nTrapezoid height = {height}\n')

            elif middle_line > 0 and square > 0:
                height = square / middle_line
                print(f'Condition middle_line > 0 and square > 0 completed, then:\nheight = square / middle_line\nTrapezoid height = {height}\n')

            elif isosceles:
                if smaller_base > 0 < bigger_base and left_side > 0:
                    height = sqrt(left_side**2 - (bigger_base - smaller_base)**2 / 4)
                    print(f'Conditions isosceles == True and smaller_base > 0 < bigger_base and left_side > 0 completed, then:\nheight = sqrt(left_side**2 - (bigger_base - smaller_base)**2 / 4)\nTrapezoid height = {height}\n')

                elif left_side > 0 and lower_left_corner > 0:
                    height = left_side * sin(radians(lower_left_corner))
                    print(f'Conditions isosceles == True and left_side > 0 and lower_left_corner > 0 completed, then:\nheight = left_side * sin(radians(lower_left_corner))\nTrapezoid height = {height}\n')

                elif smaller_base > 0 < bigger_base and lower_left_corner > 0:
                    height = (bigger_base - smaller_base) * sin(radians(lower_left_corner)) / cos(radians(lower_left_corner))
                    print(f'Conditions isosceles == True and smaller_base > 0 < bigger_base and lower_left_corner > 0 completed, then:\nheight = (bigger_base - smaller_base) / 2 * sin(radians(lower_left_corner) / cos(radians(lower_left_corner)))\nTrapezoid height = {height}\n')

                elif smaller_base > 0 < bigger_base and second_diagonal > 0 and first_angle_between_diagonals > 0:
                    height = second_diagonal**2 / (smaller_base + bigger_base) * sin(radians(first_angle_between_diagonals))
                    print(f'Conditions isosceles == True and smaller_base > 0 < bigger_base and second_diagonal > 0 and first_angle_between_diagonals > 0 completed, then:\nheight = second_diagonal**2 / (smaller_base + bigger_base) * sin(radians(first_angle_between_diagonals))\nTrapezoid height = {height}\n')

                elif middle_line > 0 and square > 0:
                    height = square / middle_line
                    print(f'Conditions isosceles == True and middle_line > 0 and square > 0 completed, then:\nheight = square / middle_line\nTrapezoid height = {height}\n')

                elif radius_inscribed_circle > 0 and radius_inscribed_circle != True:
                    height = 2 * radius_inscribed_circle
                    print(f'Conditions isosceles == True and radius_inscribed_circle > 0 and radius_inscribed_circle != True completed, then:\nheight = 2 * radius_inscribed_circle\nTrapezoid height = {height}\n')

            elif rectangular == True:
                if left_side > 0 < right_side:
                    height = min(left_side, right_side)
                    print(f'Conditions rectangular == True and left_side > 0 < right_side completed, then:\nheight = min(left_side, right_side)\nTrapezoid height = {height}\n')

                elif smaller_base > 0 < bigger_base and left_side > 0 < right_side:
                    height = sqrt(max(left_side, right_side)**2 - (bigger_base - smaller_base)**2)
                    print(f'Conditions rectangular == True and smaller_base > 0 < bigger_base and left_side > 0 < right_side completed, then:\nheight = sqrt(max(left_side, right_side)**2 - (bigger_base - smaller_base)**2)\nTrapezoid height = {height}\n')

            if height > 0:
                check()

        if left_side <= 0: #Left side is unknown
            if height > 0 and lower_left_corner > 0:
                left_side = height / sin(radians(lower_left_corner))
                print(f'Condition height > 0 and lower_left_corner > 0 completed, then:\nleft_side = height / sin(radians(lower_left_corner))\nLeft side = {left_side}\n')

            elif smaller_base > 0 < bigger_base and right_side > 0 and height > 0:
                left_side = sqrt((bigger_base - sqrt(right_side**2 - height**2) - smaller_base)**2 + height**2)
                print(f'Condition smaller_base > 0 < bigger_base and right_side > 0 and height > 0 completed, then:\nleft_side = sqrt((bigger_base - sqrt(right_side**2 - height**2) - smaller_base)**2 + height**2)\nLeft side = {left_side}\n')

            elif right_side > 0 and perimeter > 0 and radius_inscribed_circle == True:
                left_side = perimeter / 2 - right_side
                print(f'Condition right_side > 0 and perimeter > 0 and radius_inscribed_circle == True completed, then:\nleft_side = perimeter / 2 - right_side\nLeft side = {left_side}\n')

            elif isosceles == True:
                if right_side > 0:
                    left_side = right_side
                    print(f'Conditions isosceles == True and right_side > 0 completed, then:\nleft_side = perimeter / 2 - right_side\nLeft side = {left_side}\n')

                elif height > 0 and lower_left_corner > 0:
                    left_side = height / sin(radians(lower_left_corner))
                    print(f'Conditions isosceles == True and height > 0 and lower_left_corner > 0 completed, then:\nleft_side = height / sin(radians(lower_left_corner))e\nLeft side = {left_side}\n')

                elif smaller_base > 0 < bigger_base and lower_left_corner > 0:
                    left_side = (bigger_base - smaller_base ) / (2 * cos(radians(lower_left_corner)))
                    print(f'Conditions isosceles == True and smaller_base > 0 < bigger_base and lower_left_corner > 0 completed, then:\nleft_side = (bigger_base - smaller_base ) / (2 * cos(radians(lower_left_corner)))\nLeft side = {left_side}\n')

                elif smaller_base > 0 < bigger_base and second_diagonal > 0:
                    left_side = sqrt(second_diagonal**2 - smaller_base * bigger_base)
                    print(f'Conditions isosceles == True and smaller_base > 0 < bigger_base and second_diagonal > 0 completed, then:\nleft_side = sqrt(second_diagonal**2 - smaller_base * bigger_base)\nLeft side = {left_side}\n')

                elif middle_line > 0 and lower_left_corner > 0 and square > 0:
                    left_side = square / (middle_line * sin(lower_left_corner))
                    print(f'Conditions isosceles == True and middle_line > 0 and lower_left_corner > 0 and square > 0 completed, then:\nleft_side = square / (middle_line * sin(lower_left_corner))\nLeft side = {left_side}\n')

                elif smaller_base > 0 < bigger_base and height > 0:
                    left_side = sqrt(((bigger_base - smaller_base) / 2)**2 + height**2)
                    print(f'Conditions isosceles == True and smaller_base > 0 < bigger_base and height > 0 completed, then:\nleft_side = sqrt(((bigger_base - smaller_base) / 2)**2 + height**2)\nLeft side = {left_side}\n')

                elif middle_line > 0 and radius_inscribed_circle > 0:
                    left_side = middle_line
                    print(f'Conditions isosceles == True and middle_line > 0 and radius_inscribed_circle > 0 completed, then:\nleft_side = middle_line\nLeft side = {left_side}\n')

                elif smaller_base > 0 < bigger_base and perimeter > 0:
                    left_side = (perimeter - smaller_base - bigger_base) / 2
                    print(f'Conditions isosceles == True and smaller_base > 0 < bigger_base and perimeter > 0 completed, then:\nleft_side = (perimeter - smaller_base - bigger_base) / 2\nLeft side = {left_side}\n')

            elif rectangular == True:
                if height > 0 and lower_left_corner > 0:
                    left_side = height / sin(radians(lower_left_corner))
                    print(f'Conditions rectangular == True and height > 0 and lower_left_corner > 0 completed, then:\nleft_side = height / sin(radians(lower_left_corner))\nLeft side = {left_side}\n')

                elif right_side > 0 and height > 0 and right_side != height:
                    left_side = min(right_side, height)
                    print(f'Conditions rectangular == True and right_side > 0 and height > 0 and right_side != height completed, then:\nleft_side = min(right_side, height)\nLeft side = {left_side}\n')

                elif smaller_base > 0 < bigger_base and 0 < upper_left_corner != 90:
                    left_side = (bigger_base - smaller_base) / sin(radians(upper_left_corner % 90))
                    print(f'Conditions rectangular == True and smaller_base > 0 < bigger_base and 0 < upper_left_corner != 90 completed, then:\nleft_side = (bigger_base - smaller_base) / sin(radians(upper_left_corner % 90))\nLeft side = {left_side}\n')

                elif smaller_base > 0 < bigger_base and height > 0 and lower_right_corner == 90:
                    left_side = sqrt((bigger_base - smaller_base)**2 + height**2)
                    print(f'Conditions rectangular == True and smaller_base > 0 < bigger_base and height > 0 and lower_right_corner == 90 completed, then:\nleft_side = sqrt((bigger_base - smaller_base)**2 + height**2)\nLeft side = {left_side}\n')

            if left_side > 0:
                check()

        if right_side <= 0: #Right side is unknown
            if height > 0 and lower_right_corner > 0:
                right_side = height / sin(radians(lower_right_corner))
                print(f'Condition height > 0 and lower_right_corner > 0 completed, then:\nright_side = height / sin(radians(lower_right_corner))\nRight side = {right_side}\n')

            elif smaller_base > 0 < bigger_base and left_side > 0 and height > 0 and rectangular == False:
                right_side = sqrt((bigger_base - smaller_base - sqrt(left_side**2 - height**2))**2 + height**2)
                print(f'Condition smaller_base > 0 < bigger_base and left_side > 0 and height > 0 and rectangular == False completed, then:\nright_side = sqrt((bigger_base - sqrt(left_side**2 - height**2) - smaller_base)**2 + height**2)\nRight side = {right_side}\n')

            elif left_side > 0 and perimeter > 0 and radius_inscribed_circle == True:
                right_side = perimeter / 2 - left_side
                print(f'Condition left_side > 0 and perimeter > 0 and radius_inscribed_circle == True completed, then:\nright_side = perimeter / 2 - left_side\nRight side = {right_side}\n')

            elif isosceles == True:
                if left_side > 0:
                    right_side = left_side
                    print(f'Conditions isosceles == True and left_side > 0 completed, then:\nright_side = left_side\nRight side = {right_side}\n')

            elif rectangular == True:
                if left_side > 0 and height > 0 and left_side != height:
                    right_side = min(left_side, height)
                    print(f'Conditions rectangular == True and left_side > 0 and height > 0 and left_side != height completed, then:\nright_side = min(left_side, height)\nRight side = {right_side}\n')

                elif smaller_base > 0 < bigger_base and 0 < upper_right_corner != 90:
                    right_side = (bigger_base - smaller_base) / sin(radians(upper_right_corner % 90))
                    print(f'Conditions rectangular == True and smaller_base > 0 < bigger_base and 0 < upper_right_corner != 90 completed, then:\nright_side = (bigger_base - smaller_base) / sin(radians(upper_right_corner % 90))\nRight side = {right_side}\n')

                elif smaller_base > 0 < bigger_base and height > 0 and lower_left_corner == 90:
                    right_side = sqrt((bigger_base - smaller_base)**2 + height**2)
                    print(f'Conditions rectangular == True and smaller_base > 0 < bigger_base and height > 0 and lower_left_corner == 90 completed, then:\nright_side = sqrt((bigger_base - smaller_base)**2 + height**2)\nRight side = {right_side}\n')

            if right_side > 0:
                check()

        if middle_line <= 0: #The middle line of the trapezoid is unknown
            if smaller_base > 0 < bigger_base:
                middle_line = (smaller_base + bigger_base) / 2
                print(f'Condition smaller_base > 0 < bigger_base completed, then:\nmiddle_line = (smaller_base + bigger_base) / 2\nMiddle line = {middle_line}\n')

            elif isosceles == True:
                if bigger_base > 0 and height > 0 and lower_left_corner > 0:
                    middle_line = bigger_base - height * cos(radians(lower_left_corner)) / sin(radians(lower_left_corner))
                    print(f'Conditions isosceles == True and bigger_base > 0 and height > 0 and lower_left_corner > 0 completed, then:\nmiddle_line = bigger_base - height * cos(radians(lower_left_corner)) / sin(radians(lower_left_corner))\nMiddle line = {middle_line}\n')

                elif smaller_base > 0 and height > 0 and lower_left_corner > 0:
                    middle_line = smaller_base + height * cos(radians(lower_left_corner)) / sin(radians(lower_left_corner))
                    print(f'Conditions isosceles == True and smaller_base > 0 and height > 0 and lower_left_corner > 0 completed, then:\nmiddle_line = smaller_base + height * cos(radians(lower_left_corner)) / sin(radians(lower_left_corner))\nMiddle line = {middle_line}\n')

                elif bigger_base > 0 and left_side > 0 and height > 0:
                    middle_line = bigger_base - sqrt(left_side**2 - height**2)
                    print(f'Conditions isosceles == True and bigger_base > 0 and left_side > 0 and height > 0 completed, then:\nmiddle_line = bigger_base - sqrt(left_side**2 - height**2)\nMiddle line = {middle_line}\n')

                elif smaller_base > 0 and left_side > 0 and height > 0:
                    middle_line = smaller_base + sqrt(left_side**2 - height**2)
                    print(f'Conditions isosceles == True and smaller_base > 0 and left_side > 0 and height > 0 completed, then:\nmiddle_line = smaller_base + sqrt(left_side**2 - height**2)\nMiddle line = {middle_line}\n')

                elif height > 0 and second_diagonal > 0 and first_angle_between_diagonals > 0:
                    middle_line = second_diagonal**2 / (2 * height) * sin(radians(first_angle_between_diagonals))
                    print(f'Conditions isosceles == True and height > 0 and second_diagonal > 0 and first_angle_between_diagonals > 0 completed, then:\nmiddle_line = second_diagonal**2 / (2 * height) * sin(radians(first_angle_between_diagonals))\nMiddle line = {middle_line}\n')

                elif left_side > 0 and square > 0 and lower_left_corner > 0:
                    middle_line = square / (left_side * sin(radians(lower_left_corner)))
                    print(f'Conditions isosceles == True and left_side > 0 and square > 0 and lower_left_corner > 0 completed, then:\nmiddle_line = square / (left_side * sin(radians(lower_left_corner)))\nMiddle line = {middle_line}\n')

            elif rectangular == True:
                if bigger_base > 0 and height > 0 and left_side > right_side:
                    middle_line = bigger_base - height * cos(radians(lower_left_corner)) / sin(radians(lower_left_corner)) / 2
                    print(f'Conditions rectangular == True and bigger_base > 0 and height > 0 and left_side > right_side completed, then:\nmiddle_line = bigger_base - height * cos(radians(lower_left_corner)) / sin(radians(lower_left_corner)) / 2\nMiddle line = {middle_line}\n')

                elif bigger_base > 0 and height > 0 and right_side > left_side:
                    middle_line = bigger_base - height * cos(radians(lower_right_corner)) / sin(radians(lower_right_corner)) / 2
                    print(f'Conditions rectangular == True and bigger_base > 0 and height > 0 and right_side > left_side completed, then:\nmiddle_line = bigger_base - height * cos(radians(lower_right_corner)) / sin(radians(lower_right_corner)) / 2\nMiddle line = {middle_line}\n')

                elif smaller_base > 0 and height > 0 and left_side > right_side:
                    middle_line = smaller_base + height * cos(radians(lower_left_corner)) / sin(radians(lower_left_corner)) / 2
                    print(f'Conditions rectangular == True and smaller_base > 0 and height > 0 and left_side > right_side completed, then:\nmiddle_line = smaller_base + height * cos(radians(lower_left_corner)) / sin(radians(lower_left_corner)) / 2\nMiddle line = {middle_line}\n')

                elif smaller_base > 0 and height > 0 and right_side > left_side:
                    middle_line = smaller_base + height * cos(radians(lower_right_corner)) / sin(radians(lower_right_corner)) / 2
                    print(f'Conditions rectangular == True and smaller_base > 0 and height > 0 and right_side > left_side completed, then:\nmiddle_line = smaller_base + height * cos(radians(lower_right_corner)) / sin(radians(lower_right_corner)) / 2\nMiddle line = {middle_line}\n')

                elif bigger_base > 0 and left_side > right_side:
                    middle_line = bigger_base - left_side * cos(radians(lower_left_corner)) / 2
                    print(f'Conditions rectangular == True and bigger_base > 0 and left_side > right_side completed, then:\nmiddle_line = bigger_base - left_side * cos(radians(lower_left_corner)) / 2\nMiddle line = {middle_line}\n')

                elif bigger_base > 0 and right_side > left_side:
                    middle_line = bigger_base - right_side * cos(radians(lower_right_corner)) / 2
                    print(f'Conditions rectangular == True and bigger_base > 0 and right_side > left_side completed, then:\nmiddle_line = bigger_base - right_side * cos(radians(lower_right_corner)) / 2\nMiddle line = {middle_line}\n')

                elif smaller_base > 0 and left_side > right_side and lower_left_corner > 0:
                    middle_line = smaller_base + left_side * cos(radians(lower_left_corner)) / 2
                    print(f'Conditions rectangular == True and smaller_base > 0 and left_side > right_side and lower_left_corner > 0 completed, then:\nmiddle_line = smaller_base + left_side * cos(radians(lower_left_corner)) / 2\nMiddle line = {middle_line}\n')

                elif smaller_base > 0 and right_side > left_side:
                    middle_line = smaller_base + right_side * cos(radians(lower_right_corner)) / 2
                    print(f'Conditions rectangular == True and smaller_base > 0 and right_side > left_side completed, then:\nmiddle_line = smaller_base + right_side * cos(radians(lower_right_corner)) / 2\nMiddle line = {middle_line}\n')

                elif bigger_base > 0 and left_side > height:
                    middle_line = bigger_base - sqrt(left_side**2 - height**2) / 2
                    print(f'Conditions rectangular == True and bigger_base > 0 and left_side > height completed, then:\nmiddle_line = bigger_base - sqrt(left_side**2 - height**2) / 2\nMiddle line = {middle_line}\n')

                elif bigger_base > 0 and right_side > height:
                    middle_line = bigger_base - sqrt(right_side**2 - height**2) / 2
                    print(f'Conditions rectangular == True and bigger_base > 0 and right_side > height completed, then:\nmiddle_line = bigger_base - sqrt(right_side**2 - height**2) / 2\nMiddle line = {middle_line}\n')

                elif smaller_base > 0 and height > 0 and left_side > height:
                    middle_line = smaller_base + sqrt(left_side**2 - height**2) / 2
                    print(f'Conditions rectangular == True and smaller_base > 0 and height > 0 and left_side > height completed, then:\nmiddle_line = smaller_base + sqrt(left_side**2 - height**2) / 2\nMiddle line = {middle_line}\n')

                elif smaller_base > 0 and right_side > height:
                    middle_line = smaller_base + sqrt(right_side**2 - height**2) / 2
                    print(f'Conditions rectangular == True and smaller_base > 0 and right_side > height completed, then:\nmiddle_line = smaller_base + sqrt(right_side**2 - height**2) / 2\nMiddle line = {middle_line}\n')

                elif height > 0 and first_diagonal > 0 < second_diagonal and first_angle_between_diagonals > 0:
                    middle_line = first_diagonal * second_diagonal / (2 * height) * sin(radians(first_angle_between_diagonals))
                    print(f'Conditions rectangular == True and height > 0 and first_diagonal > 0 < second_diagonal and first_angle_between_diagonals > 0 completed, then:\nmiddle_line = first_diagonal * second_diagonal / (2 * height) * sin(radians(first_angle_between_diagonals))\nMiddle line = {middle_line}\n')

            if middle_line > 0:
                check()

        if square <= 0: #Area of the trapezoid is unknown
            if middle_line > 0 and height > 0:
                square = middle_line * height
                print(f'Condition middle_line > 0 and height > 0 completed, then:\nsquare = middle_line * height\nTrapezoid area = {square}\n')

            elif first_diagonal > 0 < second_diagonal and first_angle_between_diagonals > 0:
                square = first_diagonal * second_diagonal / 2 * sin(radians(first_angle_between_diagonals))
                print(f'Condition first_diagonal > 0 < second_diagonal and first_angle_between_diagonals > 0 completed, then:\nsquare = first_diagonal * second_diagonal / 2 * sin(radians(first_angle_between_diagonals))\nTrapezoid area = {square}\n')

            elif smaller_base > 0 < bigger_base and left_side > 0 < right_side:
                square = (smaller_base + bigger_base) / 2 * sqrt(left_side**2 - (((bigger_base - smaller_base)**2 + left_side**2 - right_side**2) / (2 * (bigger_base - smaller_base)))**2)
                print(f'Condition smaller_base > 0 < bigger_base and left_side > 0 < right_side completed, then:\nsquare = (smaller_base + bigger_base) / 2 * sqrt(left_side**2 - (((bigger_base - smaller_base)**2 + left_side**2 - right_side**2) / (2 * (bigger_base - smaller_base)))**2)\nTrapezoid area = {square}\n')

            elif isosceles == True:
                if smaller_base > 0 < bigger_base and left_side > 0:
                    square = (smaller_base + bigger_base) / 2 * sqrt(left_side**2 - (bigger_base - smaller_base)**2 / 4)
                    print(f'Conditions isosceles == True and middle_line > 0 and height > 0 completed, then:\nsquare = middle_line * height\nTrapezoid area = {square}\n')

                elif bigger_base > 0 and left_side > 0 and lower_left_corner > 0:
                    square = left_side * sin(radians(lower_left_corner)) * (bigger_base - left_side * cos(radians(lower_left_corner)))
                    print(f'Conditions isosceles == True and middle_line > 0 and height > 0 completed, then:\nsquare = middle_line * height\nTrapezoid area = {square}\n')

                elif smaller_base > 0 and left_side > 0 and lower_left_corner > 0:
                    square = left_side * sin(radians(lower_left_corner)) * (smaller_base + left_side * cos(radians(lower_left_corner)))
                    print(f'Conditions isosceles == True and smaller_base > 0 and left_side > 0 and lower_left_corner > 0 completed, then:\nsquare = left_side * sin(radians(lower_left_corner)) * (smaller_base + left_side * cos(radians(lower_left_corner)))\nTrapezoid area = {square}\n')

                elif second_diagonal > 0 and first_angle_between_diagonals > 0:
                    square = second_diagonal**2 / 2 * sin(radians(first_angle_between_diagonals))
                    print(f'Conditions isosceles == True and second_diagonal > 0 and first_angle_between_diagonals > 0 completed, then:\nsquare = second_diagonal**2 / 2 * sin(radians(first_angle_between_diagonals))\nTrapezoid area = {square}\n')

                elif left_side > 0 and middle_line > 0 and lower_left_corner > 0:
                    square = middle_line * left_side * sin(radians(lower_left_corner))
                    print(f'Conditions isosceles == True and left_side > 0 and middle_line > 0 and lower_left_corner > 0 completed, then:\nsquare = middle_line * left_side * sin(radians(lower_left_corner))\nTrapezoid area = {square}\n')

                elif radius_inscribed_circle > 0 and radius_inscribed_circle != True:
                    square = 4 * radius_inscribed_circle**2 / sin(radians(lower_left_corner))
                    print(f'Conditions isosceles == True and radius_inscribed_circle > 0 and radius_inscribed_circle != True completed, then:\nsquare = 4 * radius_inscribed_circle**2 / sin(radians(lower_left_corner))\nTrapezoid area = {square}\n')

                elif smaller_base > 0 < bigger_base and lower_left_corner > 0 and radius_inscribed_circle > 0 and radius_inscribed_circle != True:
                    square = 4 * smaller_base * bigger_base / sin(radians(lower_left_corner))
                    print(f'Conditions isosceles == True and smaller_base > 0 < bigger_base and lower_left_corner > 0 and radius_inscribed_circle > 0 and radius_inscribed_circle != True completed, then:\nsquare = 4 * smaller_base * bigger_base / sin(radians(lower_left_corner))\nTrapezoid area = {square}\n')

            if square > 0:
                check()

        if perimeter <= 0: #Perimeter of the trapezoid is unknown
            if smaller_base > 0 < bigger_base and left_side > 0 < right_side:
                perimeter = smaller_base + bigger_base + left_side + right_side
                print(f'Condition smaller_base > 0 < bigger_base and left_side > 0 < right_side completed, then:\nperimeter = smaller_base + bigger_base + left_side + right_side\nPerimeter of the trapezoid = {perimeter}\n')

            if perimeter > 0:
                check()

        if first_diagonal <= 0: #Diagonal from the lower left corner to the upper right corner is unknown
            if smaller_base > 0 < bigger_base and left_side > 0 < right_side:
                first_diagonal = sqrt(right_side**2 + smaller_base * bigger_base - bigger_base * (right_side**2 - left_side**2) / (bigger_base - smaller_base))
                print(f'Condition smaller_base > 0 < bigger_base and left_side > 0 < right_side completed, then:\nfirst_diagonal = sqrt(right_side**2 + smaller_base * bigger_base - bigger_base * (right_side**2 - left_side**2) / (bigger_base - smaller_base))\nDiagonal from the lower left corner to the upper right = {first_diagonal}\n')

            elif bigger_base > 0 and right_side > 0 and lower_right_corner > 0:
                first_diagonal = sqrt(bigger_base**2 + right_side**2 - 2 * bigger_base * right_side * cos(radians(lower_right_corner)))
                print(f'Condition bigger_base > 0 and right_side > 0 and lower_right_corner > 0 completed, then:\nfirst_diagonal = sqrt(bigger_base**2 + right_side**2 - 2 * bigger_base * right_side * cos(radians(lower_right_corner)))\nDiagonal from the lower left corner to the upper right = {first_diagonal}\n')

            elif bigger_base > 0 and height > 0 and lower_right_corner > 0:
                first_diagonal = sqrt(height**2 + (bigger_base - height * cos(radians(lower_right_corner)) / sin(radians(lower_right_corner)))**2)
                print(f'Condition bigger_base > 0 and height > 0 and lower_right_corner > 0 completed, then:\nfirst_diagonal = sqrt(height**2 + (bigger_base - height * cos(radians(lower_right_corner)) / sin(radians(lower_right_corner)))**2)\nDiagonal from the lower left corner to the upper right = {first_diagonal}\n')

            elif smaller_base > 0 and height > 0 and lower_left_corner > 0:
                first_diagonal = sqrt(height**2 + (smaller_base + height * cos(radians(lower_left_corner)) / sin(radians(lower_left_corner)))**2)
                print(f'Condition smaller_base > 0 and height > 0 and lower_left_corner > 0 completed, then:\nfirst_diagonal = sqrt(height**2 + (smaller_base + height * cos(radians(lower_left_corner)) / sin(radians(lower_left_corner)))**2)\nDiagonal from the lower left corner to the upper right = {first_diagonal}\n')

            elif bigger_base > 0 and right_side > 0 and height > 0:
                first_diagonal = sqrt(bigger_base**2 + right_side**2 - 2 * bigger_base * sqrt(right_side**2 - height**2))
                print(f'Condition bigger_base > 0 and right_side > 0 and height > 0 completed, then:\nfirst_diagonal = sqrt(bigger_base**2 + right_side**2 - 2 * bigger_base * sqrt(right_side**2 - height**2))\nDiagonal from the lower left corner to the upper right = {first_diagonal}\n')

            elif smaller_base > 0 < bigger_base and left_side > 0 < right_side and second_diagonal > 0:
                first_diagonal = sqrt(left_side**2 + right_side**2 + 2 * smaller_base * bigger_base - second_diagonal**2)
                print(f'Condition smaller_base > 0 < bigger_base and left_side > 0 < right_side and second_diagonal > 0 completed, then:\nfirst_diagonal = sqrt(left_side**2 + right_side**2 + 2 * smaller_base * bigger_base - second_diagonal**2)\nDiagonal from the lower left corner to the upper right = {first_diagonal}\n')

            elif second_diagonal > 0 and first_angle_between_diagonals > 0 and square > 0:
                first_diagonal = 2 * square / (second_diagonal * sin(radians(first_angle_between_diagonals)))
                print(f'Condition second_diagonal > 0 and first_angle_between_diagonals > 0 and square > 0 completed, then:\nfirst_diagonal = 2 * square / (second_diagonal * sin(radians(first_angle_between_diagonals)))\nDiagonal from the lower left corner to the upper right = {first_diagonal}\n')

            elif isosceles == True:
                if second_diagonal > 0:
                    first_diagonal = second_diagonal
                    print(f'Conditions isosceles == True and second_diagonal > 0 completed, then:\nfirst_diagonal = second_diagonal\nDiagonal from the lower left corner to the upper right = {first_diagonal}\n')

            elif rectangular == True:
                if height > 0 and smaller_base > 0 and lower_left_corner == 90:
                    first_diagonal = sqrt(height**2 + smaller_base**2)
                    print(f'Conditions rectangular == True and height > 0 and smaller_base > 0 and lower_left_corner == 90 completed, then:\nfirst_diagonal = sqrt(height**2 + smaller_base**2)\nDiagonal from the lower left corner to the upper right = {first_diagonal}\n')

                elif height > 0 and smaller_base > 0 and lower_right_corner == 90:
                    first_diagonal = sqrt(height**2 + bigger_base**2)
                    print(f'Conditions rectangular == True and height > 0 and smaller_base > 0 and lower_right_corner == 90 completed, then:\nfirst_diagonal = sqrt(height**2 + bigger_base**2)\nDiagonal from the lower left corner to the upper right = {first_diagonal}\n')

            if first_diagonal > 0:
                check()

        if second_diagonal <= 0: #Diagonal from the lower right corner to the upper left corner is unknown
            if smaller_base > 0 < bigger_base and left_side > 0 < right_side:
                second_diagonal = sqrt(left_side**2 + smaller_base * bigger_base - bigger_base * (left_side**2 - right_side**2) / (bigger_base - smaller_base))
                print(f'Condition smaller_base > 0 < bigger_base and left_side > 0 < right_side completed, then:\nsecond_diagonal = sqrt(left_side**2 + smaller_base * bigger_base - bigger_base * (left_side**2 - right_side**2) / (bigger_base - smaller_base))\nDiagonal from the lower right corner to the upper left = {second_diagonal}\n')

            elif bigger_base > 0 and left_side > 0 and lower_left_corner > 0:
                second_diagonal = sqrt(bigger_base**2 + left_side**2 - 2 * bigger_base * left_side * cos(radians(lower_left_corner)))
                print(f'Condition bigger_base > 0 and left_side > 0 and lower_left_corner > 0 completed, then:\nsecond_diagonal = sqrt(bigger_base**2 + left_side**2 - 2 * bigger_base * left_side * cos(radians(lower_left_corner)))\nDiagonal from the lower right corner to the upper left = {second_diagonal}\n')

            elif bigger_base > 0 and height > 0 and lower_left_corner > 0:
                second_diagonal = sqrt(height**2 + (bigger_base - height * cos(radians(lower_left_corner)) / sin(radians(lower_left_corner)))**2)
                print(f'Condition bigger_base > 0 and height > 0 and lower_left_corner > 0 completed, then:\nsecond_diagonal = sqrt(height**2 + (bigger_base - height * cos(radians(lower_left_corner)) / sin(radians(lower_left_corner)))**2)\nDiagonal from the lower right corner to the upper left = {second_diagonal}\n')

            elif smaller_base > 0 and height > 0 and lower_right_corner > 0:
                second_diagonal = sqrt(height**2 + (smaller_base + height * cos(radians(lower_right_corner)) / sin(radians(lower_right_corner)))**2)
                print(f'Condition smaller_base > 0 and height > 0 and lower_right_corner > 0 completed, then:\nsecond_diagonal = sqrt(height**2 + (smaller_base + height * cos(radians(lower_right_corner)) / sin(radians(lower_right_corner)))**2)\nDiagonal from the lower right corner to the upper left = {second_diagonal}\n')

            elif bigger_base > 0 and left_side > 0 and height > 0:
                second_diagonal = sqrt(bigger_base**2 + left_side**2 - 2 * bigger_base * sqrt(left_side**2 - height**2))
                print(f'Condition bigger_base > 0 and left_side > 0 and height > 0 completed, then:\nsecond_diagonal = sqrt(bigger_base**2 + left_side**2 - 2 * bigger_base * sqrt(left_side**2 - height**2))\nDiagonal from the lower right corner to the upper left = {second_diagonal}\n')

            elif smaller_base > 0 < bigger_base and left_side > 0 < right_side and first_diagonal > 0:
                second_diagonal = sqrt(left_side**2 + right_side**2 + 2 * smaller_base * bigger_base - first_diagonal**2)
                print(f'Condition smaller_base > 0 < bigger_base and left_side > 0 < right_side and first_diagonal > 0 completed, then:\nsecond_diagonal = sqrt(left_side**2 + right_side**2 + 2 * smaller_base * bigger_base - first_diagonal**2)\nDiagonal from the lower right corner to the upper left = {second_diagonal}\n')

            elif first_diagonal > 0 and first_angle_between_diagonals > 0 and square > 0:
                second_diagonal = 2 * square / (first_diagonal * sin(radians(first_angle_between_diagonals)))
                print(f'Condition first_diagonal > 0 and first_angle_between_diagonals > 0 and square > 0 completed, then:\nsecond_diagonal = 2 * square / (first_diagonal * sin(radians(first_angle_between_diagonals)))\nDiagonal from the lower right corner to the upper left = {second_diagonal}\n')

            elif isosceles == True:
                if smaller_base > 0 and left_side > 0 and lower_left_corner > 0:
                    second_diagonal = sqrt(smaller_base**2 + left_side**2 + 2 * bigger_base * left_side * cos(radians(lower_left_corner)))
                    print(f'Conditions isosceles == True and smaller_base > 0 and left_side > 0 and lower_left_corner > 0 completed, then:\nsecond_diagonal = sqrt(smaller_base**2 + left_side**2 + 2 * bigger_base * left_side * cos(radians(lower_left_corner)))\nDiagonal from the lower right corner to the upper left = {second_diagonal}\n')

                elif middle_line > 0 and height > 0:
                    second_diagonal = sqrt(height**2 + middle_line**2)
                    print(f'Conditions isosceles == True and middle_line > 0 and height > 0 completed, then:\nsecond_diagonal = sqrt(height**2 + middle_line**2)\nDiagonal from the lower right corner to the upper left = {second_diagonal}\n')

                elif bigger_base > 0 and height > 0 and lower_left_corner > 0:
                    second_diagonal = sqrt(height**2 + (bigger_base - height * cos(radians(lower_left_corner)) / sin(radians(lower_left_corner)))**2)
                    print(f'Conditions isosceles == True and bigger_base > 0 and height > 0 and lower_left_corner > 0 completed, then:\nsecond_diagonal = sqrt(height**2 + (bigger_base - height * cos(radians(lower_left_corner)) / sin(radians(lower_left_corner)))**2)\nDiagonal from the lower right corner to the upper left = {second_diagonal}\n')

                elif smaller_base > 0 and height > 0 and lower_left_corner > 0:
                    second_diagonal = sqrt(height**2 + (smaller_base + height * cos(radians(lower_left_corner)) / sin(radians(lower_left_corner)))**2)
                    print(f'Conditions isosceles == True and smaller_base > 0 and height > 0 and lower_left_corner > 0 completed, then:\nsecond_diagonal = sqrt(height**2 + (smaller_base + height * cos(radians(lower_left_corner)) / sin(radians(lower_left_corner)))**2)\nDiagonal from the lower right corner to the upper left = {second_diagonal}\n')

                elif bigger_base > 0 and left_side > 0 and height > 0:
                    second_diagonal = sqrt(bigger_base**2 + left_side**2 - 2 * bigger_base * sqrt(left_side**2 - height**2))
                    print(f'Conditions isosceles == True and bigger_base > 0 and left_side > 0 and height > 0 completed, then:\nsecond_diagonal = sqrt(bigger_base**2 + left_side**2 - 2 * bigger_base * sqrt(left_side**2 - height**2))\nDiagonal from the lower right corner to the upper left = {second_diagonal}\n')

            elif rectangular == True:
                if height > 0 and bigger_base > 0 and lower_right_corner == 90:
                    second_diagonal = sqrt(height**2 + smaller_base**2)
                    print(f'Conditions isosceles == height > 0 and bigger_base > 0 and lower_right_corner == 90 and fff completed, then:\nsecond_diagonal = sqrt(height**2 + smaller_base**2)\nDiagonal from the lower right corner to the upper left = {second_diagonal}\n')

                elif height > 0 and bigger_base > 0 and lower_left_corner == 90:
                    second_diagonal = sqrt(height**2 + bigger_base**2)
                    print(f'Conditions isosceles == True and height > 0 and bigger_base > 0 and lower_left_corner == 90 completed, then:\nsecond_diagonal = sqrt(height**2 + bigger_base**2)\nDiagonal from the lower right corner to the upper left = {second_diagonal}\n')

            if second_diagonal > 0:
                check()

        if lower_left_corner <= 0: #Lower left corner is unknown
            if upper_left_corner > 0:
                lower_left_corner = 180 - upper_left_corner
                print(f'Condition upper_left_corner > 0 completed, then:\nlower_left_corner = 180 - upper_left_corner\nLeft corner with a larger base, in degrees = {lower_left_corner}\n')

            elif left_side > 0 and height > 0:
                lower_left_corner = degrees(asin(height / left_side))
                print(f'Condition left_side > 0 and height > 0 completed, then:\nlower_left_corner = degrees(asin(height / left_side))\nLeft corner with a larger base, in degrees = {lower_left_corner}\n')

            elif isosceles == True:
                if lower_right_corner > 0:
                    lower_left_corner = lower_right_corner
                    print(f'Conditions isosceles == True and lower_right_corner > 0 completed, then:\nlower_left_corner = lower_right_corner\nLeft corner with a larger base, in degrees = {lower_left_corner}\n')

            elif rectangular == True:
                if 0 < lower_right_corner != 90:
                    lower_left_corner = 90
                    print(f'Conditions rectangular == True and 0 < lower_right_corner != 90 completed, then:\nlower_left_corner = 90\nLeft corner with a larger base, in degrees = {lower_left_corner}\n')

                elif left_side > 0 and height > 0 and left_side == height:
                    lower_left_corner = 90
                    print(f'Conditions rectangular == True and left_side > 0 and height > 0 and left_side == height completed, then:\nlower_left_corner = 90\nLeft corner with a larger base, in degrees = {lower_left_corner}\n')

            if lower_left_corner > 0:
                check()

        if lower_right_corner <= 0: #Lower right corner is unknown
            if upper_right_corner > 0:
                lower_right_corner = 180 - upper_right_corner
                print(f'Condition upper_right_corner > 0 completed, then:\nlower_right_corner = 180 - upper_right_corner\nRight angle with a larger base, in degrees = {lower_right_corner}\n')

            elif right_side > 0 and height > 0:
                lower_right_corner = degrees(asin(height / right_side))
                print(f'Condition right_side > 0 and height > 0 completed, then:\nlower_right_corner = degrees(asin(height / right_side))\nRight angle with a larger base, in degrees = {lower_right_corner}\n')

            elif isosceles == True:
                if lower_left_corner > 0:
                    lower_right_corner = lower_left_corner
                    print(f'Conditions isosceles == True and lower_left_corner > 0 completed, then:\nlower_right_corner = lower_left_corner\nRight angle with a larger base, in degrees = {lower_right_corner}\n')

            elif rectangular == True:
                if 0 < lower_left_corner != 90:
                    lower_right_corner = 90
                    print(f'Conditions rectangular == True and 0 < lower_left_corner != 90 completed, then:\nlower_right_corner = 90\nRight angle with a larger base, in degrees = {lower_right_corner}\n')

                elif right_side > 0 and height > 0 and right_side == height:
                    lower_right_corner = 90
                    print(f'Conditions rectangular == True and right_side > 0 and height > 0 and right_side == height completed, then:\nlower_right_corner = 90\nRight angle with a larger base, in degrees = {lower_right_corner}\n')

            if lower_right_corner > 0:
                check()

        if upper_left_corner <= 0: #Upper left corner is unknown
            if lower_left_corner > 0:
                upper_left_corner = 180 - lower_left_corner
                print(f'Condition lower_left_corner > 0 completed, then:\nupper_left_corner = 180 - lower_left_corner\nLeft corner with a smaller base, in degrees = {upper_left_corner}\n')

            elif isosceles == True:
                if upper_right_corner > 0:
                    upper_left_corner = upper_right_corner
                    print(f'Conditions isosceles == True and upper_right_corner > 0 completed, then:\nupper_left_corner = upper_right_corner\nLeft corner with a smaller base, in degrees = {upper_left_corner}')

            elif rectangular == True:
                if 0 < upper_right_corner != 90:
                    upper_left_corner = 90
                    print(f'Conditions rectangular == True and 0 < upper_right_corner != 90 completed, then:\nupper_left_corner = 90\nLeft corner with a smaller base, in degrees = {upper_left_corner}')

            if upper_left_corner > 0:
                check()

        if upper_right_corner <= 0: #Upper right corner is unknown
            if lower_right_corner > 0:
                upper_right_corner = 180 - lower_right_corner
                print(f'Condition lower_right_corner > 0 completed, then:\nupper_right_corner = 180 - lower_right_corner\nRight angle with a smaller base, in degrees= {upper_right_corner}\n')

            elif isosceles == True:
                if upper_left_corner > 0:
                    upper_right_corner = upper_left_corner
                    print(f'Conditions isosceles == True and upper_left_corner > 0 completed, then:\nupper_right_corner = upper_left_corner\nRight angle with a smaller base, in degrees= {upper_right_corner}\n')

            elif rectangular == True:
                if 0 < upper_left_corner != 90:
                    upper_right_corner = 90
                    print(f'Conditions rectangular == True and 0 < upper_left_corner != 90 completed, then:\nupper_right_corner = 90\nRight angle with a smaller base, in degrees= {upper_right_corner}\n')

            if upper_right_corner > 0:
                check()

        if first_angle_between_diagonals <= 0: #Angle between the diagonals resting on the side is unknown
            if second_angle_between_diagonals > 0:
                first_angle_between_diagonals = 180 - second_angle_between_diagonals
                print(f'Condition second_angle_between_diagonals > 0 completed, then:\nfirst_angle_between_diagonals = 180 - second_angle_between_diagonals\nThe angle between the diagonals, resting on the side = {first_angle_between_diagonals}\n')

            elif smaller_base > 0 and left_side > 0 < right_side and first_diagonal > 0 < second_diagonal and upper_left_corner > 0 < upper_right_corner:
                first_angle_between_diagonals = degrees(acos((smaller_base**2 + second_diagonal**2  - right_side**2) / (2 * smaller_base * second_diagonal))) + degrees(acos((first_diagonal**2 + smaller_base**2 - left_side**2) / (2 * first_diagonal * smaller_base)))
                print((smaller_base**2 + second_diagonal**2  - right_side**2), (2 * smaller_base * second_diagonal), (first_diagonal**2 + smaller_base**2 - left_side**2), (2 * first_diagonal * smaller_base))
                print(f'Condition smaller_base > 0 and left_side > 0 < right_side and first_diagonal > 0 < second_diagonal and upper_left_corner > 0 < upper_right_corner completed, then:\nfirst_angle_between_diagonals = degrees(acos((smaller_base**2 + second_diagonal**2  - right_side**2) / (2 * smaller_base * second_diagonal))) + degrees(acos((first_diagonal**2 + smaller_base**2 - left_side**2) / (2 * first_diagonal * smaller_base)))\nThe angle between the diagonals, resting on the side = {first_angle_between_diagonals}\n')

            if first_angle_between_diagonals > 0:
                check()

        if second_angle_between_diagonals <= 0: #Angle between the diagonals resting on the base is unknown
            if first_angle_between_diagonals > 0:
                second_angle_between_diagonals = 180 - first_angle_between_diagonals
                print(f'Condition first_angle_between_diagonals > 0 completed, then:\nsecond_angle_between_diagonals = 180 - first_angle_between_diagonals\nThe angle between the diagonals, resting on the base = {second_angle_between_diagonals}\n')

            elif smaller_base > 0 and left_side > 0 < right_side and first_diagonal > 0 < second_diagonal and upper_left_corner > 0 < upper_right_corner:
                first_angle_between_diagonals = 180 - degrees(acos((smaller_base**2 + second_diagonal**2  - right_side**2) / (2 * smaller_base * second_diagonal))) - degrees(acos((first_diagonal**2 + smaller_base**2 - left_side**2) / (2 * first_diagonal * smaller_base)))
                print(f'Condition smaller_base > 0 and left_side > 0 < right_side and first_diagonal > 0 < second_diagonal and upper_left_corner > 0 < upper_right_corner completed, then:\nfirst_angle_between_diagonals = 180 - degrees(acos((smaller_base**2 + second_diagonal**2  - right_side**2) / (2 * smaller_base * second_diagonal))) - degrees(acos((first_diagonal**2 + smaller_base**2 - left_side**2) / (2 * first_diagonal * smaller_base)))\nThe angle between the diagonals, resting on the base = {second_angle_between_diagonals}\n')

            if second_angle_between_diagonals > 0:
                check()

        if radius_inscribed_circle < 0 and radius_inscribed_circle != False or radius_inscribed_circle == True: #Inscribed circle exists, but is unknown
            if smaller_base > 0 < bigger_base and left_side > 0 < right_side and height > 0 and smaller_base + bigger_base == left_side + right_side:
                radius_inscribed_circle = height / 2
                print(f'Condition smaller_base > 0 < bigger_base and left_side > 0 < right_side and height > 0 and smaller_base + bigger_base == left_side + right_side completed, then:\nradius_inscribed_circle = height / 2\nRadius of the inscribed circle = {radius_inscribed_circle}\n')

            elif middle_line > 0 and radius_inscribed_circle == True:
                radius_inscribed_circle = middle_line / 2
                print(f'Condition middle_line > 0 and radius_inscribed_circle == True completed, then:\nradius_inscribed_circle = middle_line / 2\nRadius of the inscribed circle = {radius_inscribed_circle}\n')

            elif smaller_base > 0 < bigger_base and left_side > 0 < right_side and height > 0 and smaller_base + bigger_base != left_side + right_side:
                radius_inscribed_circle = False
                print(f'Condition smaller_base > 0 < bigger_base and left_side > 0 < right_side and height > 0 and smaller_base + bigger_base != left_side + right_side completed, then:\nradius_inscribed_circle = False\nRadius of the inscribed circle = {radius_inscribed_circle}\n')

            elif left_side > 0 < right_side and perimeter > 0 and radius_inscribed_circle == True and rectangular:
                radius_inscribed_circle = (perimeter / 2 - max(left_side, right_side)) / 2
                print(f'Condition left_side > 0 < right_side and perimeter > 0 and radius_inscribed_circle == True and rectangular completed, then:\nradius_inscribed_circle = (perimeter / 2 - max(left_side, right_side)) / 2\nRadius of the inscribed circle = {radius_inscribed_circle}\n')

            if radius_inscribed_circle > 0:
                check()

        if radius_circumscribed_circle < 0 and radius_circumscribed_circle != False or radius_circumscribed_circle == True: #Circumscribed circle exists, but is unknown
            if bigger_base > 0 and left_side > 0 and first_diagonal > 0 and isosceles:
                p = (bigger_base + left_side + first_diagonal) / 2
                radius_circumscribed_circle = bigger_base * left_side * first_diagonal / (4 * sqrt(p * (p - bigger_base) * (p - left_side) * (p - first_diagonal)))
                print(f'Condition bigger_base > 0 and left_side > 0 and first_diagonal > 0 and isosceles completed, then:\nradius_circumscribed_circle = bigger_base * left_side * first_diagonal / (4 * sqrt(p * (p - bigger_base) * (p - left_side) * (p - first_diagonal))), where p = (bigger_base + left_side + first_diagonal) / 2\nThe radius of the circumscribed circle = {radius_circumscribed_circle}\n')

            elif isosceles == False:
                radius_circumscribed_circle = False
                print(f'Condition isosceles == False completed, then:\nradius_circumscribed_circle = False\nThe radius of the circumscribed circle = {radius_circumscribed_circle}\n')

            if radius_circumscribed_circle > 0:
                check()

        cycle += 1
        result()

    def convert(): #Translating the entered data into a convenient format
        global smaller_base, bigger_base, left_side, right_side, middle_line, height, lower_left_corner, lower_right_corner, upper_left_corner, upper_right_corner, first_diagonal, second_diagonal, first_angle_between_diagonals, second_angle_between_diagonals, square, perimeter, isosceles, rectangular, radius_inscribed_circle, radius_circumscribed_circle

        isosceles = int(isosceles_selected.get()) #Isosceles trapezoid
        if isosceles == 2:
            isosceles = True
        elif isosceles == 1:
            isosceles = False
        elif isosceles == 0:
            isosceles = -1

        rectangular = int(rectangular_selected.get()) #Trapezoid is rectangular
        if rectangular == 2:
            rectangular = True
        elif rectangular == 1:
            rectangular = False
        elif rectangular == 0:
            rectangular = -1

        smaller_base = smaller_base_selected.get() #Smaller base
        if smaller_base == '':
            smaller_base = -1
        else:
            smaller_base = int(smaller_base)

        bigger_base = bigger_base_selected.get() #Bigger base
        if bigger_base == '':
            bigger_base = -1
        else:
            bigger_base= int(bigger_base)

        height = height_selected.get() #Trapezoid height
        if height == '':
            height = -1
        else:
            height = int(height)

        left_side = left_side_selected.get() #Left side
        if left_side == '':
            left_side = -1
        else:
            left_side = int(left_side)

        right_side = right_side_selected.get() #Right side
        if right_side == '':
            right_side = -1
        else:
            right_side = int(right_side)

        middle_line = middle_line_selected.get() #Middle line of the trapezoid
        if middle_line == '':
            middle_line = -1
        else:
            middle_line = int(middle_line)

        square = square_selected.get() #Trapezoid area
        if square == '':
            square = -1
        else:
            square = int(square)

        perimeter = perimeter_selected.get() #Perimeter of the trapezoid
        if perimeter == '':
            perimeter = -1
        else:
            perimeter = int(perimeter)

        first_diagonal = first_diagonal_selected.get() #Diagonal from the lower left corner to the upper right
        if first_diagonal == '':
            first_diagonal = -1
        else:
            first_diagonal = int(first_diagonal)

        second_diagonal = second_diagonal_selected.get() #Diagonal from the lower right corner to the upper left
        if second_diagonal == '':
            second_diagonal = -1
        else:
            second_diagonal = int(second_diagonal)

        radius_inscribed_circle = radius_inscribed_circle_selected.get() #Radius of the inscribed circle
        if int(radius_inscribed_circle) == -1:
            radius_inscribed_circle = True
        elif int(radius_inscribed_circle) == -2:
            radius_inscribed_circle = False
        else:
            radius_inscribed_circle = radius_inscribed_circle_Known.get()
            if radius_inscribed_circle == '':
                radius_inscribed_circle = -1
            else:
                radius_inscribed_circle = int(radius_inscribed_circle)

        radius_circumscribed_circle = radius_circumscribed_circle_selected.get() #The radius of the circumscribed circle
        if int(radius_circumscribed_circle) == -1:
            radius_circumscribed_circle = True
        elif int(radius_circumscribed_circle) == -2:
            radius_circumscribed_circle = False
        else:
            radius_circumscribed_circle = radius_circumscribed_circle_Known.get()
            if radius_circumscribed_circle == '':
                radius_circumscribed_circle = -1
            else:
                radius_circumscribed_circle = int(radius_inscribed_circle)

        lower_left_corner = lower_left_corner_selected.get() #Lower left corner
        if lower_left_corner == '':
            lower_left_corner = -1
        else:
            lower_left_corner = int(lower_left_corner)

        lower_right_corner = lower_right_corner_selected.get() #Lower right corner
        if lower_right_corner == '':
            lower_right_corner = -1
        else:
            lower_right_corner = int(lower_right_corner)

        upper_left_corner = upper_left_corner_selected.get() #Upper left corner
        if upper_left_corner == '':
            upper_left_corner = -1
        else:
            upper_left_corner = int(upper_left_corner)

        upper_right_corner = upper_right_corner_selected.get() #Upper right corner
        if upper_right_corner == '':
            upper_right_corner = -1
        else:
            upper_right_corner = int(upper_right_corner)

        first_angle_between_diagonals = first_angle_between_diagonals_selected.get() #The angle between the diagonals, resting on the side
        if first_angle_between_diagonals == '':
            first_angle_between_diagonals = -1
        else:
            first_angle_between_diagonals = int(first_angle_between_diagonals)

        second_angle_between_diagonals = second_angle_between_diagonals_selected.get() #The angle between the diagonals, resting on the base
        if second_angle_between_diagonals == '':
            second_angle_between_diagonals = -1
        else:
            second_angle_between_diagonals = int(second_angle_between_diagonals)

        check()

    #Creating a program window

    window = Tk()
    window.title('Calculating values')

    first_top_button = Button(text = 'Calculate', command = convert)
    first_top_button.grid(column = 0, row = 0)

    second_top_button = Button(text = 'Shut down the program', command = exit)
    second_top_button.grid(column = 1, row = 0)

    isosceles_selected = IntVar()
    isosceles_txt = Label(text = 'Trapezoid isosceles')
    isosceles_txt.grid(column = 0, row = 1)
    isosceles_True = Radiobutton(window, text = 'True', value = 2, variable = isosceles_selected)
    isosceles_True.grid(column = 1, row = 1)
    isosceles_False = Radiobutton(window, text = 'False', value = 1, variable = isosceles_selected)
    isosceles_False.grid(column = 2, row = 1)
    isosceles_Unknown = Radiobutton(window, text = 'Unknown', value = 0, variable = isosceles_selected)
    isosceles_Unknown.grid(column = 3, row = 1)

    rectangular_selected = IntVar()
    rectangular_txt = Label(text = 'Trapezoid isosceles')
    rectangular_txt.grid(column = 0, row = 2)
    rectangular_True = Radiobutton(window, text = 'True', value = 2, variable = rectangular_selected)
    rectangular_True.grid(column = 1, row = 2)
    rectangular_False = Radiobutton(window, text = 'False', value = 1, variable = rectangular_selected)
    rectangular_False.grid(column = 2, row = 2)
    rectangular_Unknown = Radiobutton(window, text = 'Unknown', value = 0, variable = rectangular_selected)
    rectangular_Unknown.grid(column = 3, row = 2)

    smaller_base_txt = Label(text = 'Smaller base')
    smaller_base_txt.grid(column = 0, row = 3)
    smaller_base_selected = Entry()
    smaller_base_selected.grid(column = 1, row = 3)

    bigger_base_txt = Label(text = 'Bigger base')
    bigger_base_txt.grid(column = 0, row = 4)
    bigger_base_selected = Entry()
    bigger_base_selected.grid(column = 1, row = 4)

    height_txt = Label(text = 'Trapezoid height')
    height_txt.grid(column = 0, row = 5)
    height_selected = Entry()
    height_selected.grid(column = 1, row = 5)

    left_side_txt = Label(text = 'Left side')
    left_side_txt.grid(column = 0, row = 6)
    left_side_selected = Entry()
    left_side_selected.grid(column = 1, row = 6)

    right_side_txt = Label(text = 'Right side')
    right_side_txt.grid(column = 0, row = 7)
    right_side_selected = Entry()
    right_side_selected.grid(column = 1, row = 7)

    middle_line_txt = Label(text = 'Middle line')
    middle_line_txt.grid(column = 0, row = 8)
    middle_line_selected = Entry()
    middle_line_selected.grid(column = 1, row = 8)

    square_txt = Label(text = 'Trapezoid area')
    square_txt.grid(column = 0, row = 9)
    square_selected = Entry()
    square_selected.grid(column = 1, row = 9)

    perimeter_txt = Label(text = 'Perimeter of the trapezoid')
    perimeter_txt.grid(column = 0, row = 10)
    perimeter_selected = Entry()
    perimeter_selected.grid(column = 1, row = 10)

    first_diagonal_txt = Label(text = 'Diagonal from the lower left corner to the upper right')
    first_diagonal_txt.grid(column = 0, row = 11)
    first_diagonal_selected = Entry()
    first_diagonal_selected.grid(column = 1, row = 11)

    second_diagonal_txt = Label(text = 'Diagonal from the lower right corner to the upper left')
    second_diagonal_txt.grid(column = 0, row = 12)
    second_diagonal_selected = Entry()
    second_diagonal_selected.grid(column = 1, row = 12)

    upper_left_corner_txt = Label(text = 'Left corner with a smaller base, in degrees')
    upper_left_corner_txt.grid(column = 0, row = 13)
    upper_left_corner_selected = Entry()
    upper_left_corner_selected.grid(column = 1, row = 13)

    upper_right_corner_txt = Label(text = 'Right angle with a smaller base, in degrees')
    upper_right_corner_txt.grid(column = 0, row = 14)
    upper_right_corner_selected = Entry()
    upper_right_corner_selected.grid(column = 1, row = 14)

    lower_left_corner_txt = Label(text = 'Left corner with a larger base, in degrees')
    lower_left_corner_txt.grid(column = 0, row = 15)
    lower_left_corner_selected = Entry()
    lower_left_corner_selected.grid(column = 1, row = 15)

    lower_right_corner_txt = Label(text = 'Right angle with a larger base, in degrees')
    lower_right_corner_txt.grid(column = 0, row = 16)
    lower_right_corner_selected = Entry()
    lower_right_corner_selected.grid(column = 1, row = 16)

    first_angle_between_diagonals_txt = Label(text = 'The angle between the diagonals, resting on the side')
    first_angle_between_diagonals_txt.grid(column = 0, row = 17)
    first_angle_between_diagonals_selected = Entry()
    first_angle_between_diagonals_selected.grid(column = 1, row = 17)

    second_angle_between_diagonals_txt = Label(text = 'The angle between the diagonals, resting on the base')
    second_angle_between_diagonals_txt.grid(column = 0, row = 18)
    second_angle_between_diagonals_selected = Entry()
    second_angle_between_diagonals_selected.grid(column = 1, row = 18)

    radius_inscribed_circle_selected = IntVar()
    radius_inscribed_circle_txt = Label(text = 'Radius of the inscribed circle')
    radius_inscribed_circle_txt.grid(column = 0, row = 19)
    radius_inscribed_circle_True = Radiobutton(window, text = 'True', value = -1, variable = radius_inscribed_circle_selected)
    radius_inscribed_circle_True.grid(column = 1, row = 19)
    radius_inscribed_circle_False = Radiobutton(window, text = 'False', value = -2, variable = radius_inscribed_circle_selected)
    radius_inscribed_circle_False.grid(column = 2, row = 19)
    radius_inscribed_circle_Known = Entry()
    radius_inscribed_circle_Known.grid(column = 3, row = 19)

    radius_circumscribed_circle_selected = IntVar()
    radius_circumscribed_circle_txt = Label(text = 'The radius of the circumscribed circle')
    radius_circumscribed_circle_txt.grid(column = 0, row = 20)
    radius_circumscribed_circle_True = Radiobutton(window, text = 'True', value = -1, variable = radius_circumscribed_circle_selected)
    radius_circumscribed_circle_True.grid(column = 1, row = 20)
    radius_circumscribed_circle_False = Radiobutton(window, text = 'False', value = -2, variable = radius_circumscribed_circle_selected)
    radius_circumscribed_circle_False.grid(column = 2, row = 20)
    radius_circumscribed_circle_Known = Entry(window)
    radius_circumscribed_circle_Known.grid(column = 3, row = 20)

    window.mainloop()
