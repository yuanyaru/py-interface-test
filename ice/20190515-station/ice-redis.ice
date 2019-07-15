module DemoArea {
    sequence<byte> ByteSeq;
    sequence<long> LongSeq;
};

module YCArea {
    struct DxPropertyYC {
        DemoArea::ByteSeq name;
        DemoArea::ByteSeq unit;
        float k;
        float b;
        short precision;
        float fullvalue;
        float mindelta;
        float zerovalue;
        short flog;
        short fplan;
        short fcache;
        bool fTrans;
        bool fMin;
        bool fMax;
        bool fAvrg;
        bool fRatio;
        bool fUpper;
        bool fLower;
        bool fUpper2;
        bool fLower2;
        bool fMinTime;
        bool fMaxTime;
        short padding;
        bool fMax2;
        bool fMaxTime2;
        short yxno;
        short alevel;
        float uppervalue;
        float lowervalue;
        float uppervalue2;
        float lowervalue2;
    };

    struct DxDTYC {
        short status;
        float value;
        int timetag;
    };

   sequence<DxDTYC> DxDTYCSeq;
};

module YXArea {
    struct DxPropertyYX {
        DemoArea::ByteSeq name;
        bool fAlarm;
        bool fAlarmCount;
        byte unused;
        int reserved;
        short ykno;
        short alarmtype;
        short alevel;
    };

    struct DxDTYX {
        short status;
        short value;
        int timetag;
    };

   sequence<DxDTYX> DxDTYXSeq;
};

module StationArea {
    struct DxPropertyStation {
        DemoArea::ByteSeq name;
        int nYX;
        int nYC;  
        short type;  
        DemoArea::ByteSeq protocol;  
        DemoArea::ByteSeq addr1;
        DemoArea::ByteSeq addr2;
        short port;
        int slaveAddr;
        DemoArea::ByteSeq devName;
        int baud;
        int dataBits;
        int stopBits;
        byte parity;
        int timeout;  
        int reserved;  

    };

};

module SystemArea {
    struct DxPropertySystem {
        DemoArea::ByteSeq name;
        short nstation;
    };
};

module CommandArea {
   interface DataCommand {
        int RPCGetYCProperty (int station, out YCArea::DxPropertyYC result);
        int RPCSetYCProperty (YCArea::DxPropertyYC YCProperty, int station);
        int RPCGetRealtimeYCData (int station, DemoArea::LongSeq pIDs, out YCArea::DxDTYCSeq result);
        int RPCGetDayYCData (int station, string datetime, long pID, out YCArea::DxDTYCSeq result);
        int RPCGetDayYCDatas (int station, string datetime, DemoArea::LongSeq pIDs, out DemoArea::LongSeq pIDNum, out YCArea::DxDTYCSeq result);
        int RPCGetProcessYCData (int station, string datetime, long pID, out YCArea::DxDTYC max , out YCArea::DxDTYC min, out YCArea::DxDTYC average);
        int RPCGetProcessYCDatas (int station, string datatime, DemoArea::LongSeq pIDs, out YCArea::DxDTYCSeq maxseq , out YCArea::DxDTYCSeq minseq, out YCArea::DxDTYCSeq averageseq);
        int RPCGetPeriodYCData(int station, string datetime0, string datetime1, long pID, out YCArea::DxDTYCSeq result);       
        int RPCGetTimePointYCData (int station, string datetime, DemoArea::LongSeq pIDs, out YCArea::DxDTYCSeq result);
        int RPCSetRealtimeYCData (int station, DemoArea::LongSeq pIDs, YCArea::DxDTYCSeq data);
        int RPCSaveYCData (int station, DemoArea::LongSeq pIDs, YCArea::DxDTYCSeq data);

        int RPCGetYXProperty (int station, out YXArea::DxPropertyYX result);
        int RPCSetYXProperty (YXArea::DxPropertyYX YXProperty, int station);
        int RPCGetRealtimeYXData (int station, DemoArea::LongSeq pIDs, out YXArea::DxDTYXSeq result);
        int RPCGetDayYXData (int station, string datetime, long pID, out YXArea::DxDTYXSeq result);
        int RPCGetDayYXDatas (int station, string datetime, DemoArea::LongSeq pIDs, out DemoArea::LongSeq pIDNum, out YXArea::DxDTYXSeq result);
        int RPCGetPeriodYXData(int station, string datetime0,string datetime1, long pID, out YXArea::DxDTYXSeq result);
        int RPCGetTimePointYXData (int station, string datetime, DemoArea::LongSeq pIDs, out YXArea::DxDTYXSeq result);
        int RPCSaveYXData (int station, DemoArea::LongSeq pIDs, YXArea::DxDTYXSeq data);

        int RPCGetStationProperty (int station, out StationArea::DxPropertyStation result);
        int RPCSetStationProperty (int station, StationArea::DxPropertyStation StationProperty);

        int RPCGetSystemProperty (out SystemArea::DxPropertySystem result);
        int RPCSetSystemProperty (SystemArea::DxPropertySystem SystemProperty);

    };
};
