from score import Score


def test_write_name():
    '''Testing the the class of collecting player's name
    in the file.txt'''

    score_test = Score("game_starter\\scores_test.txt")

    score_test.write_name("Amanda")
    score_test.write_name("Sima")
    score_test.write_name("Amanda")
    score_test.write_name("Sima")
    score_test.write_name("Sima")
    score_test.write_name("Sarah")
    score_test.write_name("Sarah")
    score_test.write_name("Sima")
    score_test.write_name("Amanda")

    with open("game_starter\\scores_test.txt", 'r') as txt_file:
        sorted_names = []
        for line in txt_file:
            line_splitted = line.split(' ')
            line_splitted.pop()
            key = ""
            for ele in line_splitted:
                key += ele
            sorted_names.append(key)
        txt_file.close()

    assert sorted_names[0] == "Sima"
    assert sorted_names[1] == "Amanda"
    assert sorted_names[2] == "Sarah"
