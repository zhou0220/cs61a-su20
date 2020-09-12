test = {
  'name': 'sevens',
  'points': 1,
  'suites': [
    {
      'type': 'sqlite',
      'setup': """
      sqlite> .read lab13.sql
      """,
      'cases': [
        {
          'locked': False,
          'code': r"""
          sqlite> SELECT * FROM sevens;
          seven
          7
          7
          7
          Choose this option instead
          7
          the number 7 below.
          """,
        },
      ],
    },
  ]
}
