/** 1) connect DB */
const mongoose = require('mongoose');

mongoose.connect(process.env.MONGO_URL, {
    useNewUrlParser: true,
    useUnifiedTopology: true,
    useCreateIndex: true,
    useFindAndModify: false,
    dbName: process.env.MONGO_DB || '',
    user: process.env.MONGO_USER || '',
    pass: process.env.MONGO_PASSWORD || '',
});

/** 2) Create a 'Person' Model */
// Schema
var personSchema = new mongoose.Schema({
  name: String,
  age: Number,
  favoriteFoods: [String]
});

/** 3) Create and Save a Person */
// Model
var Person = mongoose.model('Person', personSchema);

var createAndSavePerson = function(done){
  let someone = new Person({name:"someone", age:10, favoriteFoods:["fish","egg","god"]});

  someone.save((err,data)=>{
    if(err) return console.error(err);
    done(null, data);
  })
}

var arrayOfPeople = [{name:"someone", age:10, favoriteFoods:["fish","egg","god"]},
{name:"someone", age:10, favoriteFoods:["fish","egg","god"]},
{name:"someone", age:10, favoriteFoods:["fish","egg","god"]}];

const createManyPeople = (arrayOfPeople, done) => {
  Person.create(arrayOfPeople, (err, data) =>{
    if(err) return console.error(err);
    done(null, data);
  })
};

const findPeopleByName = (personName, done) => {
  Person.find({name:personName}, (err, data) =>{
    if(err) return console.error(err);
    done(null, data);
  })
};

const findOneByFood = (food, done) => {
  Person.findOne({favoriteFoods:food}, (err, data) =>{
    if(err) return console.error(err);
    done(null, data);
  })
};

const findPersonById = (personId, done) => {
  Person.findById({_id:personId}, (err, data)=>{
    if (err) return console.error(err);
    done(null, data);
    })
};

const findEditThenSave = (personId, done) => {
  const foodToAdd = "hamburger";
  Person.findById(personId, (err, data)=>{
    data.favoriteFoods.push(foodToAdd);
    data.save((err, updatedData)=>{
      if(err) console.error(err);
      done(null, updatedData);
    })
  })
};

const findAndUpdate = (personName, done) => {
  const ageToSet = 20;

  Person.findOneAndUpdate({name:personName}, {age:ageToSet},{new:true}, (err,update)=>{
    if(err) console.error(err);
    done(null, update);
  })
};

const removeById = (personId, done) => {
  Person.findByIdAndRemove(personId, (err, removed) => {
    if(err) console.error(err);
    done(null, removed);
  })
};

const removeManyPeople = (done) => {
  const nameToRemove = "Mary";

  Person.remove({name:nameToRemove}, (err, removed)=>{
    if(err) console.error(err);
    done(null, removed);
  })
};

const queryChain = (done) => {
  const foodToSearch = "burrito";

  Person.find({favoriteFoods:foodToSearch}).sort({name:1}).limit(2).select({age:0}).exec((err,data)=>{
    if(err) console.error(err);
    done(null, data);
  })

};

/** **Well Done !!**
/* You completed these challenges, let's go celebrate !
 */

//----- **DO NOT EDIT BELOW THIS LINE** ----------------------------------

exports.PersonModel = Person;
exports.createAndSavePerson = createAndSavePerson;
exports.findPeopleByName = findPeopleByName;
exports.findOneByFood = findOneByFood;
exports.findPersonById = findPersonById;
exports.findEditThenSave = findEditThenSave;
exports.findAndUpdate = findAndUpdate;
exports.createManyPeople = createManyPeople;
exports.removeById = removeById;
exports.removeManyPeople = removeManyPeople;
exports.queryChain = queryChain;
