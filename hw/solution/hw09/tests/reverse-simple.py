test = {
  'name': 'reverse-simple',
  'points': 1,
  'suites': [
    {
      'type': 'scheme',
      'cases': [
        {
          'code': r"""
          scm> (reverse '())
          ()
          scm> (reverse '(1))
          (1)
          scm> (reverse '(1 2 3))
          (3 2 1)
          scm> (reverse '(1 2 3 4 5))
          (5 4 3 2 1)
          scm> (reverse '(1 2 3 4 5 1 3 7))
          (7 3 1 5 4 3 2 1)
          """,
          'locked' : False,
        },
      ],
      'setup': r"""
      scm> (load-all ".")
      """,
    },
  ]
}
