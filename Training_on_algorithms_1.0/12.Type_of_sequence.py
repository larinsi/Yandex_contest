def type_of_sequence():
    status = {0: "CONSTANT",
              1: "ASCENDING",
              2: "WEAKLY ASCENDING",
              3: "DESCENDING",
              4: "WEAKLY DESCENDING",
              5: "RANDOM"}
    prev = None
    seq_type = status[5]
    len_of_seq = 0
    while True:
        num = int(input())
        if num == -2000000000:
            break
        if prev == None:
            prev = num
            seq_type = status[0]
            len_of_seq += 1
            continue
        if len_of_seq == 1:
            if num > prev:
                seq_type = status[1]
            elif num < prev:
                seq_type = status[3]
            prev = num
            len_of_seq += 1
            continue
        if num == prev:
            if seq_type in [status[1], status[2]]:
                seq_type = status[2]
            elif seq_type in [status[3], status[4]]:
                seq_type = status[4]
        elif num > prev:
            if seq_type in [status[0], status[2]]:
                seq_type = status[2]
            elif seq_type in [status[3], status[4]]:
                seq_type = status[5]
        elif num < prev:
            if seq_type in [status[0], status[4]]:
                seq_type = status[4]
            elif seq_type in [status[1], status[2]]:
                seq_type = status[5]
        prev = num
        len_of_seq += 1
    print(seq_type)


type_of_sequence()