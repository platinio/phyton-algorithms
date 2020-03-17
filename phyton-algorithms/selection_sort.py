
def selection_sort(a):
    for n in range ( len(a) - 1 ):
        minIndex = n ;
        for j in range( n + 1 , len( a ) ):
            if( a[minIndex] > a[j] ):
                minIndex = j;
        if(minIndex != n):
            swap(a , minIndex , n);
    return a;

def swap( array , indexA , indexB ):
    tmp = array[indexA];
    array[indexA] = array[indexB];
    array[indexA] = tmp;

a = list(map(int, input().split()))
a = selection_sort( a );

for n in range( len(a) ):
    print(a[n]);

