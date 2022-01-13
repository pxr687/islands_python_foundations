test = {
  'name': 'Question',
  'points': 1,
  'suites': [
    {
      'cases': [
        {
          'code': r"""
          >>> # difference_in_medians does not contain the correct value! Did you subtract the median of the `drug` scores from the median of the `placebo` scores?
          >>> difference_in_medians == placebo.median() - drug.median()
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
