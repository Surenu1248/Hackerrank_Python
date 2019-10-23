if __name__ == '__main__':
    x = int(input())
    y = int(input())
    z = int(input())
    n = int(input())

fn=[]
fn1=[]
for i in range(x+1):
    for j in range(y+1):
        for k in range(z+1):
            x=[i,j,k]
            fn.append(x)
for i in fn:
    if sum(i)!=n:
        fn1.append(i)
print(str(fn1))
