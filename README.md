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
Create file /home/gignops/work/openapi2ceres/example/pet.yml
Create file /home/gignops/work/openapi2ceres/example/pet.yml
Create file /home/gignops/work/openapi2ceres/example/pet_findbystatus.yml
Create file /home/gignops/work/openapi2ceres/example/pet_findbytags.yml
Create file /home/gignops/work/openapi2ceres/example/pet_{petid}.yml
Create file /home/gignops/work/openapi2ceres/example/pet_{petid}.yml
Create file /home/gignops/work/openapi2ceres/example/pet_{petid}.yml
Create file /home/gignops/work/openapi2ceres/example/pet_{petid}_uploadimage.yml
Create file /home/gignops/work/openapi2ceres/example/store_inventory.yml
Create file /home/gignops/work/openapi2ceres/example/store_order.yml
Create file /home/gignops/work/openapi2ceres/example/store_order_{orderid}.yml
Create file /home/gignops/work/openapi2ceres/example/store_order_{orderid}.yml
Create file /home/gignops/work/openapi2ceres/example/user.yml
Create file /home/gignops/work/openapi2ceres/example/user_createwitharray.yml
Create file /home/gignops/work/openapi2ceres/example/user_createwithlist.yml
Create file /home/gignops/work/openapi2ceres/example/user_login.yml
Create file /home/gignops/work/openapi2ceres/example/user_logout.yml
Create file /home/gignops/work/openapi2ceres/example/user_{username}.yml
Create file /home/gignops/work/openapi2ceres/example/user_{username}.yml
Create file /home/gignops/work/openapi2ceres/example/user_{username}.yml
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
methods:
  - post
path: /dwarf
post:
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