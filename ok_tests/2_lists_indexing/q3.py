test = {
  'name': 'Question',
  'points': 1,
  'suites': [
    {
      'cases': [
        {
          'code': r"""
          >>> # Hmmm, fifth_element does not contain the correct value. Have you got the index location correct? Remember that python begins counting indexes from 0, not from 1...
          >>> fifth_element == psychosis_status_observations[4]
          True

          """,
          'hidden': False,
          'locked': False
        },
        {
          'code': r"""
          >>> # It looks like you are using the wrong index, remember that python counts from 0. So the first element of a list has the index location 0. Look again at the table above to find the correct index number for the fifth element of the psychosis_status_observations list.
          >>> index_of_fifth_element == 4
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
