#include<iostream>
#include <cstdlib>
using namespace std;
int main()
{
    int T;
    cin>>T;
    while(T--)
    {
        int n;
        cin>>n;
        int *arr=new int[n];
        for(int i=0;i<n;i++)
        {
            cin>>arr[i];
        }
        int sum=0;
        int i=0,j=0,k=0;
        for(;i<n;i++)
        {
            if(i!=j)
                for(;j<n;j++)
                {
                    if(j!=k)
                        for(;k<n;k++)
                        {
                            int ans=std::abs(arr[i]-arr[j])+std::abs(arr[j]-arr[k])+std::abs(arr[k]-arr[i]);
                            sum=max(ans,sum);
                        }
                }
        }
        cout<<sum<<endl;
        delete []arr;
    }
}
