#
# Copyright 2016, Data61
# Commonwealth Scientific and Industrial Research Organisation (CSIRO)
# ABN 41 687 119 230.
#
# This software may be distributed and modified according to the terms of
# the BSD 2-Clause license. Note that NO WARRANTY is provided.
# See "LICENSE_BSD2.txt" for details.
#
# @TAG(D61_BSD)
#

// DO NOT EDIT MANUALLY!!!\n
// This file was generated by CIDL - Simple C IDL Compiler.\n\n

{{for include in includes}}
    {{include}}\n
{{endfor}}
\n\n

int rpc_sv_{{ifname}}_dispatcher(void *rpc_userptr, uint32_t label) {\n
____switch (label) {\n

        {{for func_output in func_list}}
            {{func_output}}\n
        {{endfor}}

________default:\n
____________return -1;\n
____}\n
____return 0;\n
}
\n
