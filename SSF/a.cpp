#include <iostream>
#include <vector>
#include <map>
#include <stack>
#include <queue>
#include <deque>
#include <algorithm>
#include <set>
#include <cmath>
#include <cstring>
#include <iterator>
#include <string>
#include <bits/stdc++.h>
#define T int Tests; cin>> Tests; while(Tests--)
#define F16  ios_base::sync_with_stdio(false);cin.tie(NULL);cout.tie(NULL);
#define ld long double
using namespace std;
const int N= 1e9;
int main(int argc, char const *argv[])
{
    F16
    long long basic_deposit, monthly_deposit,target; 
    cin>>basic_deposit>>monthly_deposit>>target;
    int ROI_per_year = 10;// This a Profit...     -- this is particular to each protfolio
    int the_target_without_moreYears = ((basic_deposit*ROI_per_year)/100)/12;
    if(the_target_without_moreYears >=target){
        cout<<0<<" years need for get to that target."<<endl;
    }else{
        int months = 0;
        while(((basic_deposit*ROI_per_year)/100)/12 <target){
            months++;
            basic_deposit+=monthly_deposit;
            if(months%12==0){
                basic_deposit+=(basic_deposit*ROI_per_year)/100;
            }
        }

        cout<<basic_deposit<<" your captil."<<endl;
        cout<<(months/12)<<" years "<<months%12 << " months"<<"  need for get to that target."<<endl;
        /* cout<<(months/12.0)<<" years need for get to that target."<<endl; */
    }
    // Description 👇
    /*
        now first the uesr give us the basic_deposit, monthly_deposit and target.
        then for each protfolio has the ROI_per_year and we will calculate the years need for
        that protfolio
    */
    return 0;
}
