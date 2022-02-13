'''
1.输出结果：
    1
   121
  12321
 1234321
123454321
'''
#法1：
for a in range(1,6):
    print(" "*(5-a),end="")
    s=[i for i in range(a,0,-1)]
    i=len(s)-1
    m=len(s)-1
    n=1
    while i>=0:
        print(s[i],end="")
        i=i-1
    else:
        while n<=m:
            print(s[n],end="")
            n=n+1
    print()
#法2：
for a in range(1,6):
    print(" "*(5-a),end="")
    s=[i for i in range(a,0,-1)]
    for m in range(len(s)-1,-1,-1):
        print(s[m],end="")
    for n in range(1,len(s)):
        print(s[n],end="")
    print()
#法3：
for a in range(1,6):
    print(" "*(5-a),end="")
    for m in range(1,a+1):
        print(m,end="")
    for n in range(a-1,0,-1):
        print(n,end="")
    print()
#法4：
for a in range(1,6):
    print(" "*(5-a),end="")
    for m in list(range(1,a+1))+list(range(a-1,0,-1)):
        print(m,end="")
    print()

'''
2.输出结果：
            *
           * *
          * * *
         * * * *
        * * * * *
       * * * * * *
            *
           * *
          * * *
         * * * *
        * * * * *
       * * * * * *
      * * * * * * *
     * * * * * * * *
            *
           * *
          * * *
         * * * *
        * * * * *
       * * * * * *
      * * * * * * *
     * * * * * * * *
    * * * * * * * * *
   * * * * * * * * * *
  * * * * * * * * * * *
 * * * * * * * * * * * *
           * *
           * *
           * *
           * *
           * *

'''
def fuck(n): #树
    for i in range(1,n+1):
        for j in range(13-i):
            print(" ",end="")
        for k in range(1,2*i):
            print(" " if k%2==0 else "*",end="")
        print()

for i in [6,8,12]:
    fuck(i)
for i in range(5):
    print(" "*11+"* *")


'''
3.输出结果：
        *
       * *
      * * *
     * * * *
    * * * * *
   * * * * * *
  * * * * * * *
 * * * * * * * *
* * * * * * * * *
 * * * * * * * *
  * * * * * * *
   * * * * * *
    * * * * *
     * * * *
      * * *
       * *
        *
'''
for i in range(1,10):
    for j in range(9-i):
        print(" ",end="")
    for k in range(1,2*i):
        print(" " if k%2==0 else "*",end="")
    print()
for i in range(1,9):
    for j in range(i):
        print(" ",end="")
    for k in range(1,2*(9-i)):
        print(" " if k%2==0 else "*",end="")
    print()
    
'''
4.输出结果
        *
       * *
      * * *
     * * * *
    * * * * *
   * * * * * *
  * * * * * * *
 * * * * * * * *
* * * * * * * * *
'''
for i in range(1,10):
    for j in range(9-i):
        print(" ",end="")
    for k in range(1,2*i):
        print(" " if k%2==0 else "*",end="")
    print()

'''
5.输出结果
         *                 *
        * *               * *
       * * *             * * *
      * * * *           * * * *
     * * * * *         * * * * *
    * * * * * *       * * * * * *
   * * * * * * *     * * * * * * *
  * * * * * * * *   * * * * * * * *
 * * * * * * * * * * * * * * * * * *
'''
for i in range(1,10):
    for j in range(10-i):
        print(" ",end="")
    for k in range(1,2*i):
        print(" " if k%2==0 else "*",end="")
    for a in range(1,2*(10-i)):
        print(" ",end="")
    for b in range(1,2*i):
        print(" " if b%2==0 else "*",end="")
    print()

'''
6.输出结果：
*********
 ********
  *******
   ******
    *****
     ****
      ***
       **
        *
'''
for i in range(9):
    for j in range(i):
        print(" ",end="")
    for k in range(9-i):
        print("*",end="")
    print()

'''
7.输出结果：
    *
   ###
  *****
 #######
*********
'''
for i in range(5):
    for j in range(4-i):
        print(" ",end="")
    for k in range(2*i+1):
        print("*" if i%2==0 else "#",end="")
    print()
 
'''
8.输出结果：
1 2 3 4 5 
2 3 4 5 1 
3 4 5 1 2 
4 5 1 2 3 
5 1 2 3 4 
'''
List=[[1,2,3,4,5],[2,3,4,5,1],[3,4,5,1,2],[4,5,1,2,3],[5,1,2,3,4]]
for i in List:
    for j in i:
        print(j,end=" ")
    print()
