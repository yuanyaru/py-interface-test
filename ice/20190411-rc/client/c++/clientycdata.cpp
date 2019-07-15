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
        Ice::ObjectPrx base = ic->stringToProxy("DataCommand:default -p 10000");
        DataCommandPrx DataCommand = DataCommandPrx::checkedCast(base);
        if (!DataCommand)
        {
            throw "Invalid proxy";
        }
        DemoArea::LongSeq pIDs;
        YCArea::DxDTYCSeq data;
        long key[2];
        for(int i=0;i<2;i++)
        {
          pIDs.push_back(i);
          YCArea::DxDTYC structyxdata;
          structyxdata.status=i;
          structyxdata.value=i+2.1;
          structyxdata.timetag=i;
          data.push_back(structyxdata);
        }
        long pID=1;
        string datatime1="20190408000000";
        string datatime2="20190410180000";
        //DataCommand->RPCSaveYCData (pIDs,data);
        //DataCommand->RPCSetRealtimeYCData (pIDs,data);        
        //YCArea::DxDTYCSeq data1=DataCommand->RPCGetRealtimeYCData (pIDs);
        YCArea::DxDTYCSeq data1=DataCommand->RPCGetPeriodYCData (datatime1,datatime2,pID);

        //YCArea::DxDTYCSeq data1=DataCommand->RPCGetDayYCData (datatime1,pID);
        int size_data=data1.size();
        for(int i=0;i<size_data;i++)
       {
         YCArea::DxDTYC structyxdata1=data1[i];
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
