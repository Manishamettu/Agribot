//Left Motor connected to 4,5 digitalPins
//Right Motor connected to 10,9 digitalPins #include<Servo.h>
Servo s1;

int LMP = 8; int LMN = 9; int RMP = 6; int RMN = 7; int weed = 13; void setup() {
//Motor Pins are OUTPUT pinMode(LMP, OUTPUT); pinMode(LMN, OUTPUT); pinMode(RMP, OUTPUT); pinMode(RMN, OUTPUT); pinMode(weed,OUTPUT); s1.attach(11); Serial.begin(9600);
}

void loop() {

if (Serial.available())

{

String Direction = Serial.readString();
 

 

if (Direction == "F")

{

//Move Forward digitalWrite(LMP, HIGH); digitalWrite(LMN, LOW); digitalWrite(RMP, LOW); digitalWrite(RMN, HIGH);
}

else if (Direction == "B")

{

//Move backward digitalWrite(LMP, LOW); digitalWrite(LMN, HIGH); digitalWrite(RMP, HIGH); digitalWrite(RMN, LOW);
} else if (Direction == "L")

{

//Right Turn digitalWrite(LMP, LOW);
digitalWrite(LMN, HIGH);

digitalWrite(RMP, LOW); digitalWrite(RMN, HIGH);
}

else if (Direction == "R")
 

 

{

//Left Turn digitalWrite(LMP, HIGH); digitalWrite(LMN, LOW); digitalWrite(RMP, HIGH); digitalWrite(RMN, LOW);
}

else if (Direction == "S")

{

//Stop

digitalWrite(LMP, LOW); digitalWrite(LMN, LOW); digitalWrite(RMP, LOW); digitalWrite(RMN, LOW);
}

else if (Direction == "1")

{

digitalWrite(weed,HIGH); delay(1000);
}

else if (Direction == "0")

{

digitalWrite(weed,LOW); delay(1000);
 

 

}

else if (Direction == "seed")

{

// put your main code here, to run repeatedly: s1.write(45);
delay(1000); s1.write(90);
}

}

}
