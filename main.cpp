#include <iostream>
#include <fstream>
#include <vector>
#include <string>
#include <unordered_map>
#include <ctime>
#include <cmath>
#include <cstdlib>

#ifdef _WIN32
#include <Windows.h>
#else
#include <unistd.h>
#endif // _WIN32

using namespace std;

ifstream dictionar("Cuvinte.in");

ifstream feedback("Feedback.txt");
//ofstream feedback_out("Feedback.out");
ofstream out("Entropie.out");
ifstream citeste("Valori.in");

vector <string> words,words_posibil;
unordered_map<char,int> litere[5],prodCart[5];
unordered_map<string,long double>entropieCuvant;
string cuvant;
string guess;
long double entropieGuess;
long double probabilitate;
int counter;


bool isLetterInMap(char litera,int index) //MERGE //verifica daca e in map
{
    return((litere[index].find(litera)!=litere[index].end()));
}

void generareMap(string guess,string posibil)//MERGE //face restrictia
{
    for(int index=0; index<guess.length(); index++)
    {
        if(guess[index]==posibil[index])
            litere[index][guess[index]]=2;
        else
        {
            bool ok=0;
            for(int i=0; i<posibil.length(); i++)
            {
                if(guess[index]==posibil[i])
                {
                    for(int j=0; j<posibil.length(); j++)
                    {
                        if(litere[j][guess[index]]!=2)
                            litere[j][guess[index]]=1;

                    }
                    ok=1;
                    break;

                }

            }
            if(ok==0)
                for(int j=0; j<posibil.length(); j++)
                {
                    litere[j][guess[index]]=0;

                }
        }
    }


}

void resetMaps()
{
    for(int i=0; i<5; i++)
        litere[i].clear();


}

void afisare_map()//MERGE //afiseaza map-urile
{
    cout<<"MAP1\n";
    for(auto i:litere[0])
    {
        cout<<i.first<<" "<<i.second<<'\n';
    }
    cout<<"MAP2\n";
    for(auto i:litere[1])
    {
        cout<<i.first<<" "<<i.second<<'\n';
    }
    cout<<"MAP3\n";
    for(auto i:litere[2])
    {
        cout<<i.first<<" "<<i.second<<'\n';
    }
    cout<<"MAP4\n";
    for(auto i:litere[3])
    {
        cout<<i.first<<" "<<i.second<<'\n';
    }
    cout<<"MAP5\n";
    for(auto i:litere[4])
    {
        cout<<i.first<<" "<<i.second<<'\n';
    }
}

int cazuriGenereazaRestrictia(string cuvant) //MERGE //returneaza daca cuvantul respecta restrictia
{

    int s=0;
    for(int index=0; index<5; index++)
    {

        for(auto i:litere[index])
        {
            if(i.second==2)//2 inseamna ca e pe pozitia aia
            {
                if(i.first!=cuvant[index])
                    return 0;
            }
            else if(i.second==0)
            {
                if(i.first==cuvant[index])
                    return 0;//0 inseamna ca nu este
            }
            else if(i.second==1)//1 inseamna ca este
            {
                if(cuvant.find(i.first)==(string::npos))
                    return 0;
            }
        }


    }
    return 1;

}

bool isMapInMap()
{
    for(int index=0; index<5; index++)
    {
        for(auto i:prodCart[index])
        {
            if(litere[index][i.first]!=i.second)
                return 0;
        }

    }
    return 1;


}

bool verificare(string cuvant,string cuvant2)
{

    for(int index=0; index<5; index++)
    {
        for(auto obj:prodCart[index])
        {
            if(obj.second==2)
            {
                if(cuvant2[index]!=cuvant[index])
                    return 0;
            }
            else if(obj.second==0)
            {
                if(cuvant.find(cuvant2[index])!=string::npos)
                {

                    return 0;
                }
            }
            else if(obj.second==1)
            {
                if(cuvant.find(cuvant2[index])==string::npos||cuvant2[index]==cuvant[index])
                    return 0;
            }
        }
    }
    return 1;

}

