from pyfiglet import Figlet

"""
FIGLET:
It takes ASCII text and renders it in ASCII art fonts
['1943____', '1row', '3-d', '3d-ascii', '3d_diagonal', '3x5', '4max', '4x4_offr', '5lineoblique', '5x7', '5x8', '64f1____', '6x10', '6x9', 'acrobatic', 'advenger', 'alligator', 'alligator2', 'alpha', 'alphabet', 'amc_3_line', 'amc_3_liv1', 'amc_aaa01', 'amc_neko', 'amc_razor', 'amc_razor2', 'amc_slash', 'amc_slider', 'amc_thin', 'amc_tubes', 'amc_untitled', 'ansi_regular', 'ansi_shadow', 'aquaplan', 'arrows', 'ascii_new_roman', 'ascii___', 'asc_____', 'assalt_m', 'asslt__m', 'atc_gran', 'atc_____', 'avatar', 'a_zooloo', 'b1ff', 'banner', 'banner3-D', 'banner3', 'banner4', 'barbwire', 'basic', 'battlesh', 'battle_s', 'baz__bil', 'bear', 'beer_pub', 'bell', 'benjamin', 'big', 'bigchief', 'bigfig', 'big_money-ne', 'big_money-nw', 'big_money-se', 'big_money-sw', 'binary', 'block', 'blocks', 'blocky', 'bloody', 'bolger', 'braced', 'bright', 'brite', 'briteb', 'britebi', 'britei', 'broadway', 'broadway_kb', 'bubble', 'bubble_b', 'bubble__', 'bulbhead', 'b_m__200', 'c1______', 'c2______', 'calgphy2', 'caligraphy', 'calvin_s', 'cards', 'catwalk', 'caus_in_', 'char1___', 'char2___', 'char3___', 'char4___', 'charact1', 'charact2', 'charact3', 'charact4', 'charact5', 'charact6', 'characte', 'charset_', 'chartr', 'chartri', 'chiseled', 'chunky', 'clb6x10', 'clb8x10', 'clb8x8', 'cli8x8', 'clr4x6', 'clr5x10', 'clr5x6', 'clr5x8', 'clr6x10', 'clr6x6', 'clr6x8', 'clr7x10', 'clr7x8', 'clr8x10', 'clr8x8', 'coil_cop', 'coinstak', 'cola', 'colossal', 'computer', 'com_sen_', 'contessa', 'contrast', 'convoy__', 'cosmic', 'cosmike', 'cour', 'courb', 'courbi', 'couri', 'crawford', 'crawford2', 'crazy', 'cricket', 'cursive', 'cyberlarge', 'cybermedium', 'cybersmall', 'cygnet', 'c_ascii_', 'c_consen', 'danc4', 'dancing_font', 'dcs_bfmo', 'decimal', 'deep_str', 'defleppard', 'def_leppard', 'delta_corps_priest_1', 'demo_1__', 'demo_2__', 'demo_m__', 'devilish', 'diamond', 'diet_cola', 'digital', 'doh', 'doom', 'dos_rebel', 'dotmatrix', 'double', 'double_shorts', 'drpepper', 'druid___', 'dwhistled', 'd_dragon', 'ebbs_1__', 'ebbs_2__', 'eca_____', 'eftichess', 'eftifont', 'eftipiti', 'eftirobot', 'eftitalic', 'eftiwall', 'eftiwater', 'efti_robot', 'electronic', 'elite', 'epic', 'etcrvs__', 'e__fist_', 'f15_____', 'faces_of', 'fairligh', 'fair_mea', 'fantasy_', 'fbr12___', 'fbr1____', 'fbr2____', 'fbr_stri', 'fbr_tilt', 'fender', 'filter', 'finalass', 'fireing_', 'fire_font-k', 'fire_font-s', 'flipped', 'flower_power', 'flyn_sh', 'fourtops', 'fp1_____', 'fp2_____', 'fraktur', 'funky_dr', 'fun_face', 'fun_faces', 'future_1', 'future_2', 'future_3', 'future_4', 'future_5', 'future_6', 'future_7', 'future_8', 'fuzzy', 'gauntlet', 'georgi16', 'georgia11', 'ghost', 'ghost_bo', 'ghoulish', 'glenyn', 'goofy', 'gothic', 'gothic__', 'graceful', 'gradient', 'graffiti', 'grand_pr', 'greek', 'green_be', 'hades___', 'heart_left', 'heart_right', 'heavy_me', 'helv', 'helvb', 'helvbi', 'helvi', 'henry_3d', 'heroboti', 'hex', 'hieroglyphs', 'high_noo', 'hills___', 'hollywood', 'home_pak', 'horizontal_left', 'horizontal_right', 'house_of', 'hypa_bal', 'hyper___', 'icl-1900', 'impossible', 'inc_raw_', 'invita', 'isometric1', 'isometric2', 'isometric3', 'isometric4', 'italic', 'italics_', 'ivrit', 'jacky', 'jazmine', 'jerusalem', 'joust___', 'js_block_letters', 'js_bracket_letters', 'js_capital_curves', 'js_cursive', 'js_stick_letters', 'katakana', 'kban', 'keyboard', 'kgames_i', 'kik_star', 'knob', 'konto', 'konto_slant', 'krak_out', 'larry3d', 'lazy_jon', 'lcd', 'lean', 'letters', 'letterw3', 'letter_w', 'lexible_', 'lil_devil', 'line_blocks', 'linux', 'lockergnome', 'madrid', 'mad_nurs', 'magic_ma', 'marquee', 'master_o', 'maxfour', 'mayhem_d', 'mcg_____', 'merlin1', 'merlin2', 'mig_ally', 'mike', 'mini', 'mirror', 'mnemonic', 'modern__', 'modular', 'morse', 'morse2', 'moscow', 'mshebrew210', 'muzzle', 'nancyj-fancy', 'nancyj-improved', 'nancyj-underlined', 'nancyj', 'new_asci', 'nfi1____', 'nipples', 'notie_ca', 'npn_____', 'nscript', 'ntgreek', 'nvscript', 'o8', 'octal', 'odel_lak', 'ogre', 'ok_beer_', 'old_banner', 'os2', 'outrun__', 'pacos_pe', 'panther_', "patorjk's_cheese", 'patorjk-hex', 'pawn_ins', 'pawp', 'peaks', 'pebbles', 'pepper', 'phonix__', 'platoon2', 'platoon_', 'pod_____', 'poison', 'puffy', 'puzzle', 'pyramid', 'p_skateb', 'p_s_h_m_', 'r2-d2___', 'radical_', 'rad_phan', 'rad_____', 'rainbow_', 'rally_s2', 'rally_sp', 'rammstein', 'rampage_', 'rastan__', 'raw_recu', 'rci_____', 'rectangles', 'red_phoenix', 'relief', 'relief2', 'rev', 'ripper!_', 'road_rai', 'rockbox_', 'rok_____', 'roman', 'roman___', 'rot13', 'rotated', 'rounded', 'rowancap', 'rozzo', 'runic', 'runyc', 'sans', 'sansb', 'sansbi', 'sansi', 'santa_clara', 'sblood', 'sbook', 'sbookb', 'sbookbi', 'sbooki', 'script', 'script__', 'serifcap', 'shadow', 'shimrod', 'short', 'skateord', 'skateroc', 'skate_ro', 'sketch_s', 'slant', 'slant_relief', 'slide', 'slscript', 'sl_script', 'small', 'small_caps', 'small_poison', 'small_shadow', 'small_slant', 'smisome1', 'smkeyboard', 'smscript', 'smshadow', 'smslant', 'smtengwar', 'sm______', 'soft', 'space_op', 'spc_demo', 'speed', 'spliff', 'stacey', 'stampate', 'stampatello', 'standard', 'starwars', 'star_strips', 'star_war', 'stealth_', 'stellar', 'stencil1', 'stencil2', 'stforek', 'stick_letters', 'stop', 'straight', 'street_s', 'stronger_than_all', 'sub-zero', 'subteran', 'super_te', 'swamp_land', 'swan', 'sweet', 'tanja', 'tav1____', 'taxi____', 'tec1____', 'tecrvs__', 'tec_7000', 'tengwar', 'term', 'test1', 'the_edge', 'thick', 'thin', 'this', 'thorned', 'threepoint', 'ticks', 'ticksslant', 'tiles', 'times', 'timesofl', 'tinker-toy', 'ti_pan__', 'tomahawk', 'tombstone', 'top_duck', 'train', 'trashman', 'trek', 'triad_st', 'ts1_____', 'tsalagi', 'tsm_____', 'tsn_base', 'tty', 'ttyb', 'tubular', 'twin_cob', 'twisted', 'twopoint', 'type_set', 't__of_ap', 'ucf_fan_', 'ugalympi', 'unarmed_', 'univers', 'usaflag', 'usa_pq__', 'usa_____', 'utopia', 'utopiab', 'utopiabi', 'utopiai', 'varsity', 'vortron_', 'war_of_w', 'wavy', 'weird', 'wet_letter', 'whimsy', 'wow', 'xbrite', 'xbriteb', 'xbritebi', 'xbritei', 'xchartr', 'xchartri', 'xcour', 'xcourb', 'xcourbi', 'xcouri', 'xhelv', 'xhelvb', 'xhelvbi', 'xhelvi', 'xsans', 'xsansb', 'xsansbi', 'xsansi', 'xsbook', 'xsbookb', 'xsbookbi', 'xsbooki', 'xtimes', 'xtty', 'xttyb', 'yie-ar__', 'yie_ar_k', 'z-pilot_', 'zig_zag_', 'zone7___']
"""


