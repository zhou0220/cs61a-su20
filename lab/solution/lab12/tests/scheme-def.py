test = {
  'name': 'scheme-def',
  'points': 1,
  'suites': [
    {
      'scored': True,
      'setup': """
      scm> (load-all ".")
      """,
      'type': 'scheme',
      'cases': [
        {
          'code': """
          scm> (def f(x y) (+ x y))
          f
          scm> (f 2 3)
          5
          scm> (f 10 20)
          30
          """,
          'hidden': False,
          'locked': False
        },
        {
          'code': """
          scm> (def factorial(x) (if (zero? x) 1 (* x (factorial (- x 1)))))
          factorial
          scm> (factorial 4)
          24
          """,
          'hidden' : False,
          'locked': False
        }
      ]
    }
  ]
}
