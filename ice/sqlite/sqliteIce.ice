module ByteArea {
    sequence<int> IntSeq;
};

module StructArea{
	struct  DxDTYCValue
	{
		byte status;
		float value;
		string timetag;
	};

	struct  DxDTYXValue
	{
		byte status;
		byte value;
		string timetag;
	};
	struct DxDTYX
	{
		int ID;
		string name;
		string describe;
		int ASDU;
		int wordPos;
		int bitPos;
		int bitLength;
		string address;
	};
	struct DxDTYC
	{
		int ID;
		string name;
		string describe;
		string unit;
		float kval;
		float bval;
		string address;
		float uplimt;
		float downlimt;
	};
	struct DxDTYK
	{
		int ID;
		string name;
		string describe;
		int ASDU;
		int wordPos;
		int bitPos;
		int bitLength;
		string address;
	};
	struct DxDTYT
	{
		int ID;
		string name;
		string describe;
		string unit;
		float kval;
		float bval;
		string address;
		float uplimt;
		float downlimt;
	};
	struct DxDTSOE {
		int num;
		int level;
		string time;
		string StationName;
		string SOEName;
		int pointID;
		string status;
		string Operater;
		string SOEOper;
	};
	struct DxDTLINK {
		int ID;
		string name;
		string describe;
		int ruleID;
		string address;
		int PORT;
		int role;
	};
	sequence<DxDTYX> DxDTYXSeq;
	sequence<DxDTYC> DxDTYCSeq;	
	sequence<DxDTYK> DxDTYKSeq;
	sequence<DxDTYT> DxDTYTSeq;
	sequence<string> stringSeq;
	sequence<stringSeq> quxianSeq;
	sequence<DxDTYXValue> DxDTYXValueSeq;
	sequence<DxDTYCValue> DxDTYCValueSeq;
	sequence<DxDTSOE> DxDTSOESeq;
	sequence<DxDTLINK> DxDTLINKSeq;
	sequence<DxDTYCValueSeq> DxAnalogSeq;
};

module SqliteICE {
   interface DataOperate {
		int SOETodaySelect (string time, out StructArea::DxDTSOESeq data);
		int SOERangeSelect (string starttime, string endtime, out StructArea::DxDTSOESeq data);
		int SOEPointSelect (string pointID,string stationname, string starttime, string endtime, out StructArea::DxDTSOESeq data);
		int LinkInfo (out StructArea::DxDTLINKSeq data);
		int YXInfo (string station, out StructArea::DxDTYXSeq data);
		int YCInfo (string station, out StructArea::DxDTYCSeq data);
		int YKInfo (string station, out StructArea::DxDTYKSeq data);
		int YTInfo (string station, out StructArea::DxDTYTSeq data);
		int YCRealtimeValue (string station, out StructArea::DxDTYCValueSeq data);
		int YXRealtimeValue (string station, out StructArea::DxDTYXValueSeq data);
		int YKYTOperation (string station, string type, string point, float value);
		int tableSelectOneday (ByteArea::IntSeq pIDs,string time, out StructArea::DxAnalogSeq data, out StructArea::DxDTYCValueSeq max, out StructArea::DxDTYCValueSeq min,out StructArea::DxDTYCValueSeq average);
		int tableSelectOnemouth (ByteArea::IntSeq pIDs,out StructArea::DxAnalogSeq data, out StructArea::DxDTYCValueSeq max, out StructArea::DxDTYCValueSeq min,out StructArea::DxDTYCValueSeq average);
		int quxianSelect (ByteArea::IntSeq pIDs,string starttime, string endtime,out StructArea::quxianSeq data);
		int SOERealtime (out StructArea::DxDTSOESeq data);
    };
};
