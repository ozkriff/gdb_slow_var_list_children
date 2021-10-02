import gdb


def untypedef(type_obj):
    if (type_obj.code == gdb.TYPE_CODE_REF
            or type_obj.code == getattr(gdb, 'TYPE_CODE_RVALUE_REF', None)):
        type_obj = type_obj.target()
    if type_obj.code == gdb.TYPE_CODE_TYPEDEF:
        type_obj = type_obj.strip_typedefs()
    return type_obj


def lookup(val):
    type = untypedef(val.type)
    if type.code == gdb.TYPE_CODE_PTR:
        try:
            dereferenced = val.dereference()
            dereferenced.fetch_lazy()
        except gdb.error as e:
            print('ERROR: ', str(e))
        else:
            delegate = gdb.default_visualizer(dereferenced)
            assert(delegate is None)
            # normally, the delegate would be passed into a custom pretty printer next
    return None


def register_default_printers(obj):
    gdb.printing.register_pretty_printer(obj, lookup)
