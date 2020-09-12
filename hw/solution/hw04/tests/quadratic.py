test = {
  'name': 'quadratic',
  'points': 1,
  'suites': [
    {
      'type': 'doctest',
      'setup': """
      >>> import hw04
      >>> from hw04 import *
      """,
      'cases': [
        {
          'locked': False,
          'code': """
          >>> str_interval(quadratic(interval(0, 2), -2, 3, -1))
          '-3 to 0.125'
          >>> str_interval(quadratic(interval(1, 3), 2, -3, 1))
          '0 to 10'
          """
        }
      ]
    },
    {
      'type': 'doctest',
      'setup': """
      >>> import hw04
      >>> old_abstraction = hw04.interval, hw04.lower_bound, hw04.upper_bound
      >>> hw04.interval = lambda a, b: lambda x: a if x == 0 else b
      >>> hw04.lower_bound = lambda s: s(0)
      >>> hw04.upper_bound = lambda s: s(1)
      >>> from hw04 import *
      """,
      'cases': [
        {
          'locked': False,
          'code': """
          >>> # Testing for abstraction violations
          >>> # Your code should not check for which implementation is used
          >>> str_interval(quadratic(interval(0, 2), -2, 3, -1))
          '-3 to 0.125'
          >>> str_interval(quadratic(interval(1, 3), 2, -3, 1))
          '0 to 10'
          """
        },
      ],
      'teardown': """
      >>> hw04.interval, hw04.lower_bound, hw04.upper_bound = old_abstraction
      """
    },
  ]
}
