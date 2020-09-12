test = {
  'name': 'bluedog',
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
          sqlite> SELECT * FROM bluedog;
          blue|dog
          blue|dog
          blue|dog
          blue|dog
          blue|dog
          blue|dog
          blue|dog
          blue|dog
          blue|dog
          blue|dog
          blue|dog
          sqlite> SELECT * FROM bluedog_songs;
          blue|dog|Clair De Lune
          blue|dog|Formation
          blue|dog|Dancing Queen
          blue|dog|Dancing Queen
          blue|dog|Dancing Queen
          blue|dog|Dancing Queen
          blue|dog|Clair De Lune
          blue|dog|Formation
          blue|dog|Never Be Like You
          blue|dog|Formation
          blue|dog|Never Be Like You
          """,
        },
      ],
    },
  ]
}
