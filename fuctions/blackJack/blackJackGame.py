import random

try:
    import tkinter
except ImportError:
    import Tkinter as tkinter


# function for loading cards
def load_images(card_images):
    suits = ['heart', 'club', 'diamond', 'spade']
    face_cards = ['jack', 'queen', 'king']
    if tkinter.TkVersion >= 8.6:
        extention = 'png'
    else:
        extention = 'ppm'
    for suit in suits:
        # Extract cards images from the directory 
        for card in range(1, 11):
            name = 'cards_{}/{}_{}.{}'.format(
                extention, str(card), suit, extention)
            # print(name) for debug
            image = tkinter.PhotoImage(file=name)
            card_images.append((card, image,))

        for card in face_cards:
            name = 'cards_{}/{}_{}.{}'.format(
                extention, str(card), suit, extention)
            image = tkinter.PhotoImage(file=name)
            card_images.append((10, image,))


def deal_card(frame):
    # pop the next card off the top of the deck
    next_card = deck.pop(0)
    # add the image to a label and display the label
    tkinter.Label(frame, image=next_card[1],
                  relief='raised').pack(side='left')
    # now return the card's face value
    return next_card


def deal_player():
    # player_score = 0
    def_player_score = 0
    card_value = deal_card(player_card_frame)[0]
    if card_value == 1 and not player_ace:
        card_value = 11
    def_player_score +=card_value
    player_score = def_player_score
    if def_player_score > 21 and player_ace:
        def_player_score -= 10
    player_score_label.set(def_player_score)
    if player_score > 21:
        result_text.set("Dealer wins!")


def deal_dealer():
    deal_card(dealer_card_frame)


mainWindow = tkinter.Tk()

# Set up the screen and frames
mainWindow.title("Black Jack Game")
mainWindow.geometry("640x480")

mainWindow.configure(background='green')

result_text = tkinter.StringVar()
result = tkinter.Label(mainWindow, textvariable=result_text)
result.grid(row=0, column=0, columnspan=3)

card_frame = tkinter.Frame(mainWindow, relief="sunken",
                           borderwidth=1, background="green")
card_frame.grid(row=1, column=0, sticky='ew',
                columnspan=3, rowspan=2)

dealer_score_label = tkinter.IntVar()
tkinter.Label(card_frame, text="Dealer",
              background="green", fg="white").grid(row=0, column=0)
tkinter.Label(card_frame, textvariable=dealer_score_label,
              background="green", fg="white").grid(row=1, column=0)

# embedded frame hold the card images

dealer_card_frame = tkinter.Frame(card_frame, background="green")
dealer_card_frame.grid(row=0, column=1, sticky="ew", rowspan=2)

player_score_label = tkinter.IntVar()
player_score = 0
player_ace = False

tkinter.Label(card_frame, text="Player",
              background="green", fg="white").grid(row=2, column=0)
tkinter.Label(card_frame, textvariable=player_score_label,
              backgroun="green", fg="white").grid(row=3, column=0)

# embedded frame to hold the card images
player_card_frame = tkinter.Frame(card_frame, background="green")
player_card_frame.grid(row=2, column=1, sticky="ew", rowspan=2)

button_frame = tkinter.Frame(mainWindow)
button_frame.grid(row=3, column=0, columnspan=3, sticky="w")

dealer_button = tkinter.Button(button_frame, text="Dealer",
                               command=deal_dealer)
dealer_button.grid(row=0, column=0)

player_button = tkinter.Button(button_frame, text="Player",
                               command=deal_player)
player_button.grid(row=0, column=1)

# load cards
cards = []
load_images(cards)
# print(cards)
# Create a new deck cards and shuffle them

deck = list(cards)  # Creating a new separate list
random.shuffle(deck)

# Create a lists to store the dealer's and player's hands
dealer_hand = []
player_hand = []

mainWindow.mainloop()
