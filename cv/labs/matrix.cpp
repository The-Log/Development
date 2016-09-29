//
// Created by Ankur Mishra on 9/24/16.
//

class Matrix{
public:
    Matrix(int, int);
    Matrix();
    ~Matrix();
    Matrix(const Matrix&);

    inline double& operator()(int x, int y) { return p[x][y]; }

    Matrix& operator+=(const Matrix&);
    Matrix& operator-=(const Matrix&);
    Matrix& operator*=(const Matrix&);
    Matrix& operator*=(double);

private:
    int r, c;
    double **p;
    void allocate();

};

Matrix::Matrix(int rows, int cols) :r(rows),c(cols) {
    allocate();
    for (int i = 0; i < r; ++i) {
        for (int j = 0; j < c; ++j) {
            p[i][j] = 0;
        }
    }
}

Matrix::Matrix() : r(1), c(1){
    allocate();
    p[0][0] = 0;
}

//Matrix& Matrix:: operator =(const Matrix& m)
//{
//    if (this == &m) {
//        return *this;
//    }
//
//    if (r != m.r || c != m.c) {
//        for (int i = 0; i < r; ++i) {
//            delete[] p[i];
//        }
//        delete[] p;
//
//        r = m.r;
//        c = m.c;
//        allocate();
//    }
//
//    for (int i = 0; i < r; ++i) {
//        for (int j = 0; j < c; ++j) {
//            p[i][j] = m.p[i][j];
//        }
//    }
//    return *this;
//}

Matrix::~Matrix(){
    for (int i = 0; i < r; ++i) {
        delete[] p[i];
    }
    delete[] p;
}

Matrix::Matrix(const Matrix& m) : r(m.r), c(m.c) {
    allocate();
    for (int i = 0; i < r; ++i) {
        for (int j = 0; j < c; ++j) {
            p[i][j] = m.p[i][j];
        }
    }
}
Matrix& Matrix::operator+=(const Matrix& m){
    for (int i = 0; i < r; ++i) {
        for (int j = 0; j < c; ++j) {
            p[i][j] += m.p[i][j];
        }
    }
    return *this;
}
Matrix& Matrix::operator-=(const Matrix& m)
{
    for (int i = 0; i < r; ++i) {
        for (int j = 0; j < c; ++j) {
            p[i][j] -= m.p[i][j];
        }
    }
    return *this;
}
Matrix& Matrix::operator*=(double num){
    for (int i = 0; i < r; ++i) {
        for (int j = 0; j < c; ++j) {
            p[i][j] *= num;
        }
    }
    return *this;
}
Matrix& Matrix::operator*=(const Matrix & m) {
    Matrix temp(r, m.c);
    for (int i = 0; i < temp.r; ++i) {
        for (int j = 0; j < temp.c; ++j) {
            for (int k = 0; k < c; ++k) {
                temp.p[i][j] += (p[i][k] * m.p[k][j]);
            }
        }
    }
    return (*this = temp);
}

void Matrix::allocate()
{
    p = new double*[r];
    for (int i = 0; i < r; ++i) {
        p[i] = new double[c];
    }
}

Matrix operator+(const Matrix& m1, const Matrix& m2)
{
    Matrix temp(m1);
    return (temp += m2);
}

Matrix operator-(const Matrix& m1, const Matrix& m2)
{
    Matrix temp(m1);
    return (temp -= m2);
}

Matrix operator*(const Matrix& m1, const Matrix& m2)
{
    Matrix temp(m1);
    return (temp *= m2);
}

Matrix operator*(const Matrix& m, double num)
{
    Matrix temp(m);
    return (temp *= num);
}

Matrix operator*(double num, const Matrix& m)
{
    return (m * num);
}
