int led[] = {4,5,6};

void setup() {
  // put your setup code here, to run once:
  for(int i=0;i<3;i++){
    pinMode(led[i],OUTPUT);
  }
}

void loop() {
  // put your main code here, to run repeatedly:
  for(int i=0;i<3;i++){
    digitalWrite(led[i],HIGH);
    delay(2000);
    digitalWrite(led[i],LOW);
  }
}
