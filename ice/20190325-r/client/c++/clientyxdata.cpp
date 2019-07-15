#include <Ice/Ice.h>
#include <ice-redis.h>
 
using namespace std;
using namespace YCArea;
using namespace CommandArea;
int main(int argc, char* argv[])
{
    int status = 0;
    Ice::CommunicatorPtr ic;

    try
    {
        ic = Ice::initialize(argc, argv);
        Ice::ObjectPrx base = ic->stringToProxy("DataCommand:default -h 192.168.100.24 -p 10000");
        DataCommandPrx DataCommand = DataCommandPrx::checkedCast(base);
        if (!DataCommand)
        {
            throw "Invalid proxy";
        }
        DemoArea::LongSeq pIDs;
        YXArea::DxDTYXSeq data;
        long key[2];
        for(int i=0;i<2;i++)
        {
          pIDs.push_back(i);
          YXArea::DxDTYX structyxdata;
          structyxdata.status=i;
          structyxdata.value=i+1.1;
          structyxdata.timetag=i;
          data.push_back(structyxdata);
        }
        
        DataCommand->RPCSaveYXData (pIDs,data);
        YXArea::DxDTYXSeq data1=DataCommand->RPCGetRealtimeYXData (pIDs);
        for(int i=0;i<2;i++)
       {
         YXArea::DxDTYX structyxdata1=data1[i];
         cout << "status: " << structyxdata1.status << endl;
         cout << "value: " << structyxdata1.value << endl;
         cout << "timetag: " << structyxdata1.timetag << endl;
       }

        //DataCommand->RPCSetYCProperty(structyc,station);
        //result=DataCommand->RPCGetYCProperty(station);
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
