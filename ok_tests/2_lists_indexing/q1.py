test = {
  'name': 'Question',
  'points': 1,
  'suites': [
    {
      'cases': [
        {
          'code': r"""
          >>> # psychosis_status_observations is not a list! A list is a collection of items, surrounded by sqaure brackets. E.g.: [1,2,3,4,5] is a list.
          >>> type(psychosis_status_observations) == list
          True

          """,
          'hidden': False,
          'locked': False
        },
        {
          'code': r"""
          >>> # psychosis_status_observations does not contain the correct observations. It should contain ['psychotic', 'not_psychotic', 'not_psychotic', 'not_psychotic', 'psychotic'], in this exact order.
          >>> psychosis_status_observations == ['psychotic', 'not_psychotic', 'not_psychotic', 'not_psychotic', 'psychotic']
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
