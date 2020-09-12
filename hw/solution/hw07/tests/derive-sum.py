test = {
  'name': 'derive-sum',
  'points': 1,
  'suites': [
    {
      'type': 'scheme',
      'cases': [
        {
          'code': r"""
          scm> (make-sum 1 3)
          4
          scm> (make-sum 'x 0)
          x
          scm> (make-sum 0 'x)
          x
          scm> (make-sum 'a 'x)
          (+ a x)
          scm> (make-sum 'a (make-sum 'x 1))
          (+ a (+ x 1))
          """,
        },
      ],
      'setup': r"""
      scm> (load-all ".")
      """,
    },
    {
      'type': 'scheme',
      'cases': [
        {
          'code': r"""
          scm> (derive '(+ x 3) 'x)
          1
          """,
        }
      ],
      'setup': r"""
      scm> (load-all ".")
      """,
    },
  ]
}
