#include<bits/stdc++.h>
using namespace std;

int NWC(vector<int> s,vector<int> d,vector<vector<int>> v,int r,int c) {
    int i=0,j=0;
    int cc=0;
    while(i<r) {
        if(s[i]<d[j]) {
            cc+=v[i][j]*s[i];
            d[j]-=s[i];
            i+=1;
        }
        else if(s[i]>d[j]) {
            cc+=v[i][j]*d[j];
            s[i]-=d[j];
            j+=1;
        }
        else {
            cc+=v[i][j]*d[j];
            s[i]-=d[j];
            i+=1;
            j+=1;
        }
    }
    return cc;
}

int LCM(vector<int> s,vector<int> d,vector<vector<int>> v,int r,int c,vector<int> vr,vector<int> vc) {
    int cc=0,ir,jc;
    while(1) {
        int mn=INT_MAX;
        for(int i=0;i<r;i++) {
            for(int j=0;j<c;j++) {
                if(vr[i]==0 && vc[j]==0) {
                    if(mn>v[i][j]) {
                        ir=i;
                        jc=j;
                        mn=v[i][j];
                    }
                }
            }
        }
        if(s[ir]<d[jc]) {
            cc+=v[ir][jc]*s[ir];
            d[jc]-=s[ir];
            vr[ir]+=1;
        }
        else if(s[ir]>d[jc]) {
            cc+=v[ir][jc]*d[jc];
            s[ir]-=d[jc];
            vc[jc]+=1;
        }
        else {
            cc+=v[ir][jc]*s[ir];
            d[jc]-=s[ir];
            vr[ir]+=1;
            vc[jc]+=1;
        }
        int f1=0,f2=0;
        for(int i=0;i<r;i++)
            if(vr[i]==0)
                f1=1;
        for(int i=0;i<c;i++)
            if(vc[i]==0)
                f2=1;
        if(f1==0 && f2==0)
            break;
    }
    return cc;
}

int main() {
    vector<int> supply(100),demand(100);
    vector<int> vrow(100),vcol(100);
    vector<vector<int>> v(100,vector<int>(100));
    int r,c;
    cout<<"r : ";
    cin>>r;
    cout<<"c : ";
    cin>>c;
    cout<<"data : \n";
    for(int i=0;i<r;i++)
        for(int j=0;j<c;j++)
            cin>>v[i][j];
    cout<<"supply : ";
    for(int i=0;i<r;i++)
        cin>>supply[i];
    cout<<"demand : ";
    for(int i=0;i<c;i++)
        cin>>demand[i];
    cout<<"cost by NWC : "<<NWC(supply,demand,v,r,c)<<"\n";
    cout<<"cost by LCM : "<<LCM(supply,demand,v,r,c,vrow,vcol)<<"\n";
    
    return 0;
}