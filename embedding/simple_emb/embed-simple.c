/*******************************************************
 * simple code strings: C acts like the interactive
 * prompt, code runs in __main__, no output sent to C;
 *******************************************************/

//#include <Python.h>    /* standard API def */
//
//int main() {
//    printf("embed-simple\n");
//    Py_Initialize();
//    PyRun_SimpleString("import sys");
//    PyRun_SimpleString("sys.path.append(\".\")");
//    PyRun_SimpleString("import usermod");                /* load .py file */
//    PyRun_SimpleString("print(usermod.message)");        /* on Python path */
//    PyRun_SimpleString("x = usermod.message");           /* compile and run */
//    PyRun_SimpleString("print(usermod.transform(x))");
//    Py_Finalize();
//}

/* code-strings with results and namespaces */

//#include <Python.h>
//
//int main() {
//    char *cstr;
//    PyObject *pstr, *pmod, *pdict;
//    printf("embed-string\n");
//    Py_Initialize();
//
//    /* get usermod.message */
//    pmod  = PyImport_ImportModule("usermod");
//    pdict = PyModule_GetDict(pmod);
//    pstr  = PyRun_String("message", Py_eval_input, pdict, pdict);
//
//    /* convert to C */
//    PyArg_Parse(pstr, "s", &cstr);
//    printf("%s\n", cstr);
//
//    /* assign usermod.X */
//    PyObject_SetAttrString(pmod, "X", pstr);
//
//    /* print usermod.transform(X) */
//    (void) PyRun_String("print(transform(X))", Py_file_input, pdict, pdict);
//    Py_DECREF(pmod);
//    Py_DECREF(pstr);
//    Py_Finalize();
//}


/* fetch and call objects in modules */

//#include <Python.h>
//
//int main() {
//    char *cstr;
//    PyObject *pstr, *pmod, *pfunc, *pargs;
//    printf("embed-object\n");
//    Py_Initialize();
//
//    /* get usermod.message */
//    pmod = PyImport_ImportModule("usermod");
//    pstr = PyObject_GetAttrString(pmod, "message");
//
//    /* convert string to C */
//    PyArg_Parse(pstr, "s", &cstr);
//    printf("%s\n", cstr);
//    Py_DECREF(pstr);
//
//    /* call usermod.transform(usermod.message) */
//    pfunc = PyObject_GetAttrString(pmod, "transform");
//    pargs = Py_BuildValue("(s)", cstr);
//    pstr  = PyEval_CallObject(pfunc, pargs);
//    PyArg_Parse(pstr, "s", &cstr);
//    printf("%s\n", cstr);
//
//    /* free owned objects */
//    Py_DECREF(pmod);
//    Py_DECREF(pstr);
//    Py_DECREF(pfunc);        /* not really needed in main() */
//    Py_DECREF(pargs);        /* since all memory goes away  */
//    Py_Finalize();
//}

/* make a new dictionary for code string namespace */

//#include <Python.h>
//
//int main() {
//    int cval;
//    PyObject *pdict, *pval;
//    printf("embed-dict\n");
//    Py_Initialize();
//
//    /* make a new namespace */
//    pdict = PyDict_New();
//    PyDict_SetItemString(pdict, "__builtins__", PyEval_GetBuiltins());
//
//    PyDict_SetItemString(pdict, "Y", PyLong_FromLong(2));  /* dict['Y'] = 2   */
//    PyRun_String("X = 99",  Py_file_input, pdict, pdict);  /* run statements  */
//    PyRun_String("X = X+Y", Py_file_input, pdict, pdict);  /* same X and Y    */
//    pval = PyDict_GetItemString(pdict, "X");               /* fetch dict['X'] */
//
//    PyArg_Parse(pval, "i", &cval);                         /* convert to C */
//    printf("%d\n", cval);                                  /* result=101 */
//    Py_DECREF(pdict);
//    Py_Finalize();
//}

/* precompile code strings to bytecode objects */

#include <Python.h>
#include <compile.h>
#include <eval.h>

int main() {
    int i;
    char *cval;
    PyObject *pcode1, *pcode2, *pcode3, *presult, *pdict;
    char *codestr1, *codestr2, *codestr3;
    printf("embed-bytecode\n");

    Py_Initialize();
    codestr1 = "import usermod\nprint(usermod.message)";    /* statements */
    codestr2 = "usermod.transform(usermod.message)";        /* expression */
    codestr3 = "print('%d:%d' % (X, X ** 2))";     /* use input X */

    /* make new namespace dictionary */
    pdict = PyDict_New();
    if (pdict == NULL) return -1;
    PyDict_SetItemString(pdict, "__builtins__", PyEval_GetBuiltins());

    /* precompile strings of code to bytecode objects */
    pcode1 = Py_CompileString(codestr1, "<embed>", Py_file_input);
    pcode2 = Py_CompileString(codestr2, "<embed>", Py_eval_input);
    pcode3 = Py_CompileString(codestr3, "<embed>", Py_file_input);

    /* run compiled bytecode in namespace dict */
    if (pcode1 && pcode2 && pcode3) {
        (void)    PyEval_EvalCode(pcode1, pdict, pdict);
        presult = PyEval_EvalCode(pcode2, pdict, pdict);
        PyArg_Parse(presult, "s", &cval);
        printf("%s\n", cval);
        Py_DECREF(presult);

        /* rerun code object repeatedly */
        for (i = 0; i <= 10; i++) {
            PyDict_SetItemString(pdict, "X", PyLong_FromLong(i));
            (void) PyEval_EvalCode(pcode3, pdict, pdict);
        }
        printf("\n");
    }
    /* free referenced objects */
    Py_XDECREF(pdict);
    Py_XDECREF(pcode1);
    Py_XDECREF(pcode2);
    Py_XDECREF(pcode3);
    Py_Finalize();
}
