test = {
  'name': 'parent',
  'points': 1,
  'suites': [
    {
      'type': 'sqlite',
      'ordered': True,
      'setup': """
      sqlite> .read hw08.sql
      """,
      'cases': [
        {
          'locked': False,
          'code': r"""
          sqlite> SELECT * FROM by_parent_height;
          herbert
          fillmore
          abraham
          delano
          grover
          barack
          clinton
          """,
        },
      ],
    },
  ]
}
