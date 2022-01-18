test = {
  'name': 'Question',
  'points': 1,
  'suites': [
    {
      'cases': [
        {
          'code': r"""
          >>> # n_placebo does not contain the correct value!
          >>> n_placebo == len(placebo)
          True

          """,
          'hidden': False,
          'locked': False
        },
                {
          'code': r"""
          >>> # n_drug does not contain the correct value!
          >>> n_drug == len(placebo)
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
