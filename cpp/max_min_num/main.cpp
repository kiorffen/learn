#include <cstdio>

void max_min(int a[], int begin, int end, int *max, int *min) {
    if (end == begin) {
        *max = a[begin];
        *min = a[end];

        return;
    }
    int l_max, r_max;
    int l_min, r_min;
    max_min(a, begin, begin + (end - begin) / 2, &l_max, &l_min);
    max_min(a, begin + (end - begin) / 2 + 1, end, &r_max, &r_min);
    *max = l_max > r_max ? l_max : r_max;
    *min = l_min < r_min ? l_min : r_min;
}

int main() {
    int array[] = {7,8,9,11,13,45,8,9,23,45,97,3,2,7,14,64,19};
    int len = sizeof(array) / sizeof(int);
    int max = array[0];
    int min = array[0];
    for (int i = 1; i < len; ++i) {
        if (array[i] > max) {
            max = array[i];
        } else if (array[i] < min){
            min = array[i];
        }
    }
    printf("max:%d min:%d\n", max, min);
    int start = -1;
    if (len & 0x1) {
        start = 1;
    } else {
        start = 0;
    }

    for (int i = start; i < len; i+=2) {
        if (array[i] > array[i + 1]) {
            if (array[i] > max) max = array[i];
            if (array[i + 1] < min) min = array[i + 1];
        } else if (array[i] < array[i + 1]) {
            if (array[i] < min) min = array[i];
            if (array[i + 1] > max) max = array[i + 1];
        }
    }
    printf("max:%d min:%d\n", max, min);

    max_min(array, 0, len - 1, &max, &min);
    printf("max:%d min:%d\n", max, min);

    return 0;
}
