test = {
  'name': 'group-by-nondecreasing',
  'points': 1,
  'suites': [
    {
      'type': 'scheme',
      'cases': [
        {
          'code': r"""
          scm> (first-k (group-by-nondecreasing finite-test-stream) 100)
          ((1 2 3) (1 2 2) (1))
          """,
          'locked' : False,
        },
        {
          'code': r"""
          scm> (first-k (group-by-nondecreasing infinite-test-stream) 4)
          ((1 2 2) (1 2 2) (1 2 2) (1 2 2))
          """,
          'locked' : False,
        },
      ],
      'setup': r"""
      scm> (load-all ".")
      scm> (define (first-k s k) (if (or (null? s) (= k 0)) nil (cons (car s) (first-k (cdr-stream s) (- k 1)))))
      """,
    },
  ]
}
