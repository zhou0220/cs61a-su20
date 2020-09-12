(define (cddr s) (cdr (cdr s)))

(define (cadr s) (car (cdr s)))

(define (caddr s) (car (cddr s)))

(define (sign num)
  (cond 
    ((< num 0) -1)
    ((= 0 num) 0)
    (else      1)))

(define (square x) (* x x))

(define (pow x y)
    (cond ((= y 0) 1)
          ((even? y) (square (pow x (/ y 2))))
          (else (* x (pow x (- y 1)))))
)

(define (unique s) 
    (if (null? s)
        nil
        (cons (car s)
              (unique (filter (lambda (x) (not (eq? (car s) x))) (cdr s))))
        ))

(define (replicate x n) 
    (define (replicate-helper x n so-far)
        (if (= n 0)
            so-far
            (replicate-helper x (- n 1) (append so-far (list x)))
        )
    )
    (replicate-helper x n nil)
)

(define (accumulate combiner start n term)
    (if (= n 0)
        start
        (accumulate combiner (combiner (term n) start) (- n 1) term))
)

(define (accumulate-tail combiner start n term)
    (if (= n 0)
        start
        (accumulate-tail combiner (combiner (term n) start) (- n 1) term))
)

(define-macro
 (list-of map-expr for var in lst if filter-expr)
 `(map (lambda (,var) ,map-expr) (filter (lambda (,var) ,filter-expr) ,lst))
 )
