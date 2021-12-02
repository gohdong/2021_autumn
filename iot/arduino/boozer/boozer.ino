void setup() {
  // put your setup code here, to run once:
  Serial.begin(9600);
  pinMode(8,INPUT);

}

void loop() {
  // put your main code here, to run repeatedly:
  int switch2 = digitalRead(8);
  Serial.println(switch2);
  if(switch2 == 0){
    tone(11,500,10);  
  }
}
