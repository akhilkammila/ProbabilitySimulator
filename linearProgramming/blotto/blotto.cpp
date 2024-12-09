#include <vector>
#include <iostream>
#include <util.h>
#include <map>
#include <iomanip>

using namespace std;

typedef long long ll;
typedef long double ld;
typedef string str;
typedef pair<int,int> pi;
typedef vector<int> vi;
typedef vector<ld> vd;
#define f first
#define s second
#define pb push_back
#define forr(i,a,b) for (int i = (a); i < (b); i++)
#define ford(i,a,b) for (int i = (a)-1; i >= (b); i--)
#define trav(a,x) for (auto& a: x)
template<class T> bool ckmin(T& a, const T& b) { return b < a ? a = b, 1 : 0; }
template<class T> bool ckmax(T& a, const T& b) { return a < b ? a = b, 1 : 0; }
const ll MOD = 1e9+7;

const int mxN = 2e5+5;
ld tolerance = 1e-6, eps = 1e-9;
map<int,vi> to_strat; //maps an index to a strategy
vd points;
vector<vd> mat;
struct LPSolver {
	int m, n;
	vi B, N;
	vector<vd> D;

	LPSolver(const vector<vd> &A, const vd &b, const vd &c) :
		m(b.size()), n(c.size()), N(n + 1), B(m), D(m + 2, vd(n + 2)) {
		for (int i = 0; i < m; i++) for (int j = 0; j < n; j++) D[i][j] = A[i][j];
		for (int i = 0; i < m; i++) { B[i] = n + i; D[i][n] = -1; D[i][n + 1] = b[i]; }
		for (int j = 0; j < n; j++) { N[j] = j; D[m][j] = -c[j]; }
		N[n] = -1; D[m + 1][n] = 1;
	}

	void Pivot(int r, int s) {
		ld inv = 1.0 / D[r][s];
		for (int i = 0; i < m + 2; i++) if (i != r)
			for (int j = 0; j < n + 2; j++) if (j != s)
				D[i][j] -= D[r][j] * D[i][s] * inv;
		for (int j = 0; j < n + 2; j++) if (j != s) D[r][j] *= inv;
		for (int i = 0; i < m + 2; i++) if (i != r) D[i][s] *= -inv;
		D[r][s] = inv;
		swap(B[r], N[s]);
	}

	bool Simplex(int phase) {
		int x = phase == 1 ? m + 1 : m;
		while (true) {
			int s = -1;
			for (int j = 0; j <= n; j++) {
				if (phase == 2 && N[j] == -1) continue;
				if (s == -1 || D[x][j] < D[x][s] || D[x][j] == D[x][s] && N[j] < N[s]) s = j;
			}
			if (D[x][s] > -eps) return true;
			int r = -1;
			for (int i = 0; i < m; i++) {
				if (D[i][s] < eps) continue;
				if (r == -1 || D[i][n + 1] / D[i][s] < D[r][n + 1] / D[r][s] ||
					(D[i][n + 1] / D[i][s]) == (D[r][n + 1] / D[r][s]) && B[i] < B[r]) r = i;
			}
			if (r == -1) return false;
			Pivot(r, s);
		}
	}

	ld Solve(vd &x) {
		int r = 0;
		for (int i = 1; i < m; i++) if (D[i][n + 1] < D[r][n + 1]) r = i;
		if (D[r][n + 1] < -eps) {
			Pivot(r, n);
			if (!Simplex(1) || D[m + 1][n + 1] < -eps) return -numeric_limits<ld>::infinity();
			for (int i = 0; i < m; i++) if (B[i] == -1) {
				int s = -1;
				for (int j = 0; j <= n; j++)
				if (s == -1 || D[i][j] < D[i][s] || D[i][j] == D[i][s] && N[j] < N[s]) s = j;
				Pivot(i, s);
			}
		}
		if (!Simplex(2)) return numeric_limits<ld>::infinity();
		x = vd(n);
		for (int i = 0; i < m; i++) if (B[i] < n) x[B[i]] = D[i][n + 1];
		return D[m][n + 1];
	}
};
ld fight(vi s1, vi s2, int obj) {
	if (obj < 2) {
		ld score1 = 0, score2 = 0;
		forr(i,0,(int)points.size()) {
			if (s1[i] > s2[i]) {
				score1 += points[i];
			} else if (s1[i] < s2[i]) {
				score2 += points[i];
			} else {
				score1 += points[i]/2.;
				score2 += points[i]/2.;
			}
		}
		if (obj == 0) {
			if (score1 > score2) return 1;
			else if (score1 < score2) return 0;
			else return 0.5;
		} else {
			return score1;
		}
	} else {
		ld ev = 0;
		forr(i,0,(int)points.size()) {
			if (s1[i] == 0 && s2[i] == 0) {
				ev += 0.5 * points[i];
				continue;
			}
			ev += (ld)(s1[i]*s1[i])/(ld)(s1[i]*s1[i] + s2[i]*s2[i]) * points[i];
		}
		return ev;
	}
	return 0;
}
int init_map(int units) {
	int bits = 0, t = 1;
	while (t <= units) {
		t *= 2;
		bits++;
	}
	int fields = points.size();
	int idx = 0;
	forr(i,0,1<<(bits*fields)) {
		vi distrib(fields);
		int sum = 0;
		forr(j,0,fields) {
			distrib[j] = (i>>(j*bits)) & ((1<<bits)-1);
			sum += distrib[j];
		}
		if (sum == units) {
			to_strat[idx] = distrib;
			idx++;
		}
	}
	return idx;
}

