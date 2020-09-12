test = {
  'name': 'stack',
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
          sqlite> SELECT * FROM stacks;
          abraham, delano, clinton, barack|171
          grover, delano, clinton, barack|173
          herbert, delano, clinton, barack|176
          fillmore, delano, clinton, barack|177
          eisenhower, delano, clinton, barack|180
          """,
        },
      ],
    },
  ]
}
