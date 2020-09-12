test = {
  'name': 'sign',
  'points': 1,
  'suites': [
    {
      'type': 'scheme',
      'setup': """
      scm> (load-all ".")
      """,
      'cases': [
        {
          'code': r"""
          scm> (cond ((= 1 1) 42))
          42
          scm> (cond ((= 1 1) 42) ((= 1 1) 24))
          42
          scm> (cond ((= 1 0) 42) ((= 0 1) 24) (else 999))
          999
          """,
        },
        {
          'code': r"""
          scm> (sign -42)
          -1
          """,
        },
        {
          'code': r"""
          scm> (sign 0)
          0
          """,
        },
        {
          'code': r"""
          scm> (sign 42)
          1
          """,
        },
      ],
    },
  ]
}
