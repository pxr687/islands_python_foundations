test = {
  'name': 'Question',
  'points': 1,
  'suites': [
    {
      'cases': [

      {
          'code': r"""
          >>> # It looks like you have accidentally changed some of the elements in the `names` list. Please run the following code to restore it to its proper state: names = ['roy', 'david', 'lucy', 'aiesha', 'amelia']
          >>> names == ['roy', 'david', 'lucy', 'aiesha', 'amelia']
          True

          """,
          'hidden': False,
          'locked': False
        },

        {
          'code': r"""
          >>> # Hmmm, ans_len_5 does not contain the correct value. You need to use a comparison operator to ask 'is the length of the psychosis_status_observations list equal to 5?'
          >>> is_it_david == False
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
