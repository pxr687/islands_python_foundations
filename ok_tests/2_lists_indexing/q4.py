test = {
  'name': 'Question',
  'points': 1,
  'suites': [
    {
      'cases': [
        {
          'code': r"""
          >>> # Hmmm, fourth_person does not contain the correct value. Have you got the index location correct? Remember that python begins counting indexes from 0, not from 1...
          >>> fourth_person == observations_sex[3]
          True

          """,
          'hidden': False,
          'locked': False
        },
        {
          'code': r"""
          >>> # It looks like you are using the wrong index, remember that python counts from 0. So the first element of a list has the index location 0. Look again at the table above to find the correct index number for the fourth person in the observations_sex list.
          >>> index_of_fourth_person == 3
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
