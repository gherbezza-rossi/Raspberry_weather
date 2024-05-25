#define BLINDS 13
#define SOIL1 12
#define SOIL2 11
#define WINDOW 10

String topic;
String payload;
//String mess;

  void setup() {
  // put your setup code here, to run once:
  pinMode(LED, OUTPUT);
  Serial.begin(9600);
  topic = "";
  payload = "";
  //mess = "";
  
}

void loop() {
  
  // put your main code here, to
  if (Serial.available() > 0) {
    String data = Serial.readStringUntil('\n');
    Serial.print("You sent me: ");
    
    substring(data);
    Serial.println(topic);

    if(topic != ""){
      if(topic == "BLINDS" and payload=="ON"){
        digitalWrite(BLINDS, HIGH);
        delay(500);
      }
      else if(topic == "LIGHT" and payload=="OFF"){
        digitalWrite(BLINDS, LOW);
        delay(500);
      }
      else if(topic == "SOIL1" and payload=="ON"){
        digitalWrite(SOIL1, HIGH);
        delay(500);
      }
      else if(topic == "SOIL1" and payload=="OFF"){
        digitalWrite(SOIL1, LOW);
        delay(500);
      }
      else if(topic == "SOIL2" and payload=="ON"){
        digitalWrite(SOIL2, HIGH);
        delay(500);
      }
      else if(topic == "SOIL2" and payload=="OFF"){
        digitalWrite(SOIL2, LOW);
        delay(500);
      }
    }
  }
}

void substring(String mess){
  int index = mess.indexOf(':');
    if (index != -1) {
      topic = mess.substring(0, index);
      payload = mess.substring(index+1);
    }
}
