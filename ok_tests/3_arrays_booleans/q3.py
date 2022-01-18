test = {
  'name': 'Question',
  'points': 1,
  'suites': [
    {
      'cases': [

      {
          'code': r"""
          >>> # It looks like you have accidentally changed some of the elements in the `psychosis_scores` list. Please run the following code to restore it to its proper state: names = ['roy', 'david', 'lucy', 'aiesha', 'amelia']
          >>> psychosis_scores == [80, 20, 14, 13, 91]
          True

          """,
          'hidden': False,
          'locked': False
        },

        {
          'code': r"""
          >>> # fifth_psychosis does not contain the correct value. You need to use the 'greater than' comparison operator on the final element of the psychosis_scores list, which is the score for the fifth person sampled...
          >>> fifth_psychosis == True
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
