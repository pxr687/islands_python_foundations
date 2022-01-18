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
          >>> # ans_lucy does not contain the correct value. You need to use the 'not equal' comparison operator to ask python: "is names[2] NOT EQUAL to 'lucy'"?
          >>> ans_lucy == False
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
