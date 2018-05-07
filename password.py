import sys


def passwordCracker(passwords, attempt):
    # Complete this function
    attempt = "A" + attempt
    dynamic_prog_array = [False] * len(attempt)
    dynamic_prog_array[0] = True
    results = []
    results.append("end")


    for i in range(1, len(attempt)):
        for word_in_dict in passwords:
            start = i-len(word_in_dict)+1
            end = i+1

            if start>=1:
                check = attempt[start: end]

                if word_in_dict == check and dynamic_prog_array[start-1] is True:
                    if dynamic_prog_array[i] is False:
                        results.append(check)
                    dynamic_prog_array[i] = True

        if dynamic_prog_array[i] is False:
            results.append("nah")


    if dynamic_prog_array[-1] is True:

        result_string = ""
        j = len(results)-1
        word_list = []

        while j>=0:
            word_list.append(results[j])
            j = j - len(results[j])

        word_list = word_list[:len(word_list)-1]
        word_list.reverse()

        for word in word_list:
            result_string += word + " "

        return(result_string)

    else:

        return "WRONG PASSWORD"





if __name__ == "__main__":
    t = int(input().strip())
    for a0 in range(t):
        n = int(input().strip())
        passwords = input().strip().split(' ')
        attempt = input().strip()
        result = passwordCracker(passwords, attempt)
        print(result)