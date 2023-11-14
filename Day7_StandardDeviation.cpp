#include<iostream>
#include<cmath>
using namespace std;
int main(){
    int n;
    cout<<"Enter number of values:";
    cin>>n;
    int values[n];
    cout<<"Enter values:";
    for(int i=0; i<n; i++){
        cin>>values[i];
    }
    int sum=0;
    for(int i=0; i<n; i++){
        sum+=values[i];
    }
    float mean=sum/n;
    cout<<mean<<endl;
    int diff[n];
    for(int i=0; i<n; i++){
        diff[i]=pow((values[i]-mean),2);
    }
    float sum_diff=0;
    for(int i=0; i<n; i++){
        sum_diff+=diff[i];
    }
    float variance=sum_diff/(n-1);
    cout<<"Variance is:"<<variance<<endl;
    float sd=pow(variance,0.5);
    cout<<"Standard Deviation is:"<<sd<<endl;
}
