var Faker = require('faker');
_ = require('underscore');
var db = require('riak-js').getClient();
db.saveBucket('contacts', {search: true})

function insertPerson() {
    var person = {};
    person['first-name'] = Faker.Name.firstName();
    person['last-name'] = Faker.Name.lastName();
    person['title'] = Faker.random.bs_noun();
    person['company'] = Faker.Company.companyName();
    person['phone-work'] = Faker.PhoneNumber.phoneNumber();
    person['phone-home'] = Faker.PhoneNumber.phoneNumber();
    person['phone-mobile'] = Faker.PhoneNumber.phoneNumber();
    person['city'] = Faker.Address.city();
    person['state'] = Faker.Address.usState();
    person['email'] = Faker.Internet.email();
    db.save('contacts', '', person, {contentType: 'application/json'});
}


_.times(100, insertPerson) 
