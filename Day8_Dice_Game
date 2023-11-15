#include <iostream>
#include <cstdlib>  // Required for rand() and srand()
#include <ctime>    // Required for time()
using namespace std;
int generateRandomValue(int min, int max) {
    // Seed the random number generator with the current time
    srand(static_cast<unsigned int>(time(0)));

    // Generate a random value in the range [min, max]
    int randomValue = min + rand() % (max - min + 1);

    return randomValue;
}

int main() {
    // Example: Generate a random value between 1 and 6 (inclusive)
    int minValue = 1;
    int maxValue = 6;
    int points=0;
    bool continue_rolling=true;

    while(continue_rolling){
        int randomResult = generateRandomValue(minValue, maxValue);

        cout << "Value on dice: " << randomResult << endl;

        if(randomResult==1){
            cout<<"You rolled a one! That's not good. You lose your turn."<<endl;
            cout<<"\n"<<"Points till now: "<<points;
            continue_rolling=false;
        }
        else{
            points=points+randomResult;
            cout<<"Points so far: "<<points<<endl;
            char choice;
            cout<<"Do u want to Roll Again?(y/n):"<<endl;
            cin>>choice;
            if(choice=='n' || choice=='N'){
                cout<<"You chose to end the game."<<endl;
                continue_rolling=false;
            }

        }
    }
    
}
