function transform(line) {
    var values = line.split(',');
    var obj = new Object();
    obj.PassengerId = values[0];
    obj.Survived = values[1];
    obj.Pclass = values[2];
    obj.Name = values[3];
    obj.Sex = values[4];
    obj.Age = values[5];
    obj.SibSp = values[6];
    obj.Parch = values[7];
    obj.Ticket = values[8];
    obj.Fare = values[9];
    var jsonString = JSON.stringify(obj);
    return jsonString;
   }
   
   
   
   
   
   
   
   
   
   
 

