#include <Ice/Ice.h>
#include <ice-redis.h>
 
using namespace std;
using namespace YCArea;
using namespace CommandArea;
int main(int argc, char* argv[])
{
    int status = 0;
    Ice::CommunicatorPtr ic;

    YCArea::DxPropertyYC structyc;
    for(int i=0;i<41;i++) structyc.name.push_back(i+10);
    for(int i=0;i<11;i++) structyc.unit.push_back(i);
    structyc.k=1.1;
    structyc.b=1.2;
    structyc.precision=2;
    structyc.fullvalue=2.1;
    structyc.mindelta=2.2;
    structyc.zerovalue=2.3;
    structyc.flog=30;
    structyc.fplan=31;
    structyc.fcache=32;
    structyc.fTrans=1;
    structyc.fMin=1;
    structyc.fMax=1;
    structyc.fAvrg=1;
    structyc.fRatio=1;
    structyc.fUpper=1;
    structyc.fLower=1;
    structyc.fUpper2=1;
    structyc.fLower2=1;
    structyc.fMinTime=1;
    structyc.fMaxTime=1;
    structyc.padding=40;
    structyc.fMax2=1;
    structyc.fMaxTime2=1;
    structyc.yxno=50;
    structyc.alevel=51;
    structyc.uppervalue=6.1;
    structyc.lowervalue=6.2;
    structyc.uppervalue2=6.3;
    structyc.lowervalue2=6.4;

    try
    {
        ic = Ice::initialize(argc, argv);
        Ice::ObjectPrx base = ic->stringToProxy("DataCommand:default -p 10000");
        DataCommandPrx DataCommand = DataCommandPrx::checkedCast(base);
        if (!DataCommand)
        {
            throw "Invalid proxy";
        }

        YCArea::DxPropertyYC result;
        int station=1;
        DataCommand->RPCSetYCProperty(structyc,station);
        result=DataCommand->RPCGetYCProperty(station);
         printf("name40:%d\n",result.name[40]);
        cout << "name0: " << result.name[0] << endl;
        cout << "unit1: " << result.unit[0] << endl;
        cout << "k: " << result.k << endl;
        cout << "precision: " << result.precision << endl;
        cout << "fullvalue: " << result.fullvalue << endl;
        cout << "flog: " << result.flog << endl;
        cout << "fTrans: " << result.fTrans << endl;
        cout << "padding: " << result.padding << endl;
        cout << "fMax2: " << result.fMax2 << endl;
        cout << "yxno: " << result.yxno << endl;
        cout << "uppervalue: " << result.uppervalue << endl;
        cout << "lowervalue: " << result.lowervalue << endl;
        cout << "lowervalue2: " << result.lowervalue2 << endl;
        cout << "lowervalue2: " << result.lowervalue2 << endl;
        cout << "lowervalue2: " << result.lowervalue2 << endl;
        cout << "lowervalue2: " << result.lowervalue2 << endl;

        cout << "lowervalue2: " << result.lowervalue2 << endl;
        //keycommand->keyset("name","hj");
        //result = keycommand->keyget("name");
        //test=result.name.at(0);
        //printf("client's result.name1:%d\n",result.name.at(0));
        //cout<<result.name.at(0)<<endl;
        //cout << "client's result.name1: " << result.name.size() << endl;
    }
    catch (const Ice::Exception& ex)
    {
        cerr << ex << endl;
        status = 1;
    }
    catch (const char* msg)
    {
        cerr << msg << endl;
        status = 1;
    }
 
    if (ic)
    {
        ic->destroy();
    }
 
    return status;
}
