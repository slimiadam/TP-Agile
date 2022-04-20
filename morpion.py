board = [1, 2, 3, 4, 5, 6, 7, 8, 9]
win_combinations = ((0, 1, 2), (3, 4, 5), (6, 7, 8), (0, 3, 6), (1, 4, 7), (2, 5, 8), (0, 4, 8), (2, 4, 6))

def draw():
    print(board[0], board[1], board[2])
    print(board[3], board[4], board[5])
    print(board[6], board[7], board[8])
    print()

def p1():
  n = choose_number()
  if board[n] == "X" or board[n] == "O":
    print("La case est déjà prise, veuillez rejouer")
    p1()
  else:
    board[n] = "X"
    return True

def p2():
  n = choose_number()
  if board[n] == "X" or board[n] == "O":
    print("La case est déjà prise, veuillez rejouer")
    p2()
  else:
    board[n] = "O"
    return True

def choose_number():
  while True:
    while True:
      a = input()
      try:
        a  = int(a)
        a -= 1
        if a in range(0, 9):
          return a
        else:
          print("Valeur hors plateau de jeu, veuillez rejouer")
          continue
      except ValueError:
        print("Veuillez entrer un nombre")
        continue

def check_board(board):
  count = 0
  for a in win_combinations:
    if board[a[0]] == board[a[1]] == board[a[2]] == "X":
      print("Le joueur n°1 a gagné")
      return True

    if board[a[0]] == board[a[1]] == board[a[2]] == "O":
      print("Le joueur n°2 a gagné")
      return True
  for a in range(9):
    if board[a] == "X" or board[a] == "O":
      count += 1
    if count == 9:
      print("Aucun gagnant possible, le jeu est fini")
      return True

def jeu():

  end = False
  while not end:
    draw()
    end = check_board(board)
    if end == True:
      break
    print("Joueur n°1 à vous de jouer, choisissez une case")
    p1()
    print()
    draw()
    end = check_board(board)
    if end == True:
      break
    print("Joueur n°2 à vous de jouer, choisissez une case")
    p2()
    print()

  if input("Rejouer ?(y/n)") == "y":
    print()
    jeu()

if __name__ == '__main__':
  jeu()
