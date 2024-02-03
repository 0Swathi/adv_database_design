#Performing $and operator which Returns documents where both queries matches
db.listingsAndReviews.find({$and: [{amenities: "Wifi"}, {amenities: "TV"}]}); //andlogic
#$andoror :operator where $and operator combines two conditions and $or operator is used to see aleast one specific condition is satisfied
db.routes.find({
  $and: [
    {$or: [{dst_airport: "SEA"}, {src_airport: "SEA"}]},
    {$or: [{"airline.name": "American Airlines"}, {airplane: 320}]},
  ],
});
#$elementmatch:  it's ensuring that at least one element in the amenities array meets the specified criteria
db.listingsAndReviews.find({amenities: {$elemMatch: {$eq: "Wifi"}}});
#$find operator: The find operation is fundamental to querying and retrieving data from MongoDB collections based on specified criteria.
db.grades.find({ _id: ObjectId("65b9b6f769c4895078585dc0") })
#$find array: operator Find documents where the array amenities contains an embedded document with user  wifi" 
db.listingsAndReviews.find({amenities: "Wifi"});
#$gt: Value is greater than another value
db.grades.find({ grade: { $gt:59  } })
#$gte: Value is greater than or equal to another value
db.grades.find({ "products.score": { $lt: 59  } })
#$in: Value is matched within an array
db.grades.find({ student_id: { $in: [654321, 546789] } })
db.grades.find({ _id: { $in: [ObjectId('65b9b75969c4895078585dc1'), ObjectId('65b9b75969c4895078585dc2')] } })
#$insertmany:is used to insert multiple documents into a collection in a single operation.
db.grades.insertMany([
  {
    student_id: 546789,
    products: [
      {
        type: "quiz",
        score: 50,
      },
      {
        type: "homework",
        score: 70,
      },
      {
        type: "quiz",
        score: 66,
      },
      {
        type: "exam",
        score: 70,
      },
    ],
    class_id: 551,
  },
  {
    student_id: 777777,
    products: [
      {
        type: "exam",
        score: 83,
      },
      {
        type: "quiz",
        score: 59,
      },
      {
        type: "quiz",
        score: 72,
      },
      {
        type: "quiz",
        score: 67,
      },
    ],
    class_id: 550,
  },
  {
    student_id: 223344,
    products: [
      {
        type: "exam",
        score: 45,
      },
      {
        type: "homework",
        score: 39,
      },
      {
        type: "quiz",
        score: 40,
      },
      {
        type: "homework",
        score: 88,
      },
    ],
    class_id: 551,
  },
])
#insertone:is used to insert a single document into a collection.
db.grades.insertOne({
  student_id: 654321,
  products: [
    {
      type: "exam",
      score: 90,
    },
    {
      type: "homework",
      score: 59,
    },
    {
      type: "quiz",
      score: 75,
    },
    {
      type: "homework",
      score: 88,
    },
  ],
  class_id: 550,
})
#$lt: Value is less than another value
db.grades.find({ "products.score": { $lt: 59  } })
#$lte: Value is less than or equal to another value
db.grades.find({ "products.score": { $lt: 59  } })
#$or: Returns documents where either query matches
db.listingsAndReviews.find({$or: [{amenities: "Wifi"}, {amenities: "TV"}]});

