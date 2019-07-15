module kafkaICE {
   interface DataOperate {
    int KafkaProduceData (string topic, string log, string config,string msg,string key);
	int KafkaLongConnectData (string topic,string msg,string key);
	int KafkaLongConnectUninit(string topic);
    };
};
