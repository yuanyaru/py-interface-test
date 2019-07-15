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
        YCArea::DxPropertyYC RPCGetYCProperty (int station);
        int RPCSetYCProperty (YCArea::DxPropertyYC YCProperty, int station);
        YCArea::DxDTYCSeq RPCGetRealtimeYCData (DemoArea::LongSeq pIDs);
        YCArea::DxDTYCSeq RPCGetDayYCData (string datetime, DemoArea::LongSeq pIDs);
        YCArea::DxDTYCSeq RPCGetPeriodYCData(string datetime0, string datetime1, DemoArea::LongSeq pIDs);
        int RPCSaveYCData (DemoArea::LongSeq pIDs, YCArea::DxDTYCSeq data);
        int RPCSetRealtimeYCData (DemoArea::LongSeq pIDs, YCArea::DxDTYCSeq data);

        YXArea::DxPropertyYX RPCGetYXProperty (int station);
        int RPCSetYXProperty (YXArea::DxPropertyYX YXProperty, int station);
        YXArea::DxDTYXSeq RPCGetRealtimeYXData (DemoArea::LongSeq pIDs);
        YXArea::DxDTYXSeq RPCGetDayYXData (string datetime,DemoArea::LongSeq pIDs);
        YXArea::DxDTYXSeq RPCGetPeriodYXData(string datetime0,string datetime1, DemoArea::LongSeq pIDs);
        int RPCSaveYXData (DemoArea::LongSeq pIDs, YXArea::DxDTYXSeq data);

        StationArea::DxPropertyStation RPCGetStationProperty ();
        int RPCSetStationProperty (StationArea::DxPropertyStation StationProperty);

        SystemArea::DxPropertySystem RPCGetSystemProperty ();
        int RPCSetSystemProperty (SystemArea::DxPropertySystem SystemProperty);

    };
};
