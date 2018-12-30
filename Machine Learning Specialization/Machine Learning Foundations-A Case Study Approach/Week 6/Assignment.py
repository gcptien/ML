dog = image_train[image_train['label'] == 'dog']
cat = image_train[image_train['label'] == 'cat']
car = image_train[image_train['label'] == 'automobile']
bird = image_train[image_train['label'] == 'bird']

dog_model = graphlab.nearest_neighbors.create(dog,features=['deep_features'],label='id')
cat_model = graphlab.nearest_neighbors.create(cat,features=['deep_features'],label='id')
car_model = graphlab.nearest_neighbors.create(car,features=['deep_features'],label='id')
bird_model = graphlab.nearest_neighbors.create(bird,features=['deep_features'],label='id')

# question 2
image1 = image_test[0:1]
def get_images_from_ids(query_result):
    return image_train.filter_by(query_result['reference_label'],'id')
get_images_from_ids(cat_model.query(image1))['image'].show()
get_images_from_ids(dog_model.query(image1))['image'].show()

# question 3

# quesiton 4
dog_test = image_test[image_test['label'] == 'dog']
cat_test = image_test[image_test['label'] == 'cat']
car_test = image_test[image_test['label'] == 'automobile']
bird_test = image_test[image_test['label'] == 'bird']

dog_cat_neighbors = cat_model.query(dog_test, k=1)
dog_car_neighbors = car_model.query(dog_test, k=1)
dog_bird_neighbors = bird_model.query(dog_test, k=1)

dog_distance = graphlab.SFrame({'dog-dog': dog_dog_neighbors['distance'],
                                'dog-cat': dog_cat_neighbors['distance'],
                                'dog-automobile': dog_car_neighbors['distance'],
                                'dog-bird':dog_bird_neighbors['distance']})

def is_dog_correct(row):
    if ( min(row, key=row.get) == 'dog-dog'):
        return 1
    else:
        return 0

dog_distance.apply(is_dog_correct).sum()

accuracy = dog_distance.apply(is_dog_correct).sum()*1.0/len(dog_distance)
accuracy
