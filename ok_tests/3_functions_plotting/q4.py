test = {
  'name': 'Question',
  'points': 1,
  'suites': [
    {
      'cases': [
        {
          'code': r"""
          >>> # combined_groups does not contain all of the scores from the `placebo` group and the `drug` group. Did you use `np.append()` to combine the `placebo` group and the `drug` group arrays?
          >>> len(np.setdiff1d(combined_groups, np.append(placebo, drug))) == 0
          True

          """,
          'hidden': False,
          'locked': False
        },
      ],
      'scored': True,
      'setup': '',
      'teardown': '',
      'type': 'doctest'
    }
  ]
}
