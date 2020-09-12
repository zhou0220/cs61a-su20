test = {
  'name': 'size',
  'points': 1,
  'suites': [
    {
      'type': 'sqlite',
      'setup': """
      sqlite> .read hw08.sql
      """,
      'cases': [
        {
          'locked': False,
          'code': r"""
          sqlite> SELECT * FROM sentences;
          barack and clinton are standard siblings
          abraham and grover are toy siblings
          """,
        },
      ],
    },
  ]
}
