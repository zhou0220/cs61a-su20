test = {
  'name': 'small',
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
          sqlite> SELECT name FROM size_of_dogs WHERE size="toy" OR size="mini";
          abraham
          eisenhower
          fillmore
          grover
          herbert
          """,
        },
      ],
    },
  ]
}
