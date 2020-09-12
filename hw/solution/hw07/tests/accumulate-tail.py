test = {
  'name': 'accumulate-tail',
  'points': 1,
  'suites': [
    {
      'type': 'scheme',
      'setup': """
      scm> (load-all ".")
      """,
      'cases': [
        {
          'code': """
          scm> (define (identity x) x)
          identity
          scm> (accumulate-tail * 1 5 identity)
          120
          """,
          'hidden': False,
          'locked': False
        },
        {
          'code': """
          scm> (define (square x) (* x x))
          square
          scm> (accumulate-tail + 0 5 square)
          55
          scm> (accumulate-tail + 5 5 square)
          60
          """,
          'hidden': False,
          'locked': False
        },
        {
          'code': """
          scm> (define (identity x) x)
          identity
          scm> (accumulate-tail + 0 1000 identity)
          500500
          scm> (accumulate-tail + 0 5000 identity)
          12502500
          """,
          'hidden': False,
          'locked': False
        },
      ],
    },
  ]
}
