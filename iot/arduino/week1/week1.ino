int led[] = {4};

void setup() {
  // put your setup code here, to run once:
//  for(int i=0;i<1;i++){
//    pinMode(led[i],OUTPUT);
//  }
  pinMode(8,INPUT);
}

void loop() {
  // put your main code here, to run repeatedly:
  int v = digitalRead(8);
  Serial.println(v);
  if (v == HIGH){
    digitalWrite(4, LOW);
  }
  else{
    digitalWrite(4, HIGH);
  }
//  int rand = random(0,3);
//  
//  digitalWrite(led[rand], LOW);

}
