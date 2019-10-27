# OpenAPI 2 Ceres 

[Ceres](https://github.com/laulin/ceres) is a code generation. It was designed to 
be as simple as possible. 

This tool takes an OpenAPI YAML file a input and will provide Ceres YAML entities 
as output. So you can simply generate your backend code as fast as lightning !

## Installation

From github :

```bash
foo@bar:~$ git clone https://github.com/laulin/openapi2ceres
foo@bar:~$ cd openapi2ceres
foo@bar:~/openapi2ceres$ sudo make install
```

## Usage

Based on the example in the repo, let's look at the command to make it :

```bash
foo@bar:openapi2ceres$ openapi2ceres -i /example/petstore.yaml -o example/
```

The output produced :

```
Create directory /home/foobar/openapi2ceres/example/pet
Create directory /home/foobar/openapi2ceres/example/store
Create directory /home/foobar/openapi2ceres/example/user
Create file /home/foobar/openapi2ceres/example/pet/post.pet.yml
Create file /home/foobar/openapi2ceres/example/pet/put.pet.yml
Create file /home/foobar/openapi2ceres/example/pet/get.pet_findbystatus.yml
Create file /home/foobar/openapi2ceres/example/pet/get.pet_findbytags.yml
Create file /home/foobar/openapi2ceres/example/pet/get.pet_{petid}.yml
Create file /home/foobar/openapi2ceres/example/pet/post.pet_{petid}.yml
Create file /home/foobar/openapi2ceres/example/pet/delete.pet_{petid}.yml
Create file /home/foobar/openapi2ceres/example/pet/post.pet_{petid}_uploadimage.yml
Create file /home/foobar/openapi2ceres/example/store/get.store_inventory.yml
Create file /home/foobar/openapi2ceres/example/store/post.store_order.yml
Create file /home/foobar/openapi2ceres/example/store/get.store_order_{orderid}.yml
Create file /home/foobar/openapi2ceres/example/store/delete.store_order_{orderid}.yml
Create file /home/foobar/openapi2ceres/example/user/post.user.yml
Create file /home/foobar/openapi2ceres/example/user/post.user_createwitharray.yml
Create file /home/foobar/openapi2ceres/example/user/post.user_createwithlist.yml
Create file /home/foobar/openapi2ceres/example/user/get.user_login.yml
Create file /home/foobar/openapi2ceres/example/user/get.user_logout.yml
Create file /home/foobar/openapi2ceres/example/user/get.user_{username}.yml
Create file /home/foobar/openapi2ceres/example/user/put.user_{username}.yml
Create file /home/foobar/openapi2ceres/example/user/delete.user_{username}.yml
```

## What's happen ?

Well, like Ceres, there is no magic and the process is simple. A OpenAPI is 
composed of two parts : 

- a global context :

```yaml
info:
  description: "test"
host: "api.yolo.io"
basePath: "/v2"
tags:
- name: "dwarf"
schemes:
- "https"
# ...
```

- a *paths* key that contains path :

```yaml
paths:
  /dwarf:
    post:
      tags:
      - "darf"
      summary: "Add a new dwarf"
      description: ""
      operationId: "addDwarf"
      # ...
```

The output file is named *dwarf/post.dwarf.yaml* and contains :

```yaml
name: post.dwarf

entity:
  path: /dwarf
  method:  post
  tags:
  - "darf"
  summary: "Add a new dwarf"
  description: ""
  operationId: "addDwarf"

globals:
  info:
    description: "test"
  host: "api.yolo.io"
  basePath: "/v2"
  tags:
  - name: "dwarf"
  schemes:
  - "https"
```