int main(int argc, char* argv[]) {
	cin.tie(0)->sync_with_stdio(0);

	int arg = 0;
	str query = argv[++arg];
	// parsing
	str objective = argv[++arg];
	if (objective == "--tolerance") {
		ld tol = stold(argv[++arg]);
		tolerance = tol;
		objective = argv[++arg];
	}
	int obj;
	if (objective == "--win") obj = 0;
	else if (objective == "--score") obj = 1;
	else obj = 2;
	if (query == "--find") {
		arg++;
		int units = stoi(argv[++arg]);
		points.resize(argc-arg-1);
		forr(i,arg+1,argc) {
			points[i - (arg+1)] = stoi(argv[i]);
		}
		// initialize maps
		int idx = init_map(units), fields = points.size();
		// create matrix
		mat.resize(idx, vd(idx, 0));
		forr(i,0,idx) forr(j,0,idx) {
			mat[i][j] = fight(to_strat[i], to_strat[j], obj);
		}
		// initialize simplex
		vector<vd> A(idx+2, vd(idx+1, 0));
		forr(i,0,idx) {
			forr(j,0,idx) A[i][j] = -mat[j][i];
			A[i][idx] = 1;
		}
		forr(i,0,idx) {
			A[idx][i] = 1;
			A[idx+1][i] = -1;
		}
		vd b(idx+2, 0);
		b[idx] = 1;
		b[idx+1] = -1;
		vd c(idx+1, 0);
		c[idx] = 1;
		LPSolver solver(A, b, c);
		vd x; solver.Solve(x);
		forr(i,0,idx) {
			if (x[i] == 0) continue;
			vi st = to_strat[i];
			forr(j,0,fields) cout << st[j] << ",";
			cout << setprecision(20) << x[i] << "\n";
		}
	} else {
		points.resize(argc-arg-1);
		forr(i,arg+1,argc) {
			points[i - (arg+1)] = stoi(argv[i]);
		}
		vector<pair<vi,ld>> v;
		str s;
		while (getline(cin, s)) {
			vi t;
			str curr;
			forr(i,0,(int)s.length()) {
				if (s[i] == ',') {
					t.pb(stoi(curr));
					curr = "";
				} else curr += s[i];
			}
			v.pb({t,stold(curr)});
		}
		int units = 0;
		trav(i,v[0].f) units += i;
		int idx = init_map(units);
		// run mixed strategy against every pure strategy
		ld base = 0;
		forr(i,0,(int)v.size()) {
			forr(j,0,(int)v.size()) {
				base += v[i].s * v[j].s * fight(v[i].f, v[j].f, obj);
			}
		}
		bool ok = 1;
		forr(i,0,idx) {
			ld res = 0;
			forr(j,0,(int)v.size()) {
				res += v[j].s * fight(v[j].f, to_strat[i], obj);
			}
			if (base-res > tolerance) ok = 0;
		}
		cout << (ok ? "PASSED" : "NO") << "\n";
	}
}
/*
use simplex to solve linprog

in the WIN matrix
every item is 1, 1/2 or 0 for win, loss, draw
in the SCORE matrix
score player 1 would get if those 2 pure strategies played each other
in the LOTTERY matrix
score player 1 would get if those 2 pure strategies played each other
(each battlefield's expected points calculated with probability)

ld fight(vi ditrib1, vi distrib2, int type)

calculate the matrix C we need depending on type

to validate a strategy
we need to compare every single possible non-randomized strategy
to the current strategy

10 units, 4 battlefields
there are 13c3 total strategies
every comparison is o(4)
*/