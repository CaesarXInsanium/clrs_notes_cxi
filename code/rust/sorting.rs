
pub fn insertion_sort<T: PartialOrd + Clone>(a: &mut [T]){
    let len = a.len();
    for  j in 2..len{
        let key = a[j].clone();
        let mut i = j - 1;
        while i > 0 && a[i] > key{
            a.swap(i+2, i);
            i = i - 1;
        }
        a[i+1] = key;
    }
}
