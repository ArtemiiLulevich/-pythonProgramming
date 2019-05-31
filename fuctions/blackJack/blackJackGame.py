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
        extension = 'png'
    else:
        extension = 'ppm'
    for suit in suits:
        # Extract cards images from the directory
        for card in range(1, 11):
            name = 'cards_{}/{}_{}.{}'.format(
                extension, str(card), suit, extension)
            # print(name) for debug
            image = tkinter.PhotoImage(file=name)
            card_images.append((card, image,))

        for card in face_cards:
            name = 'cards_{}/{}_{}.{}'.format(
                extension, str(card), suit, extension)
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


def score_hand(hand):
    # Calculate the total score of all cards ini the list
    # Only one ace can have the value 11, and this will be reduce to
    # 1 if th hand would bust
    score = 0
    ace = False
    for next_card in hand:
        card_value = next_card[0]
        if card_value == 1 and not ace:
            ace = True
            card_value = 11
        score += card_value
        # if we would bust, check if there is an ace and subtract 10
        if score > 21 and ace:
            score -= 10
            ace = False
    return score


def deal_player():
    player_hand.append(deal_card(player_card_frame))
    player_score = score_hand(player_hand)

    player_score_label.set(player_score)
    if player_score > 21:
        result_text.set("Dealer Wins!")
        wins_score(False)

    """
    global player_score
    global player_ace
    card_value = deal_card(player_card_frame)[0]
    if card_value == 1 and not player_ace:
        player_ace = True
        card_value = 11
    player_score +=card_value
    if player_score > 21 and player_ace:
        player_ace = False
        player_score -= 10
    player_score_label.set(player_score)
    if player_score > 21:
        result_text.set("Dealer wins!")
        """


def deal_dealer():
    dealer_score = score_hand(dealer_hand)
    while 0 < dealer_score < 17:
        dealer_hand.append(deal_card(dealer_card_frame))
        dealer_score = score_hand(dealer_hand)
        dealer_score_label.set(dealer_score)

    player_score = score_hand(player_hand)
    if player_score > 21:
        result_text.set("Dealer wins!")
        wins_score(False)
    elif dealer_score > 21 or dealer_score < player_score:
        result_text.set("Player wins!")
        wins_score(True)
    elif dealer_score > player_score:
        result_text.set("Dealer wins!")
        wins_score(False)
    else:
        result_text.set("Draw!")
        button_disabled()


def wins_score(party):
    if party:
        wins_list['P'] += 1
    else:
        wins_list['D'] += 1
    player_wins_label.set(wins_list['P'])
    dealer_wins_label.set(wins_list['D'])
    button_disabled()


def button_disabled():
    player_button["state"] = "disabled"
    dealer_button["state"] = "disabled"


def start_new_game():
    global dealer_card_frame
    global player_card_frame
    global dealer_hand
    global player_hand
    global result_text
    global deck
    global cards

    dealer_card_frame.destroy()
    dealer_card_frame = tkinter.Frame(card_frame, background="green")
    dealer_card_frame.grid(row=0, column=1, sticky="ew", rowspan=2)

    player_card_frame.destroy()
    player_card_frame = tkinter.Frame(card_frame, background="green")
    player_card_frame.grid(row=2, column=1, sticky="ew", rowspan=2)

    player_button["state"] = "active"
    dealer_button["state"] = "active"

    result_text.set("")

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

    deal_player()
    dealer_hand.append(deal_card(dealer_card_frame))
    dealer_score_label.set(score_hand(dealer_hand))
    deal_player()

# print(__name__)

# if __name__ == "__main__":
def play():
    start_new_game()
    mainWindow.mainloop()

mainWindow = tkinter.Tk()

# Set up the screen and frames
mainWindow.title("Black Jack Game")
mainWindow.geometry("640x480")

mainWindow.configure(background='green')

result_text = tkinter.StringVar()

result = tkinter.Label(mainWindow, textvariable=result_text, background='green')
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
# player_score = 0
# player_ace = False

tkinter.Label(card_frame, text="Player",
              background="green", fg="white").grid(row=2, column=0)
tkinter.Label(card_frame, textvariable=player_score_label,
              backgroun="green", fg="white").grid(row=3, column=0)

# embedded frame to hold the card images
player_card_frame = tkinter.Frame(card_frame, background="green")
player_card_frame.grid(row=2, column=1, sticky="ew", rowspan=2)

wins_frame = tkinter.Frame(mainWindow, background="green")
wins_frame.grid(row=3, column=0, columnspan=3, sticky="sewn")
player_wins_label = tkinter.IntVar()
tkinter.Label(wins_frame, text="Player",
              background="red", fg="white").grid(row=1, column=0, sticky="sewn")
tkinter.Label(wins_frame, textvariable=player_wins_label,
              backgroun="red", fg="white").grid(row=2, column=0, sticky="sewn")
dealer_wins_label = tkinter.IntVar()
tkinter.Label(wins_frame, text="Dealer",
              background="red", fg="white").grid(row=1, column=1, sticky="sewn")
tkinter.Label(wins_frame, textvariable=dealer_wins_label,
              background="red", fg="white").grid(row=2, column=1, sticky="sewn")

button_frame = tkinter.Frame(mainWindow)
button_frame.grid(row=4, column=0, columnspan=3, sticky="w")

dealer_button = tkinter.Button(button_frame, text="Dealer",
                               command=deal_dealer)
dealer_button.grid(row=0, column=0)

player_button = tkinter.Button(button_frame, text="Player",
                               command=deal_player)
player_button.grid(row=0, column=1)

new_game_button = tkinter.Button(button_frame, text="New Game",
                                 command=start_new_game)
new_game_button.grid(row=0, column=2)

wins_list = {'P': 0, 'D': 0}
player_wins_label.set(wins_list['P'])
player_wins_label.set(wins_list['D'])

# start_new_game()

# # load cards
# cards = []
# load_images(cards)
# # print(cards)
# # Create a new deck cards and shuffle them
#
# deck = list(cards)  # Creating a new separate list
# random.shuffle(deck)
#
# # Create a lists to store the dealer's and player's hands
# dealer_hand = []
# player_hand = []
#
# deal_player()
# dealer_hand.append(deal_card(dealer_card_frame))
# dealer_score_label.set(score_hand(dealer_hand))
# deal_player()

if __name__ == '__main__':
    # print(__name__)
    play()
