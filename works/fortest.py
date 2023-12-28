x=[2, 4, 3, 6, 5, 19]



def f_prime(num_3):
    m = []
    # for number in range(2, max(num_3) + 1): 
    for number in num_3:
        print(number)
        if number > 1: 
            for i in range(1, number):
                #print(i)
                # f = filter(lambda b: b % i == 0, i)    
                if(number % i) == 0: 
                    break 
                else: 
                    m.append(number)
                    # return(m)
                # print(f)
                # print(list(f))
                    print(m)
    # # for v in range(2, num_3[-1]):
    #     k=2
    #     for a in num_3:
    #         while a % k != 0:
    #             k = k + 1
                

            

 

f_prime(x)
# print(f_prime(x))