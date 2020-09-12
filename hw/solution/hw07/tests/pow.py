test = {
  'name': 'pow',
  'points': 1,
  'suites': [
    {
      'type': 'scheme',
      'cases': [
        {
          'code': r"""
          scm> (pow 2 5)
          32
          """,
        },
        {
          'code': r"""
          scm> (pow 10 3)
          1000
          """,
        },
        {
          'code': r"""
          scm> (pow 3 3)
          27
          """,
        },
        {
          'code': r"""
          scm> (pow 1 100000000000000) ; make sure you are using the logarithmic time algorithm!
          1
          """,
        },
      ],
      'setup': """
      scm> (load-all ".")
      """,
    },
  ]
}
