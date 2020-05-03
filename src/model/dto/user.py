class UserDto:
    # types

    __str = 'string'
    __bool = 'boolean'
    __int = 'integer'

    # keys
    __id = 'id'
    __username = 'username'
    __is_adm = 'is_admin'
    __pass = 'password'


    create_user_dto = {
        'properties': {
            __username: {'type': __str},
            __is_adm: {'type': __bool},
            __pass: {'type': __str},
        },
        'required': [__username, __is_adm, __pass]
    }

    update_user_dto = {
        'properties': {
            __id: {'type': __int},
            __username: {'type': __str},
            __is_adm: {'type': __bool},
            __pass: {'type': __int},
        },
        'required': [__id, __username, __is_adm, __pass]
    }

    login_dto = {
        'properties': {
            __username: {'type': __str},
            __pass: {'type': __int},
        },
        'required': [__username, __pass]
    }

    delete_user_dto = {
        'properties': {
            __id: {'type': __int},

        },
        'required': [__pass]
    }