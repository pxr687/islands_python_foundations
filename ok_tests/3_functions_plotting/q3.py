test = {
  'name': 'Question',
  'points': 1,
  'suites': [
    {
      'cases': [
        {
          'code': r"""
          >>> # difference_in_means does not contain the correct value! Did you subtract the mean of the `drug` scores from the mean of the `placebo` scores?
          >>> difference_in_means == placebo.mean() - drug.mean()
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
