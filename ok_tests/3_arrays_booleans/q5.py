test = {
  'name': 'Question',
  'points': 1,
  'suites': [
    {
      'cases': [

      {
          'code': r"""
          >>> # It looks like you have accidentally changed some of the elements in the `psychosis_scores_array`. Please run the following code to restore it to its proper state: psychosis_scores_array = np.array([80, 20, 14, 13, 91])
          >>> np.array_equiv(psychosis_scores_array, np.array([80, 20, 14, 13, 91])) == True
          True

          """,
          'hidden': False,
          'locked': False
        },

        {
          'code': r"""
          >>> # Hmmm, scores_less_than_70 does not contain the correct values. Do you use the `less_than_70_boolean_array` as a Boolean index on the `psychosis_scores_array`?
          >>> np.array_equiv(scores_less_than_70, np.array([20, 14, 13]))
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
