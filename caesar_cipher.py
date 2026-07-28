
print("-----CAESAR CIPHER-----")
user_choice=int(input("enter the choice (encrypt=0/decrypt=1) = "))
user_msg=input("enter the message = ").lower()
user_shift=int(input("enter the shift you want to do = "))
alphabet=['a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z']
encrypt=[]
decrypt=[]
for i in user_msg:
    if i in alphabet:
        index_value=alphabet.index(i)
        print("the index value of {} is = ".format(i),index_value)
        
        
        if user_choice==0:
            new_index=index_value+user_shift
            if new_index>25:
                new_index-=26
                alphabet[new_index]
                encrypt.append(alphabet[new_index])
            else:
                alphabet[new_index]
                encrypt.append(alphabet[new_index])
                
                
        elif user_choice==1:
            new_index=index_value-user_shift
            if new_index<0:
                new_index+=26
                alphabet[new_index]
                decrypt.append(alphabet[new_index])
            else:
                alphabet[new_index]
                decrypt.append(alphabet[new_index])
                
                
    else:
        if user_choice==0:
            encrypt.append(i)
        else:
            decrypt.append(i)  
                
                
print("----FINAL RESULT----")      
if user_choice==0:
    print("the encrypted message is ")
    for i in encrypt:
        print(i,end="")
else:
    print("the decrypted message is ")
    for i in decrypt:
        print(i,end="")