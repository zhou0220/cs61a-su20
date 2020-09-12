test = {
  'name': 'split-at',
  'points': 0,
  'suites': [
    {
      'type': 'scheme',
      'scored': True,
      'setup': """
      scm> (load-all ".")
      """,
      'cases': [
        {
          'code': """
          scm> (car (split-at '(1 2 3 4 5) 3))
          (1 2 3)
          """,
          'hidden': False,
          'locked' : False
        },
        {
          'code': """
          scm> (cdr (split-at '(1 2 3 4 5) 3))
          (4 5)
          """,
          'hidden': False,
          'locked' : False
        },
        {
          'code': """
          scm> (car (split-at '(1 2 3 4 5) 10))
          (1 2 3 4 5)
          """,
          'hidden': False,
          'locked' : False
        },
        {
          'code': """
          scm> (cdr (split-at '(1 2 3 4 5) 10))
          ()
          """,
          'hidden': False,
          'locked' : False
        },
        {
          'code': """
          scm> (car (split-at '(0 1 1 2 3) 0))
          ()
          """,
          'hidden': False,
          'locked' : False
        },
        {
          'code': """
          scm> (cdr (split-at '(0 1 1 2 3) 0))
          (0 1 1 2 3)
          """,
          'hidden': False,
          'locked' : False
        },
      ]
    }
  ]
}