def create_board_nums():
    # 1 | 2 | 3
    return [i for i in range(1, 3 * 3 + 1)]


def create_board():
    # ""|""|""
    return [' ' for i in range(9)]


def print_board(brd):
    for i in range(3):
        print(' | '.join([str(brd[i]) for i in range(i * 3, i * 3 + 3)]))


def empty_squares():
    return ' ' in board


def player_name_mark():
    # {'X': 'Sway', 'O': 'Ivan'}
    players_gen = {}
    for i in range(2):
        name = input(f"Player {i + 1}, enter name: ")
        if i == 1:
            symbol = 'O' if players_gen.get('X') else 'X'
            players_gen[symbol] = name
        while i == 0:
            try:
                symbol = input(f"Player {i + 1}, enter mark (X) or (O): ")
                if symbol == 'X' or symbol == 'O':
                    players_gen[symbol] = name
                    break
                raise ValueError
            except ValueError:
                print('Mark can only be (X) or (O)')
    return players_gen


def valid_square(value):
    if value in range(1, 10) and board[value - 1] == ' ':
        return True
    return False


def choose_square(player):
    while True:
        try:
            square = input(f"{players[player]} -> Choose a valid square (1-9): ")
            value = int(square)
            if valid_square(value):
                break
            raise ValueError
        except ValueError:
            print('Not a number or not an empty square')
    return value - 1


