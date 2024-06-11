#include <time.h>
#include "python.h"


static PyObject* spam_date(PyObject *self, PyObject *args)
{
	int d_day;
	if (!PyArg_ParseTuple(args, "i", &d_day)) // 매개변수 값을 분석하고 지역변수에 할당 시킵니다.
		return NULL;

	time_t timer = time(NULL);
	struct tm *t = localtime(&timer);
	char buffer[80]; // 0000-00-00 형태

	t->tm_mday -= d_day;
	mktime(t);
	strftime(buffer, 80, "%Y-%m-%d", t);

	PyObject* result = PyUnicode_FromString(buffer);
	return result;
}

static PyMethodDef SpamMethods[] = {
	{ "date", spam_date, METH_VARARGS, "d-day" },
	{ NULL, NULL, 0, NULL } // 배열의 끝을 나타냅니다.
};

static struct PyModuleDef spammodule = {
	PyModuleDef_HEAD_INIT,
	"spam",            // 모듈 이름
	"d-day.", // 모듈 설명을 적는 부분, 모듈의 __doc__에 저장됩니다.
	-1,SpamMethods
};

PyMODINIT_FUNC
PyInit_spam(void)
{
	return PyModule_Create(&spammodule);
}
