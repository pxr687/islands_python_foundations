test = {
  'name': 'Question',
  'points': 1,
  'suites': [
    {
      'cases': [
        {
          'code': r"""
          >>> # Hmmm, third_and_fourth does not contain the correct names. It should contain the third and fourth name in ['roy', 'david','lucy', 'aiesha', 'amelia']
          >>> third_and_fourth == names[2:4]
          True

          """,
          'hidden': True,
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