def make_move(player):
    idx = choose_square(player)
    board[idx] = player

    if winner(idx, player):
        print(f'Winner is {players[player]}!!')
        print_board(board)
        raise SystemExit


def winner(square, player):
    # if square = 5, row_ind = 1, board[row] = [3, 4, 5]
    row_ind = square // 3
    row = board[row_ind * 3: (row_ind + 1) * 3]
    if all(symbol == player for symbol in row):
        return True
    # if square = 5, col_ind = 1, board[col] = [1, 5, 8]
    col_idx = square % 3
    col = [board[col_idx + i * 3] for i in range(3)]
    if all(symbol == player for symbol in col):
        return True
    # diagonals
    if square % 2 == 0:
        left_diag = [board[i] for i in [2, 4, 6]]
        if all(symbol == player for symbol in left_diag):
            return True
        right_diag = [board[i] for i in [0, 4, 8]]
        if all(symbol == player for symbol in right_diag):
            return True


def play():
    figlet = Figlet('4x4_offr')

    print(figlet.renderText("TIC-TAC-TOE"))

    player = 'X'
    print_board(create_board_nums())
    while empty_squares():
        make_move(player)
        print_board(board)
        player = 'X' if player == 'O' else "O"

    if not empty_squares():
        print('DRAW')


if __name__ == "__main__":
    board = create_board()
    # players = player_name_mark()
    players = {'X': 'Sway', 'O': 'Ivan'}
    play()