void entropieMaxima()
{
    entropieGuess=-1.0;
    for(auto i:entropieCuvant)
    {
        if(i.second>entropieGuess)
        {
            entropieGuess=i.second;
            guess=i.first;

        }
    }




}
void stergeCuvinte()
{
    for(int i=0; i<words_posibil.size(); i++)
    {
        if(!verificare(words_posibil[i],guess))
        {
            words_posibil.erase(words_posibil.begin()+i);
            i--;
        }
    }



}
void citireMap()
{
    feedback.close();
    feedback.open("Feedback.txt");
    for(int i=0; i<5; i++)
    {
        feedback>>prodCart[i][guess[i]];//feedback in mod normal
    }

}




int main()
{
    int x;
    time_t run_time = time(NULL);
    cout<<"Program is (hopefully) running!";
    /*
    ofstream feedback_out("Feedback.out");
    feedback_out<<"";
    feedback_out.close();
    */
    while(dictionar>>cuvant)    //citirea tuturor cuvintelor
    {
        words.push_back(cuvant);
        words_posibil.push_back(cuvant);
    }

    int primaOara=words_posibil.size();

    while(words_posibil.size()>1)
    {

        //cout<<'z';
        if(primaOara!=words_posibil.size())
        {

            for(int i=0; i<words.size(); i++)
            {
                //cout<<words[i]<<'\n';
                entropieCuvant[words[i]]=0;
                for(int a=0; a<3; a++)
                {
                    prodCart[0][words[i][0]]=a;
                    //cout<<'a';

                    for(int b=0; b<3; b++)
                    {
                        prodCart[1][words[i][1]]=b;
                        //cout<<'b';

                        for(int c=0; c<3; c++)
                        {
                            prodCart[2][words[i][2]]=c;
                            //cout<<'c';

                            for(int d=0; d<3; d++)
                            {
                                prodCart[3][words[i][3]]=d;
                                //cout<<'d';

                                for(int e=0; e<3; e++)
                                {
                                    prodCart[4][words[i][4]]=e;
                                    counter=0;
                                    //cout<<'e';
                                    for(int j=0; j<words_posibil.size(); j++)
                                    {
                                        if(verificare(words_posibil[j],words[i]))
                                            counter++;
                                        //cout<<'f';
                                    }
                                    probabilitate = (counter*1.0)/words_posibil.size();

                                    if(probabilitate!=0)
                                    {
                                        entropieCuvant[words[i]]+=probabilitate*log2((words_posibil.size()*1.0)/counter);

                                    }

                                }

                            }

                        }

                    }

                }
                out<<words[i]<<" "<<entropieCuvant[words[i]]<<'\n';

                prodCart[0].clear();
                prodCart[1].clear();
                prodCart[2].clear();
                prodCart[3].clear();
                prodCart[4].clear();

            }
            //cout<<'y';
            entropieMaxima();
        }
        else
        {
            guess="TAREI";
        }
            ofstream data("Guesses.txt");
            //data.open("Guesses.txt");
            data<<guess;
            data.close();
            //cout<<guess<<'\n';
            //cin>>x;//asteapta
            //data.open("Guesses.txt");
            //data<<guess;
            Sleep(3000);
            while(!(feedback>>x))
            {
                Sleep(2100);
                feedback.close();
                feedback.open("Feedback.txt");
            }

            citireMap();
            feedback.close();
            stergeCuvinte();
            /*for(int j=0;j<5;j++)
                cout<<prodCart[j][guess[j]]<<" ";
            cout<<'\n';*/
            //cout<<'m';
            prodCart[0].clear();
            prodCart[1].clear();
            prodCart[2].clear();
            prodCart[3].clear();
            prodCart[4].clear();
            //cout<<'n';
            //data.open("Guesses.txt");
            //feedback_out<<"";
            //feedback_out.close();
            //feedback.close();
            //cout<<'p';
            feedback.open("Feedback.txt");
    }
        Sleep(2000);
        //cout<<words_posibil[0];
        ofstream data("Guesses.txt");
        data<<words_posibil[0];
        data.close();
        Sleep(2000);
        data.open("Guesses.txt");
        data<<"";
        data.close();
        feedback.close();
        run_time = time(NULL) - run_time;
        ofstream runTime("runtime.out");
        runTime<<words_posibil[0]<<" "<<run_time;
        runTime.close();
        return 0;
    }
