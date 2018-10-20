minimumScalarProduct(vector <int> &x, vector <int> &y){

    long long r1 = 0;
    long long r2 = 0;
    sort(x.begin(),x.end());
    sort(y.begin(),y.end());

    for (size_t i=0;i<x.size();++i) {
        r1 = r1 + x[i]*y[y.size()-1-i];
    }
    for (size_t i=0;i<x.size();++i) {
        r2 = r2 + y[i]*x[y.size()-1-i];
    }

    return (r1<=r2)?r1:r2;