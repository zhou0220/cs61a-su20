(define (rle s)
  (define (track-run elem st len)
    (cond ((null? st) (cons-stream (list elem len) nil))
          ((= elem (car st)) (track-run elem (cdr-stream st) (+ len 1)))
          (else (cons-stream (list elem len) (rle st))))
  )
  (if (null? s)
      nil
      (track-run (car s) (cdr-stream s) 1))
)



(define (group-by-nondecreasing s)
    (if (null? s)
        nil
        (begin
         (define (rest) (group-by-nondecreasing (cdr-stream s)))
         (if (or (null? (cdr-stream s))
                 (> (car s) (car (cdr-stream s))))
             (cons-stream (list (car s)) (rest))
             (cons-stream (cons (car s) (car (rest)))
                          (cdr-stream (rest)))))))


(define finite-test-stream
    (cons-stream 1
        (cons-stream 2
            (cons-stream 3
                (cons-stream 1
                    (cons-stream 2
                        (cons-stream 2
                            (cons-stream 1 nil))))))))

(define infinite-test-stream
    (cons-stream 1
        (cons-stream 2
            (cons-stream 2
                infinite-test-stream))))

