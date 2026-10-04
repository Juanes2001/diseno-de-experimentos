"""Cálculos de factoriales fraccionados 2^(k-p) en Python puro."""
import math, itertools
from statistics import NormalDist

def basic(n):
    """Diseño básico 2^n en orden estándar: lista de dicts letra->±1."""
    letters="ABCDEFGH"[:n]
    rows=[]
    for i in range(2**n):
        rows.append({L:(1 if (i>>j)&1 else -1) for j,L in enumerate(letters)})
    return rows

def col(rows,word):
    out=[]
    for r in rows:
        v=1
        for ch in word: v*=r[ch]
        out.append(v)
    return out

def add_factor(rows,name,word,sign=1):
    c=col(rows,word)
    for r,v in zip(rows,c): r[name]=sign*v
    return rows

def effect(rows,y,word):
    c=col(rows,word); N=len(y)
    contr=sum(a*b for a,b in zip(c,y))
    return contr, 2*contr/N, contr*contr/N

def mult(w1,w2):
    s=set(w1)^set(w2)
    return "".join(sorted(s))

def defining(gens):
    words=set()
    for r in range(1,len(gens)+1):
        for comb in itertools.combinations(gens,r):
            w=""
            for g in comb: w=mult(w,g)
            words.add(w)
    return sorted(words,key=lambda w:(len(w),w))

def aliases(effect_word,words,maxlen=None):
    al=[mult(effect_word,w) for w in words]
    if maxlen: al=[a for a in al if len(a)<=maxlen]
    return sorted(al,key=lambda w:(len(w),w))

# --- distribución F: P(F>f) mediante beta incompleta regularizada ---
def _betacf(a,b,x):
    MAXIT=300; EPS=3e-14; FPMIN=1e-300
    qab=a+b; qap=a+1; qam=a-1; c=1.0; d=1-qab*x/qap
    if abs(d)<FPMIN: d=FPMIN
    d=1/d; h=d
    for m in range(1,MAXIT+1):
        m2=2*m
        aa=m*(b-m)*x/((qam+m2)*(a+m2))
        d=1+aa*d; d=FPMIN if abs(d)<FPMIN else d
        c=1+aa/c; c=FPMIN if abs(c)<FPMIN else c
        d=1/d; h*=d*c
        aa=-(a+m)*(qab+m)*x/((a+m2)*(qap+m2))
        d=1+aa*d; d=FPMIN if abs(d)<FPMIN else d
        c=1+aa/c; c=FPMIN if abs(c)<FPMIN else c
        d=1/d; de=d*c; h*=de
        if abs(de-1)<EPS: break
    return h
def betai(a,b,x):
    if x<=0: return 0.0
    if x>=1: return 1.0
    bt=math.exp(math.lgamma(a+b)-math.lgamma(a)-math.lgamma(b)+a*math.log(x)+b*math.log(1-x))
    if x<(a+1)/(a+b+2): return bt*_betacf(a,b,x)/a
    return 1-bt*_betacf(b,a,1-x)/b
def f_sf(f,d1,d2):
    return betai(d2/2,d1/2,d2/(d2+d1*f))
def f_ppf(p_upper,d1,d2):
    lo,hi=0.0,1e6
    for _ in range(200):
        mid=(lo+hi)/2
        if f_sf(mid,d1,d2)>p_upper: lo=mid
        else: hi=mid
    return (lo+hi)/2
def t_sf2(t,df):  # dos colas
    return f_sf(t*t,1,df)

def normal_scores(vals):
    """Devuelve lista (valor, z) ordenada, con posiciones (i-0.5)/n."""
    n=len(vals); idx=sorted(range(n),key=lambda i:vals[i])
    out=[None]*n
    for rank,i in enumerate(idx):
        out[i]=NormalDist().inv_cdf((rank+0.5)/n)
    return out

def fit(rows,y,terms):
    """Modelo con términos ortogonales: devuelve dict con anova, ajustados, residuales."""
    N=len(y); ybar=sum(y)/N
    sst=sum((v-ybar)**2 for v in y)
    coefs={}; ss={}
    for t in terms:
        c,e,s=effect(rows,y,t); coefs[t]=e/2; ss[t]=s
    fitted=[]
    for r in rows:
        v=ybar
        for t in terms:
            x=1
            for ch in t: x*=r[ch]
            v+=coefs[t]*x
        fitted.append(v)
    res=[a-b for a,b in zip(y,fitted)]
    sse=sum(e*e for e in res); dfe=N-1-len(terms)
    mse=sse/dfe if dfe>0 else float('nan')
    an=[]
    for t in terms:
        F=ss[t]/mse; an.append((t,ss[t],1,ss[t],F,f_sf(F,1,dfe)))
    ssm=sum(ss.values())
    return dict(ybar=ybar,coefs=coefs,ss=ss,sst=sst,sse=sse,dfe=dfe,mse=mse,anova=an,
                fitted=fitted,res=res,ssm=ssm,Fm=(ssm/len(terms))/mse,pm=f_sf((ssm/len(terms))/mse,len(terms),dfe),
                r2=ssm/sst,r2adj=1-(sse/dfe)/(sst/(N-1)),S=math.sqrt(mse))

def lenth(effects):
    a=sorted(abs(e) for e in effects)
    def med(v):
        n=len(v); return v[n//2] if n%2 else (v[n//2-1]+v[n//2])/2
    s0=1.5*med(a)
    pse=1.5*med([x for x in a if x<2.5*s0])
    return pse

def t_ppf(p_two_sided, df):
    """Cuantil t tal que P(|T|>t)=p_two_sided."""
    lo,hi=0.0,1e4
    for _ in range(200):
        mid=(lo+hi)/2
        if t_sf2(mid,df)>p_two_sided: lo=mid
        else: hi=mid
    return (lo+hi)/2

def anderson_darling(x):
    """Estadístico A², A² ajustado y valor p aproximado (D'Agostino y Stephens)."""
    n=len(x); m=sum(x)/n; s=math.sqrt(sum((v-m)**2 for v in x)/(n-1))
    z=sorted((v-m)/s for v in x); nd=NormalDist()
    a2=-n-sum((2*i+1)*(math.log(nd.cdf(z[i]))+math.log(1-nd.cdf(z[n-1-i]))) for i in range(n))/n
    a=a2*(1+0.75/n+2.25/n**2)
    if a>=0.6: p=math.exp(1.2937-5.709*a+0.0186*a*a)
    elif a>0.34: p=math.exp(0.9177-4.279*a-1.38*a*a)
    elif a>0.2: p=1-math.exp(-8.318+42.796*a-59.938*a*a)
    else: p=1-math.exp(-13.436+101.14*a-223.73*a*a)
    return a2,a,p

def bartlett(groups):
    """Prueba de Bartlett: estadístico ji-cuadrada, gl y valor p (solo gl=1 exacto con erfc)."""
    k=len(groups); n=[len(g) for g in groups]; N=sum(n)
    var=[sum((v-sum(g)/len(g))**2 for v in g)/(len(g)-1) for g in groups]
    sp=sum((ni-1)*vi for ni,vi in zip(n,var))/(N-k)
    q=(N-k)*math.log(sp)-sum((ni-1)*math.log(vi) for ni,vi in zip(n,var))
    c=1+(sum(1/(ni-1) for ni in n)-1/(N-k))/(3*(k-1))
    chi=q/c
    p=math.erfc(math.sqrt(chi/2)) if k==2 else float('nan')
    return chi,k-1,p,var
