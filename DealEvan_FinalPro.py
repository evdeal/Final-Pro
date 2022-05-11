# Evan Deal
# Rough Draft Final Project
# 5/3/2022

import tkinter as tk

from tkinter import *

from tkinter import messagebox

from PIL import ImageTk, Image

# creating the root window

root = tk.Tk()

root.minsize(800, 600)  # setting the size of the main window

root.title("The Helpful Vender")  # title of the window

# opening 1st image file

image1 = Image.open("C:\\Users\\evand\\OneDrive\\Pictures\\Saved Pictures\\coke.png")

# resizing the image

image1 = image1.resize((250, 175), Image.ANTIALIAS)

test = ImageTk.PhotoImage(image1)

# opening 2nd image file

image2 = Image.open("C:\\Users\\evand\\OneDrive\\Pictures\\Saved Pictures\\snacks.png")

# resizing the image

image2 = image2.resize((250, 175), Image.ANTIALIAS)

test2 = ImageTk.PhotoImage(image2)

# setting 1st image in label l3

l3 = tk.Label(root, image=test)

l3.place(x=100, y=10)  # position the label

# setting 2nd image in label l4

l4 = tk.Label(root, image=test2)

l4.place(x=450, y=10)  # position the label

# displaying a menu for drinks

l5 = tk.Label(root, text="Drinks: Coca-Cola, Sprite, Fanta, Sweet-Tea, Water", font=("Arial", 15))

l5.place(x=50, y=200)  # position the label

# displaying a menu for snacks

l6 = tk.Label(root, text="Snacks: Cheez-it, GoldFish, Chewy Granola Bar, Pretzels", font=("Arial", 15))

l6.place(x=50, y=230)  # position the label

# displaying menu for candy
l7 = tk.Label(root, text="Candy: Crunch Bar, Nerds Rope, Chocolate Bar, Oreo's, Skittles", font=("Arial", 15))

l7.place(x=50, y=260)  # position the label

l1 = tk.Label(root, text="Enter Drink Names", font=("Arial", 15))

l1.place(x=50, y=300)  # position the label

# entry box with font  and size

t1 = tk.Entry(root, font=("Arial", 15))

t1.place(x=250, y=300)  # position of entry box

l2 = tk.Label(root, text="Enter Snack Names", font=("Arial", 15))

l2.place(x=50, y=330)  # position of label

t2 = tk.Entry(root, font=("Arial", 15))

t2.place(x=250, y=330)  # position of entry box

l3 = tk.Label(root, text="Enter Candy Names", font=("Arial", 15))

l3.place(x=50, y=360)  # position of label

t3 = tk.Entry(root, font=("Arial", 15))

t3.place(x=250, y=360)  # position of label


# function to calculate price

def calc():
    s1 = t1.get()  # all the contents from 1st entry

    s2 = t2.get()  # all the contents from 2nd entry

    s3 = t3.get()  # all the contents from 3rd entry

    drinks = s1.split(sep=',')  # separating each item from s1

    snacks = s2.split(sep=',')  # separating each item from s2

    candy = s3.split(sep=',')  # separating each item from s3

    len1 = len(drinks)  # finding the length of s1

    len2 = len(snacks)  # finding the length of s2

    len3 = len(candy)  # finding the length of s3

    Drinks_Price = len1 * 4.99  # multiplying drinks by base price

    Snacks_Price = len2 * 3.99  # multiplying snacks by base price

    Candy_Price = len3 * 2.99  # multiplying candy by base price

    # displaying in a message box

    s = 'Drinks:${} Snacks:${} Candy:${}'.format(Drinks_Price, Snacks_Price, Candy_Price)

    messagebox.showinfo('Price of Items', s)

    # returning price

    return Drinks_Price, Snacks_Price, Candy_Price, drinks, snacks, candy


def total():
    # collecting price of drinks, snacks, candy, and total amount purchased

    Drinks_Price, Snacks_Price, Candy_Price, drinks, snacks, candy = calc()

    pr_total = Drinks_Price + Snacks_Price + Candy_Price

    s = 'Total price : ' + str(pr_total)  # Display for total price

    child_w = Toplevel(root)  # creating another window

    child_w.geometry("450x350")  # size of child window

    child_w.grid_location(x=300, y=300)  # location of child window

    child_w.title("Total Price of Order")  # title of the window

    # creating labels

    label_child = Label(child_w, text=s, font='Helvetica 15')

    label_child.place(x=20, y=50)  # positioning the label

    l2 = Label(child_w, text="Thank you for ordering and please come again!", font='Helvetica 15')

    l2.place(x=20, y=100)  # positioning the label

    s2 = ' '.join(drinks) + " " + ' '.join(snacks) + " " + ' '.join(candy)

    l3 = Label(child_w, text=s2, font='Helvetica 15')

    l3.place(x=20, y=150)  # positioning the label


# creating buttons

# button to calculate price of items

b1 = tk.Button(root, text="Items Individual Total", command=calc, font=("Arial", 15))

b1.place(x=50, y=400)

# button to calculate total price of All Items

b2 = tk.Button(root, text="Total Price of All Items", command=total, font=("Arial", 15))

b2.place(x=50, y=445)

# button to exit from the program

b3 = tk.Button(root, text="Exit", command=root.destroy, font=("Arial", 15))

b3.place(x=50, y=490)

# starting the main window

root.mainloop()
