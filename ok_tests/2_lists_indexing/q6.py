test = {
  'name': 'Question',
  'points': 1,
  'suites': [
    {
      'cases': [
        {
          'code': r"""
          >>> # Hmmm, second_and_third does not contain the correct names. It should contain the second and third name in ['roy', 'david','lucy', 'aiesha', 'amelia']
          >>> second_and_third == names[1:3]
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
