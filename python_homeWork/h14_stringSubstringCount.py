def count_substring(string, sub_string):
    count=0
    stop=len(sub_string)
    for i in range(len(string)):
        print(sub_string,string[i:stop],i,stop)
        if sub_string==string[i:stop]:
            count+=1
        stop+=1    #stop value for y i.e.:[0:2],[1:3].[2:4],....
    return count

if __name__ == '__main__':
    string = 'pratik' #input().strip()
#    print(type(string))
    sub_string = 'at' #input().strip()
#    print(type(sub_string))
    
    count = count_substring(string, sub_string)
    print('count:',count)