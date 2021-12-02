void setup() {
  // put your setup code here, to run once:
  Serial.begin(9600);
  pinMode(4,OUTPUT);

}

void loop() {
  // put your main code here, to run repeatedly:
  int sensor = analogRead(1);
  Serial.println(sensor);
  tone(11,500,1000);

  if(sensor > 150){
    digitalWrite(4,HIGH);
  }
  else{
    digitalWrite(4,LOW);
  }
  delay(2000);

}
