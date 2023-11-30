#include <VarSpeedServo.h> 
VarSpeedServo servo_1;
VarSpeedServo servo_2;
VarSpeedServo servo_3;
VarSpeedServo servo_4;
VarSpeedServo num_ser[4] = {servo_1,servo_2,servo_3,servo_4};
int prev[4]= {90,90,90,90};
int angl[4]={90,90,90,90};

void rotate(int current_angle,int prev_angle,int i){
  if(current_angle>prev_angle){
    for(int q=prev_angle;q<=current_angle;q++){
      num_ser[i].write(q,30,false);
      delay(10);
  }
  }
  else{
    for(int p=prev_angle;p>=current_angle;p--){
      num_ser[i].write(p,30,false);
      delay(10);
  }
  }
}
void setup() {

  Serial.begin(9600);

  num_ser[0].attach(3);
  num_ser[1].attach(5);
  num_ser[2].attach(6);
  num_ser[3].attach(9);
  for(int i=0;i<4;i++){
    rotate(angl[i],prev[i],i);
    prev[i]=angl[i];
  }
}
char data[20];

void loop() {

  if (Serial.available() > 0){

  String data = Serial.readStringUntil('\n');

    // Parse the data using strtok function
  char *ptr = strtok(const_cast<char *>(data.c_str()), ",");
  // Assuming you have 3 servos
  

    // Loop through the tokens and convert them to integers
  for (int i = 0; i < 4 && ptr != NULL; i++) {
    angl[i] = atoi(ptr);
    ptr = strtok(NULL,",");
  }
  for (int j=0;j<4;j++){
    rotate(angl[j],prev[j],j);
    prev[j]=angl[j];
  }
  
  

  }
  
  


  
 
  // if(angles[0]<prev[0]){
  // for(int i=prev[0];i<angles[0];i--){
  //   servo.write(i);
  // }
  // prev[0] = angles[0];
  // }
  

  

 
   

  

}


