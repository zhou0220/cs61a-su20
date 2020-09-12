test = {
  'name': 'list-comp',
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
          scm> (list-of (* x x) for x in '(3 4 5) if (odd? x))
          (9 25)
          scm> (list-of (* x x) for x in '(3 4 5) if (lambda (x) x))
          (9 16 25)
          """,
          'hidden': False,
          'locked': False
        },
        {
          'code': """
          scm> (list-of (* 2 x) for x in (list-of (* y y) for y in '(1 2 3 4 5) if (lambda (x) x)) if (odd? x))
          (2 18 50)
          """,
          'hidden': False,
          'locked': False
        },
      ],
    },
  ]
}
