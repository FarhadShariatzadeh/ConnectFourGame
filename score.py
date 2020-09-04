

class Score:

    def __init__(self, file_name):
        '''geting file.txt and add the user name if win to the txt'''

        self.file_name = file_name
        self.dic_name_score = {}

    def write_name(self, user_name):
        with open(self.file_name, 'r+') as txt_file:
            for line in txt_file:
                line_splitted = line.split(' ')
                value = int(line_splitted.pop())
                key = ""
                for ele in line_splitted:
                    key += ele
                self.dic_name_score[key] = value

            if user_name in self.dic_name_score:
                self.dic_name_score[user_name] += 1
            else:
                self.dic_name_score[user_name] = 1
            sorted_dic = sorted(self.dic_name_score.items(),
                                key=lambda x: x[1], reverse=True)
            # It help to clear the txt every time and then add sorted
            # dictionary each time
            txt_file.seek(0)
            txt_file.truncate()
            for (k, v) in sorted_dic:
                string_name = str(k) + ' ' + str(v)
                txt_file.write(string_name+'\n')
            txt_file.close()
